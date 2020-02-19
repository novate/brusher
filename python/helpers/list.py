from typing import List
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def string_to_integer_list(input: str) -> List:
    return json.loads(input)


def string_to_list_node(input: str) -> ListNode:
    # Generate list from the input
    numbers = string_to_integer_list(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def list_node_to_string(node: ListNode) -> str:
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def string_to_cycle_list(input: str, pos: int) -> ListNode:
    head = string_to_list_node(input)
    if pos != -1:
        p = head
        for i in range(pos):
            p = p.next
        tail = p
        while tail.next:
            tail = tail.next
        tail.next = p
    return head
