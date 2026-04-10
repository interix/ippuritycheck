#!/usr/bin/env python3
"""
单次测试脚本：测试获取风控值和IP位置
"""

import sys
import os

# 添加 src 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ippuritycheck.monitor import fetch_data, log, FetchStatus, load_config, config, is_location_allowed

def main():
    # 先加载配置
    load_config()
    log("INFO", "开始单次测试获取数据...")
    status, risk_value, location = fetch_data()

    if status == FetchStatus.SUCCESS:
        if risk_value is not None:
            log("INFO", f"获取成功！当前风控值：{risk_value}%")
        if location:
            log("INFO", f"IP位置：{location}")
            enable_check = config.get("enable_location_check", False)
            if enable_check:
                allowed = is_location_allowed(location)
                log("INFO", f"位置检查：{'允许' if allowed else '不允许'}")
        return 0
    elif status == FetchStatus.CAPTCHA:
        log("ERROR", "遇到 Cloudflare 验证")
        return 1
    else:
        log("ERROR", "获取失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())
