import re


class DictionaryOrderNumber:
    """辞書順番号"""

    pattern = re.compile(r"([Aa]*|[_]*)([0-9]+)")

    def __init__(self, value=0):

        try:
            # 整数かどうか判定
            int_value = int(str(value), 10)
        except ValueError:
            # 整数ではなかった
            result = DictionaryOrderNumber.pattern.match(value)
            if result:
                # 構文は合っているようだ
                prefix = result.group(1)
                numeric = result.group(2)

                if prefix[:1].upper() == 'A':
                    # 正の整数
                    #
                    # 桁数比較
                    if len(prefix) + 1 == len(numeric):
                        # Aの個数が合っていた
                        self._number = int(numeric)
                    else:
                        # Aの個数が合っていない
                        raise ValueError(
                            f"not dictionary ordinal number: {value}")

                else:
                    # 負の整数
                    #
                    # 桁数比較
                    if len(prefix) == len(numeric):
                        # '_' の個数が合っていた
                        figure = len(numeric)

                        modulo = 1
                        for i in range(0, figure):
                            modulo *= 10

                        self._number = -1*(modulo - int(numeric))

                    else:
                        # '_' の個数が合っていない
                        raise ValueError(
                            f"not dictionary ordinal number: {value}")

            else:
                # 構文エラー
                raise ValueError(f"not dictionary ordinal number: {value}")
        else:
            # 整数だ
            self._number = int_value

    def __str__(self):
        if self._number < 0:
            # 負の整数
            #
            # "-1" の絶対値 "1" なら文字列の桁数は 1
            figure = len(str(abs(self._number)))

            # Underscore
            prefix_u = ""
            for i in range(0, figure):
                prefix_u += "_"

            # その負数の絶対値より１桁大きい数の中で一番小さな数
            modulo = 1
            for i in range(0, figure):
                modulo *= 10

            # 差
            diff_num = modulo + self._number
            # 前ゼロの桁数 = モジュロの桁数 - 差の桁数 - 1
            prefix_z_figure = len(str(modulo)) - len(str(diff_num)) - 1

            # 前ゼロ
            prefix_z = ""
            for i in range(0, prefix_z_figure):
                prefix_z += "0"

            return f"{prefix_u}{prefix_z}{diff_num}"

        else:
            # 零 or 正の整数
            figure = len(str(self._number))
            prefix = ""
            for i in range(1, figure):
                prefix += "A"
            return f"{prefix}{self._number}"

    @property
    def number(self):
        return self._number
