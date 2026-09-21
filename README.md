# Awesome Android Reverse Engineering

安卓逆向相关**主工具 / MCP / 脚本 / 增强与注入组件（社区俗称「武器」）**精选清单，结构对齐 [awesome-re-mcp](https://github.com/h00klod0er/awesome-re-mcp)。欢迎 PR。

> 范围：APK/DEX 静态分析、动态插桩、Root/注入框架、Frida 脚本与 Gadget、Android RE MCP、学习资源。  
> 不含：盗版激活、黑产打包器、与逆向无关的通用开发框架。

> **统计说明（2026-09-21 11:33 UTC）**：`★` = GitHub Stars；`更新` = 仓库最近一次 `pushed_at`（推送）日期。由 [GitHub Actions](.github/workflows/update-stats.yml) 每周一自动刷新；也可手动 `workflow_dispatch`。PyPI-only 包无独立 star，会注明对应源码仓。

## 目录

- [主工具介绍](#主工具介绍)
- [MCP · 安卓逆向](#mcp--安卓逆向)
- [静态分析](#静态分析)
- [动态分析 · Frida / 运行时](#动态分析--frida--运行时)
- [脚本集 · Frida Snippets](#脚本集--frida-snippets)
- [Root · 注入 · Gadget（增强组件）](#root--注入--gadget增强组件)
- [学习资源](#学习资源)
- [相关清单](#相关清单)
- [收录规范](#收录规范)

---

## 主工具介绍

### [JADX](https://github.com/skylot/jadx) · ★50,547 · 更新 2026-09-12

Dex → Java 反编译 GUI/CLI，安卓静态分析默认入口之一。支持导出 Gradle、搜索、调试插件扩展。

### [Apktool](https://github.com/iBotPeaches/Apktool) · ★25,618 · 更新 2026-09-19

APK 解码 / 回编：资源、`AndroidManifest`、smali。改包、重打包签名前的标准流水线工具。

### [smali / baksmali](https://github.com/JesusFreke/smali) · ★6,625 · 更新 2024-01-17

DEX 汇编与反汇编。Apktool 底层、手改 smali 时必用。

### [dex2jar](https://github.com/pxb1988/dex2jar) · ★13,143 · 更新 2024-07-21

DEX ↔ JAR 转换，方便丢进 JD-GUI / CFR 等 Java 反编译器（现代流程更常直接 JADX）。

### [Frida](https://frida.re/) · 源码 [frida/frida](https://github.com/frida/frida) · ★21,987 · 更新 2026-09-16

跨平台动态插桩。安卓上常配合 `frida-server` / Gadget / Magisk 模块做 Java/Native hook、ssl unpin、脱壳辅助。

### [objection](https://github.com/sensepost/objection) · ★9,402 · 更新 2026-09-17

基于 Frida 的运行时探索 CLI：类枚举、方法 hook、文件系统、常见 bypass 工作流。

### [Magisk](https://github.com/topjohnwu/Magisk) · ★62,884 · 更新 2026-09-21

系统无关 Root 方案（Zygisk 等）。大量「开机拉 Frida / 注入」模块依赖它。

### [KernelSU](https://github.com/tiann/KernelSU) · ★18,525 · 更新 2026-09-21

内核态 Root 方案，部分设备上替代/并行 Magisk 生态。

### [LSPosed](https://github.com/LSPosed/LSPosed) · ★24,771 · 更新 2026-09-14

现代 Xposed 实现（需 Root）。用于模块化改框架行为；另有免 Root 的 [LSPatch](https://github.com/LSPosed/LSPatch)。

### [Androguard](https://github.com/androguard/androguard) · ★6,278 · 更新 2026-09-19

Python 安卓分析库：DEX/APK 解析、控制流、脚本化审计。

### [Drozer](https://github.com/ReversecLabs/drozer) · ★4,617 · 更新 2026-04-08

安卓应用安全评估框架（IPC / 组件攻击面），偏动态与交互式评估。

---

## MCP · 安卓逆向

> 让 Cursor / Claude 等直接驱动 JADX / Apktool / Frida。

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | 2,807| 2026-08-30| JADX 插件 + AI/MCP 联动 | 静态分析默认首选之一 |
| [zinja-coder/jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server) | 790| 2026-08-31| 配合 JADX-AI 的独立 MCP Server | Zin MCP 套件 |
| [zinja-coder/apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server) | 655| 2026-07-02| Apktool 解码/改 smali/资源 MCP | 改包与清单分析 |
| [FuzzySecurity/kahlo-mcp](https://github.com/FuzzySecurity/kahlo-mcp) | 134| 2026-02-08| Frida MCP：会话/Job/stdlib | 偏 Agent 自主插桩 |
| [yfe404/frida-mcp](https://github.com/yfe404/frida-mcp) | 21| 2026-07-20| Frida 17 MCP（大量 tools） | 含拉 APK、jadx、unpin 等 |
| [cbxss/frida-mcp](https://github.com/cbxss/frida-mcp) | 15| 2026-01-24| Frida MCP（Python） | 设备/进程/Java hook |
| [majimboo/rexd-frida-mcp](https://github.com/majimboo/rexd-frida-mcp) | 1| 2026-04-05| Frida 通用 RE MCP | 亦收录于 awesome-re-mcp |

---

## 静态分析

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [skylot/jadx](https://github.com/skylot/jadx) | 50,547| 2026-09-12| Dex→Java 反编译 | GUI/CLI |
| [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | 25,618| 2026-09-19| 解码/回编 APK | 资源 + smali |
| [pxb1988/dex2jar](https://github.com/pxb1988/dex2jar) | 13,143| 2024-07-21| DEX/JAR 互转 | *以 API 为准 |
| [google/android-classyshark](https://github.com/google/android-classyshark) | 7,556| 2023-05-19| 字节码浏览 | 轻量查看 |
| [JesusFreke/smali](https://github.com/JesusFreke/smali) | 6,625| 2024-01-17| smali/baksmali | DEX 汇编 |
| [androguard/androguard](https://github.com/androguard/androguard) | 6,278| 2026-09-19| Python 分析框架 | 脚本化 |
| [dwisiswant0/apkleaks](https://github.com/dwisiswant0/apkleaks) | 6,305| 2025-08-20| 扫 URI/端点/密钥 | 快速情报 |
| [rednaga/APKiD](https://github.com/rednaga/APKiD) | 2,577| 2026-09-02| 识别壳/加固/混淆器 | 预研 |
| [linkedin/qark](https://github.com/linkedin/qark) | 3,390| 2024-01-16| APK 安全问题扫描 | SAST 向 |
| [patrickfav/uber-apk-signer](https://github.com/patrickfav/uber-apk-signer) | 2,753| 2023-10-30| 签名 + zipalign | 重打包收尾 |
| [reversenseorg/dexcalibur](https://github.com/reversenseorg/dexcalibur) | 1,173| 2026-09-18| 安卓逆向辅助平台（Dexcalibur 系） | 动态+静态工作流 |
| [strazzere/android-unpacker](https://github.com/strazzere/android-unpacker) | 1,177| 2020-01-20| 经典脱壳思路实现 | Defcon 演讲相关 |
| [bkerler/edl](https://github.com/bkerler/edl) | 2,592| 2026-09-19| Qualcomm EDL/Firehose | 底层刷写/拉取向 |

\* 表中日期以仓库 `pushed_at` 实时刷新为准。

---

## 动态分析 · Frida / 运行时

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [frida/frida](https://github.com/frida/frida) | 21,987| 2026-09-16| Frida 发行与核心 | 动态插桩 |
| [sensepost/objection](https://github.com/sensepost/objection) | 9,402| 2026-09-17| 运行时探索 CLI | 基于 Frida |
| [hluwa/frida-dexdump](https://github.com/hluwa/frida-dexdump) | 4,559| 2023-03-04| 内存 DEX dump | 脱壳辅助 |
| [ReversecLabs/drozer](https://github.com/ReversecLabs/drozer) | 4,617| 2026-04-08| 组件/IPC 评估框架 | 原 F-Secure/MWI 系 |
| [m0bilesecurity/RMS-Runtime-Mobile-Security](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security) | 3,091| 2026-09-03| Web UI 运行时分析 | Frida 前端 |
| [nccgroup/house](https://github.com/nccgroup/house) | 1,466| 2021-06-03| 运行时分析 Web GUI | 偏研究 |
| [dpnishant/appmon](https://github.com/dpnishant/appmon) | 1,632| 2023-05-01| 运行时监控 | 文档向 |
| [frida/frida-java-bridge](https://github.com/frida/frida-java-bridge) | 412| 2026-06-22| Java 运行时互操作 | Frida 组件 |

---

## 脚本集 · Frida Snippets

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [iddoeldor/frida-snippets](https://github.com/iddoeldor/frida-snippets) | 2,535| 2024-11-29| 手写 Frida 示例集 | 入门/速查 |
| [httptoolkit/frida-interception-and-unpinning](https://github.com/httptoolkit/frida-interception-and-unpinning) | 2,300| 2026-09-18| 拦截与证书固定绕过脚本 | 配 HTTP Toolkit |
| [Areizen/JNI-Frida-Hook](https://github.com/Areizen/JNI-Frida-Hook) | 645| 2023-08-03| 快速 hook JNI Native | Native 层 |
| [cryptax/androidre](https://github.com/cryptax/androidre) | 607| 2026-05-03| 安卓逆向笔记与脚本 | 教学向 |

---

## Root · 注入 · Gadget（增强组件）

> 社区常说的「武器/改良」多指：开机自启 Frida、Zygisk 注入 Gadget、免 Root 补丁框架等——**仅用于你有权测试的应用与设备**。

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [topjohnwu/Magisk](https://github.com/topjohnwu/Magisk) | 62,884| 2026-09-21| Magisk / Zygisk Root | 模块生态底座 |
| [LSPosed/LSPosed](https://github.com/LSPosed/LSPosed) | 24,771| 2026-09-14| Xposed 现代实现 | 需 Root |
| [tiann/KernelSU](https://github.com/tiann/KernelSU) | 18,525| 2026-09-21| 内核 Root | 设备相关 |
| [LSPosed/LSPatch](https://github.com/LSPosed/LSPatch) | 9,381| 2023-12-13| 免 Root Xposed 扩展 | 应用级补丁 |
| [ViRb3/magisk-frida](https://github.com/ViRb3/magisk-frida) | 1,455| 2026-09-09| Magisk 开机跑 frida-server | 常驻插桩 |
| [LSPosed/LSPlant](https://github.com/LSPosed/LSPlant) | 1,381| 2026-09-09| ART Hook 框架 | 模块开发基础库 |
| [lico-n/ZygiskFrida](https://github.com/lico-n/ZygiskFrida) | 1,085| 2025-10-18| Zygisk 注入 Frida Gadget | 对抗部分检测 |

---

## 学习资源

| 项目 | ★ | 更新 | 说明 |
|------|--:|------|------|
| [OWASP/mastg](https://github.com/OWASP/mastg) | 13,190| 2026-09-20| OWASP 移动应用安全测试指南 |
| [r0ysue/AndroidSecurityStudy](https://github.com/r0ysue/AndroidSecurityStudy) | 4,370| 2023-12-02| 安卓应用安全学习（中文） |
| [maddiestone/AndroidAppRE](https://github.com/maddiestone/AndroidAppRE) | 1,559| 2024-04-10| Android App RE Workshop |

---

## 相关清单

| 项目 | ★ | 更新 | 说明 |
|------|--:|------|------|
| [ashishb/android-security-awesome](https://github.com/ashishb/android-security-awesome) | 9,703| 2026-09-21| 安卓安全资源大全 |
| [h00klod0er/awesome-re-mcp](https://github.com/h00klod0er/awesome-re-mcp) | 1| 2026-09-21| 通用逆向 MCP（IDA/Ghidra/x64dbg…） |

---

## 收录规范

1. 与**安卓逆向 / 移动安全研究**直接相关  
2. 提供公开仓库或文档链接  
3. 尽量注明：静态 / 动态 / Root·注入 / MCP / 脚本  
4. 可附 stars 与最近推送（本仓库 Actions 会刷新）  
5. **不要**提交未授权破解、盗版、黑产样本分发链接  

### 建议条目格式

```md
| [org/name](https://github.com/org/name) | ★N | YYYY-MM-DD | 一句话说明 | 关键备注 |
```

---

## 免责声明

本仓库仅作工具与学习资源索引。请遵守当地法律与软件许可；仅在你**有权分析**的应用、固件与设备上使用。绕过他人应用保护、未授权访问数据可能违法。

---

## License

清单内容采用 [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)。第三方项目保留各自许可证。
