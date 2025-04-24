class Queue:
    def __init__(self):
        self.queue = [] 

    def enqueue(self, element):
        self.queue.append(element)
        print(f"Enqueued: {element}")

    def dequeue(self):
        if len(self.queue) > 0:
            removed_element = self.queue.pop(0) 
            print(f"Dequeued: {removed_element}")
        else:
            print("Queue is empty. Cannot dequeue.")

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue elements:", " -> ".join(map(str, self.queue)))

def user_input():
    queue = Queue() 

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue an element")
        print("2. Dequeue an element")
        print("3. Display the queue")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            element = input("Enter the element to enqueue: ")
            queue.enqueue(element)
        
        elif choice == '2':
            queue.dequeue()
        
        elif choice == '3':
            queue.display()
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter 1-4.")

user_input()
