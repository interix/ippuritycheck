
# ippuritycheck 项目实施计划

## Context

本项目是一个 macOS 风控监控小程序，用于定时检测 https://ping0.cc 页面上的"风控值"，当超过阈值时触发系统级告警弹窗。

项目当前状态：
- 项目模板已配置完成，包含完整的工程规范和规则
- 尚无实际应用代码
- 需要从零开始构建

根据 main.md 要求，第一步需要调研页面结构，将通过创建分析脚本来完成。

---

## 项目架构设计

### 目录结构（遵循 rules/python-rules.md）

```
ippuritycheck/
├── src/
│   └── ippuritycheck/
│       └── monitor.py          # 主监控程序
├── tests/                      # 测试目录（预留）
├── scripts/                    # 现有脚本目录
│   └── analyze_ping0.py        # 页面结构分析脚本（新增）
├── docs/
│   └── plans/               # 计划归档目录
├── rules/                    # 现有规则目录
├── Makefile                  # 工程统一入口
├── requirements.txt             # Python 依赖
└── README.md                 # 项目说明
```

### 代码结构（单文件 monitor.py）

```python
# 顶部常量配置区
URL = "https://ping0.cc"
CHECK_INTERVAL = 10  # 秒
RISK_THRESHOLD = 20
REQUEST_TIMEOUT = 10
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

# 函数定义
fetch_risk_value() -&gt; float | None
send_alert(value: float) -&gt; bool
log(level: str, msg: str)
main()
```

---

## 实施步骤

### 阶段一：页面结构调研
1. 创建页面分析脚本 `scripts/analyze_ping0.py`
2. 运行脚本获取 ping0.cc 页面内容
3. 分析页面结构，确认风控值的 HTML 元素或 API 接口
4. 更新 monitor.py 中的解析逻辑

### 阶段二：项目初始化
1. 创建目录结构（src/ippuritycheck/, tests/, docs/plans/）
2. 创建 requirements.txt（requests, beautifulsoup4）
3. 创建 Makefile（包含 help, deps, check-deps, clean, build, test, release）
4. 更新 README.md

### 阶段三：实现 monitor.py
1. 实现常量配置区
2. 实现 log() 函数（带时间戳的日志输出）
3. 实现 fetch_risk_value() 函数（网络请求 + 解析）
4. 实现 send_alert() 函数（AppleScript 弹窗）
5. 实现 main() 主循环
6. 异常处理覆盖所有要求场景

### 阶段四：验证与测试
1. 本地测试运行
2. 验证告警功能
3. 验证异常处理

---

## 关键文件清单

| 文件路径 | 用途 |
|---------|------|
| `scripts/analyze_ping0.py` | 页面结构分析脚本 |
| `src/ippuritycheck/monitor.py` | 主监控程序 |
| `requirements.txt` | Python 依赖声明 |
| `Makefile` | 工程统一入口 |
| `README.md` | 项目使用说明 |
| `docs/plans/2026-04-10-ippuritycheck-implementation-plan.md` | 本计划归档 |

---

## 风险与注意事项

1. **页面结构风险**：ping0.cc 页面结构可能变化，导致解析失败
   - 缓解：解析逻辑需健壮，失败时记录日志不崩溃

2. **macOS 权限**：AppleScript 弹窗可能需要权限
   - 缓解：提供备用通知中心方案

---

## 验证计划

1. 依赖安装：`make deps`
2. 环境检查：`make check-deps`
3. 页面分析：`python scripts/analyze_ping0.py`
4. 程序运行：`python src/ippuritycheck/monitor.py`
5. 测试告警：可临时调低阈值验证
6. 后台运行：按 README 说明测试

---

## 与项目规则的一致性

- ✅ 遵循 Python 目录规范（src/, tests/, scripts/）
- ✅ 提供 Makefile 统一入口
- ✅ 一次只解决一个明确问题（风控监控程序）
- ✅ 变更记录到 claude-input.log

---

## 页面分析结果（已完成）

通过 `scripts/analyze_ping0.py` 分析发现：
- 页面使用 Vue.js，但风控值在静态 HTML 中
- 风控值位置：`<span class="value">9%</span>`
- 示例值：9%（极度纯净）
- 阈值区间：0-15 极度纯净，15-25 纯净，25-40 中性，40-50 轻微风险，50-70 稍高风险，70-100 极度风险
