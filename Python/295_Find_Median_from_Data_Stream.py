class MedianFinder:

    def __init__(self):
        self.numbers=[]

    def addNum(self, num: int) -> None:
        l,r=0,len(self.numbers)
        
        while l<r:
            mid = (l+r)//2
            if self.numbers[mid]<num:
                l=mid+1
            else:
                r=mid
        self.numbers.insert(l,num)


    def findMedian(self) -> float:
        if len(self.numbers)==0:
            return 0
             
        if len(self.numbers)%2==0:
            return (self.numbers[(len(self.numbers)//2)-1]+self.numbers[len(self.numbers)//2])/2.0
        else:
            return self.numbers[len(self.numbers)//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()