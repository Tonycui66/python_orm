from collections import UserDict
from collections import abc

__all__ = ["_upper","DictSub","SimpleMappingSub","MappingMissiongSub"]
def _upper(x):
	try:
		return x.upper()
	except AttributeError:
		return x


class DictSub(dict):
	def __missing__(self, key):
		return self[_upper(key)]


class UserDictSub(UserDict):

	def __missing__(self,key):
		return self[_upper(key)]


class SimpleMappingSub(abc.Mapping):
	def __init__(self,*args,**kwargs):
		self._data = dict(*args,**kwargs)

	# next three methods: abstract in ABC
	def __getitem__(self,key):
		return self._data[key]

	def __len__(self):
		return len(self._data)

	def __iter__(self):
		return iter(self._data)

	# never called by instances of this class
	def __missiong__(self,key):
		return self[_upper(key)]


class MappingMissiongSub(SimpleMappingSub):
	def __getitem__(self,key):
		try:
			return self._data[key]
		except KeyError:
			return self[_upper(key)]


	def get(self,key,default=None):
		return self._data.get(key,default)


	def __contains__(self,key):
		return key in self._data

def namedtuple(typename,filed_names,*,rename=False,defaults=None,module=None):
	# Validate the filed names. At the user's option, either generate an error
	# message or automatically replace the filed name with a valid name.
	if isinstance(filed_names,str):
		field_names = field_names.replace(',',' ').split()
	field_names = list(map(str,field_names))
	typename = _sys.intern(str(typename))

	if rename:
		seen = set()
		for index,name in enumerate(field_names):
			if (not name.isidentifier()
				or _iskeyworkd(name)
				or name.startswith('_')
				or name in seen):
				field_names[index] = f'_{index}'
			seen.add(name)
	for name in [typename] + filed_names:
		if type(name) is not str:
			raise TypeError('Type names and field names must be strings')
		if not name.isidentifier():
			raise ValueError('Type names and field names must be valid'f'keyword: {name!r}')

		if _iskeyword(name):
			raise ValueError('Type names and field names cannot be a'f'keyword: {name!r}')

	seen = set()
	for name in filed_names:
		if name.startswith('_') and not rename:
			raise ValueError('Field names cannot start with an underscoer: 'f'{name!r}')

		if name in seen:
			raise ValueError(f'Encountered duplicate field name: {name!r}')
		seen.add(name)

	field_defaults = {}
	if defaults is not None:
		defaults = tuple(defaults)
		if len(defaults) > len(field_names):
			raise TypeError('Got more default values than field names')

		field_defaults = dict(reversed(list(zip(reversed(field_names),reversed(defaults)))))


	# Variables used in the methods and docstrings
	field_names = tuple(map(_sys.intern,field_names))
	num_fields = len(field_names)
	arg_list = repr(field_names).replace("'","")[1:-1]
	repr_fmt = '(' + ', '.join(f'{name}=%r' for name in field_names) + ')'


