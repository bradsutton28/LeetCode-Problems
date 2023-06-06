from heapq import *

"""
LeetCode Problem # 2336 Smallest Number in Infinite Set
https://docs.python.org/3/library/heapq.html reference to heapq documentation
You have a set which contains all positive integers
Implement the SmallestInfiniteSet class:
SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

Test Input: ["SmallestInfiniteSet","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest"]
[[],[2],[],[],[],[1],[],[],[]]
"""


class SmallestInfiniteSet:
    # Init with currentNum = 1 since it's all positive ints 1+
    # Init a blank list [] for min heap and call heapify to transform populated list into a heap
    def __init__(self):
        self.currentNum = 1
        self.minHeap = []
        self.infSet = set()
        heapify(self.minHeap)

    # while heap not empty, heappop finds smallest item from heap and pops
    def popSmallest(self) -> int:
        if self.minHeap:
            smallestValue = heappop(self.minHeap)
            self.infSet.remove(smallestValue)
            return smallestValue
        else:
            smallestValue = self.currentNum
            self.currentNum += 1
            return smallestValue

    # num passed in < currentNum AND cannot already be in the inf set per req.
    # then we heappush which pushes the num onto the heap
    def addBack(self, num: int) -> None:
        if num < self.currentNum and num not in self.infSet:
            self.infSet.add(num)
            heappush(self.minHeap, num)

