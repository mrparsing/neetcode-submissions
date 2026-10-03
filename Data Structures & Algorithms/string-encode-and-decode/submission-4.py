class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            lenght = len(s)
            encoded_string += (str(len(s)) + "#" + s)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            lenght = int(s[i:j])

            start = j + 1
            end = start + lenght
            output.append(s[start:end])

            i = end
        return output