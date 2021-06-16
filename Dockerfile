FROM python:3.8.9
LABEL maintainer="montanha.masu536@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /decotimer ./decotimer/
COPY /tests ./tests/
COPY /dist ./dist/
COPY usage.py .

CMD [ "python", "usage.py" ]
