FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install pytest
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]
