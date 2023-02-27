FROM python:3.10.6-slim

ENV APP_HOME /app
ENV PORT 8000
WORKDIR $APP_HOME
COPY . ./

RUN python3 -m pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 bmi:app
