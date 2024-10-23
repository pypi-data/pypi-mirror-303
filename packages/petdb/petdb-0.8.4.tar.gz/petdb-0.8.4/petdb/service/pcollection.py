
from __future__ import annotations

import uuid
from copy import deepcopy
from typing import Optional, Iterator, Callable, Iterable, Sized

from petdb.pcollection import PetArray
from petdb.pexceptions import QueryException
from petdb.putils import PetUtils
from petdb.service.api import API

class PetServiceMutationsChain:

	def __init__(self, name: str, api: API, mutations: list[dict] = None):
		self.name = name
		self._api = api
		self.__mutations = mutations or []
		self._mutated_data = None

	def filter(self, query: dict) -> PetServiceMutationsChain:
		return self.__mutate("filter", [query])

	def sort(self, query: str | int | Iterable[str | int] = None, reverse: bool = False) -> PetServiceMutationsChain:
		return self.__mutate("sort", [query, reverse])

	def pick(self, *queries: str | int) -> PetServiceMutationsChain:
		return self.__mutate("pick", queries)

	def omit(self, *queries: str | int) -> PetServiceMutationsChain:
		return self.__mutate("omit", queries)

	def unique(self, query: str | int = None) -> PetServiceMutationsChain:
		return self.__mutate("unique", [query])

	def groupby(self, key: str | int | Iterable[str | int] = None) -> PetServiceMutationsChain:
		return self.__mutate("groupby", [key])

	def find(self, query: dict | Callable[[dict], bool]) -> Optional[dict]:
		"""
		Returns the first element that satisfies the provided ``query``. If no values satisfy, ``None`` is returned.

		:param query: A query object that to match against
		:returns: The first matched element or ``None``
		"""
		for doc in self._data:
			if PetUtils.match(doc, query):
				return doc
		return None

	def findall(self, query: dict | Callable[[dict], bool]) -> list[dict]:
		"""
		Returns all elements that satisfy the provided ``query``. If no values satisfy, the empty list is returned.

		:param query: A query object that selects which documents to include in the result set
		:returns: List of matched documents
		"""
		return [doc for doc in self._data if PetUtils.match(doc, query)]

	def join(self, delimiter: str, adapter: Callable[[dict], str] = None) -> str:
		"""
		Compose all elements into the single string with the given ``delimiter``.

		:param delimiter: Separator used to join elements.
		:param adapter: Function to convert each element to string.
		:return: The concatenated string.
		"""
		if adapter is None:
			adapter = lambda item: str(item)
		return delimiter.join(adapter(item) for item in self._data)

	def array(self) -> PetArray[dict]:
		"""
		Returns all documents stored in the collection as a :py:class:`PetArray`

		:returns: :py:class:`PetArray` with containing documents.
		"""
		return PetArray(deepcopy(self._data))

	def map[TP](self, func: Callable[[dict], TP]) -> PetArray[TP]:
		"""Perform map mutation. Accepts only callable object."""
		return PetArray([func(deepcopy(doc)) for doc in self._data])

	def reduce[TP](self, reducer: Callable[[TP, dict], TP], init: TP = None) -> TP:
		"""
		Executes the given "reducer" callback function on each element of the array,
		passing in the return value from the calculation on the preceding element.
		The final result of running the reducer across all elements of the array is a single value.

		:param reducer: A function to execute for each element in the array
			with the next signature: ``reducer(accumulator: TP, item: T) -> TP``.
			Its return value becomes the value of the ``accumulator`` parameter
			on the next invocation of reducer. For the last invocation,
			the return value becomes the return value of reduce(). The function is called
			with the following arguments:
		:param init: A value to which ``accumulator`` is initialized the first time the callback is called.
			If ``init`` is specified, ``reducer`` starts executing with the first value in the array as ``item``.
			If ``init`` is not specified, ``accumulator`` is initialized to the first value in the array, and
			``reducer`` starts executing with the second value in the array as currentValue. In this case,
			if the array is empty (so that there's no first value to return as ``accumulator``), a ``None`` is returned.
		:return: The value that results from running the ``reducer`` callback to completion over the entire array.
		"""
		result = init if init is not None else self._data[0] if self.size() > 0 else None
		for item in self._data[0 if init is not None else 1:]:
			result = reducer(result, item)
		return result

	def foreach(self, func: Callable[[dict], None]) -> None:
		"""
		Go through all elements and call the given function with each.

		:param func: function that takes each element in the array
		"""
		for element in self._data:
			func(element)

	def contains(self, query: dict | Callable[[dict], bool]) -> bool:
		"""
		Check whether the collection contains a document matching a query.

		:param query: the query object
		"""
		for doc in self._data:
			if PetUtils.exists(doc, query):
				return True
		return False

	def exists(self, query: dict | Callable[[dict], bool]) -> bool:
		"""Alias for :py:meth:`PetDaemonMutationsChain.contains`"""
		return self.contains(query)

	def size(self, query: dict | Callable[[dict], bool] = None) -> int:
		"""Returns the amount of all documents in the collection"""
		if query is None:
			return len(self._data)
		amount = 0
		for doc in self._data:
			if PetUtils.match(doc, query):
				amount += 1
		return amount

	def length(self, query: dict | Callable[[dict], bool] = None) -> int:
		"""Returns the amount of all documents in the collection"""
		return self.size(query)

	def list(self) -> list[dict]:
		"""
		Returns all documents stored in the collection as a list

		:returns: a list with all documents.
		"""
		return self._data[:]

	@property
	def _data(self) -> list[dict]:
		return self._apply_mutations()

	def _apply_mutations(self) -> list[dict]:
		if self._mutated_data is None:
			self._mutated_data = self._api.mutate(self.name, self.__mutations)
		return self._mutated_data

	def __mutate(self, mutation: str, args: Iterable) -> PetServiceMutationsChain:
		mutations = deepcopy(self.__mutations)
		mutations.append({"type": mutation, "args": args})
		return PetServiceMutationsChain(self.name, self._api, mutations)

	def __len__(self):
		return self.size()

	def __iter__(self) -> Iterator[dict]:
		return iter(self._data)

	def __getitem__(self, item: int) -> dict:
		return self._data[item]

	def __repr__(self):
		return f"<{self.__class__.__name__} name={self.name}>"

class PetServiceCollection(PetServiceMutationsChain):

	def __init__(self, name: str, api: API):
		super().__init__(name, api)

	def insert(self, doc: dict) -> dict:
		"""
		Insert a new document into the collection.

		:param doc: the document to insert
		:returns: inserted document
		"""
		if not isinstance(doc, dict):
			raise TypeError("Document must be of type dict")
		if "_id" in doc and self.get(doc["_id"]):
			raise QueryException("Duplicate id")
		doc = deepcopy(doc)
		if "_id" not in doc:
			doc["_id"] = str(uuid.uuid4())
		self._api.insert(self.name, doc)
		return doc

	def insert_many(self, docs: Iterable[dict] & Sized) -> list[dict]:
		"""
		Insert multiple documents into the collection.

		:param docs: an Iterable of documents to insert
		:returns: a list containing the inserted documents
		"""
		new_docs = []
		for doc in docs:
			if not isinstance(doc, dict):
				raise TypeError("Document must be of type dict")
			if "_id" in doc and self.get(doc["_id"]):
				raise QueryException("Duplicate id")
			doc = deepcopy(doc)
			if "_id" not in doc:
				doc["_id"] = str(uuid.uuid4())
			new_docs.append(doc)
		self._api.insert_many(self.name, new_docs)
		return new_docs

	def update_one(self, update: dict, query: str | dict = None) -> None:
		if isinstance(query, str):
			query = {"_id": query}
		elif not isinstance(query, dict):
			raise QueryException("Invalid query type: query should be dict or str")
		self._api.update_one(self.name, update, query)

	def update(self, update: dict, query: dict | list[str | dict] = None) -> None:
		if isinstance(query, list):
			if all(isinstance(item, str) for item in query):
				query = {"_id": {"$in": query}}
			elif all(isinstance(item, dict) for item in query):
				query = {"$or": query}
			else:
				raise QueryException("Invalid query format: query list should contains only ids or only docs")
		if query is not None and not isinstance(query, dict):
			raise QueryException("Invalid query type: query should be dict or list")
		self._api.update(self.name, update, query)

	def remove(self, query: str | dict | list[str | dict] | PetServiceMutationsChain) -> list[dict]:
		if isinstance(query, str):
			query = {"_id": query}
		if isinstance(query, PetServiceMutationsChain):
			query = query.list()
		if isinstance(query, list):
			if all(isinstance(item, str) for item in query):
				query = {"_id": {"$in": query}}
			elif all(isinstance(item, dict) for item in query):
				query = {"$or": query}
			else:
				raise QueryException("Invalid delete query: it can only be a list of IDs or a list of docs")
		return self._api.remove(self.name, query)

	def clear(self):
		self._api.clear(self.name)

	def get(self, id: str) -> Optional[dict]:
		"""
		Search for the document with the given ``id``.

		:param id: document's id to search
		:returns: the document with the given ``id`` or ``None``
		"""
		return self.find({"_id": id})

	def _apply_mutations(self) -> list:
		self._mutated_data = None
		return super()._apply_mutations()
