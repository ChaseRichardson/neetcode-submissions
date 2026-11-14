class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        ret = 0
        currFleetFinishTime = 0


        cars = sorted(zip(position, speed), reverse=True)
        for car in cars:
            pos, sp = car

            finishTime = ((target - pos) / sp)

            # adding another fleet
            if currFleetFinishTime < finishTime:
                currFleetFinishTime = finishTime
                ret += 1

            
        return ret

            




            

        