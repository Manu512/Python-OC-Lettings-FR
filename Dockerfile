# set base image (host OS)
FROM python:3.9.5

# set the working directory in the container
WORKDIR /django

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN python -m venv venv
RUN source venv/bin/activate
#RUN pip install --upgrade pip

# copy the dependencies file to the working directory
COPY requirements.txt /django

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . /django

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]