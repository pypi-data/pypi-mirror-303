import re
from .beads_notation import BeadsNotation
from .dictionary_order_number import DictionaryOrderNumber


def num(*args):
    """リナンバリンギスト番号を作ります
    
    例えば o1o0 を作るときは 1 と指定してください。末尾の 0 は含めないでください

    例えば、
    import renumnum as rn
    として、
    oo = rn.num(1) のように使う方法を推奨します。
    リナンバリンギスト番号の変数名は何でも構いませんがとりあえず oo としてみましょう

    Parameters
    ----------
    *args : tuple
        可変長引数

        整数が１つ
        (1)

        整数が複数
        (1, 2)

        文字列１つで整数が１つ
        ('1')
        ('10')

        辞書順記数法
        ('_9')
        ('A10')

        数珠玉記数法
        ('O_9')
        ('OA10')
        ('O_9o1oA10')

        タプル
        ((1, 2))

        リスト
        ([1, 2])
    """

    element_list = None

    # 引数が０個か？
    if len(args) < 1:
        raise ValueError('specify one or more arguments')

    # 引数が１つか？
    elif len(args) == 1:
        try:
            # 整数かどうか判定
            int_value = int(str(args[0]), 10)

        # 整数ではなかったら
        except ValueError:
            # タプル型なら
            if type(args[0]) is list:
                # そのまま使う
                element_list = args[0]

            # タプル型なら
            elif type(args[0]) is tuple:
                # いったんリストに戻す
                element_list = list(args[0])

            # TODO 整数ではなかったら
            else:
                # 文字列と想定して解析を進める
                element_list = RenumNum.convert_str_to_list(args[0])

        # 整数だったら
        else:
            # リストに変換する
            element_list = []
            element_list.append(int_value)

    # 引数が複数個か？
    else:
        # リストに変換する
        element_list = []
        element_list.extend(list(args))

    # 0 の要素を追加
    element_list.append(0)

    # タプルに変換して使う
    return RenumNum(tuple(element_list))


class RenumnumInSrc():
    """テストで使う仕組み

    テストでは

        import renumnum as rn

    のように書けないので、
    テストでは以下のように書く

        from src.renumnum import renumnum_in_src as rn
    
    """

    @staticmethod
    def num(*arg):
        """グローバル関数の num() を呼び出す
        
        Parameters
        ----------
        *arg : tuple
            可変長引数
        """
        global num

        # arg はタプルなので、 *(arg) と書くことで、可変長引数に expanding する
        return num(*(arg))


renumnum_in_src = RenumnumInSrc()


class RenumNum:
    """リナンバー主義者の番号"""

    # めんどくさいので .upper() して 'O' と数字で構成されていればOkとする
    # 辞書順記数法に対応するために、めんどくさいので '_', 'A' が含まれていてもOkとする
    __pattern1 = re.compile(r"^([_AO\d]*)$")


    @staticmethod
    def what_is(upper_case_text):
        """種類を調べる

        先頭に O が付いているものは、［数珠玉記数法］か、［リナンバリンギスト番号］のどちらか。
        
            'o0' または 'O0' なら［数珠玉記数法］、
            それ以外で末尾に 'o0' または 'O0' が付いていたら［リナンバリンギスト番号］、
            末尾に 'o0' または 'O0' が付いていなければ［数珠玉記数法］
        
        どちらにしても先頭に付いている O は削除する。［リナンバリンギスト番号］であれば、末尾の 'o0' または 'O0' は削除する
        """
        if not upper_case_text.startswith('O'):
            return None

        if upper_case_text == 'O0':
            return 'beads'
        
        if upper_case_text.endswith('O0'):
            return 'renumnum'
        
        return 'beads'


    @staticmethod
    def convert_str_to_list(text):
        # 大文字に変換
        text = text.upper()

        # '_', 'A', 'O' と数字で構成されている必要がある
        result = RenumNum.__pattern1.match(text)
        if result:
            pass
        else:
            raise ValueError(f"not cyber vector: {text}")


        kind = RenumNum.what_is(upper_case_text=text)
        if kind == 'renumnum':
            # 先頭の 'O' １文字、末尾の 'O0' ２文字を削除する 
            text = text[1:-2]
        
        elif kind == 'beads':
            # 先頭の 'O' １文字を削除する 
            text = text[1:]


        new_element_list = []

        # 区切り文字 O で分割
        tokens = text.split('O')

        for token in tokens:
            if token[:1] == 'A':
                # A を除去する
                n = int(token.replace('A', ''))
                new_element_list.append(n)

            elif token[:1] == '_':
                # まず '_' を除去する
                token = token.replace('_', '')

                figure = len(token)
                modulo = 1
                for i in range(0, figure):
                    modulo *= 10

                z = -1 * (modulo - int(token))
                new_element_list.append(z)

            else:
                n = int(token)
                new_element_list.append(n)

        return new_element_list


    def __init__(self, vector_as_tuple):
        """初期化

        このコンストラクタを直接呼び出すことは推奨しません。
        詳しくは Init クラスの num 関数を参照してください

        Parameters
        ----------
        vector_as_tuple : tuple
            タプル
        """

        if type(vector_as_tuple) is not tuple:
            raise ValueError(f"vector_as_tuple argument type must be a tuple")

        # そのまま渡す
        self._beadsv = BeadsNotation(vector_as_tuple)
        

    def __str__(self):
        """辞書順記数法 と 数珠玉記数法 の併用"""
        text = ""
        for token in self.elements:
            text = f"{text}o{DictionaryOrderNumber(token)}"

        # 先頭だけを大文字の 'O' にする
        text = f"O{text[1:]}"
        return text


    def _kind_of_compare(self, other):
        me = self.tolist()
        you = other.tolist()
        end = max(len(me), len(you))
        #print(f"{me=}  {you=}  {end=}")
        for i in range(0, end):
            if i < len(me):
                me_val = me[i]
            else:
                # NOTE 特殊ルール：[0] と [0, 0] では、[0, 0] の方が大きい
                if you[i] == 0:
                    return 'less_than'

                me_val = 0
            
            if i < len(you):
                you_val = you[i]
            else:
                # NOTE 特殊ルール：[0, 0] と [0] では、[0, 0] の方が大きい
                if me[i] == 0:
                    return 'greater_than'

                you_val = 0

            #print(f"({i=})  {me_val=}  {you_val=}")

            if me_val < you_val:
                return 'less_than'
            
            if me_val > you_val:
                return 'greater_than'

        # equals
        return 'equals'



    def __lt__(self, other):
        """ < 演算子のオーバーロード"""
        kind = self._kind_of_compare(other=other)
        return kind == 'less_than'


    def __gt__(self, other):
        """ > 演算子のオーバーロード"""
        kind = self._kind_of_compare(other=other)
        return kind == 'greater_than'


    def __le__(self, other):
        """ <= 演算子のオーバーロード"""
        kind = self._kind_of_compare(other=other)
        return kind in ['less_than', 'equals']


    def __ge__(self, other):
        """ >= 演算子のオーバーロード"""
        kind = self._kind_of_compare(other=other)
        return kind in ['greater_than', 'equals']


    def __eq__(self, other):
        """ == 演算子のオーバーロード"""
        kind = self._kind_of_compare(other=other)
        return kind == 'equals'


    def __ne__(self, other):
        """ != 演算子のオーバーロード"""
        kind = self._kind_of_compare(other=other)
        return kind != 'equals'


    @property
    def elements(self):
        return self._beadsv.elements


    def totuple(self):
        """末尾の 0 を取り除いたリストを返す"""
        return self._beadsv.elements[0:-1]


    def tolist(self):
        """末尾の 0 を取り除いたリストを返す"""
        return list(self._beadsv.elements)[0:-1]
