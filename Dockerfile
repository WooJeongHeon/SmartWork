FROM python:3.11-alpine
ENV PYTHONUNBUFFERED 1

# 필수 패키지 설치
RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    python3-dev \
    py3-cffi

WORKDIR /SmartWork
COPY requirements.txt /SmartWork/
RUN pip install -r requirements.txt

COPY . /SmartWork/

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8002"]
#EXPOSE 8002
