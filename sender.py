from common.const import COUNT_BITS


class Sender:
    def Encrypt(self, text: str, key: list[int]):
        result = []
        for ch in text:
            num = 0
            # Проходим по битам
            for num_bit in range(COUNT_BITS):
                bit = (ord(ch) >> num_bit) & 1
                num += bit * key[COUNT_BITS - 1 - num_bit]
            result.append(num)
        return "".join([chr(s) for s in result])
