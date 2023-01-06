from typing import Self


class ListNode:
    def __init__(self, prev_node: Self) -> None:
        print(prev_node)
        print("Hi class!")

    def current(self, curr_node: Self):
        print("Hi current")


l = ListNode(ListNode)
# l2 = l.__init__(l)
# print(l2)

l_curr = ListNode(ListNode)
l_curr.current(l)
# print(l_curr)

