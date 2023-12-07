from typing import List

def code(trips: List[List[int]], capacity: int) -> bool:
    # Initialize an array to record the number of passengers at each station
    passengers_at_stations = [0] * 1001  # Assuming station indices are between 0 and 1000

    # Record the number of passengers at each station for each trip
    for trip in trips:
        passengers_at_stations[trip[1]] += trip[0]  # on-board
        passengers_at_stations[trip[2]] -= trip[0]  # drop-off

    # Calculate the cumulative sum to track the total number of passengers on board
    current_passengers = 0
    for passengers_at_station in passengers_at_stations:
        current_passengers += passengers_at_station
        if current_passengers > capacity:
            return False

    return True
