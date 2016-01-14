# beat 99.12% of python submissions.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0 : return False
        elif str(x)==str(x)[::-1] : return True
        return False
        

# beat 70.63% of python submissions.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0 : return False
        elif str(x)==str(x)[::-1] : return True
        else : return False

#beat 54.92% of python submissions.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0 : return False
        if str(x)==str(x)[::-1] : return True
        else : return False

# So, the first is the fastest. 

        
