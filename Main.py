class Node:
  """
  Class implementing node of the LinkedList
  Attributes:
    -> data - data held by the node
    -> next - link to the next node
  """
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  """
  Class implementing Queue as a LinkedList
  """
  def __init__(self):
    """
    Initialises Queue object with pointers head and tail set to None
    """
    self.head = None
    self.tail = None

  def enqueue(self, data) -> None:
    """
    Adds node containing data passed to the rear of the queue
    """
    new = Node(data)
    if not self.tail is None:
      self.tail.next = new
    if self.head is None:
      self.head = new
    self.tail = new

  def dequeue(self) -> None:
    """
    Removes node from the rear of the queue
    """
