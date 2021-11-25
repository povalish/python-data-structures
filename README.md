# Python Data Structures

This repository was created for storing 
Data Structures (that learned and explored).

All classes and interfaces created for production-ready uses.


## Table of content

- [Stack](#stack)
- [Queue](#queue)

_______________________________


### Stack

Stack is a linear data structure. It follows the 
LIFO principle which is the last-in and first-out rule.

A real-life example is a stack of plates: you can only 
take a plate from the top of the stack, and you can 
only add a plate to the top of the stack.


##### Properties

- len


##### Methods

- push(e) -- putting an element into a stack
- pop() -- remove an element from a stack and returned removed element
- top() -- just get last element
- is_empty() -- if Stack is empty
- is_full() -- if Stack is full (when using fixed size)


##### Complexity (array based)

| Operation | Running Time  |
| --------- | ------------- |
| push(e)   | O(1)*         |
| pop()     | O(1)*         |
| top()     | O(1)          |
| isEmpty() | O(1)          |
| isFull()  | O(1)          |

*amortized

_______________________________


### Queue

Queue is a linear data structure. It follows the FIFO
principle which is the first-in and last-out.

Main differences between Queue and Stack:
1. In a Stack removing the last item
2. In a Queue removing the very FIRST item

We usually say that elements enter a queue at the 
back and are removed from the front. A metaphor for 
this terminology is a line of people waiting to get ticket.


##### Methods

- push(e) -- putting an element into a queue (at the end)
- pop() -- removing element from a queue (from the start)
- first() -- just get first element in a queue
- is_empty() -- if Queue is empty
- is_full() -- if Queue is full


##### Complexity (array based)

| Operation     | Running Time  |
| ------------- | ------------- |
| push(e)       | O(1)*         |
| pop()         | O(1)*         |
| first()       | O(1)          |
| is_empty()    | O(1)          |
| is_full()     | O(1)          |

*amortized