# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_list = ''

        return sum_list

        # linked lists are reversed 
        # TODO need to revese list

        # lists need to be attached in reverse order
        # TODO re-reverse list

    def reverse_list(self, list_1):
        pass

        # lists need to be added together
        # TODO need to add together 
    def add_list_values(self, list_1, list_2):
        pass

    def build_node_list(self, num_list):
        
        for idx, num in enumerate(num_list):
            if idx == 0:
                node = ListNode(num)
            else:
                node.next = num
                ListNode(num)

            # node = ListNode(num)
            
            
        return node


num_list = [1, 5]

sol = Solution()
node = sol.build_node_list(num_list)
print(node.val)
print(node.next)
