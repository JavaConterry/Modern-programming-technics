import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    src_bucket = s3.Bucket("s3-start")
    dst_bucket = s3.Bucket("s3-finish")

    for obj in src_bucket.objects.all():
        print("Copying:", obj.key)
        copy_source = {
            'Bucket': obj.bucket_name,
            'Key': obj.key
        }

        dst_file_name = obj.key
        dst_bucket.Object(dst_file_name).copy_from(CopySource=copy_source)

    print("Copy complete")
