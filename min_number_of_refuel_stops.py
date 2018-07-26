# A car travels from a starting position to a destination which is target miles east of the starting position.
#
# Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.
#
# The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.
#
# When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
#
# What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.
#
# Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.
#
#
#
# Example 1:
#
# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.
# Example 2:
#
# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can't reach the target (or even the first gas station).
# Example 3:
#
# Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation:
# We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
# We made 2 refueling stops along the way, so we return 2.


class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        if not stations:
            return 0 if target <= startFuel else -1
        visited = [[0 for _ in stations] for __ in stations]
        T = [0 for _ in stations]
        T.append(0)
        T[0] = startFuel
        for i in range(1, len(T)):
            T[i] = T[i - 1]
            for station in stations:
                if station[0] <= T[i - 1]:
                    T[i] = max([T[i], T[i - 1] + station[1]])
        for i, x in enumerate(T):
            if x >= target:
                return i
        return -1

    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        if not stations:
            return 0 if target <= startFuel else -1
        visited = [[0 for _ in stations] for __ in stations]
        T = [0 for _ in stations]
        T.append(0)
        T[0] = startFuel
        for i, (dist, capacity) in enumerate(stations):
            for j in range(i, -1, -1):
                if T[j] >= dist:
                    T[j + 1] = max([T[j + 1], T[j] + capacity])
        for i, x in enumerate(T):
            if x >= target:
                return i
        return -1


if __name__ == '__main__':
    sln = Solution()

    target = 100
    startFuel = 10
    stations = [[10,60],[20,30],[30,30],[60,40]]
    print(sln.minRefuelStops(target, startFuel, stations))
    print("should be 2")

    target = 100
    startFuel = 1
    stations = [[10,100]]
    print(sln.minRefuelStops(target, startFuel, stations))
    print("should be -1")

    target = 1
    startFuel = 1
    stations = [[10,100]]
    print(sln.minRefuelStops(target, startFuel, stations))
    print("should be 0")


    target = 100
    startFuel = 50
    stations = [[50,50]]
    print(sln.minRefuelStops(target, startFuel, stations))
    print("should be 1")

    target = 1000
    startFuel = 83
    stations = [[25,27],[36,187],[140,186],[378,6],[492,202],[517,89],[579,234],[673,86],[808,53],[954,49]]
    print(sln.minRefuelStops(target, startFuel, stations))
    print("should be -1")
