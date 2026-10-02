class Student:
    def __init__(self, s_id, name, dob):
        self.__id = s_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob
    def get_gpa(self): return self.__gpa
    def set_gpa(self, gpa): self.__gpa = gpa


class Course:
    def __init__(self, c_id, name, credits):
        self.__id = c_id
        self.__name = name
        self.__credits = credits

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_credits(self): return self.__credits