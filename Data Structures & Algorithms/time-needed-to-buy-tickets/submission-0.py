class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        tempo_totale = 0
        
        for i in range(len(tickets)):
            if i <= k:
                tempo_totale += min(tickets[i], tickets[k])
            else:
                tempo_totale += min(tickets[i], tickets[k] - 1)
                
        return tempo_totale