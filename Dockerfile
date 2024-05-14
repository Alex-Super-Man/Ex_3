FROM python:3.11.5
RUN pip install scikit-learn
COPY . /app
WORKDIR /app
CMD ["python", "main.py"]