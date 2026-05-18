class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = []
        for s in strs:
            encode_str.append(str(len(s))+"#")
            encode_str.append(s)
        return "".join(encode_str)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            num = []
            while s[i]!= "#":
                num.append(s[i])
                i += 1
            n = int("".join(num))
            i += 1
            ch = []
            for j in range(n):
                ch.append(s[i])
                i += 1
            ans.append("".join(ch))
        return ans