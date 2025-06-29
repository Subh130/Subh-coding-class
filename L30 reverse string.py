class reverse_string():
    def __init__(self, input):
        self.input_value = input

    def reverse(self):
        return self.input_value[::-1]
    
input = input("Enter a string: ")
reverser = reverse_string(input)
reverse_str = reverser.reverse()
print("reversed string:", reverse_str)