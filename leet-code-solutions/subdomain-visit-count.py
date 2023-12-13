class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # {google.mail.com
        #  mail.com
        #  com
        #  yahoo.com
        #  intel.mail.com
        #  wiki.org
        #  org
        # }
        table=defaultdict(int)
        for cp in cpdomains:
            domain=cp.split()
            domain[0]=int(domain[0])
            for i in range(len(domain[1])-1,-1,-1):
                if domain[1][i]==".":
                    table[domain[1][i+1:]]+=domain[0]
            table[domain[1]]+=domain[0]
        ans = []
        for string in table:
            ans.append(str(table[string]) + " " + string)
        return ans
            