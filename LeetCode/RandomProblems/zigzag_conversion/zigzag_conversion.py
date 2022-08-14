class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        not_complete = True
        string_ = ""
        temp = ''

        while not_complete:
            for idx, letter in enumerate(s):
                if idx % (numRows + 1) == 0:
                    print("modulus numRows +1 ", letter)
                    string_ = string_ + letter

                else: 
                    string_ = string_ + letter
                    


            if len(s) == len(string_):
                not_complete = False
                
                    

        return string_


sol = Solution()
print(sol.convert("ABCD", 2))