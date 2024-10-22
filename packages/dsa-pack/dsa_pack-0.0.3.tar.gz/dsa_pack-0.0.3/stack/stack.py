from typing import List, Any, Optional, TypeVar, Generic

from .exceptions import StackEmptyError

T = TypeVar('T')

class Stack(Generic[T]):
    """
    Generic stack implementation.
    """

    def __init__(self) -> None:
        """
        Initialize an empty stack.
        """
        self._stack: List[T] = []

    def push(self, item: T) -> None:
        """
        Push an element into stack
        """
        self._stack.append(item)

    def pop(self) -> T:

        """
        Remove and return the top element from the stack. 
        Raises StackEmptyError if the stack is empty.
        """

        if self.is_empty():
            raise StackEmptyError("Cannot pop from empty stack.")
        
        return self._stack.pop()
    
    def peek(self) -> T:

        """
        Return the top element of the stack without removing it. 
        Raises StackEmptyError if the stack is empty.
        """

        if self.is_empty():
            raise StackEmptyError("Cannot peek from empty stack.")
        
        return self._stack[-1]

    def is_empty(self) -> bool:

        """
        Check if the stack is empty.
        """

        return len(self.stack) == 0
    
    def size(self) -> int:

        """
        Return the number of elements in the stack.
        """
        
        return len(self.stack)