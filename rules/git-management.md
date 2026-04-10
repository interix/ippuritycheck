你现在作为我的代码助手，必须严格遵守以下 Git 分支管理规范。

【分支基本原则】
1. 所有代码修改都必须在独立分支上完成。
2. 不允许直接在 main 或 master 分支上开发。
3. 一个分支只处理一个明确任务，不要把多个需求混在同一个分支里。
4. 如果任务范围扩大，必须提醒我拆分成多个分支。

【分支命名规范】
分支名格式：
<type>/<short-description>

其中：
- type 仅允许以下值：
  - feat
  - fix
  - refactor
  - docs
  - test
  - chore

- short-description 规范：
  1. 使用英文
  2. 全部小写
  3. 单词之间用中划线连接
  4. 不要超过 3~6 个关键词
  5. 不允许出现空格、中文、特殊字符
  6. 必须体现任务目的，而不是泛泛写成 update、modify、change

【示例】
- feat/mario-auto-player
- feat/add-gamepad-controller
- fix/rom-load-error
- fix/python-env-issue
- refactor/split-training-module
- docs/add-install-guide
- test/add-env-smoke-test
- chore/update-dependencies

【执行规则】
1. 每次开始新任务前，先分析任务内容。
2. 先给出建议分支名，不要直接修改代码。
3. 输出格式必须为：

建议分支名：
分支类型：
命名原因：
预计修改文件：

4. 只有在我确认后，你才可以创建分支并开始修改。
5. 未经我明确确认，不要执行以下操作：
   - git commit
   - git merge
   - git rebase
   - git push
   - git reset
   - git revert
   - 删除分支

【额外要求】
如果我给出的任务描述不清晰，你也要先尽量归纳成一个合理的任务名，并生成规范分支名。
如果一个任务同时包含功能开发和 bug 修复，请优先提醒我拆分，而不是直接混成一个分支。
