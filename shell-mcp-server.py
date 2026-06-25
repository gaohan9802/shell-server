#!/usr/bin/env python3
import os
import subprocess
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

mcp = FastMCP("shell")

@mcp.tool()
def run(command: str) -> str:
    """Execute a shell command and return output."""
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=30
        )
        output = ""
        if result.stdout:
            output += result.stdout
        if result.stderr:
            output += result.stderr
        if not output:
            output = "(no output)"
        return output
    except subprocess.TimeoutExpired:
        return "(timeout after 30s)"
    except Exception as e:
        return f"(error: {e})"

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    return JSONResponse({"status": "alive"}, status_code=200)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8005"))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
