# 后端快速 review：用 30 分钟找到有证据的问题

[返回目录](../../README.md) · [快速开始](../../QUICKSTART.md) · [术语地图](01-backend-map.md) · [数据、异步与安全](03-data-async-security.md)

> 本章提供一套审查节奏。5、15、30 分钟是安排注意力的时间盒，适合范围较小的改动；它们表示审查投入，结论覆盖范围由实际证据决定。涉及迁移、权限变化或多阶段外部副作用时，可以沿最高风险路径继续深入。

你最值得确认的事情是：**这次承诺的行为，在失败、重复和重启时是否仍然成立。** 让模型把报告写成“触发条件—代码位置—实际后果—修复建议—验证结果”，你就能判断问题的份量。

## 1. 先确定审查对象

一次有效 review 要有基线。请先明确这四项：

| 项目 | 需要知道的内容 | 示例 |
| --- | --- | --- |
| 改动范围 | 分支、提交或工作区 diff | “从已确认的基线 SHA 到当前 HEAD” |
| 用户目标 | 此次功能为何存在 | “重复点击导入时得到同一条导入记录” |
| 运行环境 | 桌面、本地服务或公网服务 | “桌面笔记应用；操作系统与存储方式按实际项目填写” |
| 可信依据 | 当前代码、项目约定、真实测试 | “现行 AGENTS/README、已有契约和脚本” |

历史交接记录适合帮助定位，当前仓库和当前分支负责确认事实。先按目标应用的部署方式和现行文档界定范围，再围绕具体行为与风险开展审查。

### 只读起手式

以下命令适用于已经进入目标 Git 仓库的终端。Bash 与 PowerShell 都可逐行执行。请先阅读项目约定，再选需要的命令。

```bash
git status --short
git branch --show-current
git log -5 --oneline
git diff --stat
git diff --cached --stat
git diff --check
rg --files -g AGENTS.md -g package.json -g '*lock*' -g '*test*' -g '*spec*'
```

工作区 diff、暂存区 diff、分支间 diff 是不同范围。审查 PR 时，应先取得真实基线 SHA，再把下面的 `BASE_SHA` 替换为该值：

```bash
git diff --name-status BASE_SHA...HEAD
git diff BASE_SHA...HEAD -- path/to/relevant-file
```

`git diff --check` 主要发现空白等格式问题；它通过以后，继续检查行为。`rg` 未命中也只说明这一种搜索表达没有找到结果。Git 的比较语义见 [git-diff 官方文档](https://git-scm.com/docs/git-diff)。

## 2. 三档时间盒

### 5 分钟：先找值得深入的位置

| 用时 | 做什么 | 产出 |
| --- | --- | --- |
| 0–1 分钟 | 对齐目标与 diff 范围 | 一句话行为目标 |
| 1–2 分钟 | 看涉及的数据写入、外部调用和依赖变更 | 最高风险入口 |
| 2–4 分钟 | 追一条主路径和一个失败分支 | 一个关键问题或已验证事实 |
| 4–5 分钟 | 写明证据与下一项检查 | 可行动的短报告 |

典型关注点：保存前便返回成功、请求参数直接拼进 SQL、重复提交触发多次副作用、异常被捕获后继续显示成功、任务结束后状态还停在运行中。它们是寻找线索的方向；命中关键词后仍要看上下文。

### 15 分钟：把一个功能走完整

在 5 分钟基础上，补齐输入校验、状态变化、错误返回和最贴近风险的一项测试。需要时读被调用模块，直到确认最终行为。

```text
请对这次改动做 15 分钟级别的聚焦 review。
先复述用户目标，再沿一条真实请求追到持久化或外部副作用。
优先检查：输入边界、重复操作、错误传播、重开后的状态。
只报告有具体触发条件与影响的问题；设计偏好放入“可选改进”。
每项附实际文件位置、证据，以及最小验证方法。
```

### 30 分钟：加入一次“坏天气”

把剩余时间用在一个实际风险上：旧版本数据升级、网络结果未知、取消与提交同时发生、重复事件、磁盘写入失败，或两个窗口编辑同一对象。

| 时间 | 审查动作 | 判断标准 |
| --- | --- | --- |
| 0–5 分钟 | 范围与危险写入定位 | 知道在核查哪一个承诺 |
| 5–12 分钟 | 追完整调用链 | 输入、范围、业务、持久化、返回都能定位 |
| 12–20 分钟 | 设计一项反例 | 能触发最可能的损失 |
| 20–26 分钟 | 运行针对性验证 | 记录环境、实际输出和覆盖范围 |
| 26–30 分钟 | 写结论与修复优先级 | 读者知道该改什么、为何现在改 |

大 diff 往往需要先缩小审查范围。让模型说“我完整追踪了材料导入与取消；安装器改动只做静态阅读”，比一个没有范围说明的“已全面 review”更有用。

## 3. 沿一条请求问七个问题

| 位置 | 核心问题 | 能接受的证据 |
| --- | --- | --- |
| 输入 | 字段含义、类型、边界是否清楚？ | 契约、验证函数、边界样例 |
| 范围 | 操作针对哪个用户/项目/文件范围？ | 可信上下文、资源匹配条件、拒绝路径 |
| 业务 | 什么规则必须始终成立？ | 状态迁移规则、业务断言 |
| 持久化 | 什么时候算真正保存？ | 事务边界、提交点、重开读取结果 |
| 外部依赖 | 超时、限流和结果未知怎样处理？ | 依赖适配器、重试分类、幂等策略 |
| 返回 | 界面知道真实状态吗？ | 结果类型、错误码、终态事件 |
| 观测 | 用户能提供哪条线索帮助排错？ | 关联 ID、结构化日志、脱敏示例 |

授权与输入校验解决不同问题。比如参数 `projectId` 是一个合法字符串，仍要确认它是这次操作允许使用的范围。公共服务需要用户或租户授权；个人本地应用也可能只需当前工作区及文件范围校验。应根据实际部署做判断。原理参见 [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)。

## 4. 怎样写一条有用的 finding

下面采用本手册自定义的优先级约定；团队已有标准时，以团队标准为准。

| 级别 | 含义 | 常见例子 |
| --- | --- | --- |
| P0 紧急 | 已证实的广泛严重损失，需要立即处置 | 正在持续破坏用户数据或暴露凭据 |
| P1 高 | 正常或合理使用即可造成重大错误 | 已保存内容丢失、关键流程被阻断、范围越界 |
| P2 中 | 特定条件下的重要缺陷 | 某类取消后任务悬挂、特定输入异常 |
| P3 低 | 影响较小且已有替代路径 | 辅助日志缺少字段、局部提示不准确 |
| 建议 | 设计取舍或潜在改进 | 命名偏好、未来扩展、尚未证明的性能担忧 |

严重度来自影响与触发条件，可信度来自证据。对于尚未复现的疑点，写成“待验证问题”，保留验证路径。把所有代码味道都标为缺陷，会让真正的数据损失被淹没。

### 推荐格式

```text
[P1] 旧编辑窗口保存会覆盖已提交的新版本

位置：实际文件路径与函数，必要时补充行号。
触发：两个窗口先后读取 revision=4；窗口 A 保存后窗口 B 再保存。
后果：窗口 B 的旧草稿覆盖 A 的内容，界面两次都显示成功。
证据：更新语句仅按 noteId 匹配；复现后正文为 B，缺少冲突返回。
建议：保存携带 expectedRevision，并以原子条件更新检查版本。
验证：旧版本保存被识别；数据库仍保留 A；界面保留 B 的草稿。
```

“可能有竞态”“建议加锁”“架构不够优雅”都还缺少决定性信息。继续追问：谁和谁竞争、以什么顺序、损失什么、哪条检查可以证明修复有效。

## 5. 实战：两次保存为什么会丢内容

这是一个原创教学案例，演示 SQLite 的条件更新。它刻意只聚焦版本冲突与项目范围；真实服务还要接入当前项目的身份、输入校验和错误协议。

**场景：** 笔记 revision 为 1。两个窗口都读到这个版本。A 先保存“新发现”，B 随后保存其旧草稿。

有问题的存储逻辑：

```sql
UPDATE notes SET body = ? WHERE id = ?;
```

它满足“写入某个 ID”，却没有表达“基于我读取的版本保存”或“此 ID 属于当前项目”。第二次保存会覆盖第一次。修复可以把两个条件放进同一次更新：

```sql
UPDATE notes
SET body = ?, revision = revision + 1
WHERE id = ?
  AND project_id = ?
  AND revision = ?;
```

然后检查影响行数：更新了一行才算本次成功；零行进入“范围/版本不匹配”的处理。对外可以按产品要求返回统一冲突，或在可信范围内进一步区分原因。SQLite 的 `UPDATE` 条件没有匹配行时会影响零行，业务层应主动解释这个结果。参见 [SQLite UPDATE](https://sqlite.org/lang_update.html)。

### 完整、可运行的微型验证

环境：Python 3 标准库 `sqlite3`，全程使用内存数据库，无需安装依赖或访问真实数据。把这一段保存为 `cas_review_demo.py`，执行 `python cas_review_demo.py`；Windows 环境也可按本机安装方式使用 `py cas_review_demo.py`。

```python
import sqlite3
import unittest


class ScopeOrRevisionConflict(Exception):
    pass


def save_note(db, project_id, note_id, expected_revision, body):
    # 本教学函数接收已经过上层验证的项目范围与参数。
    cur = db.execute(
        """UPDATE notes
           SET body = ?, revision = revision + 1
           WHERE id = ? AND project_id = ? AND revision = ?""",
        (body, note_id, project_id, expected_revision),
    )
    if cur.rowcount != 1:
        raise ScopeOrRevisionConflict()


class NoteSaveBehavior(unittest.TestCase):
    def setUp(self):
        # autocommit 让每个 UPDATE 成为独立提交的语句事务。
        self.db = sqlite3.connect(":memory:", isolation_level=None)
        self.db.execute(
            """CREATE TABLE notes (
                id TEXT PRIMARY KEY,
                project_id TEXT NOT NULL,
                body TEXT NOT NULL,
                revision INTEGER NOT NULL
            )"""
        )
        self.db.execute(
            "INSERT INTO notes VALUES (?, ?, ?, ?)",
            ("n1", "p1", "初稿", 1),
        )

    def tearDown(self):
        self.db.close()

    def read_note(self):
        return self.db.execute(
            "SELECT body, revision FROM notes WHERE id = ?", ("n1",)
        ).fetchone()

    def test_current_version_saves(self):
        save_note(self.db, "p1", "n1", 1, "新发现")
        self.assertEqual(self.read_note(), ("新发现", 2))

    def test_stale_editor_preserves_newer_content(self):
        save_note(self.db, "p1", "n1", 1, "A 的新发现")
        with self.assertRaises(ScopeOrRevisionConflict):
            save_note(self.db, "p1", "n1", 1, "B 的旧草稿")
        self.assertEqual(self.read_note(), ("A 的新发现", 2))

    def test_other_project_preserves_original(self):
        with self.assertRaises(ScopeOrRevisionConflict):
            save_note(self.db, "p2", "n1", 1, "跨项目内容")
        self.assertEqual(self.read_note(), ("初稿", 1))


if __name__ == "__main__":
    unittest.main()
```

这里的测试从业务结果出发：较新的内容被保留、错误范围的写入没有生效。它没有去断言代码必须出现哪段 SQL，因此允许换一种正确实现。复现用确定的先后顺序表达“两个编辑器基于同一旧版本”；要评估多连接锁竞争，还需要另一个专门的并发测试。

**这个例子还没有覆盖：** 上层项目范围的可信来源、进程重启、UI 草稿保留、数据库连接错误、多个表一起提交。这些应根据真实改动选择验证，而非把演示测试的通过扩大成整个系统已通过。

## 6. 让验证分工更可靠

你可以给“实现模型”和“审查模型”不同的输入：

| 角色 | 重点输入 | 期望产出 |
| --- | --- | --- |
| 实现者 | 功能目标、约束、现有结构 | 最小变更与它认为完成的证据 |
| 审查者 | 同一目标、diff、运行入口 | 从用户行为出发构造反例 |
| 你 | 两份结果与演示路径 | 判断真实体验是否达成 |

独立审查者仍然需要理解目标和约束。所谓独立，是让它自行追踪和验证，减少只重复实现者解释的倾向；增加模型数量本身并不会证明正确。

```text
请独立审查当前 diff。先从需求推导 3 个关键不变量，再读实现。
对最高风险的不变量设计一个可复现反例。
使用仓库已有测试工具，优先增加能捕获真实失败的最小验证。
对每个结论注明：静态推断、已复现，或已运行测试。
测试通过后，说明它覆盖的行为，以及仍需目标平台确认的部分。
```

对于 Node 项目，可以使用已有测试框架或官方 `node:test`。先确认项目支持的 Node 版本和脚本，再选择命令；手册不预设所有仓库都有 `npm test`、`lint`、`typecheck`。参见 [Node.js Test runner](https://nodejs.org/api/test.html)。

## 7. 一页交付模板

```text
审查对象：仓库 / 分支 / 基线 SHA / 当前 SHA / 工作区状态
行为目标：
环境：

结论：当前发现了什么，建议如何推进。

问题：
- [优先级] 标题
  触发条件：
  位置与证据：
  用户影响：
  最小修复建议：
  验证方式：

验证记录：
- 命令或步骤：
- 实际结果：
- 对应风险：

剩余边界：哪些路径只阅读了、哪些需要真实环境或目标系统。
可选改进：只有与本次目标相关、且收益明确的建议。
```

一份优质 review 可以很短。一条能防止数据丢失、可复现且修复范围明确的发现，通常比几十条格式建议更值得优先处理。

## 来源与适用范围

核对日期：**2026-10-21**。时间盒、问题分级、模板与示例代码为本手册原创实践设计。

1. [Git — git-diff](https://git-scm.com/docs/git-diff)：比较范围和 diff 命令。
2. [OWASP — Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)：入口与资源范围的授权检查。
3. [SQLite — UPDATE](https://sqlite.org/lang_update.html)：条件更新与零行匹配语义。
4. [Python — sqlite3](https://docs.python.org/3/library/sqlite3.html)：示例使用的标准库接口。
5. [Python — unittest](https://docs.python.org/3/library/unittest.html)：行为验证所用测试框架。
6. [Node.js — Test runner](https://nodejs.org/api/test.html)：Node 项目的测试工具选择。
