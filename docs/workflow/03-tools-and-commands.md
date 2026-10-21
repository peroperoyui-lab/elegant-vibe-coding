# 术语、命令与工具适配速查

[返回目录](../../README.md) · [快速开始](../../QUICKSTART.md) · [22 份指令](02-prompt-recipes.md)

> **核验日期：2026-10-21。** 下列产品入口依据当日官方文档。使用时先看本机版本、`--help` 和界面里的实际菜单；仓库的真实命令与当前约定优先。示例分支名、文件名和 `BASE` 等占位项需要按现场替换。

## 1. 五种“指令”，分别发给谁

| 类型 | 发给谁、放在哪里 | 示例 | 它的作用 |
|---|---|---|---|
| 自然语言任务 | 模型会话 | “检查导入失败后的重试行为，并给证据” | 说明目标，由代理选择工具 |
| Shell 命令 | 终端，如 PowerShell、Bash | `git status --short` | 由程序解析并执行 |
| 斜杠命令 Slash command | 特定产品的聊天输入框 | Codex 的 `/review` | 触发产品内置功能或已安装扩展 |
| 项目规则 Project instructions | 项目认可的说明文件 | `AGENTS.md`、`CLAUDE.md` | 提供多次任务共用的背景与约定 |
| API / 工具调用 Tool call | 代理运行时或应用代码 | 一个注册工具的名字与结构化参数 | 通过已定义接口执行具体操作 |

`/review` 粘进系统终端不会自动变成代码审查；`git diff` 发给聊天模型，通常意味着请求模型调用终端执行。社区教程中的 `/generate-prp`、`/opsx:...` 等命令往往来自扩展。先确认扩展已安装且当前版本确实注册该命令，再按其文档使用。

**CLI** 是命令行接口，例如 Git 或 Claude Code；**Shell** 是解析命令的环境，例如 PowerShell；**Terminal** 是承载 Shell 的窗口。理解这三个词，能解释很多“同一条命令在别人电脑能跑”的问题。

## 2. 开发协作词典

| 英文与常见说法 | 通俗解释 | 你可以怎样指挥模型 |
|---|---|---|
| Repository / repo，仓库 | 代码、文档及版本历史的集合 | “先确认当前仓库和相关约定。” |
| Working tree，工作区 | 你目前实际看到和编辑的文件 | “保留当前未提交改动。” |
| Staging area / index，暂存区 | 准备进入下次提交的改动集合 | “检查暂存区是否只包含本次任务。” |
| Commit，提交 | 带说明与唯一标识的版本记录 | “按独立行为组织提交。” |
| Branch，分支 | 一条可独立推进的版本线 | “在本次任务分支完成。” |
| Diff，差异 | 两个状态之间具体改了什么 | “逐项解释这份 diff 与目标的关系。” |
| Base / head，基线与目标版本 | 审查从哪版比到哪版 | “以已确认基线比较当前 head。” |
| Pull request / PR | 请求审阅并集成一组改动 | “写清原问题、改变和验证。” |
| Merge conflict，合并冲突 | 两组修改在同一位置难以自动整合 | “先解释双方意图，再给合并结果。” |
| Worktree，独立工作目录 | 同仓库另一分支的一套文件目录 | “让两个实施任务各用一个 worktree。” |
| Regression，回归缺陷 | 新改动破坏了原本可用的行为 | “检查最接近本次改动的原有流程。” |
| Reproduction / repro，复现 | 稳定触发同一问题的方法 | “把问题压缩成最短复现步骤。” |
| Root cause，根因 | 导致现象的实际原因 | “沿调用链找第一次偏离预期的位置。” |
| Patch，补丁 | 一组范围明确的文件修改 | “给能解决根因的最小补丁。” |
| Refactor，重构 | 保持外部行为，改善内部组织 | “用行为对照验证重构。” |
| Technical debt，技术债 | 为速度而留下、未来要付出的维护成本 | “指出它会增加哪项实际维护工作。” |
| Acceptance criteria，验收条件 | 判断任务完成的具体依据 | “每条验收写成输入、操作、结果。” |
| Definition of done，完成定义 | 项目交付共同要求 | “检查项目既有完成标准。” |
| Gate，交付检查关口 | 进入下一步前必须满足的项目条件 | “执行仓库定义的交付 gate。” |
| Smoke test，冒烟检查 | 快速检查核心路径能否运转 | “启动并走通一条主要用户任务。” |
| Fixture，测试样例 | 可重复使用的固定输入或状态 | “用脱敏 fixture 重现异常。” |
| Mock，模拟替身 | 用可控对象代替某个外部依赖 | “注明哪些依赖被 mock。” |
| Integration test，集成测试 | 检查多个模块真实协作 | “验证 UI 之后的服务与存储接线。” |
| E2E，端到端测试 | 从用户入口到最终结果的完整操作 | “沿真实入口验证保存与恢复。” |
| CI，持续集成 | 在集中环境自动运行检查 | “区分本地通过与 CI 通过。” |
| Artifact，构建或工作产物 | 安装包、报告、截图、导出文件等成果 | “说明产物路径与生成方式。” |
| Handoff，交接 | 让另一个会话继续工作的精简记录 | “保留事实、证据和下一步。” |
| ADR，架构决定记录 | 说明为什么选这一方案 | “记录背景、决定、代价与替代方案。” |
| Context window，上下文窗口 | 当前推理可使用的信息容量 | “保留当前事实，归档过期尝试。” |
| Compaction，上下文压缩 | 将已有会话整理为更短的续接内容 | “压缩前留下未解决问题与证据。” |
| Harness，代理执行环境 | 给模型提供工具、状态与执行循环的软件 | “区分模型能力与运行环境能力。” |
| Skill，任务技能包 | 可按需使用的流程说明及资源 | “只加载当前任务需要的技能。” |
| MCP，工具与上下文连接协议 | 让应用以约定方式向模型暴露能力 | “说明该工具连接什么服务、允许什么操作。” |
| Hook，事件钩子 | 某事件发生时触发的动作 | “先检查触发时机与副作用。” |
| Prompt，任务提示 | 给模型的目标、背景与约束 | “让提示包含可观察验收。” |
| Token，词元 | 模型处理文本等输入输出的计量单位 | “为上下文保留必要证据，按任务设置预算。” |

这份词典采用开发现场常用含义。Git 中具体状态和命令行为以官方手册为准；`Skill`、`MCP`、`Hook` 的可用范围以所在代理产品为准。[G1]、[G2]、[A1]、[A2]

## 3. 第一次进入项目：只读盘点

下面命令适用于已经安装相应程序的 Bash 或 PowerShell。每行独立执行，先确认当前目录就是目标仓库。

```sh
git status --short --branch
git branch --show-current
git log -5 --oneline
git diff --stat
git diff --cached --stat
```

前三行帮助确认现场；后两行分别概览未暂存和已暂存的修改。[G7]、[G8]新建且尚未跟踪的文件要从 `git status` 查看，它们不会自动出现在普通 `git diff` 中。[G1]、[G2]

找项目说明和包配置：

```sh
rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g 'README*' -g 'package.json' -g '*lock*'
```

查相关实现时，先限定目录和关键词。以下仅是假设项目有 `src` 目录的例子：

```sh
rg -n 'importMaterial|materialId' src
rg -n -F 'TASK_CANCELLED' src
```

`-n` 显示行号，`-F` 按普通文字匹配。ripgrep 默认遵守忽略规则并跳过隐藏文件；要检查隐藏目录中的项目配置，应明确指定该目录或按需使用 `--hidden`，同时排除 `.git` 和依赖目录。[G3]

这一步只收集事实。读取测试脚本时，要看它是否清理数据、写快照、启动服务或访问外部账户，然后选择合适的临时环境执行。

## 4. 看懂 diff：审查哪一份变化

| 命令 | 比较什么 |
|---|---|
| `git diff` | 工作区相对暂存区的已跟踪文件变化 |
| `git diff --cached` | 暂存区相对当前提交的变化 |
| `git diff HEAD` | 工作区与暂存区合起来，相对当前提交的已跟踪变化 |
| `git diff BASE...HEAD` | 从共同祖先到 `HEAD` 的提交变化，常用于分支审查 |
| `git diff BASE HEAD` | 两个指定提交对应文件状态的直接差异 |
| `git diff --check` | 检查差异中的部分空白错误与冲突标记 |

`BASE` 必须替换成已经确认存在的分支名或 commit。三点比较适合看一个分支带来的工作，但它只覆盖提交差异；当前未提交内容仍需单独检查。`--check` 通过仅说明对应格式检查通过。[G2]

对模型说：

> 请审查 `{{BASE}}...{{HEAD}}`，同时单列当前未提交改动。先给变更行为地图，再追踪影响最大的两条路径。审查结论附真实位置与触发条件。

当项目没有提交历史、基线尚未确认时，先描述实际现场。不要为了凑一个比较命令而假定默认分支一定叫 `main`。

## 5. 分支与 worktree：什么时候用哪个

**一个人顺序做一项任务**，普通分支往往已经够用。下面命令会创建并切换分支，需要在已确认的工作区和项目约定下执行：

```sh
git switch -c feat/material-empty-state
```

分支名是示例。它不会把原有未提交改动自动变成一个提交；先检查改动归属，再决定怎样处理。[G4]

**两个代理同时实施不同任务**，可以考虑 worktree。下面同样是会写入工作区的操作，假定目录和分支名尚未使用，并以当前 `HEAD` 为起点：

```sh
git worktree add ../worktree-material-preview -b feat/material-preview HEAD
git worktree list
```

第一条创建独立目录与新分支；第二条查看已登记的工作目录。起点是否应该用 `HEAD`，由项目当前基线决定。完成后先提交或保留需要的成果，再按 Git 官方方法移除工作目录。[G5]

**隔离的对象要说清楚**：worktree 隔离文件编辑与分支工作。两个应用进程仍可能同时访问同一数据库、用户配置或服务端口。并行任务简报里把这些位置写明，尤其是需要跑桌面应用或数据库测试的任务。

## 6. Node 项目：先发现命令，再运行

进入包含 `package.json` 的目录后，可先检查：

```sh
node --version
npm --version
npm pkg get packageManager engines scripts
npm run
```

`npm pkg get` 读取指定元数据；`npm run` 在没有脚本名时列出脚本。[N1]、[N2] 然后根据 `packageManager`、锁文件和项目说明，使用项目指定的 npm、pnpm、Yarn 或其他工具。

| 看到的东西 | 下一步怎样判断 |
|---|---|
| `scripts.test` | 读实际命令，确认测试范围与外部依赖 |
| `scripts.check` / `verify` | 看它具体包含哪些检查，名称没有统一含义 |
| `scripts.dev` | 确认启动端口、所需配置与是否连接真实服务 |
| `package-lock.json` | 结合项目说明判断是否采用 npm 的锁定依赖流程 |
| 多种锁文件 | 检查历史和约定，确认当前权威文件 |
| `workspaces` | 确认应在仓库根目录还是子包执行 |

把命令发现写进提示词：

> 请读取当前项目的脚本定义，再选择能验证本次行为的命令。报告脚本实际覆盖什么；缺少对应脚本时，给出可重复的替代验证。

`npm ci` 用已有锁文件安装，要求包清单与锁文件相符，并会替换现有依赖安装目录；安装过程可能执行生命周期脚本。它是环境准备操作，适合已审阅依赖与脚本的受控工作区。[N3] 普通文档审查或静态阅读无需先安装整套依赖。

## 7. Claude Code 与 Codex：最少掌握的入口

### Claude Code

终端中的官方入口包括：[A1]

| 命令 | 用途 |
|---|---|
| `claude --help` | 查看本机版本支持的参数 |
| `claude --version` | 查看版本 |
| `claude` | 启动交互会话 |
| `claude -c` | 继续当前目录最近一次会话 |
| `claude -r` | 选择或恢复已有会话 |
| `claude -p "说明这段代码的作用"` | 一次性请求后退出 |

一次性模式仍是代理执行方式，实际允许做什么由权限、工具和任务决定。需要只读时，应同时指定只读目标并检查环境的权限模式。

会话内的 `/help` 用于发现当前命令；`/memory` 用于查看或调整说明文件相关入口；`/compact` 用于压缩会话。自定义命令和插件命令以实际安装结果为准。[A2]

### Codex

官方文档列出这些基本入口：[O1]

| 命令或入口 | 用途 |
|---|---|
| `codex --help` / `codex --version` | 查看本机能力与版本 |
| `codex` | 开始交互任务 |
| `codex resume` | 恢复已有会话 |
| `codex review --uncommitted` | 对当前未提交变化发起审查 |
| 会话内 `/plan` | 进入规划模式 |
| 会话内 `/review` | 发起工作区审查 |

审查参数有组合限制。当前官方说明中，`--uncommitted`、`--base`、`--commit` 与自定义 review prompt 是互斥目标选择；复制命令前用 `codex review --help` 核对本机语法。[O1]

脚本化任务另有 `codex exec`，适用于受控自动化；普通个人开发从交互任务开始更容易看清执行环境与现场反馈。[O2]

### Cursor 与 GitHub Copilot

这两者都可能出现在不同界面和执行环境中。先确认是编辑器聊天、命令行、云端代理还是代码审查功能，再查对应文档。一个产品中的规则或命令支持，不会自动覆盖它的所有入口。

本手册用自然语言模板表达目标，减少对专有命令的依赖。需要产品模式时，在当前菜单选择规划、实施或审查；需要规则时，使用下面已核验的说明文件路径。

<a id="rules"></a>
## 8. 项目规则文件对照

| 工具 | 当日官方文档中的主要入口 | 实用选择 |
|---|---|---|
| Codex | `AGENTS.md`；支持按目录发现和更具体的覆盖规则 | 把共享项目事实放在短说明中，详细机制见官方发现顺序 |
| Claude Code | `CLAUDE.md`、`.claude/rules/`；新版本也有带条件的 `AGENTS.md` 支持 | 先确认实际加载结果，需要兼容时使用官方文档中的导入方式 |
| Cursor | `.cursor/rules/*.mdc`；根目录和子目录的 `AGENTS.md` | 简单项目用短 Markdown；需要路径匹配与启用条件时用规则文件 |
| GitHub Copilot | `.github/copilot-instructions.md`、`.github/instructions/*.instructions.md`；部分功能识别 agent 说明文件 | 核对当前客户端的支持矩阵，选择覆盖所需入口的形式 |

来源分别为 [O3]、[A3]、[C1]、[C2]。这张表核对的是入口；最终生效仍取决于版本、工作目录、配置与具体功能。

### 一个容易踩中的时效差异

2026-10-21 的 Claude Code 官方说明已经包含 `AGENTS.md` 支持，但加载行为受版本和 Project instructions 配置影响；默认规则还与是否存在 `CLAUDE.md` 等文件有关。需要兼容共享规范时，官方保留了在 `CLAUDE.md` 中使用 `@AGENTS.md` 导入的办法。[A3]

因此，更稳妥的操作是：请工具列出本次实际读取的说明文件，再核对内容。**文件存在、模型已经读取、规则能够一致执行，是三件需要分别确认的事。**

### “一个共享文件”的维护办法

把长期事实维护在项目已经选定的一个权威入口；工具专有文件只保留必要的适配内容。若某工具支持导入，按它的文档导入；若需要同步副本，明确同步来源和更新办法。避免两份文档分别发展成不同的架构描述。

Cursor 的 `.mdc` 与普通 Markdown 有不同格式要求；Copilot 的路径限定说明也有自己的约定。把文件换个名字，通常不足以完成跨工具适配。[C1]、[C2]

## 9. 把执行权限说得具体

| 任务意图 | 建议表达 | 重点 |
|---|---|---|
| 只想看结论 | “只读检查，给出证据与建议。” | 同时核对代理的权限环境 |
| 允许本地修复 | “在这些文件和任务范围内完成修改并验证。” | 范围与验收明确 |
| 允许提交 | “验证后按仓库约定提交到本任务分支。” | 分支、改动归属明确 |
| 允许写远端 | “把已验证改动推送到指定仓库的指定分支。” | 远端目标准确 |
| 允许上线 | “将这个已验收版本部署到指定环境。” | 版本、环境、数据影响明确 |

自然语言约定负责表达授权范围；真正的隔离由工具权限、沙箱、账户和运行配置提供。一般任务无需关闭保护或放开所有工具。给代理足够完成任务的权限，并把额外能力与具体工作相联系。

## 10. 出错后如何恢复思路

| 发生什么 | 先做什么 | 接下来的恢复方向 |
|---|---|---|
| 模型改错文件 | 查看 `git status` 与相关 diff | 按文件归属保留需要的改动，只撤销明确的本次错误 |
| 提交后发现行为回归 | 定位引入问题的 commit | 可采用修复提交，或用 `git revert` 生成反向提交 |
| 分支找不到了 | 只读检查 `git reflog` | 在确认版本后建立恢复分支 |
| 合并冲突 | 读冲突两边与原始要求 | 形成保留双方正确意图的结果，再验证 |
| 新依赖引发故障 | 对照包清单、锁文件与环境变化 | 恢复明确的依赖版本组合，再按项目方式安装 |
| 会话漂移 | 记录当前事实、复现、已证伪假设 | 新会话从简短 handoff 继续 |

`git reflog` 可查询本地引用位置的历史，用于定位可恢复的版本。[G9] `git revert` 通过新提交表达撤销，适合需要保留共享历史的场景。[G6] `reset --hard` 会改变文件现场，强制推送会改写共享分支的可见历史；它们需要明确目标与影响，日常修复通常有更容易审查的办法。这里提供恢复方向，实际操作应基于当前工作区。

## 本章官方来源

Git 和搜索：

- [G1] Git status。
- [G2] Git diff。
- [G3] ripgrep 官方仓库。
- [G4] Git switch。
- [G5] Git worktree。
- [G6] Git revert。
- [G7] Git log。
- [G8] Git branch。
- [G9] Git reflog。

包管理：

- [N1] npm pkg。
- [N2] npm run。
- [N3] npm ci。

代理产品：

- [A1] Claude Code CLI reference。
- [A2] Claude Code Commands。
- [A3] Claude Code Memory。
- [O1] Codex Developer commands；旧路径可能重定向到官方 ChatGPT Learn。
- [O2] Codex Non-interactive mode。
- [O3] Codex AGENTS.md。
- [C1] Cursor Rules。
- [C2] GitHub Copilot Custom instructions。

全部查阅于 **2026-10-21**。命令示例用于讲解，没有在读者的真实项目上自动执行。

[G1]: https://git-scm.com/docs/git-status
[G2]: https://git-scm.com/docs/git-diff
[G3]: https://github.com/BurntSushi/ripgrep
[G4]: https://git-scm.com/docs/git-switch
[G5]: https://git-scm.com/docs/git-worktree
[G6]: https://git-scm.com/docs/git-revert
[G7]: https://git-scm.com/docs/git-log
[G8]: https://git-scm.com/docs/git-branch
[G9]: https://git-scm.com/docs/git-reflog
[N1]: https://docs.npmjs.com/cli/v11/commands/npm-pkg/
[N2]: https://docs.npmjs.com/cli/v11/commands/npm-run/
[N3]: https://docs.npmjs.com/cli/v11/commands/npm-ci/
[A1]: https://code.claude.com/docs/en/cli-reference
[A2]: https://code.claude.com/docs/en/commands
[A3]: https://code.claude.com/docs/en/memory
[O1]: https://developers.openai.com/codex/developer-commands
[O2]: https://developers.openai.com/codex/non-interactive-mode
[O3]: https://developers.openai.com/codex/agent-configuration/agents-md
[C1]: https://cursor.com/docs/rules
[C2]: https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions
