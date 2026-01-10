
import math
from math import sqrt
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=int(sqrt(x))
        return s
    
print(Solution().mySqrt(16))