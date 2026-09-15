class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        # add num in order:
        self.data.append(num)

        

    def findMedian(self) -> float:
        if not self.data:
            return null
        self.data.sort()
        n = len(self.data)
        return (self.data[n //2] if (n & 1) else
                (self.data[n//2] + self.data[n//2 - 1]) / 2)
        

        
        