FROM tiangolo/meinheld-gunicorn:python3.7-alpine3.8
RUN pip install --upgrade pip
COPY . /app
RUN pip install -r requirements.txt