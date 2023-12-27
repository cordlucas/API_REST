FROM python:3.12-alpine

WORKDIR /api

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]