#!/usr/bin/env python3
import os
import subprocess
import json
from datetime import datetime, timezone, timedelta
from fastmcp import FastMCP

mcp = FastMCP("shell")

HEARTBEAT_STATE = "/app/heartbeat_state.json"
TZ = timezone(timedelta(hours=2))


def mark_active():
    try:
        state = {}
        if os.path.exists(HEARTBEAT_STATE):
            with open(HEARTBEAT_STATE, "r") as f:
                state = json.load(f)
        state["last_user_message"] = datetime.now(TZ).isoformat()
        with open(HEARTBEAT_STATE, "w") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
    except:
        pass


@mcp.tool()
def run(command: str) -> str:
    """Execute a shell command and return output."""
    mark_active()
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


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8005"))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
