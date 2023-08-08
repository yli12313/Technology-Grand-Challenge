class Solution(object):
  def gcdOfStrings(self, str1, str2):
    # Approach 1:

    # Properties:
    # 1) 't divides s' => 's = t + ... + t'

    # Rules of Modulo:
    # 1) smaller number % bigger number => smaller number
    # 2) bigger number % smaller number => smaller number | bigger number when you look at division => (bigger number)/(smaller number)
    # 3) any number % 0 => (any number)/(0) => ZeroDivisionError

    # Algorithm:
    # 1) Define the gcd function that returns the length of the gcd.
    # 2) Invoke the gcd function.
    # 3) Check if str1 == str2.
    # 4) Check if str1[:common_length] == str2[:common_length].
    # 5) If so, return the answer. 
    # 6) Return "" by default. 

    def gcd(a, b):
      while b:
          a, b = b, a%b
      return a
    
    len1 = len(str1)
    len2 = len(str2)
    gcd_length = gcd(len1, len2)
    
    # Tricky: Given the property that we have, we know that if 
    # str1+str2 == str2+str1 is NOT true, then we can return ""
    # automatically. If the condition is true, then you know both
    # strings have the same t of a specific length where "t divides s". 
    # In the beginning you have no idea if both strings given have a 
    # same t where "t divides s"!
    if str1+str2 == str2+str1:
        if str1[:gcd_length] == str2[:gcd_length]:
            return str1[:gcd_length]
   
    return ""

foo = Solution()
print(foo.gcdOfStrings("ABCABC", "ABC"))