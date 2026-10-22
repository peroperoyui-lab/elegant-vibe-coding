# 来源与核验说明

[返回目录](README.md) · [资源阅读地图](docs/workflow/04-reading-map.md)

## 这本手册怎样使用资料

初始版本记录的查阅日期为 **2026-10-21**；后续新增或复核的资料按各章及下表逐项记录。内容更新日期与资料查阅日期分别维护，重建索引本身不会更新查阅日期。设计规范与技术行为优先使用标准组织、工具维护者和厂商官方文档；社区仓库直接读取维护者说明。章节中的教学场景、中文指令、比较维度、图解和模板是围绕读者任务编排的原创内容。

| 内容类型 | 采用方式 | 适用边界 |
|---|---|---|
| W3C / WAI、协议标准 | 核对具体条款、等级、条件和例外 | 抽取常用条款并不构成完整符合性认证 |
| SQLite、Node、Git、框架官方文档 | 核对接口、事务、命令和实际语义 | 本机版本、配置和项目封装仍需确认 |
| 编码工具官方文档 | 核对说明文件、命令与功能入口 | 版本与客户端会影响可用行为 |
| 代表性开源仓库 | 介绍用途、可借鉴方法与采用成本 | README 核验与完整代码/安全/维护质量审计有不同范围 |
| 思考方法的原始研究、作者说明与机构资料 | 核对方法含义、研究对象与证据范围 | 迁移到 AI 协作的示例和组合为本手册编排，效果需按任务验证 |
| 本手册建议 | 用任务、示例与证据解释取舍 | 可按现有项目简化和调整 |

“热门”在这里落实为有代表性的公开项目清单；本版没有做趋势采样或按星标排名。资源越多，理解与维护成本也越多，选择应回到当前任务。

## 易变信息怎样维护

使用工具命令前确认本机版本与帮助；升级后重新核对规则文件加载方式。引用原页面可能重定向到维护者的新域名，优先使用正式的新入口。长期有效的设计判断，与某一版本的命令语法分别维护。

核验新来源或重新查阅后，在 [source-verifications.json](references/source-verifications.json) 登记 URL 与日期；生成器同时保留旧索引中的日期。没有日期记录的新 URL 会标为“未记录”，待实际查阅后补充。

## 章节引用索引 · 122 个 URL

以下由正文引用自动整理；同一页面的不同锚点保留，故 URL 数量不等同于独立文献数量。每条来源的具体用途见相应章节。机器可读清单为 [source-index.json](references/source-index.json)。

| 来源页面 | 出现章节 | 记录的查阅日期 |
|---|---|---|
| [agents.md/](https://agents.md/) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [atlassian.design/tokens/design-tokens/](https://atlassian.design/tokens/design-tokens/) | [frontend/01](docs/frontend/01-visual-language.md) · [frontend/02](docs/frontend/02-design-system.md) | 2026-10-21 |
| [awesome-copilot.github.com/](https://awesome-copilot.github.com/) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [aws.amazon.com/blogs/enterprise-strategy/mental-models-for-your-digital-transformation/](https://aws.amazon.com/blogs/enterprise-strategy/mental-models-for-your-digital-transformation/) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) | [backend/04](docs/backend/04-agent-runtime-review.md) | 2026-10-21 |
| [cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | [backend/01](docs/backend/01-backend-map.md) · [backend/02](docs/backend/02-review-in-30-minutes.md) | 2026-10-21 |
| [cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) | [backend/01](docs/backend/01-backend-map.md) | 2026-10-21 |
| [cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) | [backend/04](docs/backend/04-agent-runtime-review.md) | 2026-10-21 |
| [cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | [backend/01](docs/backend/01-backend-map.md) · [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [classics.mit.edu/Aristotle/physics.1.i.html](https://classics.mit.edu/Aristotle/physics.1.i.html) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) | [workflow/01](docs/workflow/01-agentic-workflow.md) · [workflow/02](docs/workflow/02-prompt-recipes.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference) | [workflow/03](docs/workflow/03-tools-and-commands.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [code.claude.com/docs/en/commands](https://code.claude.com/docs/en/commands) | [workflow/03](docs/workflow/03-tools-and-commands.md) | 2026-10-21 |
| [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) | [workflow/03](docs/workflow/03-tools-and-commands.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [community.owasp.org/attacks/Path_Traversal](https://community.owasp.org/attacks/Path_Traversal) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [cursor.com/docs/rules](https://cursor.com/docs/rules) | [workflow/03](docs/workflow/03-tools-and-commands.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [developer.mozilla.org/en-US/docs/Web/API/AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) | [cases/02](docs/cases/02-feature-walkthrough.md) | 2026-10-21 |
| [developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [developer.mozilla.org/en-US/docs/Web/API/WebSockets_API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties) | [frontend/02](docs/frontend/02-design-system.md) | 2026-10-21 |
| [developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries) | [frontend/01](docs/frontend/01-visual-language.md) · [frontend/02](docs/frontend/02-design-system.md) | 2026-10-21 |
| [developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion) | [frontend/01](docs/frontend/01-visual-language.md) | 2026-10-21 |
| [developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length) | [frontend/01](docs/frontend/01-visual-language.md) | 2026-10-21 |
| [developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | [workflow/01](docs/workflow/01-agentic-workflow.md) | 2026-10-21 |
| [developers.openai.com/codex/agent-configuration/agents-md](https://developers.openai.com/codex/agent-configuration/agents-md) | [workflow/01](docs/workflow/01-agentic-workflow.md) · [workflow/03](docs/workflow/03-tools-and-commands.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [developers.openai.com/codex/developer-commands](https://developers.openai.com/codex/developer-commands) | [workflow/03](docs/workflow/03-tools-and-commands.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [developers.openai.com/codex/non-interactive-mode](https://developers.openai.com/codex/non-interactive-mode) | [workflow/03](docs/workflow/03-tools-and-commands.md) | 2026-10-21 |
| [developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex) | [workflow/02](docs/workflow/02-prompt-recipes.md) | 2026-10-21 |
| [docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions) | [workflow/02](docs/workflow/02-prompt-recipes.md) · [workflow/03](docs/workflow/03-tools-and-commands.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [docs.npmjs.com/cli/v11/commands/npm-audit/](https://docs.npmjs.com/cli/v11/commands/npm-audit/) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [docs.npmjs.com/cli/v11/commands/npm-ci/](https://docs.npmjs.com/cli/v11/commands/npm-ci/) | [backend/03](docs/backend/03-data-async-security.md) · [workflow/03](docs/workflow/03-tools-and-commands.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [docs.npmjs.com/cli/v11/commands/npm-pkg/](https://docs.npmjs.com/cli/v11/commands/npm-pkg/) | [workflow/03](docs/workflow/03-tools-and-commands.md) | 2026-10-21 |
| [docs.npmjs.com/cli/v11/commands/npm-run/](https://docs.npmjs.com/cli/v11/commands/npm-run/) | [workflow/03](docs/workflow/03-tools-and-commands.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html) | [backend/02](docs/backend/02-review-in-30-minutes.md) | 2026-10-21 |
| [docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html) | [backend/02](docs/backend/02-review-in-30-minutes.md) | 2026-10-21 |
| [doi.org/10.1207/s15516709cog1302_1](https://doi.org/10.1207/s15516709cog1302_1) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [genai.owasp.org/llmrisk/llm062025-excessive-agency/](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) | [backend/04](docs/backend/04-agent-runtime-review.md) | 2026-10-21 |
| [git-scm.com/docs/git-branch](https://git-scm.com/docs/git-branch) | [workflow/03](docs/workflow/03-tools-and-commands.md) | 2026-10-21 |
| [git-scm.com/docs/git-diff](https://git-scm.com/docs/git-diff) | [backend/02](docs/backend/02-review-in-30-minutes.md) · [workflow/03](docs/workflow/03-tools-and-commands.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [git-scm.com/docs/git-log](https://git-scm.com/docs/git-log) | [workflow/03](docs/workflow/03-tools-and-commands.md) | 2026-10-21 |
| [git-scm.com/docs/git-reflog](https://git-scm.com/docs/git-reflog) | [workflow/03](docs/workflow/03-tools-and-commands.md) | 2026-10-21 |
| [git-scm.com/docs/git-revert](https://git-scm.com/docs/git-revert) | [workflow/03](docs/workflow/03-tools-and-commands.md) | 2026-10-21 |
| [git-scm.com/docs/git-status](https://git-scm.com/docs/git-status) | [workflow/03](docs/workflow/03-tools-and-commands.md) | 2026-10-21 |
| [git-scm.com/docs/git-switch](https://git-scm.com/docs/git-switch) | [workflow/03](docs/workflow/03-tools-and-commands.md) | 2026-10-21 |
| [git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree) | [workflow/01](docs/workflow/01-agentic-workflow.md) · [workflow/03](docs/workflow/03-tools-and-commands.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) | [workflow/03](docs/workflow/03-tools-and-commands.md) | 2026-10-21 |
| [github.com/EnzeD/vibe-coding](https://github.com/EnzeD/vibe-coding) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | [workflow/01](docs/workflow/01-agentic-workflow.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/Fission-AI/OpenSpec/blob/main/docs/getting-started.md](https://github.com/Fission-AI/OpenSpec/blob/main/docs/getting-started.md) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/agentsmd/agents.md](https://github.com/agentsmd/agents.md) | [workflow/01](docs/workflow/01-agentic-workflow.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/anthropics/skills](https://github.com/anthropics/skills) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/filipecalegario/awesome-vibe-coding](https://github.com/filipecalegario/awesome-vibe-coding) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/github/awesome-copilot](https://github.com/github/awesome-copilot) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/github/spec-kit](https://github.com/github/spec-kit) | [workflow/01](docs/workflow/01-agentic-workflow.md) · [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.com/obra/superpowers](https://github.com/obra/superpowers) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [github.github.com/spec-kit/](https://github.github.com/spec-kit/) | [workflow/04](docs/workflow/04-reading-map.md) | 2026-10-21 |
| [json-schema.org/understanding-json-schema/reference/object](https://json-schema.org/understanding-json-schema/reference/object) | [backend/04](docs/backend/04-agent-runtime-review.md) | 2026-10-21 |
| [modelcontextprotocol.io/specification/2026-07-28/server/tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) | [backend/04](docs/backend/04-agent-runtime-review.md) | 2026-10-21 |
| [nodejs.org/api/child_process.html](https://nodejs.org/api/child_process.html) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [nodejs.org/api/fs.html](https://nodejs.org/api/fs.html) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [nodejs.org/api/globals.html#class-abortcontroller](https://nodejs.org/api/globals.html#class-abortcontroller) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [nodejs.org/api/test.html](https://nodejs.org/api/test.html) | [backend/02](docs/backend/02-review-in-30-minutes.md) | 2026-10-21 |
| [opentelemetry.io/docs/concepts/signals/](https://opentelemetry.io/docs/concepts/signals/) | [backend/01](docs/backend/01-backend-map.md) | 2026-10-21 |
| [playwright.dev/docs/accessibility-testing](https://playwright.dev/docs/accessibility-testing) | [frontend/04](docs/frontend/04-design-critique.md) | 2026-10-21 |
| [playwright.dev/docs/test-snapshots](https://playwright.dev/docs/test-snapshots) | [frontend/04](docs/frontend/04-design-critique.md) | 2026-10-21 |
| [sqlite.org/backup.html](https://sqlite.org/backup.html) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [sqlite.org/lang_altertable.html](https://sqlite.org/lang_altertable.html) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [sqlite.org/lang_createindex.html](https://sqlite.org/lang_createindex.html) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [sqlite.org/lang_transaction.html](https://sqlite.org/lang_transaction.html) | [backend/01](docs/backend/01-backend-map.md) · [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [sqlite.org/lang_update.html](https://sqlite.org/lang_update.html) | [backend/02](docs/backend/02-review-in-30-minutes.md) | 2026-10-21 |
| [sqlite.org/pragma.html](https://sqlite.org/pragma.html) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [sqlite.org/pragma.html#pragma_foreign_keys](https://sqlite.org/pragma.html#pragma_foreign_keys) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [sqlite.org/pragma.html#pragma_integrity_check](https://sqlite.org/pragma.html#pragma_integrity_check) | [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [sqlite.org/wal.html](https://sqlite.org/wal.html) | [backend/01](docs/backend/01-backend-map.md) · [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [sre.google/sre-book/postmortem-culture/](https://sre.google/sre-book/postmortem-culture/) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [v2.tauri.app/concept/architecture/](https://v2.tauri.app/concept/architecture/) | [cases/01](docs/cases/01-notes-app.md) | 2026-10-21 |
| [v2.tauri.app/security/capabilities/](https://v2.tauri.app/security/capabilities/) | [backend/01](docs/backend/01-backend-map.md) | 2026-10-21 |
| [web.dev/articles/vitals](https://web.dev/articles/vitals) | [frontend/04](docs/frontend/04-design-critique.md) | 2026-10-21 |
| [www.anthropic.com/research/effective-harnesses-for-long-running-agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) | [cases/01](docs/cases/01-notes-app.md) | 2026-10-21 |
| [www.carbondesignsystem.com/building-blocks/foundations/spacing/overview](https://www.carbondesignsystem.com/building-blocks/foundations/spacing/overview) | [frontend/01](docs/frontend/01-visual-language.md) · [frontend/02](docs/frontend/02-design-system.md) | 2026-10-21 |
| [www.carbondesignsystem.com/building-blocks/foundations/typography/type-sets](https://www.carbondesignsystem.com/building-blocks/foundations/typography/type-sets) | [frontend/01](docs/frontend/01-visual-language.md) | 2026-10-21 |
| [www.christenseninstitute.org/video/what-is-jobs-to-be-done-theory/](https://www.christenseninstitute.org/video/what-is-jobs-to-be-done-theory/) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [www.debuggingbook.org/html/Intro_Debugging.html](https://www.debuggingbook.org/html/Intro_Debugging.html) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [www.designcouncil.org.uk/resources/the-double-diamond/](https://www.designcouncil.org.uk/resources/the-double-diamond/) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [www.eiffel.com/values/design-by-contract/introduction/](https://www.eiffel.com/values/design-by-contract/introduction/) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [www.law.uchicago.edu/socratic-method](https://www.law.uchicago.edu/socratic-method) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [www.nasa.gov/reference/6-8-decision-analysis/](https://www.nasa.gov/reference/6-8-decision-analysis/) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [www.psychologytoday.com/us/blog/seeing-what-others-dont/202101/the-pre-mortem-method](https://www.psychologytoday.com/us/blog/seeing-what-others-dont/202101/the-pre-mortem-method) | [workflow/05](docs/workflow/05-thinking-and-questioning.md) | 2026-10-22 |
| [www.rfc-editor.org/rfc/rfc9110.html](https://www.rfc-editor.org/rfc/rfc9110.html) | [backend/01](docs/backend/01-backend-map.md) · [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) | [backend/01](docs/backend/01-backend-map.md) · [backend/03](docs/backend/03-data-async-security.md) | 2026-10-21 |
| [www.sqlite.org/lang_transaction.html](https://www.sqlite.org/lang_transaction.html) | [cases/02](docs/cases/02-feature-walkthrough.md) | 2026-10-21 |
| [www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/TR/prov-dm/](https://www.w3.org/TR/prov-dm/) | [backend/04](docs/backend/04-agent-runtime-review.md) | 2026-10-21 |
| [www.w3.org/TR/prov-overview/](https://www.w3.org/TR/prov-overview/) | [backend/04](docs/backend/04-agent-runtime-review.md) | 2026-10-21 |
| [www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/ARIA/apg/patterns/tabs/](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/focus-visible.html](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/keyboard.html](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) | [frontend/02](docs/frontend/02-design-system.md) · [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/reflow.html](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/resize-text.html](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/status-messages.html](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) | [cases/02](docs/cases/02-feature-walkthrough.md) · [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/WCAG22/Understanding/text-spacing.html](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) | [frontend/03](docs/frontend/03-interaction-accessibility.md) | 2026-10-21 |
| [www.w3.org/WAI/test-evaluate/tools/](https://www.w3.org/WAI/test-evaluate/tools/) | [frontend/04](docs/frontend/04-design-critique.md) | 2026-10-21 |
