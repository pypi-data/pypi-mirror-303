from pg_common import rand_str, DictValType
import base64
import hashlib
import struct
import hmac
from io import BytesIO
from Crypto.Cipher import AES, PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
from Crypto import Random, Hash


__INIT_NUM__ = 100000000
__XOR_NUM__ = 0xF0F0F0

__all__ = ["uid_encode", "uid_decode", "aes_encrypt", "aes_decrypt", "decode_private_data",
           "sha256_hex", "dict_to_sign_content", "hmac_sha1", "hmac_sha1_base64", "md5", "md5_base64",
           "rsa_encrypt", "rsa_decrypt", "rsa_gen_sign", "rsa_verify_sign", "DataInputStream",
           "rsa_encrypt2", "rsa_decrypt2", "base64_encode", "base64_decode", "loads", "dumps"
           ]
__auth__ = "baozilaji@gmail.com"

__BLOCK_SIZE__ = 16
__padding__ = lambda s: s + (__BLOCK_SIZE__ - len(s) % __BLOCK_SIZE__) * chr(__BLOCK_SIZE__ - len(s) % __BLOCK_SIZE__)
__un_padding__ = lambda s: s[0:-(s[-1])]


def uid_encode(uid):
    if not uid:
        return 0
    return (uid ^ __XOR_NUM__) + __INIT_NUM__


def uid_decode(pid):
    if not pid:
        return 0
    return (pid - __INIT_NUM__) ^ __XOR_NUM__


# aes encrypt data using ecb mode
def aes_encrypt(src_data):
    _key = rand_str(_len=16)
    _cipher = AES.new(_key.encode(), AES.MODE_ECB)
    _encrypted_data = _cipher.encrypt((__padding__(src_data)).encode())
    return _key+base64.b64encode(_encrypted_data).decode()


# aes decrypt data using ecb mode
def aes_decrypt(dst_data):
    _key = dst_data[0:16]
    _base64_data = dst_data[16:]
    _aes_encrypted_data = base64.b64decode(_base64_data)
    _cipher = AES.new(_key.encode(), AES.MODE_ECB)
    return __un_padding__(_cipher.decrypt(_aes_encrypted_data)).decode()


def base64_encode(data):
    return base64.b64encode(data)

def base64_decode(data):
    return base64.b64decode(data)


def decode_private_data(data, key, iv):
    _data = base64.b64decode(data)
    _key = base64.b64decode(key)
    _iv = base64.b64decode(iv)
    _cipher = AES.new(_key, AES.MODE_CBC, _iv)
    return _cipher.decrypt(_data).decode()


def sha256_hex(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def dict_to_sign_content(data: dict[str, DictValType], key: str = "", key_name: str = "key") -> str:
    _ret = ""
    for _t in sorted(data.items()):
        if _t[1] is not None and _t[0]:
            _v = str(_t[1])
            if _v != "":
                _ret = "%s&%s=%s" % (_ret, _t[0], _t[1])
    if key:
        _ret = "%s&%s=%s" % (_ret, key_name, key)
    if len(_ret) > 0:
        _ret = _ret[1:]
    return _ret


def hmac_sha1_base64(data: str, key: str):
    hmac_code = hmac.new(key.encode(), data.encode(), hashlib.sha1).digest()
    return base64.b64encode(hmac_code).decode()


def hmac_sha1(data: str, key: str):
    return hmac.new(key.encode(), data.encode(), hashlib.sha1).hexdigest()


def md5(data: str):
    return hashlib.md5(data.encode()).hexdigest()


def md5_base64(data: str):
    return base64.b64encode(hashlib.md5(data.encode()).digest()).decode()


def rsa_encrypt(data: str, pub_key):
    rsa_key = RSA.importKey(pub_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    return base64.b64encode(cipher.encrypt(data.encode())).decode()


def rsa_encrypt2(data: str, pub_key):
    return rsa_encrypt(data, f"-----BEGIN PUBLIC KEY-----\n{pub_key}\n-----END PUBLIC KEY-----")


def rsa_decrypt(data: str, pri_key):
    rsa_key = RSA.importKey(pri_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    return cipher.decrypt(base64.b64decode(data), Random.new().read).decode()


def rsa_decrypt2(data: str, pri_key):
    return rsa_decrypt(data, f"-----BEGIN RSA PRIVATE KEY-----\n{pri_key}\n-----END RSA PRIVATE KEY-----")


def rsa_gen_sign(data: str, pri_key):
    rsa_key = RSA.importKey(pri_key)
    verify = Signature_pkcs1_v1_5.new(rsa_key)
    r_hash = Hash.SHA256.new()
    r_hash.update(data.encode())
    return base64.b64encode(verify.sign(r_hash)).decode()


def rsa_verify_sign(data: str, sign: str, pub_key):
    rsa_key = RSA.importKey(pub_key)
    verify = Signature_pkcs1_v1_5.new(rsa_key)
    r_hash = Hash.SHA256.new()
    r_hash.update(data.encode())
    return verify.verify(r_hash, base64.b64decode(sign.encode()))


def loads(data):
    if type(data) == bytes:
        return loads(BytesIO(data))
    t = ord(data.read(1))
    if t == 100:
        return None
    elif t == 99 or t == 98:
        return struct.unpack("b", data.read(1))[0]
    elif t == 97:
        return struct.unpack("h", data.read(2))[0]
    elif t == 96:
        return struct.unpack("i", data.read(4))[0]
    elif t == 95:
        return struct.unpack("q", data.read(8))[0]
    elif t == 94:
        return struct.unpack("d", data.read(8))[0]
    elif t == 90:
        l = struct.unpack("H", data.read(2))[0]
        r = ""
        while l > 0:
            r += chr(struct.unpack("H", data.read(2))[0])
            l -= 1
        return r
    elif t == 89 or t == 88:
        if t == 89:
            l = struct.unpack("B", data.read(1))[0]
        else:
            l = struct.unpack("H", data.read(2))[0]
        r = []
        while l > 0:
            r.append(loads(data))
            l -= 1
        return r
    elif t == 87 or t == 86:
        if t == 87:
            l = struct.unpack("B", data.read(1))[0]
        else:
            l = struct.unpack("H", data.read(2))[0]
        r = {}
        while l > 0:
            k = loads(data)
            v = loads(data)
            r[k] = v
            l -= 1
        return r

    raise RuntimeError(f"not support type: {t}")


def dumps(data):
    if data is None:
        return struct.pack("<b", 100)
    t = type(data)

    if t == bool:
        return struct.pack("<bb", 99, 1 if data else 0)

    if t == int:
        if -128 <= data <= 127:
            return struct.pack("<bb", 98, data)
        elif -32768 <= data <= 32767:
            return struct.pack("<bh", 97, data)
        elif -2147483647 <= data <= 2147483647:
            return struct.pack("<bi", 96, data)
        elif -9223372036854775808 <= data <= 9223372036854775807:
            return struct.pack("<bq", 95, data)
        else:
            data = float(data)
            return dumps(data)

    if t == float:
        return struct.pack("<bd", 94, data)

    if t == str:
        u = struct.pack("<bH", 90, len(data))
        return u + struct.pack("H" * len(data), *map(ord, data))

    if t == list or t == tuple:
        if len(data) <= 255:
            u = struct.pack("<bB", 89, len(data))
        else:
            u = struct.pack("<bH", 88, len(data))
        for d in data:
            u += dumps(d)
        return u

    if t == dict:
        if len(data) <= 255:
            u = struct.pack("<bB", 87, len(data))
        else:
            u = struct.pack("<bH", 86, len(data))
        for k, v in data.items():
            u += dumps(k) + dumps(v)
        return u
    raise RuntimeError(f"not support type:{t}")

class DataInputStream(object):
    def __init__(self, stream) -> None:
        self.stream = stream

    def read_boolean(self):
        return struct.unpack('?', self.stream.read(1))[0]

    def read_byte(self):
        return struct.unpack('b', self.stream.read(1))[0]

    def read_unsigned_byte(self):
        return struct.unpack('B', self.stream.read(1))[0]

    def read_char(self):
        return struct.unpack('>H', self.stream.read(2))[0]

    def read_double(self):
        return struct.unpack('>d', self.stream.read(8))[0]

    def read_float(self):
        return struct.unpack('>f', self.stream.read(4))[0]

    def read_short(self):
        return struct.unpack('>h', self.stream.read(2))[0]

    def read_unsigned_short(self):
        return struct.unpack('>H', self.stream.read(2))[0]

    def read_long(self):
        return struct.unpack('>q', self.stream.read(8))[0]

    def read_utf8(self):
        _length = self.read_unsigned_short()
        return self.stream.read(_length)

    def read_int(self):
        return struct.unpack('>i', self.stream.read(4))[0]
