# Password-Generator-Dockerized
A simple and secure Dockerized password generator written in Python.

# 🔐 Password Generator (Dockerized)

A lightweight and secure password generator written in Python — packaged in Docker for easy use anywhere.

---

## 🚀 Usage

### Build the image
```
docker build -t password-gen .
```
Generate a password
```
docker run --rm password-gen
```

Custom length
```
docker run --rm password-gen 24
```

Disable uppercase, digits, or symbols
```
docker run --rm password-gen 20 --no-upper --no-digits --no-symbols
```

🧱 Dockerfile
```
FROM python:3.12-slim
WORKDIR /app
COPY password_gen.py .
ENTRYPOINT ["python", "password_gen.py"]
```
⚙️ Local Run (without Docker)
```
python password_gen.py 16
```
