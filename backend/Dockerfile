FROM python:3.6.2-slim
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
ADD . /code
EXPOSE 5000
CMD ["python","runserver.py"]