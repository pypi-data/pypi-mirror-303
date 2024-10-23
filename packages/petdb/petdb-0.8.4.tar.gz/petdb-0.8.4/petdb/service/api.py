
import requests
from petdb import PetDB, PetArray
from petdb import __version__

DEFAULT_PORT = 3944

class API:

	debug_mode: bool = False
	localdb: PetDB | None = None

	def __init__(self, dbname: str, password: str, port: int):
		self.dbname = dbname
		self.password = password
		self.port = port

	def drop_db(self):
		if self.debug_mode:
			return self.localdb.drop()
		return self.__request("/drop")

	def drop_collection(self, name: str):
		if self.debug_mode:
			return self.localdb.drop_collection(name)
		return self.__request(f"/drop/{name}")

	def collections(self) -> list[str]:
		if self.debug_mode:
			return self.localdb.collections()
		return self.__request("/collections")

	def mutate(self, name: str, mutations: list[dict]):
		if self.debug_mode:
			array = self.localdb.collection(name)
			for mutation in mutations:
				array: PetArray = array.__getattribute__(mutation["type"])(*mutation["args"])
			return array.list()
		return self.__request(f"/mutate/{name}", {"mutations": mutations})

	def insert(self, name: str, doc: dict):
		if self.debug_mode:
			return self.localdb.collection(name).insert(doc)
		return self.__request(f"/insert/{name}", {"doc": doc})

	def insert_many(self, name: str, docs: list[dict]):
		if self.debug_mode:
			return self.localdb.collection(name).insert_many(docs)
		return self.__request(f"/insert_many/{name}", {"docs": docs})

	def update_one(self, name: str, update: dict, query: dict):
		if self.debug_mode:
			return self.localdb.collection(name).update_one(update, query)
		return self.__request(f"/update_one/{name}", {"update": update, "query": query})

	def update(self, name: str, update: dict, query: dict):
		if self.debug_mode:
			return self.localdb.collection(name).update(update, query)
		return self.__request(f"/update/{name}", {"update": update, "query": query})

	def remove(self, name: str, query: dict):
		if self.debug_mode:
			return self.localdb.collection(name).remove(query)
		return self.__request(f"/remove/{name}", {"query": query})

	def clear(self, name: str):
		if self.debug_mode:
			return self.localdb.collection(name).clear()
		return self.__request(f"/clear/{name}")

	@classmethod
	def enable_debug_mode(cls, enable: bool = True):
		cls.debug_mode = enable
		cls.localdb = PetDB.get()

	def __request(self, endpoint: str, body: dict = None):
		if self.debug_mode:
			return None
		if body is None:
			body = {}
		body["password"] = self.password
		body["dbname"] = self.dbname
		body["version"] = __version__
		response = requests.post(f"http://127.0.0.1:{self.port}{endpoint}", json=body)
		if response is not None and response.headers.get("content-type") == "application/json":
			return response.json()
