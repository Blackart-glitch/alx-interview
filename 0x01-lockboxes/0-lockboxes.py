def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    visited = set()
    queue = [0]  # Start with the first box (index 0)

    while queue:
        box_index = queue.pop(0)
        visited.add(box_index)

        # Check all the keys in the current box
        for key in boxes[box_index]:
            if key not in visited and 0 <= key < n:
                queue.append(key)

    # If all boxes are visited, we can unlock all of them
    return len(visited) == n
