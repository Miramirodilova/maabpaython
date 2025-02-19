import array
for name in array.__dict__:
    print(name) 

class person:
    def items(self,body):
        return self.person([],sorted(body))
    def items2 (self,organism,body):
        if body:
            return self.items2(organism,body[1:]) + self.items2(organism + [body][0],body[1:])
        return [organism]
for name in person.__dict__:
        print(name)

class Animal:
    def __init__(self,cat,dog,bird):
        self.cat = cat
        self.dog = dog
        self.bird = bird
    def __str__(self):
        return f"Animal(cat {self.cat}, dog {self.dog}, bird {self.bird})"
anima= Animal('mukush','rex','tommy')
print(anima)   
import builtins
help(builtins.abs)
print(builtins.abs (-115))


def student(student_id,student_name,student_grade):
    return f'student_id {student_id},student_name {student_name},student_grade {student_grade}'
print(student('123','mohira','67'))


def student_data(student_id, **kwargs):
    print(f'student_id {student_id}')
    
    if 'student_name' in kwargs:  
        print(f'student_name {kwargs["student_name"]}')
    
    if 'student_name' in kwargs and 'student_class' in kwargs:
        print(f"\nStudent Name: {kwargs['student_name']}")
        print(f"Student Class: {kwargs['student_class']}")

student_data(student_id='SV12', student_name='Jean Garner', student_class='V')

class Student:
    pass
print(Student.__dict__.keys())
print(type(student))
print(student.__module__)

class studentt:
    pass
class student_Mark:
    pass
student1 = studentt
student_Markiing = student_Mark
print(isinstance(student1, Student))
print(isinstance(student_Markiing, Student))
print(isinstance(student_Markiing, student_Mark)) 
print(isinstance(student1, student_Mark))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(student_Mark, object)) 

class student:
    student_name = 'Tom Hanks'
    student_grade = 99

print(f'student name: {getattr(student, "student_name")}')
print(f'student mark: {getattr(student, "student_grade")}')

class student:
    student_id = 45
    student_name = 'Melina'
    def dispaly():
        print(f'student_id: {student.student_id} student_name {student.student_name}')
student.dispaly()        


class Student:
    school = 'Forward Thinking'
    address = '2626/Z Overlook Drive, COLUMBUS' 
student1 = Student()
student2 = Student() 
student1.student_id = "V12"
student1.student_name = "Ernesto Mendez"
student2.student_id = "V12"
student2.marks_language = 85
student2.marks_science = 93
student2.marks_math = 95 
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')


