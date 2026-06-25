FROM python:3.11-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY shell-mcp-server.py .
EXPOSE 8005
CMD ["python", "shell-mcp-server.py"]
