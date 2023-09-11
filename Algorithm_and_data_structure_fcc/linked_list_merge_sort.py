from linked_list import linked_list


def merge_sort(linked_list):
    if linked_list.size() <= 1:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linkedlist):
    # if linkedlist == None or linkedlist.head == None:
    #     left_half = linkedlist
    #     right_half = None
    #     return left_half, right_half
    # else:
    #     size = linkedlist.size()
    #     mid = size // 2

    #     mid_node = linkedlist.node_at_index(mid - 1)

    #     left_half = linkedlist
    #     right_half = linked_list()

    #     right_half.head = mid_node.next_node
    #     mid_node.next_node = None

    #     return left_half, right_half

    left = linkedlist
    right = linked_list()

    current = linkedlist.head
    i = 0

    mid = linkedlist.size() // 2
    while current and i < mid - 1:
        current = current.next_node
        i += 1

    right.head = current.next_node
    current.next_node = None

    return left, right


def merge(left, right):
    merged = linked_list()
    merged.add(0)

    current = merged.head
    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            # call the while loop to break
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node

    head = merged.head.next_node
    merged.head = head

    return merged


l = linked_list()

l.add(13)
l.add(26)
l.add(48)
l.add(27)
l.add(3)
l.add(548)
l.add(17)
l.add(7)
l.add(5)
l.add(19)

sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
