#!/usr/bin/env python3
"""檢查內容一致性及可擴充性，不把目前課程／章節／題數當作固定規格。"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


class Extract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.capture = False
        self.data = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'script' and dict(attrs).get('id') == 'wiki-data':
            self.capture = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self.capture = False

    def handle_data(self, data):
        if self.capture:
            self.data += data


def extract(root):
    page = (root / 'index.html').read_text()
    parser = Extract()
    parser.feed(page)
    return page, json.loads(parser.data)


def check_data(root, data):
    indexes = sorted(p.parent.name for p in (root / 'wiki/courses').glob('*/index.md'))
    assert sorted(c['id'] for c in data['courses']) == indexes
    pages = {p['id']: p for p in data['pages']}
    assert len(pages) == len(data['pages']), '頁面 ID 重複'
    expected = {p.relative_to(root / 'wiki').with_suffix('').as_posix()
                for p in (root / 'wiki').rglob('*.md')
                if not p.relative_to(root / 'wiki').parts[0] == 'courses'
                or p.relative_to(root / 'wiki').parts[1] in indexes}
    assert set(pages) == expected, 'Wiki 頁面未完整加入網頁'
    question_ids = set()
    for course in data['courses']:
        assert data['routes'][course['path']] == {'kind': 'course', 'id': course['id']}
        config_path = root / 'wiki/courses' / course['id'] / 'course.json'
        config = json.loads(config_path.read_text()) if config_path.exists() else {}
        if 'sections' in config:
            assert [s['id'] for s in course['sections']] == [s['id'] for s in config['sections']]
        for section in course['sections']:
            directory = next((s.get('directory', s['id']) for s in config.get('sections', []) if s['id'] == section['id']), section['id'])
            folder = root / 'wiki/courses' / course['id'] / directory
            actual = {p.relative_to(root / 'wiki').with_suffix('').as_posix()
                      for p in folder.rglob('*.md') if p.name != 'index.md'}
            assert set(section['pageIds']) == actual
        assert set(course['sourceIds']) == {p['id'] for p in pages.values() if p['courseId'] == course['id'] and p['kind'] == 'source'}
    for page in pages.values():
        assert page['path'] in data['routes']
        assert len({h['id'] for h in page['headings']}) == len(page['headings'])
        assert not re.search(r'href="[^"#]*\.md(?:#[^"]*)?"', page['html'])
        assert '<script' not in page['html']
        assert not re.search(r'<code>[^<]*\\\|', page['html'])
        for url in re.findall(r'<img[^>]*src="([^"]+)"', page['html']):
            assert url.startswith('data:image/')
        for link in re.findall(r'href="#([^"?]+)', page['html']):
            assert unquote(link) in data['routes'], (page['id'], link)
        path = root / 'wiki' / (page['id'] + '.md')
        blocks = re.findall(r'```json\s*\n(.*?)\n```', path.read_text(), re.S)
        if page['kind'] == 'quiz':
            assert page['questions'] == (json.loads(blocks[0]) if blocks else [])
        for q in page['questions']:
            assert q['id'] not in question_ids, '題目 ID 重複'
            question_ids.add(q['id'])
            assert q['prompt'] and q['source']
            assert all(isinstance(n, int) and n >= 1 for n in q['pages'])
            if page['pages']:
                assert all(n <= page['pages'] for n in q['pages'])
            if q['type'] == 'choice':
                assert len(q['options']) >= 2 and isinstance(q['answer'], int) and 0 <= q['answer'] < len(q['options']) and q['explanation']
            elif q['type'] == 'fill':
                assert q['answers'] and all(isinstance(a, str) and a for a in q['answers']) and q['explanation']
            else:
                assert q['type'] == 'written' and q['model'] and q['rubric']
            if 'answerImage' in q:
                assert q['answerImage'] in data['images']
    return len(question_ids)


def check_js(root):
    if not shutil.which('node'):
        print('未安裝 Node：略過前端程式檢查。')
        return
    html, data = extract(root)
    js = re.findall(r'<script>(.*?)</script>', html, re.S)[-1]
    with tempfile.TemporaryDirectory() as temp:
        script = Path(temp) / 'app.js'
        payload = Path(temp) / 'data.json'
        script.write_text(js)
        payload.write_text(json.dumps(data, ensure_ascii=False))
        subprocess.run(['node', '--check', str(script)], check=True)
        subprocess.run(['node', str(ROOT / 'scripts/test_app.cjs'), str(payload), str(script)], check=True)


def check_sources():
    count = 0
    for source in (ROOT / 'wiki/sources').glob('*.md'):
        text = source.read_text()
        expected = re.search(r'SHA-256[：:]\s*`([a-f0-9]{64})`', text)
        targets = re.findall(r'\]\(([^)]+\.pdf)\)', text)
        if expected and targets:
            archived = (source.parent / targets[0]).resolve()
            assert hashlib.sha256(archived.read_bytes()).hexdigest() == expected[1], str(archived)
            count += 1
    return count


def check_links():
    problems = []
    for path in ROOT.rglob('*.md'):
        if any(part in path.parts for part in ['raw', 'vendor', 'templates', 'derived']):
            continue
        text = re.sub(r'`[^`]*`', '', path.read_text())
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in target or target.startswith('#'):
                continue
            if not (path.parent / unquote(target.split('#')[0])).resolve().exists():
                problems.append(f'{path.relative_to(ROOT)} -> {target}')
    assert not problems, '\n'.join(problems)


def check_extensibility(build, actual):
    with tempfile.TemporaryDirectory() as temp:
        fixture = Path(temp)
        (fixture / 'web').mkdir()
        (fixture / 'web/template.html').write_text((ROOT / 'web/template.html').read_text())
        (fixture / 'web/styles.css').write_text((ROOT / 'web/styles.css').read_text())
        (fixture / 'wiki/courses').mkdir(parents=True)
        (fixture / 'wiki/sources').mkdir()
        (fixture / 'wiki/sources.md').write_text('# 來源登錄\n')
        # 零門課亦能建置與使用工具頁。
        data = build(fixture)
        assert not data['courses']
        check_data(fixture, data)
        check_js(fixture)
        # 分類、資料夾名稱、路由與題數刻意不同，且不複製任何既有課程設定。
        for number, slug in enumerate(['z-course', 'a-course', 'middle-course']):
            folder = fixture / 'wiki/courses' / slug
            (folder / 'reading').mkdir(parents=True)
            (folder / 'reports').mkdir()
            (folder / 'practice').mkdir()
            (folder / 'index.md').write_text(f'---\ntitle: 新課程 {slug}\n---\n# 新課程\n')
            config = {'route': '/courses/' + slug, 'sections': [
                {'id': 'study', 'directory': 'reading', 'label': '主題閱讀', 'kind': 'lesson', 'trackReading': True},
                {'id': 'papers', 'directory': 'reports', 'label': '論文報告', 'kind': 'paper', 'trackReading': True},
                {'id': 'quiz', 'directory': 'practice', 'label': '隨堂練習', 'kind': 'quiz'}]}
            (folder / 'course.json').write_text(json.dumps(config, ensure_ascii=False))
            for chapter in range(number + 1):
                (folder / f'reading/topic-{chapter}.md').write_text(f'# 主題 {slug} {chapter}\n\n[課程](../index.md)\n')
            (folder / 'reports/paper.md').write_text('# 論文報告\n\n論文方法與限制。\n')
            questions = [dict(id=slug+'-q', type='choice', level='理解', prompt='選擇正確答案 '+slug,
                              source=slug+'-source', pages=[1], options=['甲','乙','丙'], answer=2, explanation='本題解析 '+slug)]
            (folder / 'practice/quiz.md').write_text('# 隨堂練習\n\n```json\n'+json.dumps(questions, ensure_ascii=False)+'\n```\n')
            (fixture / 'wiki/sources' / (slug+'.md')).write_text(f'---\ncourse: {slug}\ntype: source\n---\n# 測試來源 {slug}\n')
        data = build(fixture)
        check_data(fixture, data)
        check_js(fixture)
        assert sorted(len(c['sections'][0]['pageIds']) for c in data['courses']) == [1,2,3]
        before = {p['id']: (p['readKey'],p['quizKey'],p['path']) for p in data['pages']}
        # 名稱與排序改變，識別碼／路由不變；章節增刪與題數增加無須改前端。
        course_dir = fixture / 'wiki/courses/a-course'
        (course_dir / 'index.md').write_text('---\ntitle: 更名課程\n---\n# 更名課程\n')
        cfg=json.loads((course_dir/'course.json').read_text());cfg['order']=-10
        (course_dir/'course.json').write_text(json.dumps(cfg))
        (course_dir/'reading/extra.md').write_text('# 新增章節\n')
        quiz_path=course_dir/'practice/quiz.md'
        text=quiz_path.read_text()
        bank=json.loads(re.search(r'```json\s*\n(.*?)\n```',text,re.S)[1])
        bank.append(dict(id='added-question',type='fill',level='理解',prompt='新增填空題',source='new-source',pages=[1],answers=['Answer'],explanation='新題解析'))
        quiz_path.write_text('# 隨堂練習\n\n```json\n'+json.dumps(bank,ensure_ascii=False)+'\n```\n')
        (fixture/'wiki/courses/z-course/reading/topic-0.md').unlink()
        data=build(fixture)
        for page in data['pages']:
            if page['id'] in before:
                assert (page['readKey'],page['quizKey'],page['path'])==before[page['id']]
        check_data(fixture,data)
        check_js(fixture)
        # 無設定課程依實際索引發現分類。
        plain=fixture/'wiki/courses/plain-course/seminars'
        plain.mkdir(parents=True)
        (plain.parent/'index.md').write_text('# 無設定課程\n')
        (plain/'index.md').write_text('# 專題研討\n')
        (plain/'talk.md').write_text('# 研討筆記\n')
        data=build(fixture)
        check_data(fixture,data)
        assert next(c for c in data['courses'] if c['id']=='plain-course')['sections'][0]['label']=='專題研討'
        check_js(fixture)


    # 既有相容設定中的 pages 不得變成白名單；新增章節與題庫仍自動發現。
    candidate=next((c for c in actual['courses'] if any(s['kind']=='quiz' for s in c['sections']) and any(s['trackReading'] for s in c['sections'])),None)
    if candidate:
        with tempfile.TemporaryDirectory() as temp:
            fixture=Path(temp)
            for directory in ['wiki','web']:
                shutil.copytree(ROOT/directory,fixture/directory)
            course_dir=fixture/'wiki/courses'/candidate['id']
            cfg=json.loads((course_dir/'course.json').read_text())
            reading=next(s for s in cfg['sections'] if s.get('trackReading'))
            quiz_section=next(s for s in cfg['sections'] if s['kind']=='quiz')
            for section in [reading,quiz_section]:
                (course_dir/section.get('directory',section['id'])).mkdir(parents=True,exist_ok=True)
            lesson=course_dir/reading.get('directory',reading['id'])/'extension-topic.md'
            lesson.write_text('# 新增閱讀主題\n\n不需要頁面覆寫設定。\n')
            quiz=course_dir/quiz_section.get('directory',quiz_section['id'])/'extension-topic.md'
            question=dict(id='extension-test-question',type='choice',level='理解',prompt='新增題庫題目',source='extension-source',pages=[1],options=['甲','乙'],answer=1,explanation='測試解析')
            quiz.write_text('# 新增題庫\n\n```json\n'+json.dumps([question],ensure_ascii=False)+'\n```\n')
            data=build(fixture)
            check_data(fixture,data)
            original={p['id']:p for p in actual['pages']}
            for page in data['pages']:
                if page['id'] in original:
                    old=original[page['id']]
                    assert [page[k] for k in ['path','readKey','quizKey','recordChapter']]==[old[k] for k in ['path','readKey','quizKey','recordChapter']]
                    assert page['questions']==old['questions']
            assert sum(len(p['questions']) for p in data['pages'])==sum(len(p['questions']) for p in actual['pages'])+1
            new_quiz=next(p for p in data['pages'] if p['questions']==[question])
            assert new_quiz['lessonPath']==next(p['path'] for p in data['pages'] if p['title']=='新增閱讀主題')
            check_js(fixture)


def main():
    spec = importlib.util.spec_from_file_location('wiki_build', ROOT / 'scripts/build.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    html, data = extract(ROOT)
    assert (ROOT/'dist/index.html').read_text() == html, '建置結果不一致'
    assert not re.search(r'<(?:script|link)[^>]+(?:src|href)="https?://', html)
    css=(ROOT/'web/styles.css').read_text()
    assert css in html and '__WIKI_CSS__' not in html, '共用樣式未完整內嵌'
    assert not re.search(r'gradient\(|(?:backdrop-)?filter\s*:\s*blur|@import',css), '禁止漸層、模糊與外部樣式'
    assert not re.search(r'url\(\s*[\"\']?https?://',css), '不得依賴外部字體或素材'
    assert '@media (max-width: 720px)' in css and 'prefers-reduced-motion' in css
    questions=check_data(ROOT,data)
    check_links()
    hashes=check_sources()
    check_js(ROOT)
    # 前端與建置邏輯不准列舉課程代號或沿用舊資料陣列。
    for path in [ROOT/'scripts/build.py',ROOT/'web/template.html']:
        text=path.read_text()
        assert not re.search(r'DATA\.(?:chapters|hardware)|range\(1,5\)|\[1-7\]',text)
    check_extensibility(module.build, data)
    print(f'全部檢查通過：{len(data["courses"])} 門實際課程、{len(data["pages"])} 頁、{questions} 題、{hashes} 份來源雜湊；擴充與舊紀錄相容性通過。')


if __name__=='__main__':
    main()
