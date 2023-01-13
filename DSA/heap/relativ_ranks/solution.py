class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medalDict = {}
        scoreCopy = [-s for s in score]
        heapq.heapify(scoreCopy)
        
        index  = 0
        while len(scoreCopy) > 0:
            val = heapq.heappop(scoreCopy)
            medalDict[val] = index
            index += 1
        
        result = []

        for i in range(len(score)):
            match medalDict[-score[i]]:
                case 0:
                    result.append('Gold Medal')
                case 1:
                    result.append('Silver Medal')
                case 2:
                    result.append('Bronze Medal')
                case _:
                    result.append(str(medalDict[-score[i]]+1))
        return result
