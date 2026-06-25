#!/bin/bash
# 启动心跳调度器（后台）
nohup python3 /data/heartbeat_scheduler.py > /data/scheduler.log 2>&1 &

# 启动主服务
python3 shell-mcp-server.py
