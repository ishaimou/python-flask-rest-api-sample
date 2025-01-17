FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py"]
