#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git |
#========================================================================================================================================
from evo_framework.core import *
from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap
from evo_framework.core.evo_core_convert.utility.IuConvert import IuConvert
from evo_framework.core.evo_core_log.utility.IuLog import IuLog
from evo_framework.core.evo_core_key.utility.IuKey import IuKey
from evo_framework.core.evo_core_api.control.CApiFlow import CApiFlow
from evo_framework.core.evo_core_api.entity.EApi import EApi
from evo_framework.core.evo_core_api.entity.EnumApiType import EnumApiType
from evo_framework.core.evo_core_api.entity.EApiInput import EApiInput
from evo_framework.core.evo_core_api.entity.EApiOutput import EApiOutput

# ------------------------------------------------------------------------------------------------
# CActionApi
# ------------------------------------------------------------------------------------------------
class CApi():

# ------------------------------------------------------------------------------------------------
    def __init__(self):
            super().__init__()
            self.mapEApi = EvoMap()
            self.mapEApiMap = EvoMap()
            self.current_path = os.path.dirname(os.path.abspath(__file__))
            
            
# ------------------------------------------------------------------------------------------------          
    @abstractmethod
    def doAddApi(self):
        pass
# ------------------------------------------------------------------------------------------------
    async def doAction(self, eAction):
        try:
            IuLog.doVerbose(__name__, f"doAction: {eAction}")
            
            await CApiFlow.getInstance().doActionCallBack(eAction)
            
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
# ------------------------------------------------------------------------------------------------
    
    def newApi(self, id:str, callback, input:Type, output:Type, isEnabled=True, description:str="") -> EApi:
        try: 
            eApi = EApi()
            eApi.id = IuKey.generateId(id)

            eApi.callback = callback
            eApi.description = description
            eApi.isEnabled = isEnabled
            
            if hasattr(input, "VERSION"): #and len(input.VERSION) == 64:
                eApi.input =  EApiInput() 
                eApi.input.id = IuKey.generateId(f"{id}|{input.__module__}|{input.VERSION}")
                eApi.input.eObjectClass = input.__module__
                eApi.input.eClassID = input.VERSION
 
            else:
                raise Exception(f"ERROR_NOT_VALID_INPUT_ECLASS|{input.__module__}")
            
            if hasattr(output, "VERSION"): #and len(output.VERSION) == 64:
                eApi.output =  EApiOutput() 
                eApi.output.id = IuKey.generateId(f"{id}|{output.__module__}|{output.VERSION}")
                eApi.output.eObjectClass = output.__module__
                eApi.output.eClassID = output.VERSION
                 
            else:
                raise Exception(f"ERROR_NOT_VALID_OUTPUT_ECLASS|{output.__module__}")
            
            if eApi.isEnabled:
                self.mapEApi.doSet(eApi)
                self.doSetEApi(eApi)
            
            return eApi     
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise exception

# ---------------------------------------------------------------------------------------------------------------------------------------
    def doSetEApi(self, eApi: EApi):
        try:
            CApiFlow.getInstance().eApiConfig.mapEApi.doSet(eApi)
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
