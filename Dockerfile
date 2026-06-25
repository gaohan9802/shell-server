FROM python:3.10
LABEL "language"="python"
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8005
CMD ["python", "shell-mcp-server.py"]
