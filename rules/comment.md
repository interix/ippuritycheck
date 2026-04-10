从现在开始，你必须严格按照以下规范编写 commit message。除非我明确要求，否则你不得偏离这些规则。

==============================
一、基本格式
==============================

所有 commit message 必须使用以下格式：

<type>: <summary>

示例：
- feat: add mario auto-player environment
- fix: handle rom loading failure on apple silicon
- refactor: split training logic into separate module
- docs: add setup instructions for local development
- test: add smoke test for emulator startup
- chore: pin python dependencies for macos

==============================
二、type 允许值
==============================

type 只允许以下 6 类：

- feat      新功能
- fix       修复 bug
- refactor  重构（不改变外部行为）
- docs      文档修改
- test      测试相关
- chore     工程、依赖、配置、脚本等杂项

不得使用未定义类型，除非我明确要求扩展。

==============================
三、summary 编写要求
==============================

summary 必须遵守以下要求：

1. 必须具体说明“本次改动做了什么”。
2. 尽量写出改动对象、模块、场景或行为。
3. 必须简洁清晰，一行内表达完整意思。
4. 不允许空泛、模糊、无信息量的描述。
5. summary 默认使用英文；如果我明确要求中文，再改用中文。
6. 不要使用句号结尾。

推荐写法：
- feat: add rule-based mario agent
- fix: prevent crash when rom file is missing
- refactor: move controller logic into agent module
- docs: document emulator setup steps
- test: add startup validation for mario env
- chore: update local development scripts

不允许的写法：
- update
- change code
- fix bug
- optimize code
- misc changes
- cleanup
- wip
- final
- try
- adjust logic
- improve something

==============================
四、类型选择规则
==============================

请按以下规则判断 type：

1. feat
   - 新增功能、新增能力、新增接口、新增脚本入口
   - 例：feat: add ppo training entry script

2. fix
   - 修复已有 bug、异常、错误行为、兼容性问题
   - 例：fix: resolve rom path parsing error

3. refactor
   - 只改变内部结构，不改变外部行为
   - 例：refactor: split env setup from training flow

4. docs
   - 仅修改文档、说明、注释型资料
   - 例：docs: add apple silicon setup guide

5. test
   - 新增或修改测试
   - 例：test: add smoke test for emulator startup

6. chore
   - 依赖、配置、脚本、工程整理、非业务逻辑杂项
   - 例：chore: pin python package versions

如果一次改动无法明确归入其中一类，必须先指出原因，而不是随意选择。

==============================
五、拆分提交规则
==============================

如果一次改动同时包含以下任意情况，你必须先提醒我拆分提交，而不是直接生成一个笼统的 commit message：

1. 同时包含新功能和 bug 修复
2. 同时包含功能开发和重构
3. 同时包含代码修改和大块文档更新
4. 同时涉及多个相互独立的模块
5. 无法用一句话准确概括主要改动

此时你必须输出：

- 是否建议拆分提交：是
- 拆分原因：
- 建议拆分后的 commit message：
  - ...
  - ...
  - ...

==============================
六、输出要求
==============================

每次我让你整理 commit message 时，你必须按以下格式输出：

推荐 commit message：
<type>: <summary>

备选 commit message：
<type>: <summary>

type 选择原因：
- 说明为什么选择这个 type
- 说明 summary 为什么准确

是否建议拆分提交：
- 是 / 否

如果建议拆分提交：
- 拆分原因：
- 建议拆分后的提交方案：

==============================
七、质量要求
==============================

你生成的 commit message 必须满足以下标准：

1. 未来我只看 commit message，也能大致知道这次改动做了什么。
2. 不能只描述“改了代码”，必须描述“改了什么方面的代码”。
3. 不能把多个目的混成一句模糊描述。
4. 若本次改动超出原任务范围，必须在说明中指出。
5. 若本次改动边界不清，优先建议拆分，而不是勉强命名。

==============================
八、禁止事项
==============================

未经我明确允许，你禁止：

1. 用空泛词生成 commit message
2. 为多目标改动强行生成单一笼统 message
3. 隐瞒本次改动实际包含的多个目的
4. 把 refactor 错写成 feat 或 fix
5. 把依赖、配置、脚本整理误写成 feat
6. 在没有判断改动边界前直接给出 commit message

从现在开始，所有 commit message 都必须严格按以上规则执行。
