#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internationa   https://github.com/cyborg-ai-git | 
#========================================================================================================================================
from evo_framework.core import *
from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_log.utility.IuLog import IuLog
from evo_framework.core.evo_core_api.entity.EApiConfig import EApiConfig
from evo_framework.core.evo_core_api.utility.IuApiRequest import IuApiRequest
from evo_framework.core.evo_core_api.utility.IuApi import IuApi
from evo_framework.core.evo_core_text.utility.IuText import IuText
from evo_framework.core.evo_core_convert.utility.IuConvert import IuConvert
from evo_framework.core.evo_core_api.entity.EAction import EAction
from evo_framework.core.evo_core_api.entity.EApiText import EApiText
from evo_framework.core.evo_core_api.entity.EApiQuery import EApiQuery
import requests
#<

#>
# ---------------------------------------------------------------------------------------------------------------------------------------
# UApiClient
# ---------------------------------------------------------------------------------------------------------------------------------------
"""UApiClient
"""
class UApiClient():
    __instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):   
        if UApiClient.__instance != None:
            raise Exception("ERROR:SINGLETON")
        else:
            super().__init__()
            UApiClient.__instance = self
            self.currentPath = os.path.dirname(os.path.abspath(__file__))
            
            self.__url_server = "https://cyborgai-api.fly.dev/do_action"
            self.__pk_server = "6de6827317e90fcf1e40de7027aa9dace7590e22acd08f23c67d54cb13772aa866a267cc9321bc9f077b92b76d827b9e0a98bc7117ca6af02a523940387b50a7"  # pinning
            
            #self.__url_server = "http://127.0.0.1:8000/do_action"
            #self.__pk_server = "17deceb197fded7ad870d49e4a59ee7c8ecc7e138a5baf48f4ab8d52f0bf4e947e28d9c6787fabac476c2c15e24b55ad1dd888fa90d960cea17de822b85ee878"  # pinning
            
            self.__api_set = "root-set"
            self.__api_get = "root-get"
         
# ---------------------------------------------------------------------------------------------------------------------------------------
    """getInstance Singleton

    Raises:
        Exception:  api exception

    Returns:
        _type_: UApiClient instance
    """
    @staticmethod
    def getInstance():
        if UApiClient.__instance is None:
            uObject = UApiClient()  
            uObject.doInit()  
        return UApiClient.__instance
# ---------------------------------------------------------------------------------------------------------------------------------------
    """doInit

    Raises:
        Exception: api exception

    Returns:

    """   
    def doInit(self):   
        try:
#<
            #INIT ...
            pass
#>   
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doSetPeer(self, eApiConfig:EApiConfig) -> str  :
        try:
            if eApiConfig is None:
                raise Exception("ERROR_REQUIRED|eApiConfig|")

#<        

            IuLog.doVerbose(__name__, f"eApiConfig:{eApiConfig}")
            
            data=eApiConfig.toBytes()
            eActionInput = IuApiRequest.newEActionInput(
                                                id=eApiConfig.id,
                                                publicKey=eApiConfig.publicKey,
                                                secretKey=eApiConfig.secretKey,
                                                data=data
                                                )
            
            eActionInput.action = self.__api_set
            
            
            
            IuLog.doVerbose(__name__, f"eActionInput:{eActionInput}")
            
            dataERequest = eActionInput.toBytes()
           
  
            response = requests.post(self.__url_server, data=dataERequest, headers={'Content-Type': 'application/octet-stream'})

            if response.status_code == 200:
                packed_data = response.content
                  
                pkServer = IuConvert.fromHex(self.__pk_server)
                
                data_length = struct.unpack('<i', packed_data[:4])[0]

                IuLog.doVerbose(__name__, f"data_length:{data_length}")
                unpacked_data = packed_data[4:4+data_length]

                
                eActionOutput = IuApiRequest.fromEActionOutput( data=unpacked_data, publicKey=pkServer)
                
                IuLog.doVerbose(__name__, f"eActionOutput:{eActionOutput}")
                
                eApiText:EApiText = IuApi.toEObject(EApiText(), eActionOutput.output)
                IuLog.doVerbose(__name__, f"eApiText:{eApiText}")
                token = eApiText.text
                return token
            
            else:
                print(response.reason)
                
                raise Exception(
                    f"ERROR_FAILED_REGISTER_PEER_TO_CYBORGAI:{response.status_code}"
                )
#>
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doGetPeer(self, idNode:str, eApiConfig:EApiConfig|Any = None ) ->EApiConfig :
        try:
            if IuText.StringEmpty(idNode):
                raise Exception("ERROR_REQUIRED|idNode|")

#<        
            eApiQuery = EApiQuery()
            eApiQuery.doGenerateID()
            eApiQuery.eObjectID = IuConvert.fromHex(idNode)

            
            data=eApiQuery.toBytes()
            eActionInput = IuApiRequest.newEActionInput(
                                                id=eApiQuery.id,
                                                publicKey=eApiConfig.publicKey,
                                                secretKey=eApiConfig.secretKey,
                                                data=data
                                                )
            
            eActionInput.action = self.__api_get
 
            IuLog.doVerbose(__name__, f"eActionInput:{eActionInput}")
            
            dataERequest = eActionInput.toBytes()
            eHeaderInput = IuApiRequest.newEHeader(id=eActionInput.id, data=dataERequest)
            
            dataHeader = eHeaderInput.toBytes()
  
            response = requests.post(self.__url_server, data=dataHeader, headers={'Content-Type': 'application/octet-stream'})

            if response.status_code == 200:
                dataHeaderOutput = response.content
                eHeaderOutput = IuApiRequest.toEHeader(dataHeaderOutput)
                
                dataEResponse = eHeaderOutput.data
                
                pkServer = IuConvert.fromHex(self.__pk_server)
                
                eActionOutput = IuApiRequest.fromEActionOutput( data=dataEResponse, publicKey=pkServer)
                IuLog.doVerbose(__name__, f"eActionOutput:{eActionOutput}")
                
                eApiConfig:EApiConfig = IuApi.toEObject(EApiConfig(), eActionOutput.output)
                IuLog.doVerbose(__name__, f"eApiConfig:{eApiConfig}")
               
                return eApiConfig
            
            else:
                print(response.reason)
                
                raise Exception(
                    f"ERROR_FAILED_REGISTER_PEER_TO_CYBORGAI:{response.status_code}"
                )
#>
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------

#<
#OTHER METHODS ...
#>
# ---------------------------------------------------------------------------------------------------------------------------------------