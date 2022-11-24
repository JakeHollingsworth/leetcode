'''
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.
'''
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, dest = (start, destination) if start < destination else (destination, start)
        forward = sum(distance[start:dest])
        reverse = sum(distance) - forward
        return min(forward, reverse)
