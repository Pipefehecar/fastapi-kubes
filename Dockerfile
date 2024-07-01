FROM python:3.11-slim
WORKDIR /usr/src/app
COPY . .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","-m","main"]
