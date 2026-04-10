#!/usr/bin/env python3
"""
单次测试脚本：测试获取风控值
"""

import sys
import os

# 添加 src 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ippuritycheck.monitor import fetch_risk_value, log, FetchStatus

def main():
    log("INFO", "开始单次测试获取风控值...")
    status, risk_value = fetch_risk_value()

    if status == FetchStatus.SUCCESS and risk_value is not None:
        log("INFO", f"获取成功！当前风控值：{risk_value}%")
        return 0
    elif status == FetchStatus.CAPTCHA:
        log("ERROR", "遇到 Cloudflare 验证")
        return 1
    else:
        log("ERROR", "获取失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())
