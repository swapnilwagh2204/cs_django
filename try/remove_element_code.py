class Solution:
    # @param A : list of integers
    # @return an integer
    def pf_even_sum(self,ls, start, end):
        even_sum = [None]*len(ls)
        even_sum[0] =ls[0]
        for i in range(1, len(ls)):
            if(i % 2 == 0):
                even_sum[i] = even_sum[i-1]+ls[i]
            else:
                even_sum[i] = even_sum[i-1]

        return even_sum[end]-even_sum[start-1]


    def pf_odd_sum(self,ls, start, end):
        odd_sum = [None]*len(ls)
        odd_sum[0] = 0
        for i in range(1, len(ls)):
            if(i % 2 == 1):
                odd_sum[i] = odd_sum[i-1]+ls[i]
            else:
                odd_sum[i] = odd_sum[i-1]
        return odd_sum[end]-odd_sum[start-1]

    def solve(self, ls):
        count = 0
        for i in range(len(ls)):
            rm_nu=ls.pop(i)
            n = len(ls)
            total_even_sum =Solution().pf_even_sum(ls, 0, i-1)+Solution().pf_even_sum(ls, i+1, n-1)
            total_odd_sum = Solution().pf_odd_sum(ls, 0, i-1)+Solution().pf_odd_sum(ls, i+1, n-1)
            
            if total_even_sum == total_odd_sum:
                count += 1
            ls[i]= rm_nu
        return count




