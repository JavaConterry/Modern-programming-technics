FROM python:3.11-slim-buster

WORKDIR /src

COPY . /src

RUN pip install -r src/requirements.txt

ENTRYPOINT ls -al
CMD ["python", "src/main.py"]