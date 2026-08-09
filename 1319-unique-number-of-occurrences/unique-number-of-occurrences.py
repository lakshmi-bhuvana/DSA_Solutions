class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen={}
        freq=set()

        for num in arr:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        
        for num in seen:
            freq.add(seen[num])

        if len(freq)==len(seen):
            return True
        else: return False
        
