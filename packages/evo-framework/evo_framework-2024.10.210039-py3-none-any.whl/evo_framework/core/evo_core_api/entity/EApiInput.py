#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

#========================================================================================================================================
"""EApiInput

	EApi input
	
"""
class EApiInput(EObject):

	VERSION:int = 5502653192630919475

	def __init__(self):
		super().__init__()
		self.Version:int = self.VERSION
		
		self.eObjectClass:str = None
		self.eClassID:int = 0
  
	def toStream(self, stream):
		super().toStream(stream)
		
		self._doWriteStr(self.eObjectClass, stream)
		self._doWriteLong(self.eClassID, stream)
		
	def fromStream(self, stream):
		super().fromStream(stream)
		
		self.eObjectClass = self._doReadStr(stream)
		self.eClassID = self._doReadLong(stream)
	
	def __str__(self) -> str:
		strReturn = "\n".join([
				super().__str__(),
							
				f"\teObjectClass:{self.eObjectClass}",
				f"\teClassID:{self.eClassID}",
							]) 
		return strReturn
	