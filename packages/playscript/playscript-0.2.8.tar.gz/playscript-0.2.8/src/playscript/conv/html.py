import pathlib
import re
from functools import lru_cache

from jinja2 import Environment, FileSystemLoader


@lru_cache
def class_name(line_type):
    """台本行の種類を HTML の class 名に変換するフィルタ
    """
    map2class = {
        'TITLE': 'title',
        'AUTHOR': 'author',
        'CHARSHEADLINE': 'chars-headline',
        'CHARACTER': 'character',
        'H1': 'headline-1',
        'H2': 'headline-2',
        'H3': 'headline-3',
        'DIRECTION': 'direction',
        'DIALOGUE': 'dialogue',
        'ENDMARK': 'endmark',
        'COMMENT': 'comment',
        'EMPTY': 'empty',
    }
    return map2class[line_type.name]


def esc_spc(s):
    """空白文字をエスケープするフィルタ
    """
    escaped = re.sub(r'\r?\n', '<br>', s)
    escaped = re.sub(r'\s', '&nbsp;', escaped)
    return escaped


@lru_cache
def template_dir():
    """テンプレートのディレクトリを取得する
    """
    dir = pathlib.Path(__file__).resolve().parent / 'templates/html'
    return dir


def get_template(dir, file_name):
    """HTML テンプレートを取得する
    """
    loader = FileSystemLoader(dir)
    env = Environment(loader=loader)
    env.filters['class_name'] = class_name
    env.filters['esc_spc'] = esc_spc
    template = env.get_template(file_name)
    return template


@lru_cache
def default_template():
    """デフォルトの HTML テンプレートを取得する
    """
    return get_template(template_dir(), 'default.html')


@lru_cache
def default_css():
    """デフォルトのスタイルシートを取得する
    """
    files = ['app.css', 'psc.css']
    style = ''
    for fname in files:
        style_path = template_dir() / 'styles' / fname
        with open(style_path, encoding='utf-8') as f:
            style += f.read()
    return '<style type="text/css">\n' + style + '</style>'


@lru_cache
def default_js():
    """デフォルトの JavaScript を取得する
    """
    files = ['app.js', 'init.js', 'psc.js']
    js = ''
    for fname in files:
        style_path = template_dir() / 'scripts' / fname
        with open(style_path, encoding='utf-8') as f:
            js += f.read()
    return '<script type="text/javascript">\n' + js + '</script>'


def psc_to_html(psc, title=None, template=None, css=None, js=None):
    """台本オブジェクトから HTML を生成する

    Parameters
    ----------
    psc : PSc
        ソースとなる台本オブジェクト
    title : str
        HTML のタイトル
    template : str
        HTML テンプレート
    css : str
        スタイルシート部分の HTML
    js : str
        JavaScript 部分の HTML
    """
    context = {'lines': psc.lines}
    context['toc_items'] = []
    context['title'] = title if title else psc.title
    context['css'] = css if css else default_css()
    context['js'] = js if js else default_js()

    if template:
        html = template.render(context)
    else:
        html = default_template().render(context)

    return html
