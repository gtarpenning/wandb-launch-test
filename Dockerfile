FROM python:3.10.4-slim

RUN pip install -r requirements.txt .

RUN ssl/fix-python.sh

CMD ["python", "main.py"]
