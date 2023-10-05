from typing import List


class Conversor:
    # To bases
    def to_binary(self, num: str, base: str) -> str:
        if base == 'Oct':
            return self.octal_to_binary(num)
        elif base == 'Dec':
            return self.decimal_to_binary(num)
        elif base == 'Hex':
            return self.hexadecimal_to_binary(num)
        else:
            return num

    def to_octal(self, num: str, base: str) -> str:
        if base == 'Bin':
            return self.binary_to_octal(num)
        elif base == 'Dec':
            return self.decimal_to_octal(num)
        elif base == 'Hex':
            return self.hexadecimal_to_octal(num)
        else:
            return num

    def to_decimal(self, num: str, base: str) -> str:
        if base == 'Bin':
            return self.binary_to_decimal(num)
        elif base == 'Oct':
            return self.octal_to_decimal(num)
        elif base == 'Hex':
            return self.hexadecimal_to_decimal(num)
        else:
            return num

    def to_hexadecimal(self, num: str, base: str) -> str:
        if base == 'Bin':
            return self.binary_to_hexadecimal(num)
        elif base == 'Oct':
            return self.octal_to_hexadecimal(num)
        elif base == 'Dec':
            return self.decimal_to_hexadecimal(num)
        else:
            return num

    # Binary to others bases
    def binary_to_decimal(self, num: str) -> str:
        binary = list(num)[::-1]
        return str(sum([2 ** i for i, n in enumerate(binary) if n == '1']))

    def binary_to_octal(self, num: str) -> str:
        decimal = self.binary_to_decimal(num)
        return self.decimal_to_octal(decimal)

    def binary_to_hexadecimal(self, num: str) -> str:
        decimal = self.binary_to_decimal(num)
        return self.decimal_to_hexadecimal(decimal)

    # Decimal to others bases
    def decimal_to_binary(self, num: str | int) -> str:
        num = int(num) if isinstance(num, str) else num
        list_binary: List[str] = []

        while True:
            div = num // 2
            rest = num % 2
            num = div

            list_binary.insert(0, str(rest))

            if not div:
                break

        return ''.join(list_binary)

    def decimal_to_octal(self, num: str | int) -> str:
        num = int(num) if isinstance(num, str) else num
        list_octal: List[str] = []

        while True:
            div = num // 8
            rest = num % 8
            num = div

            list_octal.insert(0, str(rest))

            if not div:
                break

        return ''.join(list_octal)

    def decimal_to_hexadecimal(self, num: str | int) -> str:
        num = int(num) if isinstance(num, str) else num
        list_octal: List[str] = []

        dict_hexa = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

        while True:
            div = num // 16
            rest = num % 16
            num = div

            if rest < 10:
                list_octal.insert(0, str(rest))
            else:
                list_octal.insert(0, dict_hexa[rest])

            if not div:
                break

        return ''.join(list_octal)

    # Octal to others bases
    def octal_to_decimal(self, num: str | int) -> str:
        num = str(num) if isinstance(num, int) else num
        list_octal = [int(n) * 8 ** i for i, n in enumerate(list(num)[::-1])]
        return str(sum(list_octal))

    def octal_to_binary(self, num: str | int) -> str:
        decimal = self.octal_to_decimal(num)
        return self.decimal_to_binary(decimal)

    def octal_to_hexadecimal(self, num: str | int) -> str:
        decimal = self.octal_to_decimal(num)
        return self.decimal_to_hexadecimal(decimal)

    # Hexadecimal to others bases
    def hexadecimal_to_decimal(self, num: str) -> str:
        list_num = list(num.upper())
        dict_decimal = {'A': '10', 'B': '11', 'C': '12',
                        'D': '13', 'E': '14', 'F': '15'}

        for i, n in enumerate(list_num):
            if n in dict_decimal.keys():
                list_num[i] = dict_decimal[n]

        list_hexa = [int(n) * 16 ** i for i, n in enumerate(list_num[::-1])]

        return str(sum(list_hexa))

    def hexadecimal_to_binary(self, num: str) -> str:
        decimal = self.hexadecimal_to_decimal(num)
        return self.decimal_to_binary(decimal)

    def hexadecimal_to_octal(self, num: str) -> str:
        decimal = self.hexadecimal_to_decimal(num)
        return self.decimal_to_octal(decimal)


if __name__ == '__main__':
    c = Conversor()
    print(c.to_decimal('F', 'Dec'))
