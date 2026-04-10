#!/usr/bin/env python3
"""
ping0.cc 页面结构分析脚本
用于分析页面内容，找到风控值的位置
"""

import sys
import requests
from bs4 import BeautifulSoup

URL = "https://ping0.cc"
TIMEOUT = 10
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def main():
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print(f"正在请求 {URL} ...")
    try:
        response = requests.get(URL, headers=HEADERS, timeout=TIMEOUT, verify=False)
        print(f"HTTP 状态码: {response.status_code}")

        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text[:500]}")
            return 1

        print("\n=== 响应头 ===")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        print("\n=== 页面内容 (前2000字符) ===")
        content = response.text
        print(content[:2000])

        print("\n=== 尝试解析 HTML ===")
        soup = BeautifulSoup(content, 'html.parser')

        print("\n=== 查找包含 '风控' 的元素 ===")
        risk_elements = soup.find_all(text=lambda text: text and '风控' in text)
        if risk_elements:
            for i, elem in enumerate(risk_elements[:5]):
                print(f"\n找到元素 {i+1}:")
                print(f"  文本: {elem.strip()}")
                print(f"  父标签: {elem.parent.name if elem.parent else 'None'}")
                if elem.parent:
                    print(f"  父标签 class: {elem.parent.get('class')}")
                    print(f"  父标签 id: {elem.parent.get('id')}")
                    print(f"  完整父标签: {elem.parent}")
        else:
            print("未找到包含 '风控' 的文本")

        print("\n=== 查找所有可能的数字元素 ===")
        import re
        number_pattern = re.compile(r'\d+')
        all_elements = soup.find_all(['div', 'span', 'p', 'td', 'th', 'b', 'strong'])
        found_numbers = []
        for elem in all_elements:
            text = elem.get_text(strip=True)
            if text and number_pattern.search(text):
                found_numbers.append((elem.name, elem.get('class'), elem.get('id'), text))

        print(f"找到 {len(found_numbers)} 个包含数字的元素:")
        for i, (tag, classes, id_, text) in enumerate(found_numbers[:20]):
            print(f"  {i+1}. <{tag} class={classes} id={id_}>: {text}")

        print("\n=== 保存完整页面到 ping0_page.html ===")
        with open('ping0_page.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("已保存到 ping0_page.html")

        return 0

    except requests.exceptions.Timeout:
        print("请求超时")
        return 1
    except requests.exceptions.ConnectionError as e:
        print(f"连接错误: {e}")
        return 1
    except Exception as e:
        print(f"发生错误: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
