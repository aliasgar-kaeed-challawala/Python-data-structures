class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def ins_mid(self,prev_node,new_data):
        if prev_node is None:
            print("previous node must be in linked list")
            return 0
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head = new_node 
            return 
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=new_node
    def delete_node(self,key):#deletes the node with the given key
        cur_node=self.head
        if(cur_node and cur_node.data==key):#if the given node is head
            self.head=cur_node.next
            cur_node=None
        prev=None#to keep the track of the previous node of the node to be deleted
        while(cur_node and cur_node.data!=key):#traversing the list
            prev=cur_node
            cur_node=cur_node.next
        if cur_node is None:#If  node with given key is not present
            return
        prev.next=cur_node.next
        cur_node=None
    def delete_node_pos(self,pos):#deletes node at a given position
        cur_node=self.head
        if(cur_node and pos==0):
            self.head=cur_node.next
            cur_node=None
        c=1
        prev=None
        while(cur_node and count!=pos):
            prev=cur_node
            cur_node=cur_node.next
            c+=1
        if(cur_node is None):
            return
        prev.next=cur_node.next
        cur_node=None
    def swap_node(self,key_1,key_2):
        if key_1==key_2:
            return
        cur_1=self.head
        cur_2=self.head
        prev_1=None
        prev_2=None
        while(cur_1 and cur_1.data!=key_1):
            prev_1=cur_1
            cur_1=cur_1.next
        while(cur_2 and cur_2.data!=key_2):
            prev_2=cur_2
            cur_2=cur_2.next
        if not cur_1 or not cur_2:
            return
        if prev_1:
            prev_1.next=cur_2
        else:
            self.head=cur_2
        if prev_2:
            prev_2.next=cur_1
        else:
            self.head=cur_1
        cur_1.next,cur_2.next=cur_2.next,cur_1.next
    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name,end=' ')
            print(node.data)
    def reverse_list_iterative(self):#iterative approach to reverse a linked list
        cur=self.head
        prev=None
        while cur:
            nxt=cur.next
            cur.next=prev
            self.print_helper(prev, "PREV")
            self.print_helper(cur, "CUR")
            self.print_helper(nxt, "NXT")
            print("\n")
            prev=cur
            cur=nxt
        self.head=prev
    def reverse_recursive(self):#recursive approach to reverse a linked list

        def _reverse_list_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_list_recursive(cur, prev)

        self.head = _reverse_list_recursive(cur=self.head, prev=None)
    
    #merging two sorted linked lists
    def merge_sorted_list(self, llist):
    
        p = self.head 
        q = llist.head
        s = None
    
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                    s = p 
                    p = s.next
            else:
                s = q
                q = s.next
            new_head = s 
        while p and q:
            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p 
        return new_head
    def remove_duplictes(self):
        cur=self.head
        prev=None
        dup_values=dict()
        while cur:
           
            if cur.data in dup_values:
                #if value is already present, remove the node
                prev.next=cur.next
                cur=None
            else:
                dup_values[cur.data]=1
                prev=cur
            cur=prev.next
    def rotate(self,k):
        p=self.head
        q=self.head
        prev=None
        c=0
        while p and c<k:
            prev=p
            p=p.next
            q=q.next
            c+=1
        p=prev
        while q:
            prev=q
            q=q.next
        q=prev
        q.next=self.head
        self.head=p.next
        p.next=None




    

        

llist_1 = LinkedList()


llist_1.append(1)
llist_1.append(2)
llist_1.append(3)
llist_1.append(4)
llist_1.append(5)
llist_1.append(6)
llist_1.printList()
print()

llist_1.rotate(4)
llist_1.printList()

