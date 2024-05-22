terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.50.0"
    }
  }
}

provider "aws" {
  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"
  region                      = "us-east-1"

  s3_use_path_style           = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3 = "http://s3.localhost.localstack.cloud:4566"
  }
}

resource "aws_s3_bucket" "s3_start" {
  bucket = "s3-start"

  tags = {
    Name        = "s3-start"
    Environment = "Dev"
  }

  lifecycle_rule {
    id      = "ExpireOldBackups"
    enabled = true

    prefix = "backups/"

    expiration {
      days = 365
    }
  }
}

resource "aws_s3_bucket" "s3_finish" {
  bucket = "s3-finish"

  tags = {
    Name        = "s3-finish"
    Environment = "Dev"
  }
}


resource "aws_lambda_function" "copy_s3_objects" {
  filename         = "lambda_function.zip"
  function_name    = "CopyS3ObjectsFunction"
  role             = aws_iam_role.lambda_role.arn
  handler          = "lambda_function.lambda_handler"
  source_code_hash = filebase64sha256("lambda_function.zip")
  runtime          = "python3.8"

  environment {
    variables = {
      SOURCE_BUCKET      = aws_s3_bucket.s3_start.bucket
      DESTINATION_BUCKET = aws_s3_bucket.s3_finish.bucket
    }
  }
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_attachment" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_role.name
}

resource "aws_s3_bucket_notification" "s3_notification" {
  bucket = aws_s3_bucket.s3_start.bucket

  lambda_function {
    lambda_function_arn = aws_lambda_function.copy_s3_objects.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "backups/"
  }
}