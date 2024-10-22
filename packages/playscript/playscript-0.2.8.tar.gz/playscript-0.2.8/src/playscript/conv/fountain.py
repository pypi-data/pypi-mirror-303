from fountain import fountain

from .. import PScLineType, PScLine, PSc


def psc_from_fountain(
    s, empty_line=False, charsheadline=['登場人物'], charlines_break=False,
    default_name='*'
):
    """Fountain 文字列から台本オブジェクトを生成する

    Parameters
    ----------
    s : str
        Fountain 文字列
    empty_line : bool
        空行を空行として残すかどうか
    charsheadline : list-like[str]
        登場人物見出し行とみなす文字列のリスト
    charlines_break : bool
        登場人物行が複数行に渡るかどうか
    default_name : str
        名前部分を切り出せない場合に使う名前

    Returns
    -------
    台本オブジェクト : PSc
    """
    # Parse the string into Fountain object.
    f = fountain.Fountain(string=s)

    title = ''
    author = ''
    chars = []
    lines = []

    # Set title(s) from Fountain object.
    if 'title' in f.metadata:
        for title_ in f.metadata['title']:
            lines.append(PScLine(line_type=PScLineType.TITLE, text=title_))
        title = '\n'.join(f.metadata['title'])

    # Set author(s) from Fountain object.
    if 'author' in f.metadata:
        for author_ in f.metadata['author']:
            lines.append(PScLine(line_type=PScLineType.AUTHOR, text=author_))
        author = '\n'.join(f.metadata['author'])

    # Status definition to distinguish Character line from Direction line.
    NOT_IN_LIST = 0
    LIST_STARTED = 1
    CHARS_LISTED = 2
    char_list_status = NOT_IN_LIST

    # Who's speaking.
    last_char_name = default_name

    for e in f.elements:
        # Empty line.
        if e.element_type == 'Empty Line':
            if empty_line:
                lines.append(PScLine(line_type=PScLineType.EMPTY))
            if char_list_status == CHARS_LISTED:
                char_list_status = NOT_IN_LIST

        # Scene headline or Characters headline.
        elif e.element_type == 'Section Heading':
            text = e.element_text
            if text in charsheadline:
                # Set Headline of character list.
                lines.append(PScLine(
                    line_type=PScLineType.CHARSHEADLINE, text=text))
                char_list_status = LIST_STARTED
            else:
                # Set Headline of scene.
                if e.section_depth <= 1:
                    line_type = PScLineType.H1
                elif e.section_depth == 2:
                    line_type = PScLineType.H2
                else:
                    line_type = PScLineType.H3
                lines.append(PScLine(line_type=line_type, text=text))
                char_list_status = NOT_IN_LIST

        # Direction or Character (in character list).
        elif e.element_type == 'Action':
            text = e.element_text
            if char_list_status == NOT_IN_LIST:
                # Set Direction.
                lines.append(PScLine(
                    line_type=PScLineType.DIRECTION, text=text))
            elif charlines_break:
                # Set a Character.
                lines.append(PScLine.from_text(
                    line_type=PScLineType.CHARACTER, text=text))
                char_list_status = CHARS_LISTED
            else:
                # Set Characters.
                for charline in text.splitlines():
                    lines.append(PScLine.from_text(
                        line_type=PScLineType.CHARACTER, text=charline))
                char_list_status = CHARS_LISTED

        # Character name (preceding their line)
        elif e.element_type == 'Character':
            text = e.element_text
            if text not in chars:
                chars.append(text)
            last_char_name = text

        # Dialogue.
        elif e.element_type == 'Dialogue':
            lines.append(PScLine(
                line_type=PScLineType.DIALOGUE,
                name=last_char_name,
                text=e.element_text))
            last_char_name = default_name

        # End mark.
        elif e.element_type == 'Transition':
            lines.append(PScLine(
                line_type=PScLineType.ENDMARK, text=e.element_text))

    psc = PSc(title=title, author=author, chars=chars, lines=lines)
    return psc
