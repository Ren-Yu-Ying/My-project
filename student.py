class Member:
    def __init__(self, new_gender, new_major, new_id):
        self.__gender = new_gender
        self.major = new_major
        self.id = new_id

    def get_gender(self):
        """回傳private屬性"""
        return self.__gender
    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender == 'F':
            self.__gender = new_gender
        else:
            print('====請輸入"M"或"F"====')

    def borrow_resources(self):
        print('someone borrow')



class Student(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def get_gender(self):
        """回傳private屬性"""
        return self.__gender
    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender == 'F':
            self.__gender = new_gender
        else:
            print('====請輸入"M"或"F"====')

    def join_class(self):
        pass
    def quit_class(self):
        pass
    def borrow_resources(self):
        print('student borrow')


class Professor(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)
    def borrow_resources(self):
        print('professor borrow')
student1 = Student('M', '工管系', 'M10821027')
student2 = Student('F', '經濟系', 'M10821023')
professor1=Professor("M", '資工系', 'T11234')
professor2=Professor('F', '財稅系', 'T22567')

ls = [student1, student2, professor1, professor2]

for item in ls:
    item.borrow_resources()



