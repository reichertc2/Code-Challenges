# Challenge Summary 10
Stack and Queue

## Specifications
- Read all of these instructions carefully.
- Name things exactly as described.
- Do all your work in a your data-structures-and-algorithms public repository.
- Create a new branch in your repo named as noted below.
- Follow the language-specific instructions for the challenge type listed below.
- Update the “Table of Contents” - in the README at the root of the repository - with a link to this challenge’s README file.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![TBD](../wireframes/code-ch-10.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The approach I took was to write the code first with an idea of getting to the end point.


## Solution
<!-- Show how to run your code, and examples of it in action -->
```
class PseudoQueue:

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def dequeue(self,node = None):
        while not self.stack_in.is_empty():
            self.stack_out.push(self.stack_in.pop())
        if self.stack_out.is_empty():
            raise Exception
        return self.stack_out.pop()

    def enqueue(self,value):
        while not self.stack_out.is_empty:
            self.stack_in.push(self.stack_out.pop())
        self.stack_in.push(value)
```
