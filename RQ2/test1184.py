def test_n_equal_to_2():
    result = distanceBetweenBusStops([1, 2], 0, 1)
    expected_result = 1
    assert result == expected_result, f"Expected {expected_result}, got {result}"


# Partition 2: n > 2
def test_n_greater_than_2():
    result = distanceBetweenBusStops([1, 2, 3, 4, 5], 2, 4)
    expected_result = 7
    assert result == expected_result, f"Expected {expected_result}, got {result}"

# Partition 3: start = destination
def test_start_equal_to_destination():
    result = distanceBetweenBusStops([1, 2, 3, 4], 1, 1)
    expected_result = 0
    assert result == expected_result, f"Expected {expected_result}, got {result}

# Partition 4: start != destination
def test_start_not_equal_to_destination():
    result = distanceBetweenBusStops([1, 2, 3,4], 0, 3)
    expected_result = 4
    assert result == expected_result, f"Expected {expected_result}, got {result}"


# Partition 5: Clockwise direction is shorter
def test_clockwise_direction_shorter():
    result = distanceBetweenBusStops([1, 2, 3, 4], 1, 3)
    expected_result = 5
    assert result == expected_result, f"Expected {expected_result}, got {result}"

# Partition 6: Counterclockwise direction is shorter
def test_counterclockwise_direction_shorter():
    result = distanceBetweenBusStops([1, 2, 3], 2, 0)
    expected_result = 3
    assert result == expected_result, f"Expected {expected_result}, got {result}"