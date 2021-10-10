FROM python:3.7

COPY ./app1 /docker-flask-test

WORKDIR /docker-flask-test

ADD requirements.txt .

RUN pip install -r requirements.txt


# define the command to start the container
CMD ["gunicorn","app1:app1", "-b", "0.0.0.0:8000"]
