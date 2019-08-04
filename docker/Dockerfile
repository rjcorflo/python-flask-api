FROM python:3.7

WORKDIR /application

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "-u", "server.py" ]