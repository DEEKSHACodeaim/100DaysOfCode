'''
Reverse Words in a String III
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s_rev=''
        l=s.split(' ')

        for i in l:
            leng=len(i)
            k=''
            for j in range(leng-1,-1,-1):
                k+=i[j]

            if s_rev=="":
                s_rev+=k
            else:
                s_rev+=" "
                s_rev+=k
        return s_rev

        '''
        ----easier method----

        for i in l:
            s_rev+=i[::-1] #add space accordingly
        '''
