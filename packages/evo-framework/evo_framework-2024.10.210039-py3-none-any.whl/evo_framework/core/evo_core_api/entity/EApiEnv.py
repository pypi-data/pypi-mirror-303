#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

#========================================================================================================================================
"""EApiEnv

	
	
"""
class EApiEnv(EObject):

	VERSION:int = 261489491703560897

	def __init__(self):
		super().__init__()
		self.Version:int = self.VERSION

		
		self.data:bytes = None
  
	def toStream(self, stream):
		super().toStream(stream)
		
		self._doWriteBytes(self.data, stream)
		
	def fromStream(self, stream):
		super().fromStream(stream)
		
		self.data = self._doReadBytes(stream)
	
	def __str__(self) -> str:
		strReturn = "\n".join([
				super().__str__(),
							
				f"\tdata length:{len(self.data) if self.data else 'None'}",
							]) 
		return strReturn
	