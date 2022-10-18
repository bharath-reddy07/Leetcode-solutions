class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        length=len(indices)
        list1=list(s)
        for i in range(0,length):
            index_value=indices.index(i)
            if index_value!=i:
                temp=list1[i]
                list1[i]=list1[index_value]
                list1[index_value]=temp
                temp=indices[i]
                indices[i]=indices[index_value]
                indices[index_value]=temp
            print(list1)
        str1=""
        ans=str1.join(list1)
        return(ans)