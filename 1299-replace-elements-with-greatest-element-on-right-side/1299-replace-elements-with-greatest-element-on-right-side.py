class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last = -1
        for i in range(0,len(arr)-1):
            arr[i] = max(arr[i+1::])
        arr[-1] = -1
        return(arr)