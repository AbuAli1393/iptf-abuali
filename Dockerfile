FROM python:3.10-slim

WORKDIR /iptf-abuali

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/
COPY config/ ./config/

CMD ["python", "run_iptf.py"]