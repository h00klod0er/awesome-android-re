# Awesome Android Reverse Engineering

安卓逆向相关**主工具 / MCP / 脚本 / 增强与注入组件（社区俗称「武器」）**精选清单，结构对齐 [awesome-re-mcp](https://github.com/h00klod0er/awesome-re-mcp)。欢迎 PR。

> 范围：APK/DEX 静态分析、动态插桩、Root/注入框架、Frida 脚本与 Gadget、Android RE MCP、学习资源。  
> 不含：盗版激活、黑产打包器、与逆向无关的通用开发框架。

> **统计说明（2026-10-05 05:37 UTC）**：`★` = GitHub Stars；`更新` = 仓库最近一次 `pushed_at`（推送）日期。由 [GitHub Actions](.github/workflows/update-stats.yml) 每周一自动刷新；也可手动 `workflow_dispatch`。PyPI-only 包无独立 star，会注明对应源码仓。

## 目录

- [主工具介绍](#主工具介绍)
- [MCP · 安卓逆向](#mcp--安卓逆向)
- [静态分析](#静态分析)
- [动态分析 · Frida / 运行时](#动态分析--frida--运行时)
- [脚本集 · Frida Snippets](#脚本集--frida-snippets)
- [魔改 Frida · 反检测 server](#魔改-frida--反检测-server)
- [Codeshare · 脚本镜像合集](#codeshare--脚本镜像合集)
- [对抗专项 · Unpin / Flutter / 通用 Bypass](#对抗专项--unpin--flutter--通用-bypass)
- [Root · 注入 · Gadget（增强组件）](#root--注入--gadget增强组件)
- [学习资源](#学习资源)
- [相关清单](#相关清单)
- [收录规范](#收录规范)

---

## 主工具介绍

### [JADX](https://github.com/skylot/jadx) · ★50,746 · 更新 2026-10-03

Dex → Java 反编译 GUI/CLI，安卓静态分析默认入口之一。支持导出 Gradle、搜索、调试插件扩展。

### [Apktool](https://github.com/iBotPeaches/Apktool) · ★25,735 · 更新 2026-09-28

APK 解码 / 回编：资源、`AndroidManifest`、smali。改包、重打包签名前的标准流水线工具。

### [smali / baksmali](https://github.com/JesusFreke/smali) · ★6,626 · 更新 2024-01-17

DEX 汇编与反汇编。Apktool 底层、手改 smali 时必用。

### [dex2jar](https://github.com/pxb1988/dex2jar) · ★13,145 · 更新 2024-07-21

DEX ↔ JAR 转换，方便丢进 JD-GUI / CFR 等 Java 反编译器（现代流程更常直接 JADX）。

### [Frida](https://frida.re/) · 源码 [frida/frida](https://github.com/frida/frida) · ★22,124 · 更新 2026-10-04

跨平台动态插桩。安卓上常配合 `frida-server` / Gadget / Magisk 模块做 Java/Native hook、ssl unpin、脱壳辅助。

### [objection](https://github.com/sensepost/objection) · ★9,424 · 更新 2026-09-17

基于 Frida 的运行时探索 CLI：类枚举、方法 hook、文件系统、常见 bypass 工作流。

### [Magisk](https://github.com/topjohnwu/Magisk) · ★63,075 · 更新 2026-10-04

系统无关 Root 方案（Zygisk 等）。大量「开机拉 Frida / 注入」模块依赖它。

### [KernelSU](https://github.com/tiann/KernelSU) · ★18,864 · 更新 2026-10-05

内核态 Root 方案，部分设备上替代/并行 Magisk 生态。

### [LSPosed](https://github.com/LSPosed/LSPosed) · ★24,921 · 更新 2026-09-28

现代 Xposed 实现（需 Root）。用于模块化改框架行为；另有免 Root 的 [LSPatch](https://github.com/LSPosed/LSPatch)。

### [Androguard](https://github.com/androguard/androguard) · ★6,319 · 更新 2026-10-03

Python 安卓分析库：DEX/APK 解析、控制流、脚本化审计。

### [Drozer](https://github.com/ReversecLabs/drozer) · ★4,626 · 更新 2026-04-08

安卓应用安全评估框架（IPC / 组件攻击面），偏动态与交互式评估。

---

## MCP · 安卓逆向

> 让 Cursor / Claude 等直接驱动 JADX / Apktool / Frida。

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | 2,852| 2026-09-23| JADX 插件 + AI/MCP 联动 | 静态分析默认首选之一 |
| [zinja-coder/jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server) | 791| 2026-09-23| 配合 JADX-AI 的独立 MCP Server | Zin MCP 套件 |
| [zinja-coder/apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server) | 661| 2026-07-02| Apktool 解码/改 smali/资源 MCP | 改包与清单分析 |
| [FuzzySecurity/kahlo-mcp](https://github.com/FuzzySecurity/kahlo-mcp) | 135| 2026-02-08| Frida MCP：会话/Job/stdlib | 偏 Agent 自主插桩 |
| [yfe404/frida-mcp](https://github.com/yfe404/frida-mcp) | 24| 2026-07-20| Frida 17 MCP（大量 tools） | 含拉 APK、jadx、unpin 等 |
| [cbxss/frida-mcp](https://github.com/cbxss/frida-mcp) | 15| 2026-01-24| Frida MCP（Python） | 设备/进程/Java hook |
| [majimboo/rexd-frida-mcp](https://github.com/majimboo/rexd-frida-mcp) | 1| 2026-04-05| Frida 通用 RE MCP | 亦收录于 awesome-re-mcp |

---

## 静态分析

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [skylot/jadx](https://github.com/skylot/jadx) | 50,746| 2026-10-03| Dex→Java 反编译 | GUI/CLI |
| [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | 25,735| 2026-09-28| 解码/回编 APK | 资源 + smali |
| [pxb1988/dex2jar](https://github.com/pxb1988/dex2jar) | 13,145| 2024-07-21| DEX/JAR 互转 | *以 API 为准 |
| [google/android-classyshark](https://github.com/google/android-classyshark) | 7,553| 2023-05-19| 字节码浏览 | 轻量查看 |
| [JesusFreke/smali](https://github.com/JesusFreke/smali) | 6,626| 2024-01-17| smali/baksmali | DEX 汇编 |
| [androguard/androguard](https://github.com/androguard/androguard) | 6,319| 2026-10-03| Python 分析框架 | 脚本化 |
| [dwisiswant0/apkleaks](https://github.com/dwisiswant0/apkleaks) | 6,333| 2025-08-20| 扫 URI/端点/密钥 | 快速情报 |
| [rednaga/APKiD](https://github.com/rednaga/APKiD) | 2,591| 2026-09-02| 识别壳/加固/混淆器 | 预研 |
| [linkedin/qark](https://github.com/linkedin/qark) | 3,393| 2024-01-16| APK 安全问题扫描 | SAST 向 |
| [patrickfav/uber-apk-signer](https://github.com/patrickfav/uber-apk-signer) | 2,764| 2023-10-30| 签名 + zipalign | 重打包收尾 |
| [reversenseorg/dexcalibur](https://github.com/reversenseorg/dexcalibur) | 1,176| 2026-10-02| 安卓逆向辅助平台（Dexcalibur 系） | 动态+静态工作流 |
| [strazzere/android-unpacker](https://github.com/strazzere/android-unpacker) | 1,180| 2020-01-20| 经典脱壳思路实现 | Defcon 演讲相关 |
| [bkerler/edl](https://github.com/bkerler/edl) | 2,606| 2026-09-19| Qualcomm EDL/Firehose | 底层刷写/拉取向 |

\* 表中日期以仓库 `pushed_at` 实时刷新为准。

---

## 动态分析 · Frida / 运行时

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [frida/frida](https://github.com/frida/frida) | 22,124| 2026-10-04| Frida 发行与核心 | 动态插桩 |
| [sensepost/objection](https://github.com/sensepost/objection) | 9,424| 2026-09-17| 运行时探索 CLI | 基于 Frida |
| [hluwa/frida-dexdump](https://github.com/hluwa/frida-dexdump) | 4,558| 2023-03-04| 内存 DEX dump | 脱壳辅助 |
| [ReversecLabs/drozer](https://github.com/ReversecLabs/drozer) | 4,626| 2026-04-08| 组件/IPC 评估框架 | 原 F-Secure/MWI 系 |
| [m0bilesecurity/RMS-Runtime-Mobile-Security](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security) | 3,106| 2026-10-01| Web UI 运行时分析 | Frida 前端 |
| [nccgroup/house](https://github.com/nccgroup/house) | 1,468| 2021-06-03| 运行时分析 Web GUI | 偏研究 |
| [dpnishant/appmon](https://github.com/dpnishant/appmon) | 1,632| 2023-05-01| 运行时监控 | 文档向 |
| [frida/frida-java-bridge](https://github.com/frida/frida-java-bridge) | 413| 2026-06-22| Java 运行时互操作 | Frida 组件 |

---

## 脚本集 · Frida Snippets

> 优先收录 **star 高、近两年仍有推送** 的通用脚本集 / 工具包（DEX dump、IL2CPP、综合 hook）。
> Codeshare 镜像与 Unpin/Flutter/Bypass 专项见下方独立章节。

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [CreditTone/hooker](https://github.com/CreditTone/hooker) | 5,314| 2026-09-11| Frida 安卓逆向工具包：CLI、通用脚本、自动 hook、内存漫游、SOCKS5、JustTrustMe / BoringSSL unpin | 综合脚本工具首选之一 |
| [hluwa/frida-dexdump](https://github.com/hluwa/frida-dexdump) | 4,558| 2023-03-04| 内存 DEX dump | 脱壳辅助经典 |
| [dweinstein/awesome-frida](https://github.com/dweinstein/awesome-frida) | 3,541| 2026-04-10| Awesome Frida 资源清单 | 上游索引 |
| [Ch0pin/medusa](https://github.com/Ch0pin/medusa) | 2,348| 2026-09-06| 模块化动态分析框架（大量可组合 Frida 脚本） | Edge-Dynamic 分析 |
| [iddoeldor/frida-snippets](https://github.com/iddoeldor/frida-snippets) | 2,537| 2024-11-29| 手写 Frida 示例集 | 入门/速查 |
| [vfsfitvnm/frida-il2cpp-bridge](https://github.com/vfsfitvnm/frida-il2cpp-bridge) | 1,753| 2026-09-06| IL2CPP dump / trace / hijack（可不依赖 global-metadata.dat） | Unity 向 |
| [Perfare/Zygisk-Il2CppDumper](https://github.com/Perfare/Zygisk-Il2CppDumper) | 3,323| 2024-08-09| Zygisk 运行时 dump IL2CPP | Root 场景 |
| [interference-security/frida-scripts](https://github.com/interference-security/frida-scripts) | 664| 2022-09-26| 通用 Frida Scripts 合集 | 经典合集 |
| [Areizen/JNI-Frida-Hook](https://github.com/Areizen/JNI-Frida-Hook) | 646| 2023-08-03| 快速 hook JNI Native | Native 层 |
| [cryptax/androidre](https://github.com/cryptax/androidre) | 607| 2026-05-03| 安卓逆向笔记与脚本 | 教学向 |

---

## 魔改 Frida · 反检测 server

> 社区俗称「魔改 Frida」：改过特征的 `frida-server` / Gadget，用于降低常见反 Frida 检测命中率。**仅用于你有权测试的环境**；与官方 [frida/frida](https://github.com/frida/frida) 发行版并存时注意版本对齐。

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [Ylarod/Florida](https://github.com/Ylarod/Florida) | 2,235| 2026-10-04| 基础反检测 frida-server | 近年活跃魔改线 |
| [hzzheyang/strongR-frida-android](https://github.com/hzzheyang/strongR-frida-android) | 1,696| 2026-10-04| strongR 系 Android 反检测 frida-server | 高 star、持续更新 |
| [CrackerCat/strongR-frida-android](https://github.com/CrackerCat/strongR-frida-android) | 706| 2025-04-14| strongR-frida-android 分支/镜像 | 同源系 |
| [Exo1i/MagiskHluda](https://github.com/Exo1i/MagiskHluda) | 432| 2026-02-04| Magisk 开机跑更难检测的 frida-server（Hluda 向） | Magisk + 魔改 |
| [hluwa/Patchs](https://github.com/hluwa/Patchs) | 226| 2021-08-16| strongR-frida 相关补丁史料 | 早期资料 |
| [ViRb3/magisk-frida](https://github.com/ViRb3/magisk-frida) | 1,465| 2026-10-04| Magisk 开机拉官方/自选 frida-server | 常驻插桩底座 |
| [lico-n/ZygiskFrida](https://github.com/lico-n/ZygiskFrida) | 1,089| 2025-10-18| Zygisk 注入 Frida Gadget | 对抗部分完整性检测 |
| [March7-code/ZygiskInject](https://github.com/March7-code/ZygiskInject) | 20| 2026-04-09| 基于 ZygiskFrida 的行为分析/注入器 | 衍生改造 |
| [AeonLucid/MagiskFrida](https://github.com/AeonLucid/MagiskFrida) | 222| 2023-05-22| 早期 Magisk 跑 frida-server | 历史方案 |

---



## Codeshare · 脚本镜像合集

> [Frida CodeShare](https://codeshare.frida.re/) 官方站点脚本的镜像 / 同步仓、以及「把流行脚本打包成一箱」的合集。适合当速查库；质量参差，用前自己审一眼。

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [hookmaster/frida-all-in-one](https://github.com/hookmaster/frida-all-in-one) | 3,149| 2019-11-04| 《FRIDA 操作手册》资料合集（hluwa / r0ysue 系） | 中文入门史料 |
| [0xdea/frida-scripts](https://github.com/0xdea/frida-scripts) | 1,666| 2026-08-02| 作者自维护的 Frida 插桩脚本集 | 持续更新 |
| [deathmemory/FridaContainer](https://github.com/deathmemory/FridaContainer) | 1,514| 2025-11-13| 常用 Frida 脚本整合容器 | 中文社区高星合集 |
| [zengfr/frida-codeshare-scripts](https://github.com/zengfr/frida-codeshare-scripts) | 116| 2026-09-27| codeshare 实用脚本同步 | 偏全量镜像 |
| [hyugogirubato/Frida-CodeShare](https://github.com/hyugogirubato/Frida-CodeShare) | 80| 2026-02-08| CodeShare 向脚本整理 | 拦截/改行为类 |
| [frida/frida-codeshare](https://github.com/frida/frida-codeshare) | 23| 2026-05-18| Frida 官方 codeshare 相关仓 | 官方侧 |
| [konsumer/frida-codeshare](https://github.com/konsumer/frida-codeshare) | 1| 2024-08-02| codeshare 可搜索镜像 | 镜像工具 |

站点入口：[codeshare.frida.re](https://codeshare.frida.re/)（网页检索，不占用本表 ★）。

---

## 对抗专项 · Unpin / Flutter / 通用 Bypass

> 「厂商/加固对抗」在开源侧多体现为：**SSL Pinning 绕过、Flutter TLS、Root/模拟器/完整性检测绕过、Burp↔Frida 桥**。下面按专项收；**仅用于授权测试**。单一 App（某银行/某社交）的私仓样本一般不收录。

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [Fuzion24/JustTrustMe](https://github.com/Fuzion24/JustTrustMe) | 5,368| 2024-09-02| Xposed 关证书校验（非 Frida，但安卓 MitM 经典） | SSL 专项 |
| [ax/apk.sh](https://github.com/ax/apk.sh) | 3,840| 2026-01-26| 解码/回编/重签流水线自动化 | 改包前置 |
| [Impact-I/reFlutter](https://github.com/Impact-I/reFlutter) | 2,765| 2026-09-24| Flutter 逆向框架 | Flutter 专项 |
| [httptoolkit/frida-interception-and-unpinning](https://github.com/httptoolkit/frida-interception-and-unpinning) | 2,310| 2026-09-18| 运行时改写 + HTTPS unpin | 网络拦截 |
| [federicodotta/Brida](https://github.com/federicodotta/Brida) | 1,899| 2025-10-30| Burp Suite ↔ Frida 桥 | 抓包联动 |
| [chame1eon/jnitrace](https://github.com/chame1eon/jnitrace) | 1,862| 2023-07-18| JNI API 调用追踪 | Native 专项 |
| [ptswarm/reFlutter](https://github.com/ptswarm/reFlutter) | 1,461| 2022-04-11| reFlutter 早期公开仓 | Flutter 史料 |
| [NVISOsecurity/disable-flutter-tls-verification](https://github.com/NVISOsecurity/disable-flutter-tls-verification) | 676| 2026-06-17| 关闭 Flutter TLS 校验的 Frida 脚本 | Flutter unpin |
| [ReversecLabs/android-keystore-audit](https://github.com/ReversecLabs/android-keystore-audit) | 476| 2025-07-17| Android Keystore 审计相关 | 密钥/证书向 |
| [okankurtuluss/FridaBypassKit](https://github.com/okankurtuluss/FridaBypassKit) | 166| 2025-06-12| 通用 Root / SSL Pinning / 检测绕过套件 | 综合 Bypass |
| [yohanes/zygisk-reflutter](https://github.com/yohanes/zygisk-reflutter) | 143| 2025-05-10| Zygisk 版 reFlutter | Flutter + Root |
| [CYRUS-STUDIO/frida-ssl-pinning-bypass](https://github.com/CYRUS-STUDIO/frida-ssl-pinning-bypass) | 82| 2026-04-26| Java + Native 通用 SSL Pinning 绕过 | unpin 脚本 |

---
## Root · 注入 · Gadget（增强组件）

> 社区常说的「武器/改良」多指：开机自启 Frida、Zygisk 注入 Gadget、免 Root 补丁框架等——**仅用于你有权测试的应用与设备**。

| 项目 | ★ | 更新 | 说明 | 备注 |
|------|--:|------|------|------|
| [topjohnwu/Magisk](https://github.com/topjohnwu/Magisk) | 63,075| 2026-10-04| Magisk / Zygisk Root | 模块生态底座 |
| [LSPosed/LSPosed](https://github.com/LSPosed/LSPosed) | 24,921| 2026-09-28| Xposed 现代实现 | 需 Root |
| [tiann/KernelSU](https://github.com/tiann/KernelSU) | 18,864| 2026-10-05| 内核 Root | 设备相关 |
| [LSPosed/LSPatch](https://github.com/LSPosed/LSPatch) | 9,409| 2023-12-13| 免 Root Xposed 扩展 | 应用级补丁 |
| [ViRb3/magisk-frida](https://github.com/ViRb3/magisk-frida) | 1,465| 2026-10-04| Magisk 开机跑 frida-server | 常驻插桩 |
| [LSPosed/LSPlant](https://github.com/LSPosed/LSPlant) | 1,392| 2026-09-24| ART Hook 框架 | 模块开发基础库 |
| [lico-n/ZygiskFrida](https://github.com/lico-n/ZygiskFrida) | 1,089| 2025-10-18| Zygisk 注入 Frida Gadget | 对抗部分检测 |

---

## 学习资源

| 项目 | ★ | 更新 | 说明 |
|------|--:|------|------|
| [OWASP/mastg](https://github.com/OWASP/mastg) | 13,221| 2026-10-01| OWASP 移动应用安全测试指南 |
| [r0ysue/AndroidSecurityStudy](https://github.com/r0ysue/AndroidSecurityStudy) | 4,373| 2023-12-02| 安卓应用安全学习（中文） |
| [maddiestone/AndroidAppRE](https://github.com/maddiestone/AndroidAppRE) | 1,562| 2024-04-10| Android App RE Workshop |

---

## 相关清单

| 项目 | ★ | 更新 | 说明 |
|------|--:|------|------|
| [ashishb/android-security-awesome](https://github.com/ashishb/android-security-awesome) | 9,728| 2026-10-05| 安卓安全资源大全 |
| [h00klod0er/awesome-re-mcp](https://github.com/h00klod0er/awesome-re-mcp) | 1| 2026-09-28| 通用逆向 MCP（IDA/Ghidra/x64dbg…） |

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
