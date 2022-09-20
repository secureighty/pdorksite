FROM python:3.10-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN touch output.txt
RUN chmod 777 output.txt

COPY app.py .

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=8080"]

