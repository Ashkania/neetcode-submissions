class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # O(n^2), O(1)
        ans = []
        for i in range(len(arr)-1):
            ans.append(max(arr[i+1:]))
        ans.append(-1)
        
        return ans

        # O(n), O(n)