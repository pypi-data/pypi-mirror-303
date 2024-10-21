#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

from evo_framework.core.evo_core_api.entity.EnumEApiQuery import EnumEApiQuery
#========================================================================================================================================
"""EApiQueryResult

	EApiQueryResult defines the structure for result of EApiQuery within the EVO framework, including collection, eObjectID ID, and query string.
	
"""
class EApiQueryResult(EObject):

	VERSION:int = 1200251599260753688

	def __init__(self):
		super().__init__()
		self.Version:int = self.VERSION
		
		self.enumEApiQuery:EnumEApiQuery = EnumEApiQuery.GET
		self.collection:int = 0
		self.data:bytes = None
		self.isError:bool = None
		self.error:str = None
  
	def toStream(self, stream):
		super().toStream(stream)
		
		self._doWriteInt(self.enumEApiQuery.value, stream)
		self._doWriteLong(self.collection, stream)
		self._doWriteBytes(self.data, stream)
		self._doWriteBool(self.isError, stream)
		self._doWriteStr(self.error, stream)
		
	def fromStream(self, stream):
		super().fromStream(stream)
		
		self.enumEApiQuery = EnumEApiQuery(self._doReadInt(stream))
		self.collection = self._doReadLong(stream)
		self.data = self._doReadBytes(stream)
		self.isError = self._doReadBool(stream)
		self.error = self._doReadStr(stream)
	
	def __str__(self) -> str:
		strReturn = "\n".join([
				super().__str__(),
							
				f"\tenumEApiQuery:{self.enumEApiQuery}",
				f"\tcollection:{self.collection}",
				f"\tdata length:{len(self.data) if self.data else 'None'}",
				f"\tisError:{self.isError}",
				f"\terror:{self.error}",
							]) 
		return strReturn
	