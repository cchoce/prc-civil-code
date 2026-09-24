# prc-civil-code 插件 1.0.0

中国《民法典》与买卖合同司法解释（2020修正）技能插件。

## 内容

- 民法典七编体系、1260条条号索引、八份体系与应用指南。
- 买卖合同司法解释（2020修正）33条原文、导航与分析指南。
- 请求权基础分析、概念速查、法条定位脚本。

民法典部分是结构化体系和条号索引，不是1260条正文全集。具体案件须联网核验权威现行法律。

## 在 ChatGPT 桌面版使用

这是插件源代码包，尚未通过公共插件目录审核。下载 ZIP 或分享仓库链接不会自动安装插件。

在支持本地插件市场的 ChatGPT 桌面环境中，用 Codex CLI 添加这个插件来源：

```sh
codex plugin marketplace add cchoce/prc-civil-code --ref plugin-v1
```

然后在 ChatGPT 桌面版的 Plugins 中选择“中国民法典插件”来源，打开 prc-civil-code 并安装，在新对话中使用。
若使用解压目录，也可运行 `codex plugin marketplace add /完整路径/prc-civil-code-plugin-v1`，路径应指向本包根目录。
实际入口受版本和账号策略限制；不要向只支持 MCP URL 的连接窗口填写 ZIP 或 GitHub 地址。

安装后可提问：“使用 prc-civil-code，结合买卖合同司法解释，分析这份合同。”

## 手机或网页版的一键安装

本包目前没有公共 ChatGPT 安装链接。面向其他独立账号通过公共目录安装，需要提交插件、完成开发者身份验证和平台审核后发布。包可作为 Skills only ZIP 提交；工作区内发布仅覆盖该工作区，不能替代跨账号公共发布。

官方说明：
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission-errors

## 隐私与权限

不包含用户聊天记录、私人合同、账号凭证或外部服务连接，不配置 MCP 或自动执行钩子。法条定位脚本仅读取插件内的条号索引。
