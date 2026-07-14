class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}
        if (len(s) == len(t)) and (len(set(s)) == len(set(t))):
            for i,val in enumerate(s):
                if val in s_dic:
                    s_dic[val] +=1
                else:
                    s_dic[val] = 1
            
            for i,val  in enumerate(t):
                if val in t_dic:
                    t_dic[val] += 1
                else:
                    t_dic[val] = 1
            if s_dic == t_dic:
                return True
        return False

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) !=len(t)):
            return False 
       
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
              
        return True     