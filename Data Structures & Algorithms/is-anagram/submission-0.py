class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False

        s_map = {}
        t_map = {}

        for c in range(len(s)):
            i = s[c]
            j= t[c]
            if(s_map.get(i)):
                s_map[i]+=1
            else:
                s_map[i]=1

            if(t_map.get(j)):
                t_map[j]+=1
            else:
                t_map[j]=1

        return (s_map==t_map)
        