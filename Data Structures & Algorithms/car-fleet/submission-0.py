class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleets = 0
        stack = []
        cars = []

        for i in range(len(position)):
            car = (position[i], speed[i])
            cars.append(car)

        cars.sort(reverse=True)
        for car in cars:
            time = (target - car[0]) / car[1]
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
            






        