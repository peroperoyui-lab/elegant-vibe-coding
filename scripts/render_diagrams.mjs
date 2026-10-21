// Render trusted repository Mermaid sources to offline SVG. No model/API calls.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import { chromium } from 'playwright';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const out = path.join(root, 'assets/diagrams');
await fs.mkdir(out, { recursive: true });
const mermaidPath = process.env.EVC_MERMAID_JS || path.join(root, 'node_modules/mermaid/dist/mermaid.min.js');
const browser = await chromium.launch({
  headless: true,
  ...(process.env.EVC_BROWSER_PATH ? { executablePath: process.env.EVC_BROWSER_PATH } : {}),
  args: ['--no-sandbox'],
});
const manifest = [];
async function files(dir) {
  const list = [];
  for (const e of await fs.readdir(dir, { withFileTypes: true })) {
    if (e.isDirectory()) list.push(...await files(path.join(dir, e.name)));
    else if (e.name.endsWith('.md')) list.push(path.join(dir, e.name));
  }
  return list.sort();
}
try {
  const page = await browser.newPage({ viewport: { width: 1600, height: 1400 } });
  await page.setContent('<!doctype html><html><meta charset="utf-8"><body></body></html>');
  await page.addScriptTag({ path: mermaidPath });
  await page.evaluate(() => mermaid.initialize({
    startOnLoad: false, securityLevel: 'strict', theme: 'base',
    fontFamily: 'Noto Sans CJK SC, Microsoft YaHei, Arial, sans-serif',
    themeVariables: { primaryColor: '#eaf1df', primaryTextColor: '#172b31', primaryBorderColor: '#6d837a', lineColor: '#647a70', secondaryColor: '#f5f3ec', tertiaryColor: '#ffffff', fontSize: '19px' },
    flowchart: { htmlLabels: false, curve: 'basis' },
  }));
  for (const file of await files(path.join(root, 'docs'))) {
    const source = await fs.readFile(file, 'utf8');
    let index = 0;
    for (const match of source.matchAll(/^```mermaid\s*\n([\s\S]*?)^```\s*$/gm)) {
      const code = match[1].trim();
      const hash = createHash('sha256').update(code).digest('hex').slice(0, 16);
      const id = 'diagram-' + hash;
      let svg = await page.evaluate(async ({ id, code }) => (await mermaid.render(id, code)).svg, { id, code });
      const title = `手册流程图 ${path.basename(file, '.md')} ${++index}`;
      svg = svg.replace(/(<svg\b[^>]*>)/, `$1<title>${title}</title><desc>根据本章 Mermaid 源码渲染；节点与连线说明见相邻正文。</desc>`);
      const relative = `assets/diagrams/${hash}.svg`;
      await fs.writeFile(path.join(root, relative), svg + '\n');
      manifest.push({ chapter: path.relative(root, file).replaceAll(path.sep, '/'), index, hash, svg: relative });
    }
  }
  await fs.writeFile(path.join(root, 'references/diagram-index.json'), JSON.stringify({ renderer: 'mermaid 11.12.2', diagrams: manifest }, null, 2) + '\n');
  console.log(`Rendered ${manifest.length} Mermaid diagrams to offline SVG.`);
} finally {
  await browser.close();
}
