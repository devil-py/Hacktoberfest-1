def merge(intervals):

        intervals.sort(key=lambda x: x[0])

        m = []
        for i in intervals:
            if not m or m[-1][1] < i[0]:
                m.append(i)
            else:
                m[-1][1] = max(m[-1][1], i[1])

        return m
        
intervals=[[7,7],[2,3],[6,11],[1,2]]
print(merge(intervals))
