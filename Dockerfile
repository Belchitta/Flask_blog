FROM python:3.9.1-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

COPY entrypoint.sh .
RUN chmod u+x entrypoint.sh

CMD ["sh", "entrypoint.sh"]
