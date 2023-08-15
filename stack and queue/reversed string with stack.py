class Stack:
    def __init__(self):
        self.items = []


    def is_empty(self):
        return len(self.items) == 0

    def push(self,data):
        self.items.append(data)
        return self.items 

    

    def pop(self):
        return self.items.pop()
def string_reverses(input_string):
    temp_stack  = Stack()
    for i in input_string:
        temp_stack.push(i)
    reversed_string = ""
    while  not temp_stack.is_empty():
        reversed_string += temp_stack.pop()

    return reversed_string                 


input_string = "hello"
result = string_reverses(input_string)
print(result)