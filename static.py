class Static:
    @staticmethod
    def static_islower_text(text):
        if text.islower():
            return text.upper()
        return text
    
    @staticmethod
    def static_isupper_text(text):
        if text.isupper():
            return text.lower()
        return text
    
    @staticmethod
    def static_remove_numbers_text(text):
        return ''.join(char for char in text if not char.isdigit())
    
    @staticmethod
    def static_remove_numbers_sorted_text(text):
        letters = [char for char in text if char.isalpha()]
        return ''.join(sorted(letters))

static_class = Static()

print(static_class.static_islower_text("hello"))  
print(static_class.static_isupper_text("HELLO"))   
print(static_class.static_remove_numbers_text("123hello456world789")) 
print(static_class.static_remove_numbers_sorted_text("321cba456")) 
print(static_class.static_remove_numbers_sorted_text("z5a4x3c2v1"))  

