---
name: prc-civil-code
description: "Structured knowledge base for the Civil Code of the People's Republic of China (中华人民共和国民法典). Use for PRC civil-law issue spotting, claim-basis analysis, Code article navigation, contract/property/personality/marriage/succession/tort questions, or studying the Code's system. Verify current judicial interpretations and exact statutory wording before high-stakes reliance."
---

<!-- argument-hint: [争议事实、主题、编章或条号] -->

# 中华人民共和国民法典
**制定机关**：第十三届全国人民代表大会第三次会议  
**通过**：2020-05-28｜**施行**：2021-01-01｜**条文**：1260条｜**生成**：2026-09-20

## 使用规则

1. 先识别法律关系和请求权，再检索条文；不要从单个关键词直接跳到结论。
2. 对事实按“主体—行为—标的—时间—证据—损害/履行状态”整理。
3. 准确区分法典正文、其他法律、司法解释、案例与学理观点。
4. 本技能提供体系和条文定位，不保存整部法典原文。引用具体条文时，尤其是诉讼、合同审查或高风险决定，应核对国家法律法规数据库等权威现行文本。
5. 涉及司法解释或时效性规则时必须联网核验，不得假定技能生成日之后没有变化。

## 核心分析模型

### 民事法律关系六要素
- **主体**：自然人、法人、非法人组织；能力、身份、代表/代理权限。
- **客体**：物、行为、智力成果、人格利益、数据等。
- **权利义务**：物权、债权、人格权、身份权、继承权及救济权。
- **法律事实**：法律行为、事实行为、事件或违法行为。
- **责任**：继续履行、返还、停止侵害、赔偿等；区分违约与侵权。
- **程序**：举证、时效、保全、管辖、执行。

### 请求权检索顺序
1. 找特别法或特别编的具体请求权基础。
2. 检查总则对主体、行为效力、代理、责任及时效的共同规则。
3. 列明构成要件，并逐项对应事实和证据。
4. 检查抗辩、免责、减责、权利失效与请求权竞合。
5. 给出法律效果和现实执行路径。

### 关键区分
- 合同成立 ≠ 生效 ≠ 有效 ≠ 已履行；解除也不等于自始无效。
- 债权行为 ≠ 物权变动；合同有效不代表所有权已经转移。
- 无权处分 ≠ 合同当然无效；无权代理与表见代理另行判断。
- 诉讼时效届满 ≠ 实体权利自动消灭。
- 共同债务、共同侵权、连带责任均需法律依据，不能由“关系密切”推出。

## 编章索引

| 文件 | 范围 | 核心主题 |
|---|---|---|
| [ch01](chapters/ch01-general-provisions.md) | 第1—204条 | 主体、法律行为、代理、责任、时效 |
| [ch02](chapters/ch02-property-rights.md) | 第205—462条 | 物权变动、所有权、用益物权、担保、占有 |
| [ch03](chapters/ch03-contracts.md) | 第463—988条 | 合同通则、典型合同、准合同 |
| [ch04](chapters/ch04-personality-rights.md) | 第989—1039条 | 生命健康、姓名肖像、名誉、隐私与个人信息 |
| [ch05](chapters/ch05-marriage-family.md) | 第1040—1118条 | 结婚、家庭关系、离婚、收养 |
| [ch06](chapters/ch06-succession.md) | 第1119—1163条 | 法定继承、遗嘱、遗产管理与债务 |
| [ch07](chapters/ch07-tort-liability.md) | 第1164—1260条 | 一般侵权、特殊侵权、附则 |
| [ch08](chapters/ch08-system-application.md) | 跨编 | 请求权基础与法律检索方法 |

## 主题路由
- **合同效力、违约、解除、保证、租赁、委托** → ch01 + ch03
- **房屋、所有权、抵押、质押、居住权、业主共有** → ch02，必要时 ch03
- **隐私、肖像、名誉、个人信息、性骚扰** → ch04，侵权救济另看 ch07
- **婚姻、夫妻财产、共同债务、离婚、收养** → ch05 + ch01
- **遗嘱、法定继承、遗产债务** → ch06
- **损害赔偿、网络侵权、医疗、环境、动物、高空抛物** → ch07
- **不知道从哪里开始** → ch08

## 支持文件
- [article-index.md](references/article-index.md) — 1260条对应的编、分编、章、节位置
- [glossary.md](glossary.md) — 核心民法术语
- [patterns.md](patterns.md) — 可重复使用的法律分析模式
- [cheatsheet.md](cheatsheet.md) — 单页式决策规则
- [authority-and-update.md](references/authority-and-update.md) — 权威来源、版本与更新边界

## 范围限制
本技能只把《民法典》正文结构化，不自动包含司法解释、指导性案例、地方规定或其他部门法。它不替代针对具体案件的证据审查和专业法律意见。
