class Solution(object):
    def reverseString(self, s):
        left_pointer, right_pointer = 0, len(s) - 1

        while right_pointer > left_pointer:
            s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
            left_pointer += 1
            right_pointer -= 1
        return s
