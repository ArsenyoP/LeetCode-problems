class Solution(object):
    def isAnagram(self, s, t):

        s_count = {}
        t_count = {}

        if len(s) != len(t):
            return False

        for i in s:
            s_count[i] = s_count.get(i, 0) + 1

        for i in t:
            t_count[i] = t_count.get(i, 0) + 1

        return s_count == t_count


