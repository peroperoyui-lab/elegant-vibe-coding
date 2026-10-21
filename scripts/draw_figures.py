"""Rebuild the original, dependency-free SVG teaching figures."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets'
INK, PAPER, GREEN, TEAL, MUTED, LINE, WHITE = '#172b31', '#f5f3ec', '#c7ef81', '#2f6659', '#596b6a', '#d8ded7', '#ffffff'

class Figure:
    def __init__(self, w, h, title, desc, dark=False):
        self.w, self.h = w, h
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">', f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>', '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#6d837a"/></marker></defs>']
        self.rect(0,0,w,h,INK if dark else PAPER)
    def rect(self,x,y,w,h,fill=WHITE,stroke=None,r=0,sw=1):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
    def text(self,x,y,s,size=22,fill=INK,weight=400,anchor='start',family=None):
        family = family or "Noto Sans CJK SC, Microsoft YaHei, PingFang SC, Arial, sans-serif"
        self.parts.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')
    def line(self,x1,y1,x2,y2,color=LINE,width=1,arrow=False,dash=False):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="8 7"' if dash else '')+'/>')
    def path(self,d,color=LINE,width=2,arrow=False,dash=False):
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="8 7"' if dash else '')+'/>')
    def circle(self,x,y,r,fill,stroke=None,sw=1):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
    def badge(self,x,y,n):
        self.circle(x,y,17,GREEN)
        self.text(x,y+6,str(n),17,INK,700,'middle')
    def header(self,kicker,title,subtitle):
        self.text(64,53,kicker,16,TEAL,700)
        self.text(64,110,title,39,INK,700)
        self.text(64,151,subtitle,20,MUTED)
    def footer(self,label):
        self.line(64,self.h-57,self.w-64,self.h-57)
        self.text(64,self.h-27,'ELEGANT VIBE CODING  /  '+label,15,MUTED,500)
        self.text(self.w-64,self.h-27,'原创教学图 · 2026',15,MUTED,400,'end')
    def save(self,name):
        (OUT/name).write_text('\n'.join(self.parts+['</svg>']),encoding='utf-8')

def cover():
    f=Figure(1600,640,'Elegant Vibe Coding','A Chinese field guide connecting intention, design and engineering evidence.',True)
    for x in range(960,1600,40): f.line(x,0,x,640,'#263a40')
    for y in range(0,640,40): f.line(960,y,1600,y,'#263a40')
    f.rect(70,63,190,34,GREEN,r=17)
    f.text(165,86,'THE FIELD GUIDE',15,INK,700,'middle')
    f.text(70,240,'ELEGANT',118,PAPER,700,family='Arial, sans-serif')
    f.text(70,365,'VIBE CODING',118,PAPER,700,family='Arial, sans-serif')
    f.line(72,411,865,411,'#627771',1)
    f.text(74,464,'把想法说清 · 把设计做实 · 把结果验明',27,'#e0e8df',500)
    f.text(74,563,'DESIGN LANGUAGE    /    ENGINEERING REVIEW    /    AGENT WORKFLOWS',16,'#a7beb2',500)
    for i,(t,sub) in enumerate([('INTENT','What should the user achieve?'),('SYSTEM','What must the software do?'),('EVIDENCE','How will we know it works?')]):
        y=99+i*148
        f.rect(1030,y,475,114, '#203a3e' if i!=1 else GREEN, '#4c635b' if i!=1 else None,12)
        c=INK if i==1 else PAPER
        f.text(1064,y+40,'0'+str(i+1),17,c,600)
        f.text(1110,y+42,t,28,c,700)
        f.text(1064,y+81,sub,19,c)
        if i<2:f.line(1267,y+117,1267,y+144,'#c7ef81',2,True)
    f.circle(1492,562,22,'none',GREEN,2)
    f.line(1477,562,1507,562,GREEN,2)
    f.line(1492,547,1492,577,GREEN,2)
    f.save('cover.svg')

def workflow():
    f=Figure(1400,830,'从需求到可审查交付的协作闭环','六个阶段围绕一个用户结果形成闭环：核对基线、任务说明、实现、验证、审查、交接。')
    f.header('01 / WORKFLOW','把任务与证据放在同一个闭环里','根据改动影响选择深度；一个清楚的用户结果，贯穿实现与验收。')
    coords=[(80,220),(525,220),(970,220),(970,520),(525,520),(80,520)]
    data=[('01','核对基线','Read the actual project','分支 · 现有规则 · 相关代码'),('02','写清任务','Define the outcome','目标 · 范围 · 验收'),('03','完成切片','Build a small slice','复用 · 接通 · 可运行'),('04','取得证据','Verify the behaviour','操作 · 测试 · 截图'),('05','聚焦审查','Review the change','触发 · 影响 · 最小修复'),('06','留下路标','Leave a clear handoff','当前状态 · 证据 · 下一步')]
    for (x,y),(n,a,b,c) in zip(coords,data):
        f.rect(x,y,350,166,WHITE,LINE,14)
        f.text(x+26,y+34,n,16,TEAL,700)
        f.text(x+26,y+76,a,30,INK,700)
        f.text(x+26,y+110,b,17,MUTED)
        f.text(x+26,y+145,c,18,TEAL)
    for (x1,y1,x2,y2) in [(430,303,518,303),(875,303,963,303),(1145,386,1145,512),(970,603,882,603),(525,603,437,603),(255,520,255,393)]:f.line(x1,y1,x2,y2,'#6d837a',2,True)
    f.rect(480,420,440,57,GREEN,r=28)
    f.text(700,457,'ONE SMALL USER OUTCOME',20,INK,700,'middle')
    f.footer('TASK → IMPLEMENTATION → OBSERVABLE RESULT')
    f.save('workflow-loop.svg')

def workstation():
    f=Figure(1600,1030,'资料管理工作台布局解剖','教学界面示意：左侧导航、中间资料与工作内容、右侧来源详情；紧凑列表与舒适阅读密度分开。')
    f.header('02 / WORKSPACE ANATOMY','让布局回答：去哪里、做什么、来自哪里','示例配色与尺寸是教学建议；真实产品沿用其现行设计系统。')
    f.rect(65,203,1470,618,WHITE,LINE,16)
    f.rect(65,203,1470,58,INK,r=16)
    f.rect(65,233,1470,28,INK)
    f.text(90,241,'DOCUMENT DESK',20,PAPER,700)
    f.text(363,240,'收藏夹 / 使用手册',18,'#cbd8d2')
    f.rect(1288,216,218,31,'#344c4d',r=6)
    f.text(1308,238,'搜索项目…    Ctrl K',15,PAPER)
    f.rect(66,262,230,558,'#ecefe7')
    f.text(90,301,'工作空间',16,MUTED,600)
    for i,t in enumerate(['项目概览','资料与证据','工作笔记','任务与结果','设置']):
        y=327+i*58
        if i==1:f.rect(79,y-7,201,43,'#d5e7c1',r=7)
        f.circle(100,y+13,6,TEAL if i==1 else '#8d9c95')
        f.text(121,y+20,t,18,TEAL if i==1 else INK,600 if i==1 else 400)
    f.text(90,781,'本地项目 · 教学示例',14,MUTED)
    f.line(296,262,296,819)
    f.text(327,309,'资料与证据',28,INK,700)
    f.text(327,343,'按工作主题整理材料，随时回到原文。',17,MUTED)
    f.rect(965,282,166,42,TEAL,r=7)
    f.text(1048,310,'＋ 导入资料',18,WHITE,600,'middle')
    f.rect(327,366,803,43,'#f5f7f2',LINE,7)
    f.text(347,394,'搜索标题、作者或标签…',17,MUTED)
    f.text(327,441,'全部资料',17,TEAL,700)
    f.text(443,441,'待阅读',17,MUTED)
    f.text(537,441,'已标注',17,MUTED)
    f.line(327,454,1130,454)
    rows=[('家用咖啡器具使用手册','参考文档 · 2024','已就绪'),('室内植物养护指南','使用指南 · 2025','处理中'),('文档分类与整理说明','工作笔记 · 今天','已就绪'),('Camera setup and maintenance','参考文档 · 2023','需重试')]
    for i,(title,sub,status) in enumerate(rows):
        y=472+i*75
        if i==0:f.rect(317,y-5,823,69,'#eff5e8',r=8)
        f.rect(336,y+9,26,32,'#e2e9de',r=3)
        f.text(380,y+26,title,18,INK,600 if i==0 else 400)
        f.text(380,y+51,sub,14,MUTED)
        f.text(1050,y+29,status,16,TEAL if status!='需重试' else '#9c4836',500,'middle')
        f.line(327,y+66,1130,y+66,'#e9ede5')
    f.line(1160,262,1160,819)
    f.text(1187,307,'来源详情',21,INK,700)
    f.text(1187,352,'家用咖啡器具使用手册',19,INK,600)
    f.text(1187,390,'材料类型',14,MUTED)
    f.text(1187,418,'参考文档 · 教学数据',17)
    f.text(1187,463,'定位',14,MUTED)
    f.text(1187,491,'第 3 节 / 操作说明',17)
    f.rect(1187,521,320,122,'#f6f6ef',r=8)
    for i,t in enumerate(['“清洁前断开电源…', '依次清洗可拆卸部件，', '晾干后再重新安装。”']):f.text(1205,552+i*30,t,17,INK)
    f.rect(1187,673,320,43,WHITE,TEAL,7)
    f.text(1347,702,'打开原文',18,TEAL,600,'middle')
    for x,n,t,sub in [(182,1,'稳定导航','位置与对象始终可识别'),(722,2,'主任务区域','高密度扫描，清晰主动作'),(1347,3,'上下文详情','按需解释，返回路径清楚')]:
        f.badge(x-120,874,n)
        f.text(x-92,881,t,21,INK,600)
        f.text(x-120,919,sub,17,MUTED)
    f.footer('NAVIGATION / WORK / CONTEXT')
    f.save('workstation-anatomy.svg')

def before_after():
    f=Figure(1600,940,'同一工作台的设计层级比较','左侧多个装饰与主动作相互竞争；右侧用清楚的层级、对齐和紧凑列表强调同一资料任务。')
    f.header('03 / DESIGN CRITIQUE','相同材料，不同的信息组织与注意力分配','比较标准：用户是否更容易识别主动作、扫描资料、理解状态。')
    for x,label in [(64,'A  /  元素彼此竞争'),(835,'B  /  任务层级清楚')]:
        f.text(x,205,label,24,INK,600)
        f.rect(x,228,701,490,WHITE,LINE,14)
    x=64
    f.rect(x+20,249,660,75,'#eee5ff',r=18)
    f.text(x+44,291,'✨ SMART RESEARCH STUDIO',25,'#6044a4',700)
    f.text(x+35,359,'我的资料中心',27,INK,700)
    for i,t in enumerate(['新建','导入','智能分析']):
        f.rect(x+32+i*220,382,204,49,['#8660d0','#d7597c','#417dc7'][i],r=24)
        f.text(x+134+i*220,414,t,18,WHITE,600,'middle')
    for i,t in enumerate(['咖啡器具使用手册','室内植物养护指南','相机设置与维护笔记']):
        y=452+i*78
        f.rect(x+31,y,638,64,'#faf8ff','#d8cef0',15,2)
        f.rect(x+46,y+13,39,39,'#e6dcff',r=12)
        f.text(x+103,y+29,t,21,INK,600)
        f.text(x+103,y+52,'资料  ·  已保存  ·  参考文档',15,'#706786')
        f.rect(x+535,y+17,108,30,'#4d73bd',r=15)
        f.text(x+589,y+39,'查看',16,WHITE,600,'middle')
    x=835
    f.text(x+31,281,'资料与证据',28,INK,700)
    f.text(x+31,313,'把材料放回工作主题之中。',17,MUTED)
    f.rect(x+520,255,152,43,TEAL,r=7)
    f.text(x+596,283,'＋ 导入资料',17,WHITE,600,'middle')
    f.rect(x+31,340,640,43,'#f6f7f3',LINE,7)
    f.text(x+50,368,'搜索资料标题…',17,MUTED)
    f.text(x+33,417,'标题',15,MUTED)
    f.text(x+457,417,'类型',15,MUTED)
    f.text(x+585,417,'状态',15,MUTED)
    f.line(x+31,431,x+670,431)
    for i,t in enumerate(['咖啡器具使用手册','室内植物养护指南','相机设置与维护笔记']):
        y=451+i*72
        if i==0:f.rect(x+21,y-5,660,63,'#eff5e8',r=6)
        f.text(x+34,y+24,t,20,INK,500)
        f.text(x+34,y+48,'更新于今天  ·  含来源定位',14,MUTED)
        f.text(x+457,y+29,'参考文档',16,MUTED)
        f.circle(x+589,y+23,4,TEAL)
        f.text(x+603,y+29,'就绪',16,TEAL)
        f.line(x+31,y+62,x+671,y+62,'#e5eae1')
    f.text(x+33,696,'3 份材料                           选中资料后打开来源详情 →',15,MUTED)
    for x,lines in [(64,['多个强色与按钮争夺注意力','边界重复，资料内容获得的空间偏少']), (835,['一个主动作，其他动作随情境出现','对齐、间距与状态共同表达结构'])]:
        for i,s in enumerate(lines):
            f.circle(x+8,771+i*37,4,TEAL)
            f.text(x+25,778+i*37,s,21,INK)
    f.footer('SAME CONTENT / DIFFERENT HIERARCHY')
    f.save('design-before-after.svg')

def request_review():
    f=Figure(1400,930,'沿一条请求审查后端','入口接收请求，应用服务处理规则与状态，再分别访问存储和外部依赖；结果和诊断回到界面。')
    f.header('04 / BACKEND REVIEW','沿一条请求，找事实与副作用','每个问题写清：位置、触发条件、后果、证据、最小修复。')
    nodes=[(80,216,340,130,'01  入口 / API · IPC','输入 · 契约 · 错误语义'),(530,216,340,130,'02  应用服务','业务规则 · 任务状态'),(980,216,340,130,'03  结果与反馈','返回值 · 真实终态 · 下一步'),(350,491,340,153,'04  持久化','数据库 · 文件 · 迁移'),(800,491,340,153,'05  外部依赖','模型 · 网络 · 解析器')]
    for x,y,w,h,a,b in nodes:
        f.rect(x,y,w,h,WHITE,LINE,14)
        f.text(x+23,y+47,a,23,INK,600)
        f.text(x+23,y+85,b,18,MUTED)
    f.line(420,279,523,279,'#6d837a',2,True)
    f.line(870,279,973,279,'#6d837a',2,True)
    f.path('M 630 346 L 630 413 L 520 413 L 520 483','#6d837a',2,True)
    f.path('M 770 346 L 770 413 L 970 413 L 970 483','#6d837a',2,True)
    f.text(470,393,'写入何时完成？',18,TEAL)
    f.text(890,393,'失败怎样恢复？',18,TEAL)
    f.text(374,615,'事务边界 · 重复写入 · 重开',17,TEAL)
    f.text(824,615,'超时 · 重试 · 取消 · 预算',17,TEAL)
    f.rect(80,704,1240,101,INK,r=12)
    f.text(110,745,'审查证据',23,GREEN,600)
    f.text(300,745,'可复现输入  +  状态变化  +  持久结果  +  运行记录',23,PAPER,500)
    f.text(300,779,'把已确认缺陷、待验证疑点与维护建议分别表达。',18,'#cbd8d2')
    f.footer('TRACE THE REQUEST / EXPLAIN THE FAILURE')
    f.save('request-review.svg')

def states():
    f=Figure(1400,940,'任务状态与取消竞争','queued进入processing。处理可成功或失败；取消先进入cancel_requested，停止后cancelled，已完成提交则仍可ready。')
    f.header('05 / ASYNC STATES','取消请求与最终结果，是两件需要确认的事','任务终态以执行侧的持久结果为准；界面按结果说明已完成或已停止的部分。')
    def node(x,y,w,a,b,fill=WHITE):
        f.rect(x,y,w,100,fill,LINE,12)
        f.text(x+w/2,y+40,a,24,INK,600,'middle')
        f.text(x+w/2,y+73,b,17,MUTED,'400','middle')
    node(70,220,270,'queued','等待处理')
    node(535,220,330,'processing','正在读取与保存')
    node(1060,220,270,'ready','必要结果已保存', '#e1efd2')
    node(535,467,330,'cancel_requested','已收到取消请求','#f1e8cc')
    node(70,467,270,'failed','失败原因可解释','#f4ddd4')
    node(535,701,330,'cancelled','确认停止并记录结果','#e9ece7')
    f.line(340,270,527,270,'#6d837a',2,True)
    f.line(865,270,1052,270,'#6d837a',2,True)
    f.text(907,247,'提交成功',17,TEAL)
    f.line(700,320,700,459,'#6d837a',2,True)
    f.text(720,401,'请求取消',18,TEAL)
    f.path('M 535 290 L 430 290 L 430 517 L 348 517','#6d837a',2,True)
    f.text(375,407,'出错',17,'#9c4836')
    f.line(700,567,700,693,'#6d837a',2,True)
    f.text(720,636,'实际停止',18,TEAL)
    f.line(535,542,348,542,'#6d837a',2,True)
    f.text(364,577,'执行失败',17,'#9c4836')
    f.path('M 865 517 L 1195 517 L 1195 328','#6d837a',2,True,True)
    f.text(955,475,'若完成先于取消生效',18,TEAL)
    f.text(973,507,'保留成功结果',18,TEAL)
    f.rect(70,701,350,100,WHITE,LINE,12)
    f.text(93,741,'关闭面板 / 断开连接',21,INK,600)
    f.text(93,777,'仅凭此现象无法判定任务终态',16,MUTED)
    f.footer('REQUESTED ACTION / COMMITTED OUTCOME')
    f.save('task-states.svg')

def tokens():
    f=Figure(1400,840,'设计token从原始值到语义和组件','原始颜色与间距通过语义token映射到组件。主题切换改变语义映射，组件仍使用语义名。')
    f.header('06 / DESIGN TOKENS','用语义连接视觉意图与组件实现','示例数值是教学选择；颜色对比需按实际前景、背景与状态测量。')
    for x,t,s in [(70,'原始值 / Primitive','颜色、间距、圆角的素材'),(535,'语义 / Semantic','明确用途，而非外观名称'),(1000,'组件 / Component','组合成可用的交互状态')]:
        f.text(x,218,t,23,INK,600)
        f.text(x,253,s,17,MUTED)
    f.rect(70,285,330,325,WHITE,LINE,13)
    for i,(c,t) in enumerate([(INK,'ink-950   #172b31'),(TEAL,'green-700   #2f6659'),(GREEN,'lime-200   #c7ef81'),(PAPER,'paper-50   #f5f3ec')]):
        f.rect(94,311+i*58,34,34,c,LINE,6)
        f.text(145,335+i*58,t,17,INK)
    f.text(94,581,'space: 4 / 8 / 12 / 16 / 24',18,MUTED)
    f.rect(535,285,330,325,INK,r=13)
    for i,t in enumerate(['text.primary','surface.canvas','action.primary','border.subtle','space.control-gap']):f.text(565,336+i*55,t,21,GREEN if i==2 else PAPER,500)
    f.rect(1000,285,330,325,WHITE,LINE,13)
    f.rect(1030,319,270,52,TEAL,r=8)
    f.text(1165,353,'保存结果',20,WHITE,600,'middle')
    f.rect(1030,397,270,52,WHITE,TEAL,8)
    f.rect(1024,391,282,64,'none',TEAL,12,2)
    f.text(1165,431,'键盘焦点',20,TEAL,600,'middle')
    f.text(1030,513,'default / hover / focus',17,MUTED)
    f.text(1030,548,'disabled / loading',17,MUTED)
    f.text(1030,583,'状态与主题一起验证',18,TEAL)
    f.line(400,445,527,445,'#6d837a',2,True)
    f.line(865,445,992,445,'#6d837a',2,True)
    f.rect(70,662,1260,70,'#e6eddd',r=10)
    f.text(700,706,'主题切换：调整语义映射；组件保持同一套使用方式。',23,INK,500,'middle')
    f.footer('PRIMITIVE → SEMANTIC → COMPONENT')
    f.save('design-tokens.svg')

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    for draw in [cover,workflow,workstation,before_after,request_review,states,tokens]: draw()
    print('Generated 7 original SVG figures.')
