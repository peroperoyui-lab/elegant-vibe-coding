// Executable smoke checks. Requires npm ci and Playwright Chromium.
// Opens the generated file offline; writes screenshots/results only under .qa/.
// Clipboard is stubbed to check copied content, not OS clipboard permissions.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from 'playwright';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const qa = path.join(root, '.qa');
await fs.mkdir(qa, {recursive:true});
const added = [
  'docs/workflow/05-thinking-and-questioning.md',
  'docs/cases/04-question-to-evidence.md',
  'templates/QUESTION-CANVAS.md',
  'templates/EXPERIMENT-CARD.md',
  'checklists/thinking.md',
];
const file = pathToFileURL(path.join(root, 'reader/index.html')).href;
const browser = await chromium.launch({headless:true});
const results = [];
try {
  for (const viewport of [{width:1440,height:900},{width:390,height:844}]) {
    const context = await browser.newContext({viewport, offline:true});
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('console', message => {if(message.type()==='error') errors.push(message.text());});
    await page.addInitScript(() => {
      window.__copied = null;
      Object.defineProperty(navigator, 'clipboard', {configurable:true, value:{
        writeText: async text => {window.__copied = text;},
      }});
    });
    await page.goto(file);
    const book = await page.locator('#book-data').evaluate(el => JSON.parse(el.textContent));
    for (const id of added) {
      const doc = book.documents.find(d => d.id===id);
      assert.ok(doc, `Missing embedded document: ${id}`);
      assert.equal(doc.raw, await fs.readFile(path.join(root,id),'utf8'), `Stale document: ${id}`);
      await page.goto(file+'#'+new URLSearchParams({doc:id}));
      await page.waitForFunction(title => document.querySelector('#content h1')?.textContent===title, doc.title);
      assert.equal(await page.locator('#content h1').count(),1);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth<=innerWidth+2),true,`Page overflow: ${id}`);
    }
    await page.locator('#search-button').click();
    await page.locator('#query').fill('提问的思想');
    const hit=page.locator('.search-result').filter({has:page.locator('strong',{hasText:'提问的思想：让问题推动开发'})}).first();
    await hit.click();
    await page.waitForFunction(() => document.querySelector('#content h1')?.textContent==='提问的思想：让问题推动开发');
    await page.locator('#content a[data-anchor="m08"]').first().click();
    await page.waitForFunction(() => new URLSearchParams(location.hash.slice(1)).get('section')==='m08');
    assert.equal(await page.locator('#m08').count(),1);
    const copyButton=page.locator('#content .copy-code').first();
    const expected=await page.locator('#content .code-wrap code').first().textContent();
    await copyButton.click();
    await page.waitForFunction(text => window.__copied===text, expected);
    const oldTheme=await page.locator('html').getAttribute('data-theme');
    await page.locator('#theme-button').click();
    assert.notEqual(await page.locator('html').getAttribute('data-theme'),oldTheme);
    await page.locator('#theme-button').click();
    if(viewport.width<800) {
      await page.locator('#menu-button').click();
      assert.equal(await page.locator('#menu-button').getAttribute('aria-expanded'),'true');
      await page.locator('#nav a[data-doc="templates/QUESTION-CANVAS.md"]').click();
      await page.waitForFunction(() => document.querySelector('#content h1')?.textContent==='提问画布：把未知变成下一步');
      assert.equal(await page.locator('#menu-button').getAttribute('aria-expanded'),'false');
    }
    await page.goto(file+'#'+new URLSearchParams({doc:added[0]}));
    await page.waitForFunction(() => document.querySelector('#content h1')?.textContent==='提问的思想：让问题推动开发');
    await page.keyboard.press('Control+k');
    assert.equal(await page.locator('#search-dialog').evaluate(el=>el.open),true);
    await page.keyboard.press('Escape');
    assert.equal(await page.locator('#search-dialog').evaluate(el=>el.open),false);
    // Capture a settled reading state, not a sidebar transition or copy toast.
    if(viewport.width<800) {
      await page.waitForFunction(() => document.getElementById('sidebar').getBoundingClientRect().right<=0.5);
      assert.equal(await page.locator('#sidebar').evaluate(el=>el.inert),true);
    }
    await page.waitForFunction(() => !document.getElementById('toast').classList.contains('show'));
    await page.evaluate(() => {document.activeElement?.blur();window.scrollTo(0,0);});
    await page.screenshot({path:path.join(qa,`questioning-${viewport.width}.png`),fullPage:false,animations:'disabled'});
    assert.deepEqual(errors,[],`Browser errors at ${viewport.width}px`);
    results.push({viewport,documents:added.length,checks:['source parity','chapter rendering','global overflow','full-text search','method anchor','copy handler (stubbed clipboard)','theme toggle','keyboard search and escape',...(viewport.width<800?['mobile navigation','closed sidebar fully offscreen and inert']:[])],passed:true});
    await context.close();
  }
  const report={source_commit:process.env.GITHUB_SHA||null,node:process.version,chromium:browser.version(),platform:process.platform,network:'offline',results};
  await fs.writeFile(path.join(qa,'reader-results.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));
} finally {
  await browser.close();
}
