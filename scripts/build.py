#!/usr/bin/env python3
"""由 Wiki Markdown 與各課程設定建置離線網站，不列舉特定課程。"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import base64
import hashlib
import html
import json
import mimetypes
import re
import sys

sys.path.insert(0, str(Path(__file__).parent / 'vendor'))
import markdown

ROOT = Path(__file__).resolve().parents[1]


def scalar(value):
    value = value.strip()
    if value.startswith('[') and value.endswith(']'):
        return [scalar(part) for part in value[1:-1].split(',') if part.strip()]
    try:
        return json.loads(value)
    except (ValueError, TypeError):
        return value.strip("\"'")


def read_markdown(path):
    text = path.read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    meta = {}
    if match:
        for line in match[1].splitlines():
            field = re.match(r'^([\w-]+):\s*(.*)$', line)
            if field:
                meta[field[1]] = scalar(field[2])
        text = text[match.end():]
    heading = re.search(r'^# (.+)', text, re.M)
    meta.setdefault('title', heading[1] if heading else path.stem)
    return meta, text


def description(body):
    return next((line.strip() for line in body.splitlines()
                 if line.strip() and not line.startswith(('#', '-', '[', '|', '>'))), '瀏覽課程筆記與相關內容。')


def build(root=ROOT):
    root = Path(root).resolve()
    wiki = root / 'wiki'
    courses, pages, routes, pathroutes = [], [], {route: {'kind': 'tool'} for route in ['/', '/sources', '/search', '/records', '/wrong']}, {}
    pagepaths = {}
    images = {}
    asset_names = {}
    for asset in sorted((wiki / 'assets').rglob('*')):
        if asset.is_file() and (mimetypes.guess_type(asset.name)[0] or '').startswith('image/'):
            uri = 'data:' + mimetypes.guess_type(asset.name)[0] + ';base64,' + base64.b64encode(asset.read_bytes()).decode()
            images[asset.relative_to(wiki / 'assets').as_posix()] = uri
            asset_names.setdefault(asset.name, []).append(uri)
    for name, values in asset_names.items():
        if len(values) == 1:
            images[name] = values[0]  # 保留舊題庫的圖檔識別碼。

    def register(path, route, **fields):
        path = path.resolve()
        if path in pathroutes:
            raise ValueError(f'頁面被重複分類：{path}')
        if route in routes:
            raise ValueError(f'路由重複：{route}')
        if not route.startswith('/') or any(char in route for char in '?#"<> '):
            raise ValueError(f'路由格式錯誤：{route}')
        meta, body = read_markdown(path)
        page_id = path.relative_to(wiki).with_suffix('').as_posix()
        item = dict(id=page_id, path=route, title=meta['title'], short=meta['title'],
                    desc=description(body), courseId=meta.get('course'), sectionId=None,
                    kind=meta.get('type', 'article'), status=meta.get('status', ''),
                    source='／'.join(str(s) for s in meta.get('sources', [])), pages=None,
                    questions=[], trackReading=False, metadata=meta)
        item.update(fields)
        item['readKey'] = str(item.get('readKey', page_id))
        item['quizKey'] = str(item.get('quizKey', page_id))
        item['recordChapter'] = item.get('recordChapter', item['quizKey'])
        pages.append(item)
        routes[route] = dict(kind='page', id=page_id)
        pathroutes[path] = route
        pagepaths[page_id] = (path, body)
        return item

    directories = sorted((wiki / 'courses').glob('*/index.md'))
    configured = []
    for index in directories:
        directory = index.parent
        config_path = directory / 'course.json'
        config = json.loads(config_path.read_text()) if config_path.exists() else {}
        meta, body = read_markdown(index)
        course_id = directory.name
        accent = config.get('accent')
        if accent is not None:
            if not isinstance(accent, str) or not re.fullmatch(r'#[0-9a-fA-F]{6}', accent):
                raise ValueError(f'{config_path} 的 accent 必須是六位十六進位色碼')
            def luminance(color):
                channels = [int(color[i:i+2], 16) / 255 for i in (1, 3, 5)]
                linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in channels]
                return sum(v * w for v, w in zip(linear, (0.2126, 0.7152, 0.0722)))
            if (luminance(accent) + 0.05) / (luminance('#111111') + 0.05) < 4.5:
                raise ValueError(f'{config_path} 的 accent 與黑字對比不足 4.5:1')
        route = config.get('route', '/courses/' + course_id)
        course = dict(id=course_id, title=meta['title'], path=route,
                      description=config.get('description', description(body)),
                      order=config.get('order', 0), accent=accent, sections=[], sourceIds=[])
        courses.append(course)
        home = register(index, route, courseId=course_id, kind='course')
        course['indexId'] = home['id']
        routes[route] = dict(kind='course', id=course_id)
        # 未設定的課程從實際分類索引讀取，不假定固定分類名稱。
        sections = config.get('sections')
        if sections is None:
            sections = []
            for section_index in sorted(directory.glob('*/index.md')):
                smeta, _ = read_markdown(section_index)
                sections.append(dict(id=section_index.parent.name, label=smeta['title'],
                                     directory=section_index.parent.name,
                                     kind=smeta.get('type', 'article')))
        seen_sections = set()
        for settings in sections:
            section_id = settings['id']
            if section_id in seen_sections:
                raise ValueError(f'{course_id} 分類重複：{section_id}')
            seen_sections.add(section_id)
            folder = (directory / settings.get('directory', section_id)).resolve()
            if directory.resolve() not in folder.parents:
                raise ValueError('分類目錄必須位於所屬課程內')
            section_route = route + '/' + settings.get('route', section_id)
            section = dict(id=section_id, label=settings['label'], path=section_route,
                           kind=settings.get('kind', 'article'),
                           trackReading=settings.get('trackReading', False), showIntro=settings.get('showIntro', False), pageIds=[])
            course['sections'].append(section)
            section_index = folder / 'index.md'
            if section_index.exists():
                entry = register(section_index, section_route, courseId=course_id,
                                 sectionId=section_id, kind='section')
                section['indexId'] = entry['id']
                section['subtitle'] = entry['metadata'].get('subtitle', '')
            else:
                if section_route in routes:
                    raise ValueError(f'路由重複：{section_route}')
            routes[section_route] = dict(kind='section', courseId=course_id, id=section_id)
            for nested in sorted(folder.rglob('index.md')):
                if nested == section_index:
                    continue
                nested_route = section_route + '/' + nested.parent.relative_to(folder).as_posix()
                register(nested, nested_route, courseId=course_id, sectionId=section_id, kind='section-index')
            candidates = sorted(f for f in folder.rglob('*.md') if f.name != 'index.md')
            for path in candidates:
                relative = path.relative_to(directory).as_posix()
                options = dict(config.get('pages', {}).get(relative, {}))
                page_route = options.pop('route', section_route + '/' + path.relative_to(folder).with_suffix('').as_posix())
                item = register(path, page_route, courseId=course_id, sectionId=section_id,
                                kind=section['kind'], trackReading=section['trackReading'], **options)
                section['pageIds'].append(item['id'])
            section['pageIds'].sort(key=lambda pid: (next(p for p in pages if p['id'] == pid).get('order', 0), pid))
        configured.append((directory, config, course))

    # 其餘 Wiki 頁面同樣可閱讀、追溯與搜尋，不增設未選用的主要分類。
    for path in sorted(wiki.rglob('*.md')):
        if path.resolve() in pathroutes:
            continue
        relative = path.relative_to(wiki)
        if relative.parts[0] == 'sources':
            route = '/sources/' + path.stem
        elif relative.parts[0] == 'courses':
            course = next((c for c in courses if c['id'] == relative.parts[1]), None)
            if not course:
                continue
            suffix = list(relative.with_suffix('').parts[2:])
            if suffix[-1] == 'index':
                suffix.pop()
            route = course['path'] + '/' + '/'.join(suffix)
        else:
            route = '/wiki/' + relative.with_suffix('').as_posix()
        register(path, route)

    by_id = {page['id']: page for page in pages}
    for directory, config, course in configured:
        for section in course['sections']:
            for pid in section['pageIds']:
                item = by_id[pid]
                path, body = pagepaths[pid]
                if item['kind'] == 'quiz':
                    blocks = re.findall(r'```json\s*\n(.*?)\n```', body, re.S)
                    item['questions'] = json.loads(blocks[0]) if blocks else []
                lesson = item.get('lesson')
                if lesson:
                    paired = (directory / lesson).resolve()
                    if paired not in pathroutes:
                        raise ValueError(f'找不到對應課程：{path} -> {lesson}')
                    item['lessonPath'] = pathroutes[paired]
                else:
                    # 相同檔名的閱讀頁可自動配對；也可在設定中指定。
                    candidates = [p for p in pages if p['courseId'] == course['id']
                                  and p['trackReading'] and Path(p['id']).name == path.stem]
                    item['lessonPath'] = candidates[0]['path'] if len(candidates) == 1 else course['path']
        course['sourceIds'] = [p['id'] for p in pages if p['kind'] == 'source' and p['courseId'] == course['id']]

    def compile_page(item):
        path, body = pagepaths[item['id']]
        if item['kind'] == 'quiz':
            body = re.sub(r'```json\s*\n.*?\n```', '', body, flags=re.S)
        body = re.sub(r'`([^`\n]+)`', lambda m: '`' + m[1].replace('|', r'\|') + '`', body)
        rendered = markdown.markdown(body, extensions=['tables', 'fenced_code']).replace('\\|', '|')
        prefix = 'p-' + hashlib.sha256(item['id'].encode()).hexdigest()[:12]
        headings = []

        def heading(match):
            text = html.unescape(re.sub('<[^>]+>', '', match[2]))
            ident = prefix + '-s' + str(len(headings) + 1)
            headings.append(dict(id=ident, text=text))
            return f'<h{match[1]} id="{ident}">{match[2]}</h{match[1]}>'

        rendered = re.sub(r'<h([23])>(.*?)</h\1>', heading, rendered)

        def image(match):
            asset = (path.parent / unquote(html.unescape(match[2]))).resolve()
            if not asset.is_relative_to(wiki / 'assets'):
                raise ValueError(f'圖片必須位於 wiki/assets：{path} -> {asset}')
            key = asset.relative_to(wiki / 'assets').as_posix()
            return '<img' + match[1] + 'src="' + images[key] + '"'

        rendered = re.sub(r'<img([^>]*?)src="([^"]+)"', image, rendered)

        def link(match):
            target = html.unescape(match[1])
            if target.startswith(('https://', 'http://')):
                return 'href="' + html.escape(target, quote=True) + '" target="_blank" rel="noopener"'
            if target.startswith('#'):
                return match[0]
            resolved = (path.parent / unquote(urlsplit(target).path)).resolve()
            if resolved in pathroutes:
                return 'href="#' + pathroutes[resolved] + '"'
            if (root / 'raw') in resolved.parents:
                return 'href="#/sources" title="原始教材保存在專案 raw 資料夾"'
            if target.endswith('.md'):
                raise ValueError(f'未建立閱讀路由：{path} -> {target}')
            return match[0]

        rendered = re.sub(r'href="([^"]+)"', link, rendered)
        item.update(html=rendered, text=body, headings=headings, sectionCount=len(headings))
        item['searchText'] = ' '.join(html.unescape(re.sub('<[^>]+>', ' ', rendered)).split())
        item['searchText'] += ' ' + ' '.join(q['prompt'] for q in item['questions'])

    for item in pages:
        compile_page(item)
    courses.sort(key=lambda c: (c['order'], c['id']))
    question_ids, read_keys, quiz_keys = set(), set(), set()
    for item in pages:
        if item['trackReading']:
            if item['readKey'] in read_keys:
                raise ValueError(f'閱讀識別碼重複：{item["readKey"]}')
            read_keys.add(item['readKey'])
        if item['kind'] == 'quiz':
            if str(item['recordChapter']) != item['quizKey']:
                raise ValueError('recordChapter 與 quizKey 必須表示相同的穩定識別碼')
            if item['quizKey'] in quiz_keys:
                raise ValueError(f'測驗紀錄識別碼重複：{item["quizKey"]}')
            quiz_keys.add(item['quizKey'])
        for q in item['questions']:
            if q['id'] in question_ids:
                raise ValueError(f'題目 ID 重複：{q["id"]}')
            question_ids.add(q['id'])
    data = dict(schemaVersion=2, courses=courses, pages=pages, routes=routes, images=images)
    template = (root / 'web/template.html').read_text()
    if template.count('__WIKI_DATA__') != 1:
        raise ValueError('網站資料插槽數量錯誤')
    if template.count('__WIKI_CSS__') != 1:
        raise ValueError('共用樣式插槽數量錯誤')
    template = template.replace('__WIKI_CSS__', (root / 'web/styles.css').read_text())
    payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    result = template.replace('__WIKI_DATA__', payload)
    (root / 'index.html').write_text(result, encoding='utf-8')
    (root / 'dist').mkdir(exist_ok=True)
    (root / 'dist/index.html').write_text(result, encoding='utf-8')
    print(f'建置完成：{len(courses)} 門課程、{len(pages)} 頁、{len(question_ids)} 題。')
    return data


if __name__ == '__main__':
    build()
