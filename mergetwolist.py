def mergeSortedList(head1,head2):
    temp1= head1
    temp2 = head2
    temp3 = None
    head3 = None

    while temp1 is not None and temp2 is not None:
        if temp1.data < temp2.data:
            selected_node = temp1
            temp1 = temp1.next
        else:
            selected_node = temp2
            temp2 = temp2.next

        if head3 is None:
            head3 = selected_node
            temp3 = head3
        else:
            temp3.next = selected_node
            temp3 = temp3.next

    if temp1 is not None:
        temp3.next = temp1
    if temp2 is not None:
        temp3.next = temp2
    return head3