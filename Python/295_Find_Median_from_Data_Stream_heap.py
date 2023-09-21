class MedianFinder
    def __init__(self)
        self.leftheap=[]
        self.rightheap=[]
    
    def addNum(self,numint)- None
        if self.rightheap and num self.rightheap[0] 
            heapq.heappush(self.rightheap,num)
        else
            heapq.heappush(self.leftheap,-1num)
        
        if len(self.leftheap)  len(self.rightheap)+1
            heapq.heappush(self.rightheap,-1heapq.heappop(self.leftheap))
        if len(self.rightheap)  len(self.leftheap)+1
            heapq.heappush(self.leftheap,-1heapq.heappop(self.rightheap))
        

    def findMedian(self)- float
        if len(self.leftheap)len(self.rightheap)
            return -1 self.leftheap[0]
        elif len(self.leftheap)len(self.rightheap)
            return self.rightheap[0]
        else
            return ((-1self.leftheap[0])+self.rightheap[0])2


