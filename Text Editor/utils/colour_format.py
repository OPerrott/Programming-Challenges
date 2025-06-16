class Colour_Format:
    def __init__(self, value):
        self.FORMAT_ERROR = "[ERROR] \"{self.value}\" is not a valid colour format!\nSuggestion: (???, ???, ???) || #??????"
        
        self.value = value
        self.normalised = self.correct_format()
             
    def correct_format(self):
        if isinstance(self.value, tuple):
            return self.rgb_to_hex()
        elif isinstance(self.value, str) and self.is_hex():
            return self.value if len(self.value) == 7 else print(self.FORMAT_ERROR)
        else:
            print(self.FORMAT_ERROR)

    def is_hex(self):
        if not isinstance(self.value, str):
            return False

        v = self.value
        if v.startswith('#'):
            v = v[1:]
        
        # Check if string is non-empty and all hex digits
        if len(v) == 0:
            return False

        try:
            int(v, 16)
            return True
        except ValueError:
            return False

    def rgb_to_hex(self):
        
        invalid = None
        
        # Check if self.value is a tuple with 3 ints
        if (not isinstance(self.value, tuple) or len(self.value) != 3 or not all(isinstance(c, int) for c in self.value) or not all(0 <= c <= 255 for c in self.value)):
            invalid = True
            
        if invalid:
            print(self.FORMAT_ERROR)
        else:
            return "#%02x%02x%02x" % self.value

    def __str__(self):
        return self.normalised if self.normalised is not None else ""

    def __repr__(self):
        return f"Colour_Format({repr(self.value)}) -> {repr(self.normalised)}"

if __name__ == '__main__':
    print(Colour_Format('#FFFFFF'))