import argparse
import os
import subprocess
import uuid
from datetime import datetime

from bs4 import BeautifulSoup
from markdownify import markdownify


def flomo2json(source):
    bs = BeautifulSoup(source, 'html.parser')
    result = []
    for memo in bs.find_all('div', class_='memo'):
        item = memo2json(memo)
        result.append(item)

    return result


def mdify(html):
    return markdownify(html)


def memo2json(memo_div):
    time = memo_div.find('div', class_='time').text

    content = memo_div.find('div', class_='content')
    markdown = mdify(str(content))

    imgs = memo_div.find_all('img')
    links = []
    for img in imgs:
        links.append(img['src'])

    item = {
        'time': time,
        'content': markdown,
        'files': links,
    }

    return item


def memo2md(memo_div):
    item = memo2json(memo_div)
    time = item['time']
    content = item['content'].strip().replace('\\', '')
    files = item['files']
    if files:
        images = '\nimages:\n' + ''.join([f'* ![]({x})\n' for x in files])
    else:
        images = ''

    md = create_md(time, content, images)
    return {'created_at': time, 'md': md}


def create_md(time, content, images):
    return (
        f"""# {time}

{content}
"""
        + images
    )


def flomo2md(source):
    bs = BeautifulSoup(source, 'html.parser')
    result = []
    for memo in bs.find_all('div', class_='memo'):
        item = memo2md(memo)
        result.append(item)

    return result


def modify_file_times(file_path, time_str):
    # 将时间格式化为 "mm/dd/yy HH:MM:SS" 格式
    creation_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    creation_time_str = creation_time.strftime('%m/%d/%y %H:%M:%S')
    # modification_time_str = modification_time.strftime('%m/%d/%y %H:%M:%S')

    # 使用 SetFile 命令修改文件的创建时间和修改时间
    subprocess.run(['SetFile', '-d', creation_time_str, '-m', creation_time_str, file_path])


def main():
    input, output = cli()

    os.makedirs(output, exist_ok=True)

    with open(input, encoding='utf-8') as f:
        source = f.read()
        items = flomo2md(source)
        for item in items:
            created_at = item['created_at']
            md = item['md']
            title = uuid.uuid4().hex + '.md'
            md_path = os.path.join(output, title)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md)
            modify_file_times(md_path, created_at)


def cli():
    p = argparse.ArgumentParser()
    p.add_argument('input', type=str)
    p.add_argument('output', type=str)
    args = p.parse_args()
    input = args.input
    output = args.output
    return input, output


if __name__ == '__main__':
    main()
