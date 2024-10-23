import os

from petdb.pcollection import PetCollection

class PetDB:
	"""
	The main class of PetDB.

	The ``PetDB`` class is responsible for storing and managing this database's collections.

	Collection access is provided by forwarding all unknown method calls
	and property access operations to the :py:meth:`PetDB.collection` method
	by implementing :py:meth:`PetDB.__getattr__` and :py:meth:`PetDB.__getitem__`.

	:param root: The root path where the folder for storing will be created
	"""

	__instances = {}

	@classmethod
	def get(cls, root: str = None):
		if root not in cls.__instances:
			PetDB(root)
		return cls.__instances[root]

	def __init__(self, root: str = None):
		if root in self.__class__.__instances:
			raise Exception("This class is a singleton. Please use PetDB.get() instead.")
		self.__class__.__instances[root] = self
		if root is None:
			root = os.getcwd()
		if not os.path.exists(root):
			raise Exception("Root directory does not exist")
		self.__root = os.path.join(root, "petstorage")
		if not os.path.exists(self.__root):
			os.mkdir(self.__root)

	def __getpath(self, name: str):
		return os.path.join(self.__root, f"{name}.json")

	def collection(self, name: str) -> PetCollection:
		"""
		Get access to the specific collection with the given name.

		If the collection hasn't been accessed yet, a new collection instance will be
		created. Otherwise, the previously created collection instance will be returned.

		:param name: The name of the collection.
		:return: :py:class:`PetCollection`
		"""
		return PetCollection.get_instance(self.__getpath(name))

	def collections(self) -> list[str]:
		"""
		Get the names of all collections in the database.

		:returns: a list of collections names
		"""
		return [os.path.basename(path).rsplit(".", 1)[0] for path in PetCollection.instances().keys()]

	def drop_collection(self, name: str):
		"""
		Deletes the collection with the given name

		:param name: The name of the collection to delete
		"""
		if self.__getpath(name) in PetCollection.instances():
			col = PetCollection.get_instance(self.__getpath(name))
			col.clear()
			os.remove(self.__getpath(name))
			PetCollection.instances().pop(self.__getpath(name))

	def drop(self) -> None:
		"""
		Drop all collections from the database. **CANNOT BE REVERSED!**
		"""
		for col in self:
			col.clear()
			os.remove(self.__getpath(col.name))
		PetCollection.instances().clear()

	def reload(self):
		PetCollection.instances().clear()

	def __getattr__(self, name: str) -> PetCollection:
		"""
		Alias for :py:meth:`PetDB.collection`

		:return: :py:class:`PetCollection`
		"""
		return self.collection(name)

	def __getitem__(self, name: str) -> PetCollection:
		"""
		Alias for :py:meth:`PetDB.collection`

		:return: :py:class:`PetCollection`
		"""
		if not isinstance(name, str):
			raise TypeError("Name must be a string")
		return self.collection(name)

	def __len__(self):
		return len(PetCollection.instances())
