def code234(head):
    # Initialize an empty list to store values from the linked list
    values = []
    
    # Traverse the linked list and store values in the list
    current = head
    while current:
        values.append(current.val)
        current = current.next

    # Check if the list of values is equal to its reverse
    return values == values[::-1]
