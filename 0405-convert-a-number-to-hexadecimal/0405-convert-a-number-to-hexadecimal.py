class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = []

        # Handle negative numbers using 32-bit two's complement
        num &= 0xFFFFFFFF

        while num:
            result.append(hex_chars[num & 15])  # Last 4 bits
            num >>= 4                           # Shift right by 4 bits

        return "".join(result[::-1])