#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

from evo_framework.core.evo_core_api.entity.EObject import EObject
#========================================================================================================================================
"""EApiQueryMap

	EApiQueryMap defines the structure for the result of querying within the EVO framework, including collection, eObjectID ID, and query string.
	
"""
class EApiQueryMap(EObject):

	VERSION:int = 5881762927697717090

	def __init__(self):
		super().__init__()
		self.Version:int = self.VERSION
		
		self.collection:int = 0
		self.mapEObject:EvoMap = EvoMap()
  
	def toStream(self, stream):
		super().toStream(stream)
		
		self._doWriteLong(self.collection, stream)
		self._doWriteMap(self.mapEObject, stream)
		
	def fromStream(self, stream):
		super().fromStream(stream)
		
		self.collection = self._doReadLong(stream)
		self.mapEObject = self._doReadMap(EObject, stream)
	
	def __str__(self) -> str:
		strReturn = "\n".join([
				super().__str__(),
							
				f"\tcollection:{self.collection}",
				f"\tmapEObject:{self.mapEObject}",
							]) 
		return strReturn
	