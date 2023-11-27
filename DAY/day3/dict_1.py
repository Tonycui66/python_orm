from collections import UserDict
from collections import abc


def _upper(x):
	try:
		return x.upper()
	except KeyError:
		return x

class DictSub(dict):
	def __missing__(self, key):
		return self[_upper(key)]


class UserDictSub(UserDict):
	def __missing__(self, key):
		return self[_upper(key)]


class SimpleMappingSub(abc.Mapping):
	pass