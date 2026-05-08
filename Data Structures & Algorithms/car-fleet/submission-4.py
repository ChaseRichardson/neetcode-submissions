class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # list sorted by how close pos is to end (pos, speed)
        pair_list = []
        ret = 0

        for i in range(len(position)):
            pair_list.append((position[i], speed[i]))

        # sort list descending (pos, speed)
        pair_list.sort(key=lambda x: (-x[0]))

        fleet_num_ticks = 0
        for item in pair_list:

            # number of ticks for car i to finish
            pos = item[0]
            speed = item[1]
            local_num_ticks = (target - pos) / speed

            # # quick check for exact landing
            # if local_num_ticks * speed + pos != target:

            # won't catch up to fleet ahead -- make new one
            if fleet_num_ticks < local_num_ticks:
                ret += 1
                fleet_num_ticks = local_num_ticks


        return ret


            


