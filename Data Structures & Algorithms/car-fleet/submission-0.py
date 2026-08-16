class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        car_tuple = [(-position[i], speed[i]) for i in range(n)]
        car_tuple.sort()
        for t in car_tuple:
            time = (target + t[0])/t[1]
            if not (stack and stack[-1] >= time):
                stack.append(time)
        return len(stack)
