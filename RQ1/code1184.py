class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        if start == destination:
            return 0
        elif start > destination:
            start, destination = destination, start

        clockwise_distance = sum(distance[start:destination])
        counterclockwise_distance = sum(distance) - clockwise_distance
        return min(clockwise_distance, counterclockwise_distance)