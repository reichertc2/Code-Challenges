# loop through the s string



class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_a = False
        letter_b = False
        letter_hold_ = ''
        bool_list_s = []
        bool_list_t = []
        for idx,letter in enumerate(s):
            print(letter)
            if idx == 0:
                letter_hold = letter
                print(letter_hold)
            if letter_hold == letter:
                letter_hold = letter
                letter_a = False
                bool_list_s.append(letter_a)
            else:
                letter_a = True
                letter_hold = letter
                bool_list_s.append(letter_a)

        for idx,letter in enumerate(t):
            print(letter)
            if idx == 0:
                letter_hold = letter
                print(letter_hold)
            if letter_hold == letter:
                letter_hold = letter
                letter_a = False
                bool_list_t.append(letter_a)
            else:
                letter_a = True
                letter_hold = letter

                bool_list_t.append(letter_a)
        print("bool_list at end ", bool_list_s)
        print("bool_list at end ", bool_list_t)

        for idx,item in enumerate(bool_list_s):
            print(item)
            print((bool_list_t[idx]))
            if item != bool_list_t[idx]:
                return False

        return True
        # if bool_list_s == bool_list_t:
        #     return True
        # else:
        #     return False
            # if letter_a !=0 and letter_a == letter:
            #     print('in if ',letter)
            #     letter_a 
            # print('not in if ', letter)

        


sol = Solution()
s = 'foo'
t = 'bar'
print(sol.isIsomorphic(s, t))