class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None 

    def display(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  
            return
        last = self.head
        while last.next:
            last = last.next 
        last.next = new_node  

    def delete(self, data):
        if self.head is None:
            print("The linked list is empty. Nothing to delete.")
            return

        if self.head.data == data:
            self.head = self.head.next 
            print(f"Node with value {data} deleted.")
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next 
                print(f"Node with value {data} deleted.")
                return
            current = current.next
        
        print(f"Node with value {data} not found.")

def user_input():
    linked_list = LinkedList()
    
    while True:
        print("\nLinked List Operations:")
        print("1. Insert a node")
        print("2. Delete a node")
        print("3. Display the linked list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            data = int(input("Enter the value to insert: "))
            linked_list.insert(data)
        
        elif choice == '2':
            data = int(input("Enter the value to delete: "))
            linked_list.delete(data)
        
        elif choice == '3':
            linked_list.display()
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter 1-4.")

user_input()
