"""The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251": Then the output should be "23321511"
Because there are 2 3's, 3 2's, 1 5 and 1 1.

Given a positive integer n, return the nth term of the count-and-say sequence.

 

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"  """


class Solution:
    def countAndSay(self, n: int) -> str:
        i=2
        ans="1"
        if n==1:
            return("1")
        else:
            while i<=n:
                ans=Solution.say(ans)
                i+=1
        return ans
    def say(ans: str)-> str:
        count=-1
        i=0
        prevele=""
        delimiter=""
        newans=[]
        length=len(ans)
        while i<length:
            if count==-1:
                prevele=ans[i]
                count=1
                i+=1
                continue
            if ans[i]==prevele:
                count+=1
                i+=1
                continue
            else:
                newans.append(str(count)+str(prevele))
                count=-1
        newans.append(str(count)+str(prevele))
        return(delimiter.join(newans))