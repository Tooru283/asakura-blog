# Blogos / Transparent Respiration 🌊

<div align="center">
    <h2>透明的呼吸感 (Transparent Respiration)</h2>
    <p>基于 <b>浅仓透 (Asakura Toru)</b> 的印象意境设计，基于 <a href="https://astro.build/">Astro</a> 与 <a href="https://github.com/Motues/Momo">Momo 模板</a> 深度定制重构的博客引擎。</p>
</div>

## ✨核心美学 (Aesthetics)
我们从“风、海、宇宙”中汲取灵感，摒弃了传统的平铺直叙，为“观测记录”与“碎碎念”提供了一个绝对静谧、清透的容器。

* **毛玻璃质感 (Glassmorphism)**：全局采用 `backdrop-filter` 搭建视觉层叠。界面不再是阻挡，而是像水面一样透射后方流动的光影。
* **潜入式交互 (Dive-In Portal)**：拥有一个 3D 视差引导的动态环境入口，用户化身为“风”，通过点击破除毛玻璃“沉降”至博客主世界，每次浏览如同一次深海潜水。
* **绝对的冷峻色调**：日间（过曝白 `#FDFDFD` 到 浅海蓝 `#E0F2F7`）；夜间（深海蓝 `#0A192F` 沉降至 宇宙黑 `#010409`）。
* **思源黑体 (Noto Sans SC)**：全站字体极致克制，追求足够的行距与呼吸感留白。

## 🧩 拓展功能 (Features)
* **语录挂件 (Asakura Quotes)**：角落自顾自悬浮的浅仓透语录挂件（Svelte 实现），在鼠标不经意的触发中传递偶像片段。
* **碎碎念同步流 (Fragments Sync)**：通过定制的 Python 脚本，极速同步并平铺您的 Obsidian 日常沉淀，打造随性纯粹的时间流体验。
* 完整继承自上游 Momo 的配置：支持页面搜索 (Pagefind)、多语言支持、RSS 等底层应用能力。

## 🚀快速使用指南
```bash
# 安装依赖
pnpm install

# 本地同步黑曜石(Obsidian)文章至碎片流
python scripts/sync_obsidian.py

# 启动开发服务器
pnpm dev
```

该系统专为“记录者”设计，兼顾了高维的视觉沉浸感与作为文字管理枢纽的极简原则。