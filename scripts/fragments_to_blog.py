"""
把 src/content/fragments/ 下的文章转换为 blog 格式
输出到 src/content/blog/fragments/<filename>/zh-cn.md
"""
import os
import re
import glob
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
FRAGMENTS_DIR = BASE_DIR / "src" / "content" / "fragments"
BLOG_DEST_DIR = BASE_DIR / "src" / "content" / "blog" / "fragments"

def slugify(name: str) -> str:
    """把文件名转为 URL 友好的 slug（保留日文/中文字符，用于 slugId）"""
    name = re.sub(r'\.md$', '', name)
    name = name.replace(' ', '-')
    return name

def extract_first_heading(content: str) -> str | None:
    """从 markdown 内容中提取第一个 # 标题"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def sanitize_for_yaml(text: str, max_len: int = 70) -> str:
    """清理文本，使其可以安全地作为 YAML 双引号字符串值使用"""
    text = text.replace('\\', '')         # 先移除反斜杠
    text = text.replace('"', '\\"')       # 转义双引号
    text = text.replace('\n', ' ')        # 换行变空格
    if len(text) > max_len:
        text = text[:max_len] + '...'
    return text.strip()

def extract_first_paragraph(content: str) -> str:
    """提取正文第一段作为 description"""
    # 移除 frontmatter
    body = re.sub(r'^---[\s\S]*?---\n', '', content).strip()
    # 移除标题行、引用块、列表、代码块等
    body = re.sub(r'^#{1,6}\s+.+\n?', '', body, flags=re.MULTILINE)
    body = re.sub(r'^>\s*.+\n?', '', body, flags=re.MULTILINE)
    body = re.sub(r'^\s*[-*]\s+.+\n?', '', body, flags=re.MULTILINE)
    body = re.sub(r'```[\s\S]*?```', '', body)
    # 移除 markdown 加粗/斜体标记
    body = re.sub(r'\*{1,2}(.+?)\*{1,2}', r'\1', body)
    body = re.sub(r'_{1,2}(.+?)_{1,2}', r'\1', body)
    # 提取第一个非空段落
    for line in body.split('\n'):
        line = line.strip()
        if line and not line.startswith(('#', '>', '-', '*', '`', '|', '---')):
            return sanitize_for_yaml(line)
    return ''

def convert_fragment_to_blog(fragment_path: Path):
    filename = fragment_path.stem  # 例如：10個、光
    slug = slugify(fragment_path.name)
    
    with open(fragment_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 解析现有的 frontmatter
    date_str = datetime.now().strftime('%Y-%m-%d')
    existing_image = ''
    
    fm_match = re.match(r'^---\n([\s\S]*?)\n---\n', content)
    body_content = content
    
    if fm_match:
        fm_text = fm_match.group(1)
        body_content = content[fm_match.end():]  # frontmatter 之后的内容
        
        # 提取 date
        date_match = re.search(r'^date:\s*(.+)$', fm_text, re.MULTILINE)
        if date_match:
            date_str = date_match.group(1).strip()
        
        # 提取 image
        image_match = re.search(r'^image:\s*(.+)$', fm_text, re.MULTILINE)
        if image_match:
            existing_image = image_match.group(1).strip()
    
    # 提取标题
    title = extract_first_heading(body_content) or filename
    # 提取描述
    description = extract_first_paragraph(body_content)
    # 生成 slugId
    slug_id = f"fragments/{slug.replace('.md', '')}"
    
    # 构建新的 frontmatter
    new_frontmatter = f"""---
title: {title}
pubDate: {date_str}
description: "{description}"
category: 碎碎念
image: "{existing_image}"
draft: false
slugId: {slug_id}
---
"""
    
    # 最终内容 = 新 frontmatter + 原正文（去掉 frontmatter）
    final_content = new_frontmatter + '\n' + body_content.lstrip('\n')
    
    # 创建目标目录
    dest_folder = BLOG_DEST_DIR / slug.replace('.md', '')
    dest_folder.mkdir(parents=True, exist_ok=True)
    
    dest_file = dest_folder / "zh-cn.md"
    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"  ✓ {filename} → blog/fragments/{slug.replace('.md', '')}/zh-cn.md")
    return dest_file

def main():
    print(f"🔄 从 fragments 转换到 blog 格式...")
    print(f"   源: {FRAGMENTS_DIR}")
    print(f"   目标: {BLOG_DEST_DIR}\n")
    
    if not FRAGMENTS_DIR.exists():
        print(f"❌ fragments 目录不存在: {FRAGMENTS_DIR}")
        return
    
    md_files = list(FRAGMENTS_DIR.glob("*.md"))
    if not md_files:
        print("❌ 没有找到任何 .md 文件")
        return
    
    count = 0
    for md_file in sorted(md_files):
        try:
            convert_fragment_to_blog(md_file)
            count += 1
        except Exception as e:
            print(f"  ✗ {md_file.name}: {e}")
    
    print(f"\n✅ 完成！共转换了 {count} 篇文章到 src/content/blog/fragments/")

if __name__ == "__main__":
    main()
