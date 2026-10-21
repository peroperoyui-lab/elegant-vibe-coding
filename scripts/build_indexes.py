"""Build the glossary and source-link inventory from the chapter sources."""
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def terms(path, mode):
    result = []
    section = ''
    active = mode != 'workflow'
    for line in (ROOT / path).read_text(encoding='utf-8').splitlines():
        if line.startswith('## '):
            section = line[3:]
            if mode == 'workflow':
                active = section.startswith('2.')
        if not active or not line.startswith('|'):
            continue
        cells = [x.strip() for x in line.strip().strip('|').split('|')]
        if mode == 'frontend' and len(cells) == 4 and cells[0].isdigit():
            result.append((section, cells[1]))
        elif mode == 'backend' and len(cells) == 3 and re.match(r'^[A-Za-z]', cells[0]):
            result.append((section, cells[0]))
        elif mode == 'workflow' and len(cells) == 3 and re.match(r'^[A-Za-z]', cells[0]):
            result.append((section, cells[0]))
    return result

def glossary():
    groups = [
        ('前端设计', 'docs/frontend/01-visual-language.md', 'frontend'),
        ('后端工程', 'docs/backend/01-backend-map.md', 'backend'),
        ('开发协作', 'docs/workflow/03-tools-and-commands.md', 'workflow'),
    ]
    items = [(name,path,terms(path,mode)) for name,path,mode in groups]
    total = sum(len(data) for _,_,data in items)
    lines = ['# 术语入口与中英索引', '', '[返回目录](README.md) · [快速开始](QUICKSTART.md)', '',
        f'本索引收录三份核心词典中的 **{total} 个条目**，按原章节组织；同名词在不同语境下保留。完整解释、适用情境和可复制指令在对应章节。离线阅读器可以直接搜索中英文关键词。', '',
        '## 先分清几个常见的同名词', '',
        '| 表述 | 在这里分别是什么意思 |', '|---|---|',
        '| Token | Design token 是被命名的设计决定；LLM token 是模型处理输入输出的计量单位 |',
        '| Repository | Git repository 是代码与版本历史；数据层 repository 是封装存储访问的模块 |',
        '| State / Event | State 表示当前处境；Event 表示已经发生的一件事，两者可互相关联 |',
        '| Run / Session | Run 通常指一次执行；Session 通常指可延续的会话容器，具体含义以产品契约为准 |',
        '| Focus / Selected | Focus 是当前键盘操作位置；Selected 是被选中的对象，二者可以同时存在 |',
        '| Authentication / Authorization | 前者确认调用者身份；后者判断允许的动作与资源范围 |',
        '| CLI / Shell / Terminal | CLI 是命令行接口；Shell 解析命令；Terminal 是承载交互的窗口 |',
        '| Schema / Contract | Schema 约束数据形状；Contract 还包括行为、错误和重复调用等含义 |',
        '| Cancel requested / Cancelled | 前者表示收到取消意图；后者表示执行侧确认停止后的状态 |',
        '', '这些区别帮助澄清沟通。具体工具的命名与加载机制，以其版本文档和项目约定为准。', '']
    for name,path,data in items:
        lines += [f'## {name} · {len(data)} 个条目', '', f'[打开完整词典]({path})', '']
        current = None
        for section,term in data:
            if section != current:
                lines += [f'### {section}', '', '| 中文与 English | 详细解释与指令 |', '|---|---|']
                current = section
            lines.append(f'| {term} | [查看原章]({path}) |')
        lines.append('')
    lines += ['---', '', '本索引由 `python3 scripts/build_indexes.py` 从章节表格生成，维护时修改原章节即可。', '']
    (ROOT/'GLOSSARY.md').write_text('\n'.join(lines),encoding='utf-8')
    return {name:len(data) for name,_,data in items}

def sources():
    links = defaultdict(set)
    for p in sorted((ROOT/'docs').rglob('*.md')):
        text = p.read_text(encoding='utf-8')
        text = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M|re.S)
        urls = re.findall(r'\]\((https?://[^\s)]+)',text)
        urls += re.findall(r'^\[[^\]]+\]:\s*(https?://\S+)',text,flags=re.M)
        for url in urls:
            clean=url.rstrip('>.,;')
            if 'example.' not in clean and 'localhost' not in clean:
                links[clean].add(p.relative_to(ROOT).as_posix())
    rows = [{'url':url, 'chapters':sorted(chapters), 'accessed_on':'2026-10-21'} for url,chapters in sorted(links.items())]
    (ROOT/'references').mkdir(exist_ok=True)
    (ROOT/'references/source-index.json').write_text(json.dumps({'note':'Chapter citation inventory; access date records this edition, not a promise of future availability.','sources':rows},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines = ['# 来源与核验说明', '', '[返回目录](README.md) · [资源阅读地图](docs/workflow/04-reading-map.md)', '',
        '## 这本手册怎样使用资料', '',
        '本版查阅日期为 **2026-10-21**。设计规范与技术行为优先使用标准组织、工具维护者和厂商官方文档；社区仓库直接读取维护者说明。章节中的教学场景、中文指令、比较维度、图解和模板是围绕读者任务编排的原创内容。', '',
        '| 内容类型 | 采用方式 | 适用边界 |', '|---|---|---|',
        '| W3C / WAI、协议标准 | 核对具体条款、等级、条件和例外 | 抽取常用条款并不构成完整符合性认证 |',
        '| SQLite、Node、Git、框架官方文档 | 核对接口、事务、命令和实际语义 | 本机版本、配置和项目封装仍需确认 |',
        '| 编码工具官方文档 | 核对说明文件、命令与功能入口 | 版本与客户端会影响可用行为 |',
        '| 代表性开源仓库 | 介绍用途、可借鉴方法与采用成本 | README 核验与完整代码/安全/维护质量审计有不同范围 |',
        '| 本手册建议 | 用任务、示例与证据解释取舍 | 可按现有项目简化和调整 |', '',
        '“热门”在这里落实为有代表性的公开项目清单；本版没有做趋势采样或按星标排名。资源越多，理解与维护成本也越多，选择应回到当前任务。', '',
        '## 易变信息怎样维护', '',
        '使用工具命令前确认本机版本与帮助；升级后重新核对规则文件加载方式。引用原页面可能重定向到维护者的新域名，优先使用正式的新入口。长期有效的设计判断，与某一版本的命令语法分别维护。', '',
        f'## 章节引用索引 · {len(rows)} 个 URL', '',
        '以下由正文引用自动整理；同一页面的不同锚点保留，故 URL 数量不等同于独立文献数量。每条来源的具体用途见相应章节。机器可读清单为 [source-index.json](references/source-index.json)。', '',
        '| 来源页面 | 出现章节 |', '|---|---|']
    for item in rows:
        u=item['url']; split=urlsplit(u)
        label=split.netloc+split.path+(('#'+split.fragment) if split.fragment else '')
        ch=' · '.join(f'[{Path(p).parent.name}/{Path(p).name[:2]}]({p})' for p in item['chapters'])
        lines.append(f'| [{label}]({u}) | {ch} |')
    lines.append('')
    (ROOT/'SOURCES.md').write_text('\n'.join(lines),encoding='utf-8')
    return len(rows)

if __name__=='__main__':
    print(json.dumps({'glossary':glossary(),'source_urls':sources()},ensure_ascii=False))
