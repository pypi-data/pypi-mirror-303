import re
from ebooklib import epub


def txt_to_epub(txt_file, epub_file, book_title, author_name):
    # 创建一个新的EPUB书籍对象
    book = epub.EpubBook()
    book.set_identifier('id123456')
    book.set_title(book_title)
    book.set_language('zh')
    book.add_author(author_name)

    # 读取TXT文件内容
    with open(txt_file, 'rb') as f:
        content = f.read()
    content = content.decode('gb2312', errors='ignore')

    # 分割章节
    chapters = re.split(r'\n\s*(第\d+章.*)\n', content)

    for i in range(1, len(chapters), 2):
        chapter_title = chapters[i]
        chapter_content = chapters[i + 1]

        chapter = epub.EpubHtml(title=chapter_title, file_name=f'chap_{i // 2 + 1}.xhtml', lang='zh')
        chapter.content = f'<h1>{chapter_title}</h1><p>{chapter_content.replace("\n", "<br>")}</p>'
        book.add_item(chapter)

        # 添加章节到目录
        book.toc.append(chapter)
        book.spine.append(chapter)

    # 添加书籍必要的导航文件
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # 定义CSS样式
    style = 'BODY {font-family: Arial, Helvetica, sans-serif;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)

    # 将书籍写入EPUB文件
    epub.write_epub(epub_file, book, {})


# 文件路径和书籍信息
txt_file = '/mnt/data/我爹绝对被人夺舍了.txt'
epub_file = '/mnt/data/我爹绝对被人夺舍了.epub'
book_title = '我爹绝对被人夺舍了'
author_name = '未知作者'

# 调用转换函数
txt_to_epub(txt_file, epub_file, book_title, author_name)
print(f'转换完成，EPUB文件保存在: {epub_file}')
