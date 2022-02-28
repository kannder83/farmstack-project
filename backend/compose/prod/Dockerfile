FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN python3 -m pip install --no-cache-dir -r requirements.txt
COPY . .
CMD python3 main.py