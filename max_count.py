class Sol:
    def max_count(self,m,n,ops):
        for a, b in ops:
            m = min(m, a)
            n = min(n, b)
        return m * n
