FROM python:3.11-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /SmartWork
COPY requirements.txt /SmartWork/
RUN pip install -r requirements.txt

COPY . /SmartWork/

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8002"]
#EXPOSE 8002