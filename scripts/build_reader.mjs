// Build a self-contained offline reader from trusted repository Markdown.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import { Marked } from 'marked';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const entries = [
  ['开始','README.md','手册总览'],
  ['开始','QUICKSTART.md','十分钟开始'],
  ['开始','GLOSSARY.md','183 个术语入口'],
  ['前端设计','docs/frontend/01-visual-language.md','01 · 视觉语言'],
  ['前端设计','docs/frontend/02-design-system.md','02 · 设计系统'],
  ['前端设计','docs/frontend/03-interaction-accessibility.md','03 · 交互与可访问性'],
  ['前端设计','docs/frontend/04-design-critique.md','04 · 设计评审'],
  ['后端审查','docs/backend/01-backend-map.md','01 · 后端地图'],
  ['后端审查','docs/backend/02-review-in-30-minutes.md','02 · 30 分钟 review'],
  ['后端审查','docs/backend/03-data-async-security.md','03 · 数据、异步与边界'],
  ['后端审查','docs/backend/04-agent-runtime-review.md','04 · 智能体运行时'],
  ['AI 协作','docs/workflow/01-agentic-workflow.md','01 · 持续推进的工作流'],
  ['AI 协作','docs/workflow/02-prompt-recipes.md','02 · 22 份提示词'],
  ['AI 协作','docs/workflow/03-tools-and-commands.md','03 · 工具与命令'],
  ['AI 协作','docs/workflow/04-reading-map.md','04 · 资源阅读地图'],
  ['完整实战','docs/cases/01-notes-app.md','01 · 桌面笔记应用'],
  ['完整实战','docs/cases/02-feature-walkthrough.md','02 · 资料导入走查'],
  ['完整实战','docs/cases/03-say-it-precisely.md','03 · 准确表达'],
  ['随手模板','templates/TASK-BRIEF.md','任务说明'],
  ['随手模板','templates/DESIGN-BRIEF.md','设计说明'],
  ['随手模板','templates/REVIEW-REPORT.md','审查记录'],
  ['随手模板','templates/ACCEPTANCE.md','验收条件'],
  ['随手模板','templates/HANDOFF.md','交接记录'],
  ['随手模板','templates/ADR.md','架构决定'],
  ['随手模板','templates/PROJECT-CONTEXT.md','项目上下文'],
  ['验收与图解','checklists/frontend.md','前端验收清单'],
  ['验收与图解','checklists/backend.md','后端审查清单'],
  ['验收与图解','checklists/delivery.md','交付检查清单'],
  ['验收与图解','assets/README.md','原创图解导览'],
  ['验收与图解','examples/frontend-lab/README.md','设计实验室说明'],
  ['维护与来源','SOURCES.md','来源与核验'],
  ['维护与来源','CONTRIBUTING.md','维护这本手册'],
  ['维护与来源','CHANGELOG.md','更新记录'],
  ['维护与来源','VALIDATION.md','本版验证记录'],
];
const ids = new Set(entries.map(x=>x[1]));
const escape = s => String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const slug = s => s.toLowerCase().replace(/<[^>]*>/g,'').replace(/[^\p{L}\p{N}\s_-]/gu,'').replace(/ /g,'-');
const imageCache = new Map();
async function imageData(relative) {
  if (!imageCache.has(relative)) {
    const bytes = await fs.readFile(path.join(root,relative));
    const ext=path.extname(relative).toLowerCase();
    const mime=ext==='.svg'?'image/svg+xml':ext==='.png'?'image/png':'image/jpeg';
    imageCache.set(relative,`data:${mime};base64,${bytes.toString('base64')}`);
  }
  return imageCache.get(relative);
}
// Preload local figures so synchronous Markdown renderers can embed them.
async function imageFiles(dir) {
  for (const e of await fs.readdir(path.join(root,dir),{withFileTypes:true})) {
    const rel=path.posix.join(dir,e.name);
    if(e.isDirectory()) await imageFiles(rel);
    else if(/\.(svg|png|jpg|jpeg)$/i.test(e.name)) await imageData(rel);
  }
}
await imageFiles('assets');
const documents=[];
for(const [group,id,label] of entries) {
  const raw=await fs.readFile(path.join(root,id),'utf8');
  const headings=[],counts=new Map();
  const resolveLocal = href => {
    const [file,fragment='']=href.split('#');
    return {doc:file?path.posix.normalize(path.posix.join(path.posix.dirname(id),decodeURIComponent(file))):id,anchor:decodeURIComponent(fragment)};
  };
  const renderer={
    heading({tokens,depth}) {
      const html=this.parser.parseInline(tokens);
      const text=html.replace(/<[^>]+>/g,'').replace(/&amp;/g,'&');
      const base=slug(text),count=counts.get(base)||0; counts.set(base,count+1);
      const anchor=base+(count?'-'+count:'');
      if(depth===2||depth===3)headings.push({anchor,text,depth});
      return `<h${depth} id="${escape(anchor)}">${html}</h${depth}>\n`;
    },
    link({href,title,tokens}) {
      const label=this.parser.parseInline(tokens);
      if(/^https?:\/\//.test(href))return `<a href="${escape(href)}" target="_blank" rel="noopener noreferrer">${label}<span class="external" aria-hidden="true">↗</span></a>`;
      if(/^mailto:/.test(href))return `<a href="${escape(href)}">${label}</a>`;
      const {doc,anchor}=resolveLocal(href);
      if(ids.has(doc))return `<a href="#${new URLSearchParams({doc,...(anchor?{section:anchor}:{})})}" data-doc="${escape(doc)}" data-anchor="${escape(anchor)}">${label}</a>`;
      if(doc==='reader/index.html')return `<a href="#doc=README.md" data-doc="README.md">${label}</a>`;
      if(doc==='examples/frontend-lab/index.html')return `<button type="button" class="text-link" data-lab>${label}</button>`;
      if(imageCache.has(doc))return `<button type="button" class="text-link" data-image="${escape(doc)}">${label}</button>`;
      return `<a href="../${escape(doc)}${anchor?'#'+escape(anchor):''}">${label}</a>`;
    },
    image({href,text}) {
      const {doc}=resolveLocal(href);
      const src=imageCache.get(doc)||href;
      return `<figure><button class="figure-button" type="button" data-image="${escape(doc)}" aria-label="放大：${escape(text)}"><img src="${escape(src)}" alt="${escape(text)}" loading="lazy"></button><figcaption>${escape(text)} · 点击放大</figcaption></figure>`;
    },
    code({text,lang}) {
      if((lang||'').trim()==='mermaid') {
        const hash=createHash('sha256').update(text.trim()).digest('hex').slice(0,16);
        const rel=`assets/diagrams/${hash}.svg`;
        if(!imageCache.has(rel))throw new Error(`Missing rendered diagram for ${id}. Run npm run render:diagrams.`);
        return `<figure><button class="figure-button diagram" type="button" data-image="${rel}" aria-label="放大流程图"><img src="${imageCache.get(rel)}" alt="本节流程图，详细说明见相邻正文" loading="lazy"></button><figcaption>流程图 · 点击放大</figcaption></figure><details class="diagram-source"><summary>查看可编辑的 Mermaid 图源</summary><pre><code class="language-mermaid">${escape(text)}</code></pre></details>`;
      }
      return `<div class="code-wrap"><div class="code-top"><span>${escape(lang||'text')}</span><button type="button" class="copy-code">复制</button></div><pre><code class="language-${escape(lang||'text')}">${escape(text)}</code></pre></div>`;
    },
    table(token) {
      const cell=(t,tag)=>`<${tag}>${this.parser.parseInline(t.tokens)}</${tag}>`;
      return `<div class="table-scroll" role="region" aria-label="对照表，可横向滚动" tabindex="0"><table><thead><tr>${token.header.map(c=>cell(c,'th')).join('')}</tr></thead><tbody>${token.rows.map(r=>'<tr>'+r.map(c=>cell(c,'td')).join('')+'</tr>').join('')}</tbody></table></div>`;
    },
  };
  const md=new Marked({gfm:true,renderer});
  let html=await md.parse(raw);
  // The README's raw HTML cover is trusted source; inline its asset too.
  html=html.replace(/src="(?!https?:|data:)([^\"]+)"/g,(whole,href)=>{
    const {doc}=resolveLocal(href);return imageCache.has(doc)?`src="${imageCache.get(doc)}"`:whole;
  });
  const title=(raw.match(/^#\s+(.+)$/m)||[])[1]||label;
  const plain=raw.replace(/^\[[^\]]+\]:.*$/gm,'').replace(/```[^\n]*\n/g,'').replace(/[#*`>|]/g,'').replace(/!?\[([^\]]+)\]\([^)]+\)/g,'$1').replace(/<[^>]+>/g,'');
  documents.push({id,group,label,title,html,raw,plain,headings,minutes:Math.max(1,Math.ceil((raw.match(/[\u4e00-\u9fff]/g)||[]).length/450))});
}
let lab=await fs.readFile(path.join(root,'examples/frontend-lab/index.html'),'utf8');
const labCss=await fs.readFile(path.join(root,'examples/frontend-lab/tokens.css'),'utf8');
lab=lab.replace('<link rel="stylesheet" href="tokens.css">',`<style>${labCss}</style>`);
lab=lab.replaceAll('href="../../docs/frontend/02-design-system.md"','href="#design-system" data-handbook-doc="docs/frontend/02-design-system.md"');
// In srcdoc, native fragment URLs otherwise inherit the parent reader URL.
lab=lab.replace('</body>',`<script>document.addEventListener('click',event=>{const chapter=event.target.closest('[data-handbook-doc]');if(chapter){event.preventDefault();parent.postMessage({type:'evc:open-chapter',id:chapter.dataset.handbookDoc},'*');return}const link=event.target.closest('a[href^="#"]');if(!link)return;const target=document.getElementById(decodeURIComponent(link.getAttribute('href').slice(1)));if(!target)return;event.preventDefault();if(!target.hasAttribute('tabindex'))target.setAttribute('tabindex','-1');target.focus({preventScroll:true});target.scrollIntoView({block:'start'});});</script></body>`);
const data={edition:'2026-10-21',documents,images:Object.fromEntries(imageCache),lab};
const payload=JSON.stringify(data).replaceAll('<','\\u003c').replaceAll('\u2028','\\u2028').replaceAll('\u2029','\\u2029');
let template=await fs.readFile(path.join(root,'scripts/reader-template.html'),'utf8');
template=template.replace('<!--BOOK_DATA-->',()=>`<script type="application/json" id="book-data">${payload}</script>`);
await fs.mkdir(path.join(root,'reader'),{recursive:true});
await fs.writeFile(path.join(root,'reader/index.html'),template);
console.log(`Built offline reader: ${documents.length} documents, ${imageCache.size} embedded images, ${Buffer.byteLength(template)} bytes.`);
