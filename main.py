def linear_search(list, target):
    for i, element in enumerate(list):
        if element == target:
            return i

    return -1


def binary_search(sorted_list, target):
    start, end = 0, len(sorted_list) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_element = sorted_list[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            start = mid + 1
        else:
            end = mid - 1
    return - 1


def bisect_problem(list):
    start, end = 0, len(list) - 1

    while start < end:
        mid = (start + end) // 2
        if is_failure(list[mid]):
            end = mid
        else:
            start = mid + 1

    return start


def is_failure(entry):
    return entry.startswith("F")


students_list = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry"]
target = "Emma"
print("Linear search: " + str(linear_search(students_list, target)))

print("Binary search: " + str(binary_search(sorted(students_list), target)))

print("Bisect problem: " + str(bisect_problem(students_list)))