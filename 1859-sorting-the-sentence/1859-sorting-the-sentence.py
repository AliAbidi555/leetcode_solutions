class Solution:
    def sortSentence(self, s: str) -> str:
        index,sentence = [],[]
        ans = []
        s_list = s.split()
        for i in s_list:
            index.append(i[-1])
            sentence.append(i[:-1])
        ans = [x for _,x in sorted(zip(index,sentence))]
        return ' '.join(ans)