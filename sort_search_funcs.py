def selection_sort(obj_list):
    for i in range(len(obj_list)-1, 0, -1):
        position_of_max = 0
        for location in range(1, i + 1):
            if obj_list[location].compare(obj_list[position_of_max]) > 0:
                position_of_max = location

        temp = obj_list[i]
        obj_list[i] = obj_list[position_of_max]
        obj_list[position_of_max] = temp


def insertion_sort(obj_list):
    for index in range(1, len(obj_list)):
        current_value = obj_list[index]
        position = index

        while position > 0 and obj_list[position - 1].compare(current_value) > 0:
            obj_list[position] = obj_list[position - 1]
            position = position - 1

        obj_list[position] = current_value


def merge_sort(obj_list):
    if len(obj_list) > 1:
        mid = len(obj_list) // 2
        lefthalf = obj_list[:mid]
        righthalf = obj_list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i].compare(righthalf[j]) < 0:
                obj_list[k] = lefthalf[i]
                i = i + 1
            else:
                obj_list[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            obj_list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            obj_list[k] = righthalf[j]
            j = j + 1
            k = k + 1


def quick_sort(obj_list):
    q_sort(obj_list, 0, len(obj_list) - 1)


def q_sort(obj_list, left, right):
    if left >= right:
        return
    if right - left == 1:
        if obj_list[left].compare(obj_list[right]) > 0:
            temp = obj_list[left]
            obj_list[left] = obj_list[right]
            obj_list[right] = temp
            return
    pivot = partition(obj_list, left, right)
    q_sort(obj_list, left, pivot - 1)
    q_sort(obj_list, pivot + 1, right)


def partition(obj_list, left, right):
    pivot = left + (right - left) // 2
    temp = obj_list[left]
    obj_list[left] = obj_list[pivot]
    obj_list[pivot] = temp

    pivot = left
    left = left + 1

    while right >= left:
        while left <= right and obj_list[left].compare(obj_list[pivot]) <= 0:
            left = left + 1
        while left <= right and obj_list[right].compare(obj_list[pivot]) > 0:
            right = right - 1
        if left <= right:
            temp = obj_list[left]
            obj_list[left] = obj_list[right]
            obj_list[right] = temp

            left = left + 1
            right = right - 1
        else:
            break
    temp = obj_list[right]
    obj_list[right] = obj_list[pivot]
    obj_list[pivot] = temp

    return right


def heapify(obj_heap, size, root):
    largest = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    if left < size and obj_heap[left].compare(obj_heap[root]) > 0:
        largest = left
    if right < size and obj_heap[right].compare(obj_heap[largest]) > 0:
        largest = right
    if largest != root:
        obj_heap[root], obj_heap[largest] = obj_heap[largest], obj_heap[root]
        heapify(obj_heap, size, largest)


def heap_sort(obj_list):
    size = len(obj_list)

    # Build a maxheap.
    for i in range(size, -1, -1):
        heapify(obj_list, size, i)

    # Remove elements from the heap
    for i in range(size - 1, 0, -1):
        obj_list[i], obj_list[0] = obj_list[0], obj_list[i]  # Swap
        heapify(obj_list, i, 0)
