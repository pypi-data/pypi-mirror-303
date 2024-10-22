# playscript

[> English version](https://github.com/satamame/playscript/blob/master/README_en.md)

## 概要

台本を構造化データとして扱うためのパッケージです。

- PyPI : https://pypi.org/project/playscript/
- Doc : https://satamame.github.io/playscript/

## インストール

PyPI からインストールする場合は、追加で fountain をインストールします。

```
> pip install playscript
> pip install git+https://github.com/Tagirijus/fountain.git@7da5447abae640f34448dd36fee83f47a7415fcf
```

GitHub からインストールする場合は、以下のコマンドでインストールされます。

```
> pip install git+https://github.com/satamame/playscript.git
```

## クラス

### PSc

台本データのクラスです。

### PScLine

PSc オブジェクトに含まれる各行を表すクラスです。  
"type" 属性により、セリフやト書きといった「行の種類」が決まります。

### PScLineType

PScLine の "type" を定義する enum 型です。

## 例

### 行を定義して台本を作る

```python
from playscript import PScLineType, PScLine, PSc

title = PScLine.from_text(PScLineType.TITLE, 'ろくでなしの冒険')
h1 = PScLine.from_text(PScLineType.H1, 'シーン１')
direction = PScLine.from_text(PScLineType.DIRECTION, '六郎と七郎、登場。')
dialogue1 = PScLine.from_text(PScLineType.DIALOGUE, '六郎「どうする？」')
dialogue2 = PScLine.from_text(PScLineType.DIALOGUE, '七郎「帰って寝る」')
endmark = PScLine.from_text(PScLineType.ENDMARK, 'おわり')

script = PSc(
    lines=[
        title,
        h1,
        direction,
        dialogue1,
        dialogue2,
        endmark,
    ]
)
```

### Fountain (日本式) から台本を作る

```python
import textwrap
from playscript.conv.fountain import psc_from_fountain

fountain_str = textwrap.dedent('''\
    Title: ろくでなしの冒険
    Author: アラン・スミシ

    # 登場人物

    六郎
    七郎

    # シーン１

    六郎と七郎、登場。

    @六郎
    どうする？

    @七郎
    帰って寝る

    > おわり
''')

script = psc_from_fountain(fountain_str)
```

### Fountain (日本式) を読み込んで PDF にする

```python
from playscript.conv import fountain, pdf

with open('example.fountain', encoding='utf-8-sig') as f:
    script = fountain.psc_from_fountain(f.read())

pdf_stream = pdf.psc_to_pdf(script)

with open('out.pdf', 'wb') as f:
    f.write(pdf_stream.read())
```

### Fountain (日本式) を読み込んで HTML にする

```python
from playscript.conv import fountain, html

with open('example.fountain', encoding='utf-8-sig') as f:
    script = fountain.psc_from_fountain(f.read())

html_str = html.psc_to_html(script)
with open('out.html', 'w', encoding='utf-8') as f:
    f.write(html_str)
```
