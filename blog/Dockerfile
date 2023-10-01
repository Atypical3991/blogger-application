# syntax=docker/dockerfile:1
FROM python:3

# Setting workdir where your code with reside
WORKDIR /code

RUN chmod -R 777 /code/

# Copy requirements.txt file into code directory inside docker
COPY requirements.txt /code/

# To Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# To Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

RUN pip install uwsgi
RUN pip install -r requirements.txt

COPY . /code/
CMD ["uwsgi", "--ini", "/code/blog.ini"]
