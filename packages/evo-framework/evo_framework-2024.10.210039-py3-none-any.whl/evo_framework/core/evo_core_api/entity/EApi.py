#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

from evo_framework.core.evo_core_api.entity.EApiInput import EApiInput
from evo_framework.core.evo_core_api.entity.EApiOutput import EApiOutput
#========================================================================================================================================
"""EApi

	EApi outlines the API configuration details such as description, input, output, and required fields.
	
"""
class EApi(EObject):

	VERSION:int = 8184583589049623658

	def __init__(self):
		super().__init__()
		self.Version:int = self.VERSION
	
		self.description:str = None
		self.input:EApiInput = None
		self.output:EApiOutput = None
		self.required:str = None
#<
		#INTERNAL
		self.context = {}
		self.callback = None
		self.isEnabled:bool = True
#>
  
	def toStream(self, stream):
		super().toStream(stream)
		
		self._doWriteStr(self.description, stream)
		self._doWriteEObject(self.input, stream)
		self._doWriteEObject(self.output, stream)
		self._doWriteStr(self.required, stream)
		
	def fromStream(self, stream):
		super().fromStream(stream)
		
		self.description = self._doReadStr(stream)
		self.input = self._doReadEObject(EApiInput, stream)
		self.output = self._doReadEObject(EApiOutput, stream)
		self.required = self._doReadStr(stream)
	
	def __str__(self) -> str:
		strReturn = "\n".join([
				super().__str__(),
							
				f"\tdescription:{self.description}",
				f"\tinput:{self.input}",
				f"\toutput:{self.output}",
				f"\trequired:{self.required}",
							]) 
		return strReturn
	