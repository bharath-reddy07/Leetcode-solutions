class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        count=0
        i=num-1
        if num==0 or num==2:
            count=1
        while i>=int((num/2)):
            count=0
            a=i
            a=str(a)
            a=a[::-1]
            a=int(a)
            #print(a,i,a+i)
            if (a+i)==num:
                print("yes")
                count=1 
                break
            i-=1
        if count==0:
            print("no")
            ans="no"
            return False
        elif count ==1:
            print("yes")
            ans="yes"
            return True