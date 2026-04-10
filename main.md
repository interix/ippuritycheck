# macOS 风控监控小程序 — 开发提示词

## 任务目标

为我开发一个运行在 macOS 上的 Python 后台监控小程序，用于定时检测 <https://ping0.cc> 页面上的"风控值"，当风控值超过阈值时触发系统级告警弹窗。

---

## 第一步：调研页面结构（必须先做）

在写任何代码之前，请先分析 <https://ping0.cc> 的页面结构：

- 该页面是否直接返回 HTML？是否有 JS 渲染？
- "风控值"字段的 HTML 标签、class 名或 id 是什么？
- 是否存在可直接调用的 JSON 接口（如 `/api/...`）可以返回风控值？
- 请求时是否需要携带特定 Header（如 `User-Agent`）？

根据分析结果，选择最简单可靠的获取方式（优先 JSON 接口，其次 BeautifulSoup 解析 HTML）。

---

## 程序功能要求

| 功能点 | 要求 |
|--------|------|
| 运行平台 | macOS，Python 3.8+ |
| 运行方式 | 终端启动后静默持续运行，不需要 GUI |
| 检测频率 | 每隔 30 秒请求一次（间隔可通过常量 `CHECK_INTERVAL` 配置） |
| 风控阈值 | 默认 > 20 触发告警（阈值可通过常量 `RISK_THRESHOLD` 配置） |

---

## 核心逻辑流程

```
启动 → 循环开始
  └─ 发起 HTTP GET 请求 https://ping0.cc
       ├─ 成功 → 解析页面/接口，提取风控值（整数或浮点数）
       │         ├─ 风控值 > RISK_THRESHOLD → 触发告警（弹窗 + 日志）
       │         └─ 风控值 ≤ RISK_THRESHOLD → 仅记录日志（正常）
       └─ 失败 → 捕获异常，记录错误日志，不崩溃
  └─ 等待 CHECK_INTERVAL 秒 → 进入下一轮
```

---

## 告警方式（双通道）

### 1. macOS 系统弹窗（优先使用 AppleScript，更稳定）

- 使用 `osascript` 命令调用 AppleScript 弹窗
- 弹窗内容：`当前风控值过高（当前值：XX），存在风险！`
- 备用方案：若 AppleScript 失败，尝试使用 `osascript` 发送 macOS 通知中心通知

### 2. 终端日志输出（带时间戳）

```
[2024-01-01 12:00:00] [INFO]  当前风控值：15，状态正常
[2024-01-01 12:00:00] [ALERT] 当前风控值：25，触发告警！
[2024-01-01 12:00:00] [ERROR] 网络请求失败：<异常信息>
```

---

## 技术栈要求

| 用途 | 库/工具 |
|------|---------|
| 网络请求 | `requests`（设置 `timeout=10`） |
| HTML 解析 | `BeautifulSoup4`（仅在无 JSON 接口时使用） |
| 系统弹窗 | `subprocess` 调用 `osascript`（macOS 内置，无需安装） |

> 不使用任何复杂框架，标准库 + 上述两个第三方库即可。

---

## 异常处理要求（必须覆盖以下所有场景）

| 异常类型 | 处理方式 |
|----------|----------|
| 网络超时（`Timeout`） | 捕获，记录 ERROR 日志，跳过本轮，继续下一轮 |
| 网络连接失败（`ConnectionError`） | 同上 |
| HTTP 状态码非 200 | 记录状态码，跳过本轮 |
| HTML 解析失败（找不到目标元素） | 记录 ERROR 日志，跳过本轮 |
| 风控值无法转换为数字 | 记录原始内容，跳过本轮 |
| `osascript` 弹窗调用失败 | 记录 ERROR 日志，不影响主循环 |
| `KeyboardInterrupt`（Ctrl+C） | 优雅退出，打印"程序已停止" |

---

## 代码结构要求

请按以下结构组织代码（单文件 `monitor.py`）：

```
monitor.py
├── 顶部常量配置区（URL、阈值、间隔、请求头）
├── fetch_risk_value()  →  返回风控值数字或 None
├── send_alert(value)   →  触发 AppleScript 弹窗
├── log(level, msg)     →  统一日志输出（带时间戳）
└── main()              →  主循环入口
```

---

## 输出要求

请提供：

### 1. 完整可运行的 `monitor.py` 代码

### 2. 依赖安装命令

```bash
pip install requests beautifulsoup4
```

### 3. 运行说明

**前台运行（终端直接启动）：**

```bash
python3 monitor.py
```

**后台运行并保留日志：**

```bash
nohup python3 monitor.py > monitor.log 2>&1 &
```

**查看后台进程：**

```bash
ps aux | grep monitor.py
```

**终止后台进程：**

```bash
kill <PID>
```
