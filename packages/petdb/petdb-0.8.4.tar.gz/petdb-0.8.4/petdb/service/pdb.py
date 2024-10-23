
from petdb.service.api import API, DEFAULT_PORT
from petdb.service.pcollection import PetServiceCollection

class PetServiceDB:

	def __init__(self, name: str, password: str, port: int = DEFAULT_PORT):
		self.__api = API(name, password, port or DEFAULT_PORT)

	def collection(self, name: str) -> PetServiceCollection:
		return PetServiceCollection(name, self.__api)

	def collections(self) -> list[str]:
		return self.__api.collections()

	def drop(self):
		self.__api.drop_db()

	def drop_collection(self, name: str):
		self.__api.drop_collection(name)

	@staticmethod
	def enable_debug_mode(enable: bool = True):
		API.enable_debug_mode(enable)
