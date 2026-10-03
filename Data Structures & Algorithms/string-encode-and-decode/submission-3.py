class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            lenght = len(s)
            encoded_string += ("#" + str(len(s)) + "#" + s)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            print(i, s[i])
            if s[i] == "#":
                lenght = ""
                while i < len(s)-1 and s[i+1] != "#":
                    lenght += s[i+1]
                    i += 1
                start = i+2
                end = start + int(lenght)
                output.append(s[start:end])
                i = end
                continue
            i += 1
        return output