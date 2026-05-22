class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # # O(n^2), O(1)
        # ans = []
        # for i in range(len(arr)-1):
        #     ans.append(max(arr[i+1:]))
        # ans.append(-1)

        # return ans

        # O(n), O(1)
        n = len(arr)
        ans = n*[0]
        current_max = -1

        for i in range(n-1,-1,-1):
            ans[i] = current_max
            current_max = max(current_max, arr[i])

        return ans

