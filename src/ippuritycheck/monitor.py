#!/usr/bin/env python3
"""
macOS 风控监控小程序
定时检测 ping0.cc 上的风控值，超过阈值时触发系统告警
"""

import sys
import time
import subprocess
import json
import os
from datetime import datetime
from enum import Enum

import requests
from bs4 import BeautifulSoup
import urllib3

# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==================== 默认配置 ====================
DEFAULT_CONFIG = {
    "url": "https://ping0.cc",
    "check_interval": 10,
    "risk_threshold": 20,
    "captcha_retry_wait": 60,
    "request_timeout": 10
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 全局配置变量
config = {}


class FetchStatus(Enum):
    """获取状态枚举"""
    SUCCESS = "success"
    CAPTCHA = "captcha"
    ERROR = "error"


def load_config(config_path: str = None) -> dict:
    """
    加载配置文件

    Args:
        config_path: 配置文件路径，默认使用 config/config.json

    Returns:
        配置字典
    """
    if config_path is None:
        # 默认配置文件路径：项目根目录的 config/config.json
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(script_dir))
        config_path = os.path.join(project_root, "config", "config.json")

    if not os.path.exists(config_path):
        print(f"[WARN] 配置文件不存在: {config_path}，使用默认配置")
        return DEFAULT_CONFIG.copy()

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            loaded_config = json.load(f)
        # 合并默认配置
        result = DEFAULT_CONFIG.copy()
        result.update(loaded_config)
        return result
    except Exception as e:
        print(f"[WARN] 读取配置文件失败: {e}，使用默认配置")
        return DEFAULT_CONFIG.copy()


def log(level: str, msg: str) -> None:
    """
    统一日志输出（带时间戳）

    Args:
        level: 日志级别 (INFO, ALERT, ERROR)
        msg: 日志消息
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level:5s}] {msg}", flush=True)


def is_captcha_page(soup: BeautifulSoup) -> bool:
    """
    判断是否是 Cloudflare 验证页面

    Args:
        soup: BeautifulSoup 对象

    Returns:
        是否是验证页面
    """
    # 检查 Turnstile 验证元素
    if soup.find('div', class_='cf-turnstile'):
        return True
    if soup.find('div', id='captcha-element'):
        return True
    # 检查验证相关的脚本
    if soup.find('script', src=lambda src: src and 'challenges.cloudflare.com' in src):
        return True
    return False


def fetch_risk_value() -> tuple[FetchStatus, float | None]:
    """
    获取风控值

    Returns:
        (状态, 风控值或None)
        状态: SUCCESS-成功, CAPTCHA-遇到验证, ERROR-其他错误
    """
    try:
        url = config.get("url", DEFAULT_CONFIG["url"])
        timeout = config.get("request_timeout", DEFAULT_CONFIG["request_timeout"])

        response = requests.get(url, headers=HEADERS, timeout=timeout, verify=False)

        if response.status_code != 200:
            log("ERROR", f"HTTP 请求失败，状态码: {response.status_code}")
            return FetchStatus.ERROR, None

        soup = BeautifulSoup(response.text, 'html.parser')

        # 检查是否是验证页面
        if is_captcha_page(soup):
            log("ERROR", "遇到 Cloudflare Turnstile 人机验证")
            return FetchStatus.CAPTCHA, None

        # 查找风控值: <span class="value">9%</span>
        value_span = soup.find('span', class_='value')
        if not value_span:
            log("ERROR", "未找到风控值元素")
            return FetchStatus.ERROR, None

        value_text = value_span.get_text(strip=True)
        if not value_text:
            log("ERROR", "风控值文本为空")
            return FetchStatus.ERROR, None

        # 移除百分号并转换为数字
        value_str = value_text.replace('%', '').strip()
        try:
            risk_value = float(value_str)
            return FetchStatus.SUCCESS, risk_value
        except ValueError:
            log("ERROR", f"无法转换风控值为数字: {value_text}")
            return FetchStatus.ERROR, None

    except requests.exceptions.Timeout:
        log("ERROR", "网络请求超时")
        return FetchStatus.ERROR, None
    except requests.exceptions.ConnectionError as e:
        log("ERROR", f"网络连接失败: {e}")
        return FetchStatus.ERROR, None
    except Exception as e:
        log("ERROR", f"获取风控值时发生错误: {type(e).__name__}: {e}")
        return FetchStatus.ERROR, None


def send_alert(value: float) -> bool:
    """
    触发 macOS 系统弹窗告警（风控值过高）

    Args:
        value: 当前风控值

    Returns:
        是否成功发送告警
    """
    try:
        # 使用 AppleScript 显示弹窗
        script = f'display dialog "当前风控值过高（当前值：{value}%），存在风险！" buttons {{"知道了"}} default button "知道了" with icon caution with title "风控告警"'
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return True
        else:
            log("ERROR", f"AppleScript 执行失败: {result.stderr}")
            return try_send_notification(value, "值过高，存在风险！")
    except subprocess.TimeoutExpired:
        log("ERROR", "AppleScript 调用超时")
        return try_send_notification(value, "值过高，存在风险！")
    except Exception as e:
        log("ERROR", f"发送告警失败: {type(e).__name__}: {e}")
        return try_send_notification(value, "值过高，存在风险！")


def send_captcha_alert() -> bool:
    """
    触发 macOS 系统弹窗告警（连续遇到验证码）

    Returns:
        是否成功发送告警
    """
    try:
        script = 'display dialog "连续遇到 Cloudflare 人机验证，需要手动处理！" buttons {"知道了"} default button "知道了" with icon stop with title "验证告警"'
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return True
        else:
            log("ERROR", f"AppleScript 执行失败: {result.stderr}")
            return try_send_notification(0, "连续遇到 Cloudflare 人机验证！")
    except Exception as e:
        log("ERROR", f"发送验证码告警失败: {type(e).__name__}: {e}")
        return try_send_notification(0, "连续遇到 Cloudflare 人机验证！")


def try_send_notification(value: float, subtitle: str) -> bool:
    """
    备用方案：发送 macOS 通知中心通知

    Args:
        value: 当前风控值
        subtitle: 通知副标题

    Returns:
        是否成功发送通知
    """
    try:
        if value > 0:
            script = f'display notification "当前风控值：{value}%" with title "风控告警" subtitle "{subtitle}"'
        else:
            script = f'display notification "请检查！" with title "风控告警" subtitle "{subtitle}"'
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0
    except Exception:
        return False


def main() -> None:
    """主循环入口"""
    global config
    config = load_config()

    url = config.get("url", DEFAULT_CONFIG["url"])
    check_interval = config.get("check_interval", DEFAULT_CONFIG["check_interval"])
    risk_threshold = config.get("risk_threshold", DEFAULT_CONFIG["risk_threshold"])
    captcha_retry_wait = config.get("captcha_retry_wait", DEFAULT_CONFIG["captcha_retry_wait"])

    log("INFO", f"风控监控程序启动")
    log("INFO", f"监控地址: {url}")
    log("INFO", f"检测间隔: {check_interval}秒")
    log("INFO", f"告警阈值: {risk_threshold}%")
    log("INFO", f"验证码重试等待: {captcha_retry_wait}秒")
    log("INFO", "按 Ctrl+C 停止程序")
    print("-" * 60)

    consecutive_captcha = 0  # 连续遇到验证码的次数

    try:
        while True:
            status, risk_value = fetch_risk_value()

            if status == FetchStatus.SUCCESS:
                consecutive_captcha = 0  # 重置验证码计数
                if risk_value > risk_threshold:
                    log("ALERT", f"当前风控值：{risk_value}%，触发告警！")
                    send_alert(risk_value)
                else:
                    log("INFO", f"当前风控值：{risk_value}%，状态正常")

            elif status == FetchStatus.CAPTCHA:
                consecutive_captcha += 1
                if consecutive_captcha == 1:
                    # 第一次遇到验证码，等待后重试
                    log("INFO", f"等待 {captcha_retry_wait} 秒后重试...")
                    time.sleep(captcha_retry_wait)
                    continue  # 跳过后面的 sleep，直接进入下一轮
                else:
                    # 连续遇到验证码，触发告警
                    log("ALERT", f"连续 {consecutive_captcha} 次遇到验证，触发告警！")
                    send_captcha_alert()

            else:  # ERROR
                consecutive_captcha = 0
                log("ERROR", "获取风控值失败，跳过本轮")

            # 等待下一轮检测
            time.sleep(check_interval)

    except KeyboardInterrupt:
        print("\n" + "-" * 60)
        log("INFO", "程序已停止")
        sys.exit(0)


if __name__ == "__main__":
    main()
