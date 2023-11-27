import dataclasses

@dataclasses.dataclass
class Car:
	wheels: int

	def __repr__(self):
		return f"repr is {self.wheels}"

	def __str__(self):
		return f"str is {self.wheels}"

c = Car(5)
print(c)

dct = {1: c}
print(dct)