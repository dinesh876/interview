class Solution:
    def fillCups(self, amount: List[int]) -> int:
        seconds = 0
        amount = [-s for s in amount]
        heapq.heapify(amount)
        while amount != [0,0,0]:
            firstCup = abs(heapq.heappop(amount)) - 1
            secondCup =  abs(heapq.heappop(amount)) - 1
            if firstCup <= 0: firstCup = 0
            if secondCup <= 0: secondCup = 0
            heapq.heappush(amount,-firstCup)
            heapq.heappush(amount,-secondCup)
            seconds += 1
        return seconds
