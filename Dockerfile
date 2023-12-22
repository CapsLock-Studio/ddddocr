FROM python:3.11.2

WORKDIR /app

COPY . .

RUN pip install pipenv && \
  pipenv install

ENTRYPOINT [ "pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0" ]