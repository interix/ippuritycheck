# ippuritycheck

macOS 风控监控小程序，定时检测 ping0.cc 上的风控值，超过阈值时触发系统告警弹窗。

## 功能特性

- 每 10 秒自动检测一次风控值
- 风控值超过 20% 时触发 macOS 系统弹窗告警
- 终端日志输出（带时间戳）
- 异常处理完善，不崩溃

## 快速开始

### 安装依赖

```bash
make deps
```

### 检查环境

```bash
make check-deps
```

### 前台运行

```bash
make run
```

或直接运行：

```bash
source .venv/bin/activate
python src/ippuritycheck/monitor.py
```

### 后台运行

```bash
make start
```

日志将输出到 `monitor.log`。

### 查看状态

```bash
make status
```

### 停止服务

```bash
make stop
```

## 配置

复制配置示例文件并修改：

```bash
cp config/config.json.example config/config.json
```

编辑 [config/config.json](config/config.json)：

| 配置项 | 说明 | 默认值 |
|--------|------|-------|
| `url` | 监控地址 | https://ping0.cc |
| `check_interval` | 检测间隔（秒） | 10 |
| `risk_threshold` | 告警阈值（百分比） | 20 |
| `captcha_retry_wait` | 遇到验证码等待时间（秒） | 60 |
| `request_timeout` | 请求超时（秒） | 10 |

## 项目结构

```
ippuritycheck/
├── config/
│   ├── config.json              # 配置文件（需从 config.json.example 复制）
│   └── config.json.example      # 配置文件示例
├── src/
│   └── ippuritycheck/
│       └── monitor.py          # 主监控程序
├── tests/                      # 测试目录（预留）
├── scripts/
│   ├── analyze_ping0.py        # 页面结构分析脚本
│   └── test_single.py          # 单次测试脚本
├── docs/plans/                 # 项目计划归档
├── rules/                      # 工程规范
├── Makefile                     # 工程统一入口
├── requirements.txt             # Python 依赖
└── README.md                   # 本文件
```

## Makefile 命令

| 命令 | 说明 |
|-----|------|
| `make help` | 显示帮助信息 |
| `make deps` | 安装依赖 |
| `make check-deps` | 检查依赖状态 |
| `make clean` | 清理临时文件 |
| `make run` | 前台运行 |
| `make start` | 后台启动 |
| `make status` | 查看状态 |
| `make stop` | 停止服务 |
