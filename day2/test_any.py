from typing import TypeVar,Generic,Union,Dict,List,Optional


T = TypeVar('T')

class Box(Generic[T]):
	def __init__(self,content : T):
		self.content = content

	def get(self)->T:
		return self.content


class Student:
	def __init__(self,name:str,age: int,major: Optional[str]=None):
		self.name = name
		self.age = age
		self.major = major


StudentData = Union[Student,Dict[str,Union[str,int]]]

def add_major(student:StudentData,major:str)->None:
	student.major = major


def display(student_data:StudentData)->None:
	if isinstance(student_data,Student):
		print(f"Student:{student_data.name},Age:{student_data.age},Major:{student_data.major}")
	elif isinstance(student_data,dict):
		print(f"Student:{student_data['name']},Age:{student_data['age']},Major:{student_data.get('major')}")


student1=Student("Alice",18)
student2={"name":"Bob","age":18}
box1= Box(student1)
box2= Box(student2)

if type(box1.get()) is Student:
	add_major(box1.get(),"Computer Science")

display(box1.get())
display(box2.get())


num : List[int] =[1,2,3,4]
print(num)