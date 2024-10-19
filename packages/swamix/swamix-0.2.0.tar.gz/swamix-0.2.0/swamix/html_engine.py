import logging
import re
import timeit
import requests

from bs4 import BeautifulSoup
from cssutils import parseString
from selectolax.parser import HTMLParser
from tinycss2.parser import parse_stylesheet


def remove_junk(raw_css):
    raw_css = re.sub(r'[\n\t]', '', raw_css)  # remove all newlines and tabs
    raw_css = re.sub(r'/\*.*?\*/', '', raw_css)  # remove commnets
    return raw_css


def minify_css_with_domselect(html_content, css_content, out_path="./styles.css"):
    import re

    # from pyquery import PyQuery
    stylesheet = parse_stylesheet(css_content, skip_comments=True, skip_whitespace=True)
    really_important = []
    reselect = re.compile(r":[\w]+")
    i = 0
    for token in stylesheet:
        ts = token.serialize()
        if token.type == 'qualified-rule':
            selector = "".join([p.serialize() for p in token.prelude])
            selector = re.sub(reselect, "", selector)
            try:
                # test = BeautifulSoup(html_content, 'xml').select(selector)
                # test = PyQuery(html_content, parser="html").find(selector)
                test = HTMLParser(html_content).css(selector)
                if test:
                    really_important.append(ts)

            except Exception as e:
                really_important.append(ts)
                # print("ERRORED: ", e, i, ts)

        i += 1
        # print((i / len(stylesheet)) * 100, "%", end="\r")

    open(out_path, 'w', encoding="utf-8").write('\n'.join(really_important))

    initsize = len(css_content)
    finalsize = len(open(OUT, encoding="utf-8").read())
    print('bytes saved :', (initsize - finalsize) / initsize * 100, '%')


def minify_with_tokenparsing(html, css, out_path="./styles.css"):
    """Parse HTML to identify used CSS classes"""

    html_used_tokens = set()
    soup = BeautifulSoup(html, 'html.parser')
    important = []
    stylesheet = parse_stylesheet(css, skip_comments=True, skip_whitespace=True)

    for tag in soup.find_all(True):
        if tag.has_attr('class'):
            html_used_tokens.update(tag['class'])
        if tag.has_attr('id'):
            html_used_tokens.add(tag['id'])

    # get all types of tags and add them to the set
    for tag in soup.find_all(True):
        html_used_tokens.add(tag.name)

    # print((html_used_tokens))

    for token in stylesheet:
        ts = token.serialize()
        if token.type == 'qualified-rule':
            for p in token.prelude:
                try:
                    if p.value.startswith(':'):
                        important.append(ts)
                        break
                except:
                    pass

                if p.type in ['ident', 'hash'] and p.value in html_used_tokens:
                    important.append(ts)
                    break

        if token.type == 'at-rule':
            continue

    open(out_path, 'w', encoding="utf-8").write('\n'.join(important))
    initsize = len(css_content)
    finalsize = len(open(OUT, encoding="utf-8").read())
    print('bytes saved :', (initsize - finalsize) / initsize * 100, '%')


def minify_with_plain_regex(html, css, out_path="./styles.css"):
    def seperate_media_queries(raw_css):
        matches = re.findall(r'(@media[^{]*){([^}]+})}|([^{]+){([^}]+)}', raw_css)
        return matches

    def parse_rules(raw_css):
        raw_css = re.sub(r'[\n\t]', '', raw_css)

    parsed = seperate_media_queries(css_content)
    regular_rules = []
    media_queries = [
        {s1.strip(): s2} if s1.startswith('@media') else regular_rules.append({s3.strip(): s4})
        for s1, s2, s3, s4 in parsed
    ]
    media_queries = filter(lambda x: x, media_queries)
    regular_rule_dict = {}
    DOM = HTMLParser(html_content)
    for r in regular_rules:
        sel, props = tuple(r.items())[0]
        props = [prop.strip() for prop in props.split(';')]
        props = [
            prop for prop in props if not prop.startswith('-')
        ]  # remove browser compatibility rules "-prop-erty: ...;"

        csv_classes = []
        replace_problematic = re.compile(r'[>}]')
        sel = re.sub(replace_problematic, ' ', sel)
        for s in sel.split(','):
            normalized = re.sub(r':.*', '', s)
            if DOM.css(normalized):
                csv_classes.append(s)

        csv_classes = ','.join(csv_classes)
        if csv_classes:
            if regular_rule_dict.get(csv_classes):
                print([csv_classes], regular_rule_dict[csv_classes])
                regular_rule_dict[csv_classes].extend(props)

            else:
                regular_rule_dict[csv_classes] = props

    # write to file
    with open(OUT, 'w', encoding="utf-8") as f:
        for sel, props in regular_rule_dict.items():
            if sel == "":
                continue
            props = ";".join(props)
            f.write(f"{sel} {{{props}}}\n")

    initsize = len(css_content)
    finalsize = len(open(OUT, encoding="utf-8").read())
    print('bytes saved :', (initsize - finalsize) / initsize * 100, '%')


def convert_to_markdown(html):
    from markdownify import markdownify
    import selectolax

    # remove scripts and styles, link
    dom = selectolax.parser.HTMLParser(html)
    for el in dom.css('script, style, link'):
        el.decompose()
    # print(dom.html)
    # convert to html

    md = markdownify(dom.html)
    return md


def img_compress(file):
    """
    Purpose: rename to webp all images in html file.
    INPUT: html or css file
    """

    file = Path(file)

    # check if file is html
    if file.suffix == '.html':
        with open(file, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')

        for img in soup.find_all('img'):
            # replace all extensions except .svg and .ico

            if img['src'].split('.')[-1] not in ['svg', 'ico']:
                img['src'] = img['src'].replace(img['src'].split('.')[-1], 'webp')

        # append new to new index
        with open(file.with_name('index.html'), 'w') as f:
            f.write(str(soup))

    # if css
    if file.suffix == '.css':
        # try using regex
        with open(file, 'r') as f:
            text = f.read()

        # replace all extensions except .svg and .ico
        for i in re.findall(r'url\((.*?)\)', text):
            if i.split('.')[-1] not in ['svg', 'ico']:
                text = text.replace(i.split('.')[-1], 'webp')

        with open(file.with_name('style.css'), 'w') as f:
            f.write(text)
