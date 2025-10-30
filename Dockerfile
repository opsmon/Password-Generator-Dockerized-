FROM python:3.12-slim
WORKDIR /app
COPY password_gen.py .
ENTRYPOINT ["python", "password_gen.py"]
