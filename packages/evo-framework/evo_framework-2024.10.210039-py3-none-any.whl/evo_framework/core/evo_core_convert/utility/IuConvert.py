import base64
from evo_framework.core.evo_core_crypto.utility.IuCryptHash import IuCryptHash
class IuConvert:
    @staticmethod
    def toBase64(data: bytes, charset: str = 'utf-8') -> str:
        # Encode bytes to base64 and decode it using the specified charset
        return base64.b64encode(data).decode(charset)

    @staticmethod
    def fromBase64(strBase64: str, charset: str = 'utf-8') -> bytes:
        # Decode a base64 string to bytes
        return base64.b64decode(strBase64)

    @staticmethod
    def toHex(data: bytes) -> str:
        # Return hexadecimal string representation of bytes
        if data is None:
            return "NONE"
        else:
            return data.hex()

    @staticmethod
    def fromHex(strHex: str) -> bytes:
        # Convert a hex string back to bytes
        if strHex is None:
            return b"NONE"
        else:
            return bytes.fromhex(strHex)
    
    @staticmethod
    def toInt64(input_string:str):
        # Create a SHA-256 hash of the input string
        sha256_hash = IuCryptHash.toSha256(input_string)
        
        # Convert the hash (hex) to an integer
        hash_as_int = int(sha256_hash, 16)
        
        # Convert to int64 by using modulo to fit within the 64-bit signed integer range
        int64_value = hash_as_int % (2**63)  # This ensures we stay within the 64-bit range
        
        # If the result is out of signed int64 range, adjust for negatives
        if int64_value >= 2**63:
            int64_value -= 2**64
        
        return int64_value
    
