class Solution:
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            total_w=0
            used_day=1
            for w in weights:
                total_w+=w
                if total_w > capacity:
                    total_w= w
                    used_day+=1
            return used_day <= days


        l_capa= max(weights)
        r_capa= sum(weights)
        
        while l_capa < r_capa:
            curr_capa=(l_capa+r_capa)//2
            if can_ship(curr_capa):
                r_capa=curr_capa
            else:
                l_capa=curr_capa+1
        return l_capa
                

        
