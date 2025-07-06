class RomanConverter:
    def __init__(self):
        # Define mapping of Roman numerals
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
    
    def converter(self, num):
        result = ""
        for value, symbol in self.value_map:
            while num >= value:
                result += symbol
                num -= value
        return result
            
num = RomanConverter()
int = int(input("enter any number: "))
roman = num.converter(int)
print(f"{int} in roman numerical is {roman}")