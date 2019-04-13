class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        d={}
        d[0]=[""]
        d[1]=["()"]

        for num in range(2,n+1):
            prev=num-1
            k=[]
            for combination in d[prev]:
                for i in range(len(combination)):
                    if(combination[i]=='('):
                        temp=combination[:i+1]
                        for comb in d[1]:
                            temp+=comb+combination[i+1:]
                            k.append(temp)
                            temp=combination[:i+1]

                # final one combination
                for comb in d[1]:
                    k.append(combination+comb)

            d[num]=list(set(k))
            
        return d[n]


# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]