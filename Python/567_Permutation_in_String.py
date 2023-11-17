class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        len_s1, len_s2 = len(s1), len(s2)
        count_s1={}
        for i in s1:
            count_s1[i]=count_s1.get(i,0) +1 

        count_window = {}
        print(count_s1, count_window)
        for i in range(len_s2):
            count_window[s2[i]] = 1+ count_window.get(s2[i],0)

            if i >= len_s1:
                if count_window[s2[i - len_s1]] == 1:
                    count_window.pop(s2[i - len_s1])
                else:
                    count_window[s2[i - len_s1]] -= 1

            if count_window == count_s1:
                return True

        return False   