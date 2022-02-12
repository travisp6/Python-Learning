FROM python:3.10-alpine

WORKDIR /NewFlask

ADD . /NewFlask

RUN pip install -r requirements.txt

COPY . .

CMD ["python","app.py"]