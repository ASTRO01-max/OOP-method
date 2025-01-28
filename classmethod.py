class Pupil:
    school_name = "299"
    school_address = "Unknown"
    total_students = 0
    max_students = 500
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pupil.total_students += 1

    @classmethod
    def change_school(cls, name):
        cls.school_name = name

    @classmethod
    def update_address(cls, address):
        cls.school_address = address

    @classmethod
    def check_capacity(cls):
        return cls.total_students < cls.max_students

    @classmethod
    def increase_capacity(cls, amount):
        cls.max_students += amount
        return cls.max_students

    @classmethod
    def reset_school_info(cls):
        cls.school_name = "Unknown"
        cls.school_address = "Unknown"
        cls.total_students = 0
        cls.max_students = 500
        print("School info reset to default.")

    def __del__(self):
        Pupil.total_students -= 1
        print(f"{self.name} deleted. Remaining students: {Pupil.total_students}")

Zoir = Pupil("Zoir", 16)
Shuhrat = Pupil("Shuhrat", 16)

Pupil.change_school("PDP School")
print("New school name:", Zoir.school_name)

Pupil.update_address("Tashkent City")
print("New school address:", Pupil.school_address)

print("Has capacity:", Pupil.check_capacity())

Pupil.increase_capacity(100)
print("New maximum capacity:", Pupil.max_students)

Pupil.reset_school_info()
print("School name after reset:", Pupil.school_name)
print("Total students after reset:", Pupil.total_students)