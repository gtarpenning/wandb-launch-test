FROM python:3.10.4-slim

RUN pip install -r requirements.txt .

ENV WANDB_BASE_URL=https://api.wandb.test
RUN ssl/setup.sh
RUN ssl/fix-python.sh

CMD ["python", "main.py"]
