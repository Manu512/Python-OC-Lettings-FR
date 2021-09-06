# set base image (host OS)
FROM python:3.9.5-alpine

## install dependencies
#RUN apk update && \
#    apk add --virtual build-deps gcc musl-dev && \
#    apk add postgresql-dev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ALLOWED_HOSTS=127.0.0.1,[::1],0.0.0.0,.herokuapp.com
ENV SECRET_KEY="fp$9^59[3]sriajg$_%]=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"

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