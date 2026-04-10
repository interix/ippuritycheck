.PHONY: help deps check-deps clean build test release

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

help:
	@echo "ippuritycheck - macOS 风控监控小程序"
	@echo ""
	@echo "可用 targets:"
	@echo "  help        - 显示此帮助信息"
	@echo "  deps        - 安装项目依赖"
	@echo "  check-deps  - 检查依赖状态"
	@echo "  clean       - 清理临时文件"
	@echo "  build       - 构建项目（当前无需构建）"
	@echo "  test        - 运行测试（当前无测试）"
	@echo "  release     - 打包发布（当前无需打包）"
	@echo ""
	@echo "运行方式:"
	@echo "  前台运行:  make run"
	@echo "  后台运行:  make start"
	@echo "  查看状态:  make status"
	@echo "  停止服务:  make stop"

deps:
	@echo "正在安装依赖..."
	@if [ ! -d "$(VENV)" ]; then \
		echo "创建虚拟环境..."; \
		python3 -m venv $(VENV); \
	fi
	@$(PIP) install -q -r requirements.txt
	@echo "依赖安装完成"

check-deps:
	@echo "检查依赖状态..."
	@if [ ! -d "$(VENV)" ]; then \
		echo "❌ 虚拟环境不存在，请运行: make deps"; \
		exit 1; \
	fi
	@if [ ! -f "$(VENV)/bin/activate" ]; then \
		echo "❌ 虚拟环境损坏，请运行: make deps"; \
		exit 1; \
	fi
	@$(PYTHON) -c "import requests; import bs4" 2>/dev/null && \
		echo "✅ 依赖已就绪" || \
		(echo "❌ 依赖不完整，请运行: make deps"; exit 1)

clean:
	@echo "清理临时文件..."
	@rm -f ping0_page.html
	@rm -f monitor.log
	@rm -f nohup.out
	@rm -rf __pycache__
	@rm -rf *.pyc
	@echo "清理完成"

build:
	@echo "构建项目（本项目无需构建步骤）"

test:
	@echo "运行测试（当前无测试用例）"

release:
	@echo "打包发布（当前无需打包）"

run:
	@$(PYTHON) src/ippuritycheck/monitor.py

start:
	@echo "启动后台服务..."
	@nohup $(PYTHON) src/ippuritycheck/monitor.py > monitor.log 2>&1 &
	@echo "服务已启动，日志: monitor.log"
	@echo "查看状态: make status"

status:
	@ps aux | grep "src/ippuritycheck/monitor.py" | grep -v grep || echo "服务未运行"

stop:
	@echo "停止服务..."
	@-pkill -f "src/ippuritycheck/monitor.py" 2>/dev/null || true
	@echo "已停止"
