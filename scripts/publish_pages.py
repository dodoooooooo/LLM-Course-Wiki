#!/usr/bin/env python3
"""建置、檢查並將單檔網站發布到 gh-pages，不切換 main 工作目錄。"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def git(*args, data=None):
    return subprocess.run(
        ['git', *args], cwd=ROOT, input=data, stdout=subprocess.PIPE,
        text=True, check=True,
    ).stdout.strip()


def main():
    if git('branch', '--show-current') != 'main':
        raise SystemExit('請從 main 分支執行。')
    if git('status', '--porcelain'):
        raise SystemExit('請先提交 main 的變更，再執行發布。')
    git('fetch', 'origin')
    if git('rev-parse', 'HEAD') != git('rev-parse', 'origin/main'):
        raise SystemExit('請先同步並推送 main，再執行發布。')
    for script in ('build.py', 'check.py'):
        subprocess.run([sys.executable, str(ROOT / 'scripts' / script)], cwd=ROOT, check=True)
    if git('status', '--porcelain'):
        raise SystemExit('建置更新了追蹤檔案；請先提交、推送，再重新發布。')
    old = git('ls-remote', '--heads', 'origin', 'refs/heads/gh-pages')
    parent = old.split()[0] if old else None
    if parent:
        git('fetch', 'origin', 'refs/heads/gh-pages')
        files = git('ls-tree', '-r', '--name-only', parent).splitlines()
        if sorted(files) != ['.nojekyll', 'index.html']:
            raise SystemExit('遠端 gh-pages 含額外檔案，停止以免覆蓋人工內容。')
    html = git('hash-object', '-w', 'dist/index.html')
    empty = git('hash-object', '-w', '--stdin', data='')
    tree = git('mktree', data=f'100644 blob {empty}\t.nojekyll\n100644 blob {html}\tindex.html\n')
    if parent and git('rev-parse', f'{parent}^{{tree}}') == tree:
        print('網站產物未變更，無須推送或重複觸發 Pages。')
        return
    args = ['commit-tree', tree]
    if parent:
        args += ['-p', parent]
    commit = git(*args, data=f'發布網站，來源 main {git("rev-parse", "HEAD")}\n')
    # 不使用 force；若遠端同時更新，push 會拒絕，保留遠端內容。
    git('push', 'origin', f'{commit}:refs/heads/gh-pages')
    print(f'已推送 gh-pages：{commit}；仍須確認 GitHub Pages 部署結果。')


if __name__ == '__main__':
    main()
