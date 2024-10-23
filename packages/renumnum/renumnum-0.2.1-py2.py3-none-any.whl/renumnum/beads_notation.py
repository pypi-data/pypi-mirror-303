import re


class BeadsNotation:
    """数珠玉記数法"""

    def __init__(self, value=0):

        # 整数かどうか判定
        try:
            int_value = int(str(value), 10)
        except ValueError:
            # 整数でなければ次へ
            pass
        else:
            # タプルとして格納する
            self._elements = int_value,
            return

        # タプル型か？
        if type(value) is tuple:
            # そのまま入れる
            self._elements = value
            return

        # それ以外は文字列として扱う
        new_element_list = convert_text_to_element_list(value)

        # タプルとして格納する
        self._elements = tuple(new_element_list)

    def __str__(self):
        """数珠玉記数法"""
        return to_str(self._elements)

    @property
    def elements(self):
        return self._elements


def index_qp(text):
    # print(f"index_qp text:{text}")

    try:
        q = text.index('Q')
        # print(f"Q:{q}")

        p = text.index('P', q)
        # print(f"P:{p}")

        return q, p
    except:
        return None, None


def convert_text_to_element_list(text):
    # 大文字に変換
    text = text.upper()
    # print(f"convert_text_to_element_list text:{text}")

    q, p = index_qp(text)  # WIP

    new_element_list = []

    if not q is None and not p is None:
        # print(f"q:{q} p:{p}")

        a_str = text[:q]
        b_str = text[q+1:p]
        c_str = text[p+1:]
        # print(f"a:{a_str}")
        # print(f"b:{b_str}")
        # print(f"c:{c_str}")

        if a_str:  # 空文字列を避ける
            new_element_list.extend(convert_text_to_element_list(a_str))

        if b_str:
            new_element_list.append(
                tuple(convert_text_to_element_list(b_str)))

        if c_str:
            new_element_list.extend(convert_text_to_element_list(c_str))

    else:
        # print(f"q,p なし q:{q} p:{p} text:{text}")
        # 区切り文字 'O' で分割
        tokens = text.split('O')

        for token in tokens:
            # 整数かどうか判定
            try:
                int_element = int(str(token), 10)
                new_element_list.append(int_element)

            except ValueError:
                # 整数でなければ
                raise ValueError(f"no beads vector notation: {text}")

    return new_element_list


import re

# 英字，アンダースコアか
__pat_alphabet_etc = re.compile(r"^[A-Za-z_]$")

# @staticmethod
# def is_alphabet_etc_of_left_end(text):
#    """左端は英字などか？"""
#    return __pat_alphabet_etc.match(text[:1])


def is_alphabet_etc_of_right_end(text):
    """右端は英字などか？"""
    return __pat_alphabet_etc.match(text[-1:])


def to_str(elements):
    text = ""
    for element in elements:

        # タプル型か？
        if type(element) is tuple:
            text2 = to_str_from_tuple(element)
            text = f"{text}{text2}"

        else:
            # 左項の右端が英字などなら、セパレーターの `o` は不要
            if is_alphabet_etc_of_right_end(text):
                separator = ""
            else:
                separator = "o"

            # 接続
            text = f"{text}{separator}{element}"

    # 先頭の 'o' は除去します
    return text.lstrip('o')


def to_str_from_tuple(element_list):
    # `q`, `p` で挟んだものを `o` で接続
    sub_text = ""
    for elem in element_list:
        sub_text = f"{sub_text}o{elem}"
    # 先頭の 'o' は除去します
    sub_text = sub_text.lstrip('o')

    # `q` が間に入るので、頭の `o` は不要
    return f"q{sub_text}p"
