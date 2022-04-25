class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''
        longest = max(strs,key=len)
        if len(strs)==1:
                return(strs[0])
        elif len(set(strs)) == 1:
            return(strs[0])
        else:
            for i in range(1,len(longest)):
                list_i = [j[0:i] for j in strs]
                print(set(list_i))
                if len(set(list_i))==1:
                    common = strs[1][0:i]
                    print(longest[0:i])
        return(common)