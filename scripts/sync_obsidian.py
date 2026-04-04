import os
import shutil
import glob
from pathlib import Path
from datetime import datetime

# Obsidian 碎碎念笔记的来源目录 (请在此处修改为实际路径)
OBSIDIAN_DIR = "/Users/moca/Documents/笔记/研究生/01_Projects/Noctchill/tooru"
# 博客项目中的对应目标目录
TARGET_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "content", "fragments")

def sync_fragments():
    print(f"Syncing fragments from {OBSIDIAN_DIR} to {TARGET_DIR} ...")
    
    if not os.path.exists(OBSIDIAN_DIR):
        print(f"Error: Obsidian source directory '{OBSIDIAN_DIR}' does not exist.")
        return

    os.makedirs(TARGET_DIR, exist_ok=True)
    
    # 获取所有的 .md 文件
    md_files = glob.glob(os.path.join(OBSIDIAN_DIR, "*.md"))
    
    count = 0
    for file_path in md_files:
        filename = os.path.basename(file_path)
        target_path = os.path.join(TARGET_DIR, filename)
        
        # 读取内容处理前置数据 (frontmatter)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        mtime = os.path.getmtime(file_path)
        date_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
        
        if content.startswith('---'):
            # 已经有 frontmatter 的情况，检查是否有 date
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                if 'date:' not in frontmatter:
                    parts[1] = f"{frontmatter.rstrip()}\ndate: {date_str}\n"
                    content = '---'.join(parts)
        else:
            # 没有 frontmatter，添加一个新的
            frontmatter = f"---\ndate: {date_str}\n---\n\n"
            content = frontmatter + content
            
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        count += 1
        
    print(f"Sync complete! {count} files have been processed and copied.")

if __name__ == "__main__":
    sync_fragments()
