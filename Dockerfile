# set base image (host OS)
FROM python:3.9.5-alpine

RUN apt-get update
RUN apt-get -y install libpq-dev gcc
RUN pip install psycopg2

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set the working directory in the container
WORKDIR /django

# install dependencies
#RUN python -m venv venv
#RUN source venv/bin/activate
#RUN pip install --upgrade pip

# copy the dependencies file to the working directory
COPY requirements.txt /django

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . /django

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]