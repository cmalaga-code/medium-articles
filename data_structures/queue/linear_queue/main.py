from queue import Queue

def main():
    q = Queue()
    print("___Enqueue___")
    q.enqueue("My First Node")
    q.enqueue("My Second Node")
    q.enqueue("My Third Node")
    q.enqueue("My Fourth Node")
    print("___Count Queue Objects___")
    print(f"I have {q.node_count} nodes in queue")
    print("___Dequeue___")
    print(f"I deleted this node from the queue: {q.dequeue().data}")
    print("___Count Queue Objects___")
    print(f"I have {q.node_count} nodes in queue")
    print("___Dequeue___")
    print(f"I deleted this node from the queue: {q.dequeue().data}")
    print("___Count Queue Objects___")
    print(f"I have {q.node_count} nodes in queue")
    print("___Peek___")
    q.peek()

if __name__ == "__main__":
    main()
