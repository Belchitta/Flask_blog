FROM python:3.10-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache --user -r requirements.txt
RUN pip install python-dotenv

COPY . .

EXPOSE 5000

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]