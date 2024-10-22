#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git |
#========================================================================================================================================

import base64
import json
import os

from evo_framework.core.evo_core_setting.entity.ESetting import ESetting
from evo_framework.core.evo_core_log.utility.IuLog import IuLog
from evo_framework.core.evo_core_system.utility.IuSystem import IuSystem
from evo_framework.core.evo_core_setting.utility.IuSettings import IuSettings
from evo_framework.core.evo_core_text.utility.IuText import IuText
from urllib.parse import unquote
import sys
current_path = os.path.dirname(os.path.abspath(__file__))
#----------------------------------------------------------------------------------------------------------------------------------------
class CSetting:
    __instance = None
#----------------------------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getInstance():
        """ Static access method. """
        if CSetting.__instance == None:
            cObject = CSetting()
            cObject.doInit()
        return CSetting.__instance
#----------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        if CSetting.__instance != None:
            raise Exception("ERROR_SINGLETON")
        else:
            CSetting.__instance = self
            self.mapSetting = {}
#----------------------------------------------------------------------------------------------------------------------------------------            
    def doInit(self):
        try:
            self.eSettings = ESetting()
            try:
               self.eSettings.path_output =  IuSystem.do_sanitize_path( f"{current_path}/../../../../assets/")
            except Exception as exception:
                IuLog.doException(__name__,exception)
            
            secretEnv =os.environ.get('CYBORGAI_SECRET')
            
            if IuText.StringEmpty(secretEnv):
                IuLog.doError(__name__, "ERROR_REQUIRED_ENV|CYBORGAI_SECRET")
                sys.exit(1)
            
            settingsEnv =os.environ.get('CYBORGAI_SETTINGS')
            
            if IuText.StringEmpty(settingsEnv):
                IuLog.doError(__name__, "ERROR_REQUIRED_ENV|CYBORGAI_SETTINGS")
                sys.exit(1)
            
            
            mapSettingsTmp =  IuSettings.doDecryptSettings(settingsEnv)
            
            if mapSettingsTmp is None:
                IuLog.doError(__name__, "ERROR_DECRYPT_SETTINGS_ENV|CYBORGAI_SETTINGS")
                sys.exit(1)

            self.mapSetting = mapSettingsTmp
            
            passwordEnv=self.doGet('CYBORGAI_PASSWORD')
            
            if IuText.StringEmpty(passwordEnv):
                IuLog.doError(__name__, "ERROR_REQUIRED_ENV|CYBORGAI_PASSWORD")
                sys.exit(1)
            
            if len(passwordEnv) <16:
                IuLog.doError(__name__, "ERROR_REQUIRED_ENV|CYBORGAI_PASSWORD_LENGTH < 16")
                sys.exit(1)

            self.mapSetting = mapSettingsTmp
                
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
#---------------------------------------------------------------------------------------------------------------------------------------- 
    def doGet(self, key:str, isStripQuota=True):
        try:
            value = self.mapSetting.get(key)
            
            if value is not None:
                IuLog.doVerbose(__name__,f"{key} => {value}")
                return value
            
            value = os.environ.get(key)

            if value is not None:             
                if isStripQuota:
                    valueTmp=str(value)
                    if valueTmp.startswith('"'):
                        value = valueTmp.strip('"') 
                    if valueTmp.startswith("'"):
                        value = valueTmp.strip("'") 
                        
                self.mapSetting[key] = value
        
            return value
           
        except Exception as exception:
            IuLog.doError(__name__,f"{exception}")
            return None
#----------------------------------------------------------------------------------------------------------------------------------------       