FROM python:3.10

WORKDIR /src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Use FastMCP CLI to run the server with HTTP transport
CMD ["fastmcp", "run", "shell-mcp-server.py:mcp", "--transport", "http", "--host", "0.0.0.0", "--port", "8005"]
