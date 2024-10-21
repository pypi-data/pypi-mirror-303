#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git |
#========================================================================================================================================
import os
import aiofiles
import asyncio
class IuFile:
    @staticmethod
    def doCreateDirs(path:str):
        if not os.path.exists(path):
            os.makedirs(path)
            
    @staticmethod
    async def doWrite(path_file: str, data: bytes, is_append: bool = False):
        mode = 'ab' if is_append else 'wb'
        
        async with aiofiles.open(path_file, mode=mode) as file:
            await file.write(data)
            
    @staticmethod
    async def doRead(path_file: str) -> str:
    
        async with aiofiles.open(path_file, mode="r") as file:
            dataStr = await file.read()
            return dataStr