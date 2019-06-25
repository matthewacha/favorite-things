FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip3 install -r requirements.txt

COPY . /code/

RUN chmod +x /code/entrypoint.sh

# RUN apt-get update && \
#     apt-get install netcat -y

# CMD ["./entrypoint.sh"]