class Solution:
    def countSeniors(self, details: List[str]) -> int:
        pattern = r'\d+[A-Z](\d{2})\d{2}'
        count = 0

        for d in details:
            res = re.search(pattern, d)

            count += 1 if int(res.group(1)) > 60 else 0
        return count