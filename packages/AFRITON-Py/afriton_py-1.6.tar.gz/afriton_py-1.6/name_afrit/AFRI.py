



from hashlib import md5
import ctypes
import json
import random
import requests
import time
from urllib.parse import urlparse, urlencode
from binascii        import hexlify
from uuid            import uuid4
from requests        import request



import hashlib
import math


def int_overflow(val):
    maxint = 2147483647
    if not -maxint - 1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def unsigned_right_shitf(n, i):
    if n < 0:
        n = ctypes.c_uint32(n).value
    if i < 0:
        return -int_overflow(n << abs(i))
    return int_overflow(n >> i)


def decode(string):
    _0x50ff23 = {
        48: 0, 49: 1, 50: 2, 51: 3, 52: 4, 53: 5,
        54: 6, 55: 7, 56: 8, 57: 9, 97: 10, 98: 11,
        99: 12, 100: 13, 101: 14, 102: 15
    }
    arr = []
    for i in range(0, 32, 2):
        arr.append(_0x50ff23[ord(string[i])] << 4 | _0x50ff23[ord(string[i + 1])])
    return arr


def md5_arry(arry):
    m = hashlib.md5()
    m.update(bytearray(arry))
    return m.hexdigest()


def md5_string(s):
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()


def encodeWithKey(key, data):
    result = [None] * 256
    temp = 0
    output = ""
    for i in range(256):
        result[i] = i
    for i in range(256):
        temp = (temp + result[i] + key[i % len(key)]) % 256
        temp1 = result[i]
        result[i] = result[temp]
        result[temp] = temp1
    temp2 = 0
    temp = 0
    for i in range(len(data)):
        temp2 = (temp2 + 1) % 256
        temp = (temp + result[temp2]) % 256
        temp1 = result[temp2]
        result[temp2] = result[temp]
        result[temp] = temp1
        output += chr(ord(data[i]) ^ result[(result[temp2] + result[temp]) % 256])
    return output


def b64_encode(string, key_table="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="):
    last_list = list()
    for i in range(0, len(string), 3):
        try:
            num_1 = ord(string[i])
            num_2 = ord(string[i + 1])
            num_3 = ord(string[i + 2])
            arr_1 = num_1 >> 2
            arr_2 = ((3 & num_1) << 4 | (num_2 >> 4))
            arr_3 = ((15 & num_2) << 2) | (num_3 >> 6)
            arr_4 = 63 & num_3
        except IndexError:
            arr_1 = num_1 >> 2
            arr_2 = ((3 & num_1) << 4) | 0
            arr_3 = 64
            arr_4 = 64
        last_list.append(arr_1)
        last_list.append(arr_2)
        last_list.append(arr_3)
        last_list.append(arr_4)
    return "".join([key_table[value] for value in last_list])


def cal_num_list(_num_list):
    new_num_list = []
    for x in [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 4, 6, 8, 10, 12, 14, 16, 18, 20]:
        new_num_list.append(_num_list[x - 1])
    return new_num_list


def _0x22a2b6(_0x59d7ab, _0x151cde, _0x1e0c94, _0x54aa83, _0x76d8ab, _0x550bdb, _0xb90041, _0x44b16d, _0x28659f,
              _0x252c2c, _0x365218, _0x48af11, _0x25e3db, _0x34084f, _0x4f0729, _0x46a34c, _0x1f67f1, _0x5cd529,
              _0x53097b):
    _0xa0a6ac = [0] * 19
    _0xa0a6ac[-0x1 * -0x2192 + 0x11b * 0x5 + -0x2719 * 0x1] = _0x59d7ab
    _0xa0a6ac[0x4a * 0x3 + -0x6d * 0xb + -0x1e9 * -0x2] = _0x365218
    _0xa0a6ac[-0x59f * -0x3 + -0x46c * -0x4 + -0x228b] = _0x151cde
    _0xa0a6ac[0x11a1 + 0xf3d * -0x1 + 0x3 * -0xcb] = _0x48af11
    _0xa0a6ac[-0x1 * -0xa37 + 0x13 * 0x173 + -0x25bc] = _0x1e0c94
    _0xa0a6ac[-0x4 * -0x59f + -0x669 * 0x4 + 0x32d] = _0x25e3db
    _0xa0a6ac[-0x1b42 + 0x10 * -0x24 + 0x1d88] = _0x54aa83
    _0xa0a6ac[0x2245 + 0x335 * 0x6 + -0x357c] = _0x34084f
    _0xa0a6ac[0x3fb + 0x18e1 + -0x1cd4] = _0x76d8ab
    _0xa0a6ac[0x3 * 0x7a + 0x1 * 0x53f + 0x154 * -0x5] = _0x4f0729
    _0xa0a6ac[0x25a * -0x9 + 0x11f6 + 0xa6 * 0x5] = _0x550bdb
    _0xa0a6ac[-0x1b * -0x147 + -0x21e9 * -0x1 + 0x445b * -0x1] = _0x46a34c
    _0xa0a6ac[-0x2f * 0xaf + 0x22f0 + -0x2c3] = _0xb90041
    _0xa0a6ac[0x2f * 0x16 + 0x17 * 0x19 + -0x63c] = _0x1f67f1
    _0xa0a6ac[-0x46a * 0x1 + 0xb * -0x97 + 0xaf5] = _0x44b16d
    _0xa0a6ac[0x47 * 0x4f + -0x8cb * -0x4 + -0x3906] = _0x5cd529
    _0xa0a6ac[-0x7 * 0x40e + 0xb8b + 0x10e7] = _0x28659f
    _0xa0a6ac[0x6f9 + 0x196b + 0x5 * -0x677] = _0x53097b
    _0xa0a6ac[-0xa78 + 0x1b89 + 0xe5 * -0x13] = _0x252c2c
    return ''.join([chr(x) for x in _0xa0a6ac])


def _0x263a8b(_0x2a0483):
    return "\u0002" + "ÿ" + _0x2a0483


def get_x_bogus(params, data, user_agent):
    s0 = md5_string(data)
    s1 = md5_string(params)
    s0_1 = md5_arry(decode(s0))
    s1_1 = md5_arry(decode(s1))
    d = encodeWithKey([0, 1, 12], user_agent)
    ua_str = b64_encode(d)
    ua_str_md5 = md5_string(ua_str)
    timestamp = int(time.time())
    canvas = 536919696
    salt_list = [timestamp, canvas, 64, 0, 1, 12, decode(s1_1)[-2], decode(s1_1)[-1], decode(s0_1)[-2],
                 decode(s0_1)[-1], decode(ua_str_md5)[-2], decode(ua_str_md5)[-1]]
    for x in [24, 16, 8, 0]:
        salt_list.append(salt_list[0] >> x & 255)
    for x in [24, 16, 8, 0]:
        salt_list.append(salt_list[1] >> x & 255)
    _tem = 64
    for x in salt_list[3:]:
        _tem = _tem ^ x
    salt_list.append(_tem)
    salt_list.append(255)
    num_list = cal_num_list(salt_list)
    short_str_2 = encodeWithKey([255], _0x22a2b6(*num_list))
    short_str_3 = _0x263a8b(short_str_2)
    x_b = b64_encode(short_str_3, "Dkdpgh4ZKsQB80/Mfvw36XI1R25-WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe")
    return x_b


def random_k(unm):
    y = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    z = []
    for i in range(unm):
        z.append(random.choice(y))

    return ''.join(z)


def random_32():
    reut = 'xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx'
    hex_t = '0123456789abcdef'
    reut_li = []
    for i in reut:
        if i == 'x':
            reut_li.append(random.choice(hex_t))
        else:
            reut_li.append(i)
    return ''.join(reut_li)


def int32(i):
    return int(0xFFFFFFFF & i)


def fixk(k):
    if len(k) < 4:
        k = k[:4]
        k.extend([0] * (4 - len(k)))
    return k

def mx(sum, y, z, p, e, k):
    tmp = (((z >> 5) ^ (y << 2)) + ((y >> 3) ^ (z << 4)))
    tmp ^= ((sum ^ y) + (k[p & 3 ^ e] ^ z))
    return tmp


def toBinaryString(v, includeLength):
    length = len(v)
    n = length << 2
    if includeLength:
        m = v[length - 1]
        n -= 4
        if m < n - 3 or m > n:
            return None
        n = m
    for i in range(length):
        v[i] = chr(v[i] & 0xFF) + chr((v[i] >> 8) & 0xFF) + chr((v[i] >> 16) & 0xFF) + chr((v[i] >> 24) & 0xFF)
    result = ''.join(v)
    if includeLength:
        return result[:n]
    return result


def encryptUint32Array(v, k):
    DELTA = 2654435769
    length = len(v)
    n = length - 1
    y, z, sum, e, p, q = 0, 0, 0, 0, 0, 0
    z = v[n]
    sum = 0
    for q in range(int(6 + 52 / length)):
        sum = int32(sum + DELTA)
        e = int(sum >> 2) & 3
        for p in range(n):
            y = v[p + 1]
            z = v[p] = int32(v[p] + mx(sum, y, z, p, e, k))
        y = v[0]
        z = v[n] = int32(v[n] + mx(sum, y, z, n, e, k))
    return v


def decryptUint32Array(v, k):
    DELTA = 2654435769
    length = len(v)
    n = length - 1
    y, z, sum, e, p, q = 0, 0, int32(0), 0, 0, 0
    y = v[0]
    q = math.floor(6 + 52 / length)
    sum = int32(q * DELTA)
    while sum != 0:
        e = int32(sum >> 2 & 3)
        p = n
        while p > 0:
            z = v[p - 1]
            y = v[p] = int32(v[p] - mx(sum, y, z, p, e, k))
            p -= 1
        z = v[n]
        y = v[0] = int32(v[0] - mx(sum, y, z, 0, e, k))
        sum = int32(sum - DELTA)
    return v


def utf8DecodeShortString(bs, n):
    charCodes = []
    i = 0
    off = 0
    len_ = len(bs)
    while i < n and off < len_:
        unit = ord(bs[off])
        off += 1
        if unit < 0x80:
            charCodes.append(unit)
        elif 0xc2 <= unit < 0xe0 and off < len_:
            charCodes.append(((unit & 0x1F) << 6) | (ord(bs[off]) & 0x3F))
            off += 1
        elif 0xe0 <= unit < 0xf0 and off + 1 < len_:
            charCodes.append(((unit & 0x0F) << 12) |
                             ((ord(bs[off]) & 0x3F) << 6) |
                             (ord(bs[off + 1]) & 0x3F))
            off += 2
        elif 0xf0 <= unit < 0xf8 and off + 2 < len_:
            rune = (((unit & 0x07) << 18) |
                    ((ord(bs[off]) & 0x3F) << 12) |
                    ((ord(bs[off + 1]) & 0x3F) << 6) |
                    (ord(bs[off + 2]) & 0x3F)) - 0x10000
            if 0 <= rune <= 0xFFFFF:
                charCodes.append(((rune >> 10) & 0x03FF) | 0xD800)
                charCodes.append((rune & 0x03FF) | 0xDC00)
            else:
                raise ValueError('Character outside valid Unicode range: '
                                 + hex(rune))
            off += 3
        else:
            raise ValueError('Bad UTF-8 encoding 0x' + hex(unit))
        i += 1
    return ''.join(chr(code) for code in charCodes)


def utf8DecodeLongString(bs, n):
    buf = []
    char_codes = [0] * 0x8000
    i = off = 0
    len_bs = len(bs)
    while i < n and off < len_bs:
        unit = ord(bs[off])
        off += 1
        divide = unit >> 4
        if divide < 8:
            char_codes[i] = unit
        elif divide == 12 or divide == 13:
            if off < len_bs:
                char_codes[i] = ((unit & 0x1F) << 6) | (ord(bs[off]) & 0x3F)
                off += 1
            else:
                raise ValueError('Unfinished UTF-8 octet sequence')
        elif divide == 14:
            if off + 1 < len_bs:
                char_codes[i] = ((unit & 0x0F) << 12) | ((ord(bs[off]) & 0x3F) << 6) | (ord(bs[off + 1]) & 0x3F)
                off += 2
            else:
                raise ValueError('Unfinished UTF-8 octet sequence')
        elif divide == 15:
            if off + 2 < len_bs:
                rune = (((unit & 0x07) << 18) | ((ord(bs[off]) & 0x3F) << 12) | ((ord(bs[off + 1]) & 0x3F) << 6) | (
                            ord(bs[off + 2]) & 0x3F)) - 0x10000
                off += 3
                if 0 <= rune <= 0xFFFFF:
                    char_codes[i] = (((rune >> 10) & 0x03FF) | 0xD800)
                    i += 1
                    char_codes[i] = ((rune & 0x03FF) | 0xDC00)
                else:
                    raise ValueError('Character outside valid Unicode range: 0x' + hex(rune))
            else:
                raise ValueError('Unfinished UTF-8 octet sequence')
        else:
            raise ValueError('Bad UTF-8 encoding 0x' + hex(unit))
        if i >= 0x7FFF - 1:
            size = i + 1
            char_codes = char_codes[:size]
            buf.append(''.join([chr(c) for c in char_codes]))
            n -= size
            i = -1
        i += 1
    if i > 0:
        char_codes = char_codes[:i]
        buf.append(''.join([chr(c) for c in char_codes]))
    return ''.join(buf)


def utf8Decode(bs, n=None):
    if n is None or n < 0:
        n = len(bs)
    if n == 0:
        return ''
    if all(0 <= ord(c) <= 127 for c in bs) or not all(0 <= ord(c) <= 255 for c in bs):
        if n == len(bs):
            return bs
        return bs[:n]
    return utf8DecodeShortString(bs, n) if n < 0x7FFF else utf8DecodeLongString(bs, n)


def decrypt(data, key):
    if data is None or len(data) == 0:
        return data

    key = utf8Encode(key)

    return utf8Decode(
        toBinaryString(decryptUint32Array(toUint32Array(data, False), fixk(toUint32Array(key, False))), True))


def encrypt(data, key):
    if (data is None) or (len(data) == 0):
        return data
    data = utf8Encode(data)
    key = utf8Encode(key)
    return toBinaryString(
        encryptUint32Array(
            toUint32Array(data, True),
            fixk(toUint32Array(key, False))
        ),
        False
    )


def strData(x, y):
    b = [i for i in range(256)]
    c = 0
    d = ""
    for i in range(256):
        c = (c + b[i] + ord(x[i % len(x)])) % 256
        a = b[i]
        b[i] = b[c]
        b[c] = a
    e = 0
    c = 0
    for i in range(len(y)):
        e = (e + 1) % 256
        c = (c + b[e]) % 256
        a = b[e]
        b[e] = b[c]
        b[c] = a
        d += chr(ord(y[i]) ^ b[(b[e] + b[c]) % 256])
    return d


def bytes_to_string(a, b=None, c=None):
    d = 'Dkdpgh4ZKsQB80/Mfvw36XI1R25+WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe='
    e = '='
    if c:
        e = ''
    if b:
        d = b
    g = ''
    h = 0
    while len(a) >= h + 3:
        f = 0
        f = f | ord(a[h]) << 16
        f = f | ord(a[h + 1]) << 8
        f = f | ord(a[h + 2]) << 0
        g += d[(16515072 & f) >> 18]
        g += d[(258048 & f) >> 12]
        g += d[(4032 & f) >> 6]
        g += d[63 & f]
        h += 3
    if len(a) - h > 0:
        f = (255 & ord(a[h])) << 16 | (ord(a[h + 1]) << 8 if len(a) > h + 1 else 0)
        g += d[(16515072 & f) >> 18]
        g += d[(258048 & f) >> 12]
        g += d[(4032 & f) >> 6] if len(a) > h + 1 else e
        g += e
    return g


def bool_0_1(x):
    if x is None:
        return ''
    elif isinstance(x, bool):
        return '1' if x else '0'
    else:
        return x


def fromCharCode(value_typ):
    unc = ''
    for c in value_typ:
        unc += chr(c & 0xffff)

    return unc


def utf8Encode(str):
    if all(ord(c) < 128 for c in str):
        return str
    buf = []
    n = len(str)
    i = 0
    while i < n:
        codeUnit = ord(str[i])
        if codeUnit < 0x80:
            buf.append(str[i])
            i += 1
        elif codeUnit < 0x800:
            buf.append(chr(0xC0 | (codeUnit >> 6)))
            buf.append(chr(0x80 | (codeUnit & 0x3F)))
            i += 1
        elif codeUnit < 0xD800 or codeUnit > 0xDFFF:
            buf.append(chr(0xE0 | (codeUnit >> 12)))
            buf.append(chr(0x80 | ((codeUnit >> 6) & 0x3F)))
            buf.append(chr(0x80 | (codeUnit & 0x3F)))
            i += 1
        else:
            if i + 1 < n:
                nextCodeUnit = ord(str[i + 1])
                if codeUnit < 0xDC00 and 0xDC00 <= nextCodeUnit and nextCodeUnit <= 0xDFFF:
                    rune = (((codeUnit & 0x03FF) << 10) | (nextCodeUnit & 0x03FF)) + 0x010000
                    buf.append(chr(0xF0 | ((rune >> 18) & 0x3F)))
                    buf.append(chr(0x80 | ((rune >> 12) & 0x3F)))
                    buf.append(chr(0x80 | ((rune >> 6) & 0x3F)))
                    buf.append(chr(0x80 | (rune & 0x3F)))
                    i += 2
                    continue
            raise ValueError('Malformed string')
    return ''.join(buf)


def toUint32Array(bs, includeLength):
    length = len(bs)
    n = length >> 2
    if (length & 3) != 0:
        n += 1
    if includeLength:
        v = [0] * (n + 1)
        v[n] = length
    else:
        v = [0] * n
    for i in range(length):
        v[i >> 2] |= ord(bs[i]) << ((i & 3) << 3)
    return v


def bytes2string_1(a, b="", c=False):
    d = 'Dkdpgh4ZKsQB80/Mfvw36XI1R25+WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe'
    e = ''
    if c:
        e = ''
    if b:
        d = b
    g = ''
    h = 0
    while len(a) >= h + 3:
        f = 0
        f |= ord(a[h]) << 16
        f |= ord(a[h + 1]) << 8
        f |= ord(a[h + 2]) << 0
        g += d[(16515072 & f) >> 18]
        g += d[(258048 & f) >> 12]
        g += d[(4032 & f) >> 6]
        g += d[63 & f]
        h += 3
    if len(a) - h > 0:
        f = (255 & ord(a[h])) << 16
        if len(a) > h + 1:
            f |= (255 & ord(a[h + 1])) << 8
        g += d[(16515072 & f) >> 18]
        g += d[(258048 & f) >> 12]
        if len(a) > h + 1:
            g += d[(4032 & f) >> 6]
        else:
            g += e
        g += e
    return g


def douyin_xxbg_q_encrypt(obj, obj_2=None):
    if obj_2:
        j = 0
        for i in range(len(obj)):
            if obj[j]['p']:
                obj[j]['r'] = obj_2[j]
                j += 1
    temp_text = ''
    for arg in obj:
        temp_text += bool_0_1(arg['r']) + '^^'
    temp_text += str(int(time.time() * 1000))
    salt = random_32()
    temp_num = math.floor(ord(salt[3]) / 8) + ord(salt[3]) % 8
    key = salt[4:4 + temp_num]
    entrypt_byte = encrypt(temp_text, key) + salt
    res = bytes2string_1(entrypt_byte, 'Dkdpgh4ZKsQB80/Mfvw36XI1R25+WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe==')
    return res


def tiktok_mssdk_encode(value):
    b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-."
    k = random_k(4)
    q = encrypt(value, k)
    result = k + bytes2string_1(q, b64)
    return result


def encrypt_strData(text):
    key_num = random.randint(200, 256)
    temp = fromCharCode([65, key_num]) + strData(fromCharCode([key_num]), text)
    return bytes_to_string(temp)




def left_shift(x, y):
    return ctypes.c_int(x << y).value


def get_time():
    return str(int(time.time() * 1000))


class AFREncrypt:
    def __init__(self, user_agent):
        self.ua = user_agent
        self.href_hash = ""
        self.ua_hash = ""
        self.params_hash = ""
        self.fix_hash = 65599
        self.fix_bin = 8240
        self.fix_seq = 65521
        self.canvas_hash = 536919696
        # self.ctx = self.load_js()

    # def load_js(self):
    #     # with open("./DouyinRegisterDevice/app/jsFiles/websdk.js", mode="r", encoding="utf-8") as f:
    #     with open("./websdk.js", mode="r", encoding="utf-8") as f:
    #         ctx = execjs.compile(f.read())
    #     # 本地
    #     # with open("./jsFiles/websdk.js", mode="r", encoding="utf-8") as f:
    #     #     ctx = execjs.compile(f.read())
    #
    #     return ctx

    @staticmethod
    def move_char_calc(nor):
        if 0 <= nor < 26:
            char_at = nor + 65
        elif 26 <= nor < 52:
            char_at = nor + 71
        elif nor == 62 or nor == 63:
            char_at = nor - 17
        else:
            char_at = nor - 4
        return chr(char_at)

    @staticmethod
    def unsigned_right_shift(signed, i=0):
        shift = signed % 0x100000000
        return shift >> i

    def sdb_hash(self, string=None, sdb_value=0):
        for index, char in enumerate(string):
            if string.startswith("_02B4Z6wo00"):
                sdb_value = self.unsigned_right_shift((sdb_value * self.fix_hash) + ord(char))
            elif string.startswith("{"):
                if index in [0, 1]:
                    sdb_value = self.unsigned_right_shift((sdb_value * self.fix_hash) ^ ord(char))
                else:
                    sdb_value = self.unsigned_right_shift((sdb_value * self.fix_hash) + ord(char))
            else:
                sdb_value = self.unsigned_right_shift((sdb_value ^ ord(char)) * self.fix_hash)
        return sdb_value

    def char_to_signature(self, sequence_num):
        offsets = [24, 18, 12, 6, 0]
        string = ""
        for offset in offsets:
            nor = sequence_num >> offset & 63
            string += self.move_char_calc(nor)
        return string

    def href_sequence(self, url):
        timestamp = int(time.time())
        timestamp_hash = self.sdb_hash(str(timestamp))
        self.href_hash = self.sdb_hash(url.split("//")[-1], sdb_value=timestamp_hash)
        sequence = timestamp ^ (self.href_hash % self.fix_seq * self.fix_seq)
        sequence = self.unsigned_right_shift(sequence)
        str_bin_sequence = str(bin(sequence)).replace("0b", "")
        fix_zero = "0" * (32 - len(str_bin_sequence))
        binary = f"{bin(self.fix_bin)}{fix_zero}{str_bin_sequence}".replace("0b", "")
        sequence_number = int(binary, 2)
        return sequence_number

    def char_to_signature1(self, sequence):
        sequence_first = sequence >> 2
        signature_one = self.char_to_signature(sequence_first)
        return signature_one

    def char_to_signature2(self, sequence):
        sequence_second = (sequence << 28) ^ (self.fix_bin >> 4)
        signature_two = self.char_to_signature(sequence_second)
        return signature_two

    def char_to_signature3(self, sequence):
        timestamp_sequence = sequence ^ self.canvas_hash
        sequence_three = left_shift(self.fix_bin, 26) ^ self.unsigned_right_shift(timestamp_sequence, i=6)
        signature_three = self.char_to_signature(sequence_three)
        return signature_three

    def char_to_signature4(self, sequence):
        timestamp_sequence = sequence ^ self.canvas_hash
        signature_four = self.move_char_calc(timestamp_sequence & 63)
        return signature_four

    def char_to_signature5(self, sequence, params, body=None):
        if body:
            new_body = dict()
            for key in sorted(body):
                new_body[key] = body[key]
            body_str = json.dumps(new_body, ensure_ascii=False).replace(" ", "")
            body_hash = self.sdb_hash(body_str)
            params = f"body_hash={body_hash}&{params}"
        sdb_sequence = self.sdb_hash(str(sequence))
        self.ua_hash = self.sdb_hash(self.ua, sdb_sequence)
        self.params_hash = self.sdb_hash(params, sdb_sequence)
        sequence_five = (((self.ua_hash % self.fix_seq) << 16) ^ (self.params_hash % self.fix_seq)) >> 2
        signature_five = self.char_to_signature(sequence_five)
        return signature_five

    def char_to_signature6(self, sequence):
        ua_remainder = self.ua_hash % self.fix_seq
        data_remainder = self.params_hash % self.fix_seq
        ua_data_number = ((int(ua_remainder) << 16) ^ int(data_remainder)) << 28
        sequence_six = ua_data_number ^ self.unsigned_right_shift((288 ^ sequence), 4)
        signature_six = self.char_to_signature(sequence_six)
        return signature_six

    def char_to_signature7(self):
        sequence_seven = self.href_hash % self.fix_seq
        signature_seven = self.char_to_signature(int(sequence_seven))
        return signature_seven

    def char_to_signature_hex(self, signature):
        sdb_signature = self.sdb_hash(signature)
        hex_signature = hex(sdb_signature).replace("0x", "")
        return hex_signature[-2:]

    def get_x_bogus(self, params, body=None, content_type=None):
        body_str = ""
        if content_type == "data":
            body_str = urlencode(body)
        elif content_type == "json":
            body_str = json.dumps(body, ensure_ascii=False).replace(" ", "")
        # x_bogus = self.ctx.call("get_xb", params, body_str, self.ua, self.canvas_hash)
        x_bogus = get_x_bogus(params, body_str, self.ua)
        return x_bogus

    def sign_100(self, ttscid):
        # sign = self.ctx.call("tiktok_mssdk_encode", ttscid)
        sign = tiktok_mssdk_encode(ttscid)
        return sign

    def generate_signature(self, href, api, body=None, content_type=None, ttscid="", prefix="_02B4Z6wo00001"):
        params = api.split("?")[1]
        params_str = str()
        if urlparse(api).query.split("&"):
            params_dict = {item.split("=")[0]: item.split("=")[1] for item in urlparse(api).query.split("&")}
            sort_dict = dict(sorted(params_dict.items(), key=lambda item: item[0]))
            for key, value in sort_dict.items():
                params_str += f"{key}={value}&"
        params_str += f"pathname={urlparse(api).path}&tt_webid=&uuid="
        x_bogus = self.get_x_bogus(params, body, content_type)
        params_str = f"X-Bogus={x_bogus}&{params_str}"
        sequence = self.href_sequence(href)
        sign1 = self.char_to_signature1(sequence)
        sign2 = self.char_to_signature2(sequence)
        sign3 = self.char_to_signature3(sequence)
        sign4 = self.char_to_signature4(sequence)
        sign5 = self.char_to_signature5(sequence, params_str, body)
        sign6 = self.char_to_signature6(sequence)
        sign7 = self.char_to_signature7()
        signature = f"{prefix}{sign1}{sign2}{sign3}{sign4}{sign5}{sign6}{sign7}"
        if ttscid:
            signature = f"{signature}{self.sign_100(ttscid)}"
        sign8 = self.char_to_signature_hex(signature)
        _signature = f"{signature}{sign8}"
        return x_bogus, _signature

    def cookie_signature(self, href, ac_nonce, ttscid="", prefix="_02B4Z6wo00f01"):
        sequence = self.href_sequence(href)
        sign1 = self.char_to_signature1(sequence)
        sign2 = self.char_to_signature2(sequence)
        sign3 = self.char_to_signature3(sequence)
        sign4 = self.char_to_signature4(sequence)
        sign5 = self.char_to_signature5(sequence, ac_nonce)
        sign6 = self.char_to_signature6(sequence)
        sign7 = self.char_to_signature7()
        signature = f"{prefix}{sign1}{sign2}{sign3}{sign4}{sign5}{sign6}{sign7}"
        sign8 = self.char_to_signature_hex(signature)
        if ttscid:
            _signature = f"{signature}{self.sign_100(ttscid)}{sign8}"
        else:
            _signature = f"{signature}{sign8}"
        return _signature

    def encrypt_strData(self, canvas_chrome_str):
        # strData = self.ctx.call("encrypt_strData", canvas_chrome_str)
        strData =encrypt_strData(canvas_chrome_str)
        return strData

    def ms_token(self, href):
        url = "https://mssdk.snssdk.com/web/report?msToken="
        canvas_chrome = {
            "tokenList": [],
            "navigator": {
                "appCodeName": self.ua.split("/")[0],
                "appMinorVersion": "undefined",
                "appName": "Netscape",
                "appVersion": self.ua.replace("Mozilla/", ""),
                "buildID": "undefined",
                "doNotTrack": "null",
                "msDoNotTrack": "undefined",
                "oscpu": "undefined",
                "platform": "Win32",
                "product": "Gecko",
                "productSub": "20030107",
                "cpuClass": "undefined",
                "vendor": "Google Inc.",
                "vendorSub": "",
                "deviceMemory": "8",
                "language": "zh-CN",
                "systemLanguage": "undefined",
                "userLanguage": "undefined",
                "webdriver": "false",
                "cookieEnabled": 1,
                "vibrate": 3,
                "credentials": 99,
                "storage": 99,
                "requestMediaKeySystemAccess": 3,
                "bluetooth": 99,
                "hardwareConcurrency": 4,
                "maxTouchPoints": -1,
                "languages": "zh-CN",
                "touchEvent": 2,
                "touchstart": 2,
            },
            "wID": {
                "load": 0,
                "nativeLength": 33,
                "jsFontsList": "17f",
                "syntaxError": "Failed to construct WebSocket: The URL Create WebSocket is invalid.",
                "timestamp": get_time(),
                "timezone": 8,
                "magic": 3,
                "canvas": str(self.canvas_hash),
                "wProps": 374198,
                "dProps": 2,
                "jsv": "1.7",
                "browserType": 16,
                "iframe": 2,
                "aid": 6383,
                "msgType": 1,
                "privacyMode": 0,
                "aidList": [6383, 6383, 6383],
                "index": 1,
            },
            "window": {
                "Image": 3,
                "isSecureContext": 1,
                "ActiveXObject": 4,
                "toolbar": 99,
                "locationbar": 99,
                "external": 99,
                "mozRTCPeerConnection": 4,
                "postMessage": 3,
                "webkitRequestAnimationFrame": 3,
                "BluetoothUUID": 3,
                "netscape": 4,
                "localStorage": 99,
                "sessionStorage": 99,
                "indexDB": 4,
                "devicePixelRatio": 1,
                "location": href,
            },
            "webgl": {
                "antialias": 1,
                "blueBits": 8,
                "depthBits": 24,
                "greenBits": 8,
                "maxAnisotropy": 16,
                "maxCombinedTextureImageUnits": 32,
                "maxCubeMapTextureSize": 16384,
                "maxFragmentUniformVectors": 1024,
                "maxRenderbufferSize": 16384,
                "maxTextureImageUnits": 16,
                "maxTextureSize": 16384,
                "maxVaryingVectors": 30,
                "maxVertexAttribs": 16,
                "maxVertexTextureImageUnits": 16,
                "maxVertexUniformVectors": 4096,
                "shadingLanguageVersion": "WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)",
                "stencilBits": 0,
                "version": "WebGL 1.0 (OpenGL ES 2.0 Chromium)",
                "vendor": "Google Inc. (Intel)",
                "renderer": "ANGLE (Intel, Intel(R) HD Graphics 620 Direct3D11 vs_5_0 ps_5_0, D3D11)",
            },
            "document": {
                "characterSet": "UTF-8",
                "compatMode": "CSS1Compat",
                "documentMode": "undefined",
                "layers": 4,
                "all": 12,
                "images": 99,
            },
            "screen": {
                "innerWidth": random.randint(1200, 1600),
                "innerHeight": random.randint(600, 800),
                "outerWidth": random.randint(1200, 1600),
                "outerHeight": random.randint(600, 800),
                "screenX": 0,
                "screenY": 0,
                "pageXOffset": 0,
                "pageYOffset": 0,
                "availWidth": random.randint(1200, 1600),
                "availHeight": random.randint(600, 800),
                "sizeWidth": random.randint(1200, 1600),
                "sizeHeight": random.randint(600, 800),
                "clientWidth": random.randint(1200, 1600),
                "clientHeight": random.randint(600, 800),
                "colorDepth": 24,
                "pixelDepth": 24,
            },
            "plugins": {
                "plugin": [
                    "internal-pdf-viewer|application/pdf|pdf",
                    "internal-pdf-viewer|text/pdf|pdf",
                    "internal-pdf-viewer|application/pdf|pdf",
                    "internal-pdf-viewer|text/pdf|pdf",
                    "internal-pdf-viewer|application/pdf|pdf",
                    "internal-pdf-viewer|text/pdf|pdf",
                    "internal-pdf-viewer|application/pdf|pdf",
                    "internal-pdf-viewer|text/pdf|pdf",
                    "internal-pdf-viewer|application/pdf|pdf",
                    "internal-pdf-viewer|text/pdf|pdf",
                ],
                "pv": "0",
            },
            "custom": {},
        }
        str_data = self.encrypt_strData(json.dumps(canvas_chrome).replace(" ", ""))
        payload = {
            "dataType": 8,
            "magic": 538969122,
            "strData": str_data,
            "tspFromClient": int(get_time()),
            "version": 1,
        }
        x_bogus = self.get_x_bogus(url.split("?")[-1], payload, content_type="json")
        url = url + "&X-Bogus=" + x_bogus
        headers = {"user-agent": self.ua}
        response = requests.post(url, json=payload, headers=headers)
        return response.cookies.get("msToken")

    def get_info(self, url):
        api = "https://xxbg.snssdk.com/websdk/v1/getInfo?"
        startTime = int(time.time() * 1000)
        timestamp1 = startTime + random.randint(1, 3)
        timestamp2 = timestamp1 + random.randint(10, 15)
        timestamp3 = timestamp2 + random.randint(100, 150)
        timestamp4 = timestamp3 + random.randint(1, 10)
        plain_arr_1 = [
            {"n": "aid", "f": 4, "r": 6383},
            {"n": "startTime", "f": 3, "r": startTime},
            {"n": "abilities", "f": 3, "r": "111"},
            {"n": "canvas", "f": 3, "r": self.canvas_hash},
            {"n": "timestamp1", "f": 3, "r": timestamp1},
            {"n": "platform", "f": 0, "r": "Win32"},
            {"n": "hardwareConcurrency", "f": 0, "r": 4},
            {"n": "deviceMemory", "f": 0, "r": 8},
            {"n": "language", "f": 0, "r": "zh-CN"},
            {"n": "languages", "f": 0,
             "r": random.sample(['zh-CN', 'zh-TW', 'zh', 'en-US', 'en', 'zh-HK', 'ja'], random.randint(1, 7))},
            {"n": "resolution", "f": 3, "r": f"{random.randint(1200, 1600)}_{random.randint(600, 800)}_24"},
            {"n": "availResolution", "f": 3, "r": f"{random.randint(1200, 1600)}_{random.randint(600, 800)}"},
            {"n": "screenTop", "f": 1, "r": 0},
            {"n": "screenLeft", "f": 1, "r": 0},
            {"n": "devicePixelRatio", "f": 1, "r": 1.25},
            {"n": "productSub", "f": 0, "r": "20030107"},
            {"n": "battery", "f": 3, "p": 1, "r": "true_0_Infinity_1"},
            {"n": "touchInfo", "f": 3, "r": "0_false_false"},
            {"n": "timezone", "f": 3, "r": 480},
            {"n": "timestamp2", "f": 3, "r": timestamp2},
            {
                "n": "gpuInfo",
                "f": 3,
                "r": "Google Inc. (Intel)/ANGLE (Intel, Intel(R) HD Graphics 620 Direct3D11 vs_5_0 ps_5_0, D3D11)",
            },
            {"n": "jsFontsList", "f": 3, "r": "17f"},
            {
                "n": "pluginsList",
                "f": 3,
                "r": "PDF Viewerinternal-pdf-viewerapplication/pdftext/pdf##Chrome PDF Viewerinternal-pdf-viewerapplication/pdftext/pdf##Chromium PDF Viewerinternal-pdf-viewerapplication/pdftext/pdf##Microsoft Edge PDF Viewerinternal-pdf-viewerapplication/pdftext/pdf##WebKit built-in PDFinternal-pdf-viewerapplication/pdftext/pdf",
            },
            {"n": "timestamp3", "f": 3, "r": timestamp3},
            {"n": "userAgent", "f": 0, "r": self.ua},
            {"n": "everCookie", "f": 3, "m": "tt_scid"},
            {
                "n": "syntaxError",
                "f": 3,
                "r": "Failed to construct 'WebSocket': The URL 'Create WebSocket' is invalid.",
            },
            {"n": "nativeLength", "f": 3, "r": 33},
            {"n": "rtcIP", "f": 3, "p": 1, "r": "58.19.72.31"},
            {"n": "location", "f": 1, "r": url},
            {"n": "fpVersion", "f": 4, "r": "2.11.0"},
            # {"n": "clientId", "f": 3, "r": self.ctx.call("random_32")},
            {"n": "clientId", "f": 3, "r": random_32()},
            {"n": "timestamp4", "f": 3, "r": timestamp4},
            {"n": "extendField", "f": 4},
        ]
        plain_arr_2 = ["true_0_Infinity_1", "58.19.72.31"]
        # q = self.ctx.call("douyin_xxbg_q_encrypt", plain_arr_1, plain_arr_2)
        q = douyin_xxbg_q_encrypt(plain_arr_1, plain_arr_2)

        headers = {"user-agent": self.ua}
        params = {"q": q, "callback": f"_7013_{get_time()}"}
        response = requests.get(api, headers=headers, params=params)
        return response.cookies

class Signer:
    shift_array = "Dkdpgh4ZKsQB80/Mfvw36XI1R25-WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe"
    magic = 536919696

    def md5_2x(string):
        return md5(md5(string.encode()).digest()).hexdigest()

    def rc4_encrypt(plaintext: str, key: list[int]) -> str:
        s_box = [_ for _ in range(256)]
        index = 0

        for _ in range(256):
            index = (index + s_box[_] + key[_ % len(key)]) % 256
            s_box[_], s_box[index] = s_box[index], s_box[_]

        _ = 0
        index = 0
        ciphertext = ""

        for char in plaintext:
            _ = (_ + 1) % 256
            index = (index + s_box[_]) % 256

            s_box[_], s_box[index] = s_box[index], s_box[_]
            keystream = s_box[(s_box[_] + s_box[index]) % 256]
            ciphertext += chr(ord(char) ^ keystream)

        return ciphertext

    def b64_encode(
        string,
        key_table="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
    ):
        last_list = list()
        for i in range(0, len(string), 3):
            try:
                num_1 = ord(string[i])
                num_2 = ord(string[i + 1])
                num_3 = ord(string[i + 2])
                arr_1 = num_1 >> 2
                arr_2 = (3 & num_1) << 4 | (num_2 >> 4)
                arr_3 = ((15 & num_2) << 2) | (num_3 >> 6)
                arr_4 = 63 & num_3

            except IndexError:
                arr_1 = num_1 >> 2
                arr_2 = ((3 & num_1) << 4) | 0
                arr_3 = 64
                arr_4 = 64

            last_list.append(arr_1)
            last_list.append(arr_2)
            last_list.append(arr_3)
            last_list.append(arr_4)

        return "".join([key_table[value] for value in last_list])

    def filter(num_list: list):
        return [
            num_list[x - 1]
            for x in [3,5,7,9,11,13,15,17,19,21,4,6,8,10,12,14,16,18,20,
            ]
        ]

    def scramble(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s) -> str:
        return "".join(
            [
                chr(_)
                for _ in [a,k,b,l,c,m,d,n,e,o,f,p,g,q,h,r,i,s,j,
                ]
            ]
        )

    def checksum(salt_list: str) -> int:
        checksum = 64
        _ = [checksum := checksum ^ x for x in salt_list[3:]]

        return checksum

    def _x_bogus(params, user_agent, timestamp, data) -> str:

        md5_data = Signer.md5_2x(data)
        md5_params = Signer.md5_2x(params)
        md5_ua = md5(
            Signer.b64_encode(Signer.rc4_encrypt(user_agent, [0, 1, 14])).encode()
        ).hexdigest()

        salt_list = [
            timestamp,
            Signer.magic,
            64,
            0,
            1,
            14,
            bytes.fromhex(md5_params)[-2],
            bytes.fromhex(md5_params)[-1],
            bytes.fromhex(md5_data)[-2],
            bytes.fromhex(md5_data)[-1],
            bytes.fromhex(md5_ua)[-2],
            bytes.fromhex(md5_ua)[-1],
        ]

        salt_list.extend([(timestamp >> i) & 0xFF for i in range(24, -1, -8)])
        salt_list.extend([(salt_list[1] >> i) & 0xFF for i in range(24, -1, -8)])
        salt_list.extend([Signer.checksum(salt_list), 255])

        num_list = Signer.filter(salt_list)
        rc4_num_list = Signer.rc4_encrypt(Signer.scramble(*num_list), [255])

        return Signer.b64_encode(f"\x02ÿ{rc4_num_list}", Signer.shift_array)
    
def tim():
    _rticket = int(time.time() * 1000)
    ts=str(int(time.time() * 1000))[:10]
    ts1=str(int(time.time() * 1000))[:10]
    icket = int(time.time() * 1000)
    return _rticket,ts,ts1,icket

import gzip
import binascii
import random

class AFRITON:
    __content = []
    __content_raw = []
    CF = 0
    begining = [0x74, 0x63, 0x05, 0x10, 0, 0]
    dword_0 = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]
    dword_1 = [16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 452984832, 905969664]
    dword_2 = [0, 235474187, 470948374, 303765277, 941896748, 908933415, 607530554, 708780849, 1883793496, 2118214995, 1817866830, 1649639237, 1215061108, 1181045119, 1417561698, 1517767529, 3767586992, 4003061179, 4236429990, 4069246893, 3635733660, 3602770327, 3299278474, 3400528769, 2430122216, 2664543715, 2362090238, 2193862645, 2835123396, 2801107407, 3035535058, 3135740889, 3678124923, 3576870512, 3341394285, 3374361702, 3810496343, 3977675356, 4279080257, 4043610186, 2876494627, 2776292904, 3076639029, 3110650942, 2472011535, 2640243204, 2403728665, 2169303058, 1001089995, 899835584, 666464733, 699432150, 59727847, 226906860, 530400753, 294930682, 1273168787, 1172967064, 1475418501, 1509430414, 1942435775, 2110667444, 1876241833, 1641816226, 2910219766, 2743034109, 2976151520, 3211623147, 2505202138, 2606453969, 2302690252, 2269728455, 3711829422, 3543599269, 3240894392, 3475313331, 3843699074, 3943906441, 4178062228, 4144047775, 1306967366, 1139781709, 1374988112, 1610459739, 1975683434, 2076935265, 1775276924, 1742315127, 1034867998, 866637845, 566021896, 800440835, 92987698, 193195065, 429456164, 395441711, 1984812685, 2017778566, 1784663195, 1683407248, 1315562145, 1080094634, 1383856311, 1551037884, 101039829, 135050206, 437757123, 337553864, 1042385657, 807962610, 573804783, 742039012, 2531067453, 2564033334, 2328828971, 2227573024, 2935566865, 2700099354, 3001755655, 3168937228, 3868552805, 3902563182, 4203181171, 4102977912, 3736164937, 3501741890, 3265478751, 3433712980, 1106041591, 1340463100, 1576976609, 1408749034, 2043211483, 2009195472, 1708848333, 1809054150, 832877231, 1068351396, 766945465, 599762354, 159417987, 126454664, 361929877, 463180190, 2709260871, 2943682380, 3178106961, 3009879386, 2572697195, 2538681184, 2236228733, 2336434550, 3509871135, 3745345300, 3441850377, 3274667266, 3910161971, 3877198648, 4110568485, 4211818798, 2597806476, 2497604743, 2261089178, 2295101073, 2733856160, 2902087851, 3202437046, 2968011453, 3936291284, 3835036895, 4136440770, 4169408201, 3535486456, 3702665459, 3467192302, 3231722213, 2051518780, 1951317047, 1716890410, 1750902305, 1113818384, 1282050075, 1584504582, 1350078989, 168810852, 67556463, 371049330, 404016761, 841739592, 1008918595, 775550814, 540080725, 3969562369, 3801332234, 4035489047, 4269907996, 3569255213, 3669462566, 3366754619, 3332740144, 2631065433, 2463879762, 2160117071, 2395588676, 2767645557, 2868897406, 3102011747, 3069049960, 202008497, 33778362, 270040487, 504459436, 875451293, 975658646, 675039627, 641025152, 2084704233, 1917518562, 1615861247, 1851332852, 1147550661, 1248802510, 1484005843, 1451044056, 933301370, 967311729, 733156972, 632953703, 260388950, 25965917, 328671808, 496906059, 1206477858, 1239443753, 1543208500, 1441952575, 2144161806, 1908694277, 1675577880, 1842759443, 3610369226, 3644379585, 3408119516, 3307916247, 4011190502, 3776767469, 4077384432, 4245618683, 2809771154, 2842737049, 3144396420, 3043140495, 2673705150, 2438237621, 2203032232, 2370213795]
    dword_3 = [0, 185469197, 370938394, 487725847, 741876788, 657861945, 975451694, 824852259, 1483753576, 1400783205, 1315723890, 1164071807, 1950903388, 2135319889, 1649704518, 1767536459, 2967507152, 3152976349, 2801566410, 2918353863, 2631447780, 2547432937, 2328143614, 2177544179, 3901806776, 3818836405, 4270639778, 4118987695, 3299409036, 3483825537, 3535072918, 3652904859, 2077965243, 1893020342, 1841768865, 1724457132, 1474502543, 1559041666, 1107234197, 1257309336, 598438867, 681933534, 901210569, 1052338372, 261314535, 77422314, 428819965, 310463728, 3409685355, 3224740454, 3710368113, 3593056380, 3875770207, 3960309330, 4045380933, 4195456072, 2471224067, 2554718734, 2237133081, 2388260884, 3212035895, 3028143674, 2842678573, 2724322336, 4138563181, 4255350624, 3769721975, 3955191162, 3667219033, 3516619604, 3431546947, 3347532110, 2933734917, 2782082824, 3099667487, 3016697106, 2196052529, 2313884476, 2499348523, 2683765030, 1179510461, 1296297904, 1347548327, 1533017514, 1786102409, 1635502980, 2087309459, 2003294622, 507358933, 355706840, 136428751, 53458370, 839224033, 957055980, 605657339, 790073846, 2373340630, 2256028891, 2607439820, 2422494913, 2706270690, 2856345839, 3075636216, 3160175349, 3573941694, 3725069491, 3273267108, 3356761769, 4181598602, 4063242375, 4011996048, 3828103837, 1033297158, 915985419, 730517276, 545572369, 296679730, 446754879, 129166120, 213705253, 1709610350, 1860738147, 1945798516, 2029293177, 1239331162, 1120974935, 1606591296, 1422699085, 4148292826, 4233094615, 3781033664, 3931371469, 3682191598, 3497509347, 3446004468, 3328955385, 2939266226, 2755636671, 3106780840, 2988687269, 2198438022, 2282195339, 2501218972, 2652609425, 1201765386, 1286567175, 1371368976, 1521706781, 1805211710, 1620529459, 2105887268, 1988838185, 533804130, 350174575, 164439672, 46346101, 870912086, 954669403, 636813900, 788204353, 2358957921, 2274680428, 2592523643, 2441661558, 2695033685, 2880240216, 3065962831, 3182487618, 3572145929, 3756299780, 3270937875, 3388507166, 4174560061, 4091327024, 4006521127, 3854606378, 1014646705, 930369212, 711349675, 560487590, 272786309, 457992840, 106852767, 223377554, 1678381017, 1862534868, 1914052035, 2031621326, 1211247597, 1128014560, 1580087799, 1428173050, 32283319, 182621114, 401639597, 486441376, 768917123, 651868046, 1003007129, 818324884, 1503449823, 1385356242, 1333838021, 1150208456, 1973745387, 2125135846, 1673061617, 1756818940, 2970356327, 3120694122, 2802849917, 2887651696, 2637442643, 2520393566, 2334669897, 2149987652, 3917234703, 3799141122, 4284502037, 4100872472, 3309594171, 3460984630, 3545789473, 3629546796, 2050466060, 1899603969, 1814803222, 1730525723, 1443857720, 1560382517, 1075025698, 1260232239, 575138148, 692707433, 878443390, 1062597235, 243256656, 91341917, 409198410, 325965383, 3403100636, 3252238545, 3704300486, 3620022987, 3874428392, 3990953189, 4042459122, 4227665663, 2460449204, 2578018489, 2226875310, 2411029155, 3198115200, 3046200461, 2827177882, 2743944855]
    dword_4 = [0, 218828297, 437656594, 387781147, 875313188, 958871085, 775562294, 590424639, 1750626376, 1699970625, 1917742170, 2135253587, 1551124588, 1367295589, 1180849278, 1265195639, 3501252752, 3720081049, 3399941250, 3350065803, 3835484340, 3919042237, 4270507174, 4085369519, 3102249176, 3051593425, 2734591178, 2952102595, 2361698556, 2177869557, 2530391278, 2614737639, 3145456443, 3060847922, 2708326185, 2892417312, 2404901663, 2187128086, 2504130317, 2555048196, 3542330227, 3727205754, 3375740769, 3292445032, 3876557655, 3926170974, 4246310725, 4027744588, 1808481195, 1723872674, 1910319033, 2094410160, 1608975247, 1391201670, 1173430173, 1224348052, 59984867, 244860394, 428169201, 344873464, 935293895, 984907214, 766078933, 547512796, 1844882806, 1627235199, 2011214180, 2062270317, 1507497298, 1423022939, 1137477952, 1321699145, 95345982, 145085239, 532201772, 313773861, 830661914, 1015671571, 731183368, 648017665, 3175501286, 2957853679, 2807058932, 2858115069, 2305455554, 2220981195, 2474404304, 2658625497, 3575528878, 3625268135, 3473416636, 3254988725, 3778151818, 3963161475, 4213447064, 4130281361, 3599595085, 3683022916, 3432737375, 3247465558, 3802222185, 4020912224, 4172763771, 4122762354, 3201631749, 3017672716, 2764249623, 2848461854, 2331590177, 2280796200, 2431590963, 2648976442, 104699613, 188127444, 472615631, 287343814, 840019705, 1058709744, 671593195, 621591778, 1852171925, 1668212892, 1953757831, 2037970062, 1514790577, 1463996600, 1080017571, 1297403050, 3673637356, 3623636965, 3235995134, 3454686199, 4007360968, 3822090177, 4107101658, 4190530515, 2997825956, 3215212461, 2830708150, 2779915199, 2256734592, 2340947849, 2627016082, 2443058075, 172466556, 122466165, 273792366, 492483431, 1047239000, 861968209, 612205898, 695634755, 1646252340, 1863638845, 2013908262, 1963115311, 1446242576, 1530455833, 1277555970, 1093597963, 1636604631, 1820824798, 2073724613, 1989249228, 1436590835, 1487645946, 1337376481, 1119727848, 164948639, 81781910, 331544205, 516552836, 1039717051, 821288114, 669961897, 719700128, 2973530695, 3157750862, 2871682645, 2787207260, 2232435299, 2283490410, 2667994737, 2450346104, 3647212047, 3564045318, 3279033885, 3464042516, 3980931627, 3762502690, 4150144569, 4199882800, 3070356634, 3121275539, 2904027272, 2686254721, 2200818878, 2384911031, 2570832044, 2486224549, 3747192018, 3528626907, 3310321856, 3359936201, 3950355702, 3867060991, 4049844452, 4234721005, 1739656202, 1790575107, 2108100632, 1890328081, 1402811438, 1586903591, 1233856572, 1149249077, 266959938, 48394827, 369057872, 418672217, 1002783846, 919489135, 567498868, 752375421, 209336225, 24197544, 376187827, 459744698, 945164165, 895287692, 574624663, 793451934, 1679968233, 1764313568, 2117360635, 1933530610, 1343127501, 1560637892, 1243112415, 1192455638, 3704280881, 3519142200, 3336358691, 3419915562, 3907448597, 3857572124, 4075877127, 4294704398, 3029510009, 3113855344, 2927934315, 2744104290, 2159976285, 2377486676, 2594734927, 2544078150]
    dword_5 = [0, 151849742, 303699484, 454499602, 607398968, 758720310, 908999204, 1059270954, 1214797936, 1097159550, 1517440620, 1400849762, 1817998408, 1699839814, 2118541908, 2001430874, 2429595872, 2581445614, 2194319100, 2345119218, 3034881240, 3186202582, 2801699524, 2951971274, 3635996816, 3518358430, 3399679628, 3283088770, 4237083816, 4118925222, 4002861748, 3885750714, 1002142683, 850817237, 698445255, 548169417, 529487843, 377642221, 227885567, 77089521, 1943217067, 2061379749, 1640576439, 1757691577, 1474760595, 1592394909, 1174215055, 1290801793, 2875968315, 2724642869, 3111247143, 2960971305, 2405426947, 2253581325, 2638606623, 2487810577, 3808662347, 3926825029, 4044981591, 4162096729, 3342319475, 3459953789, 3576539503, 3693126241, 1986918061, 2137062819, 1685577905, 1836772287, 1381620373, 1532285339, 1078185097, 1229899655, 1040559837, 923313619, 740276417, 621982671, 439452389, 322734571, 137073913, 19308535, 3871163981, 4021308739, 4104605777, 4255800159, 3263785589, 3414450555, 3499326569, 3651041127, 2933202493, 2815956275, 3167684641, 3049390895, 2330014213, 2213296395, 2566595609, 2448830231, 1305906550, 1155237496, 1607244650, 1455525988, 1776460110, 1626319424, 2079897426, 1928707164, 96392454, 213114376, 396673818, 514443284, 562755902, 679998000, 865136418, 983426092, 3708173718, 3557504664, 3474729866, 3323011204, 4180808110, 4030667424, 3945269170, 3794078908, 2507040230, 2623762152, 2272556026, 2390325492, 2975484382, 3092726480, 2738905026, 2857194700, 3973773121, 3856137295, 4274053469, 4157467219, 3371096953, 3252932727, 3673476453, 3556361835, 2763173681, 2915017791, 3064510765, 3215307299, 2156299017, 2307622919, 2459735317, 2610011675, 2081048481, 1963412655, 1846563261, 1729977011, 1480485785, 1362321559, 1243905413, 1126790795, 878845905, 1030690015, 645401037, 796197571, 274084841, 425408743, 38544885, 188821243, 3613494426, 3731654548, 3313212038, 3430322568, 4082475170, 4200115116, 3780097726, 3896688048, 2668221674, 2516901860, 2366882550, 2216610296, 3141400786, 2989552604, 2837966542, 2687165888, 1202797690, 1320957812, 1437280870, 1554391400, 1669664834, 1787304780, 1906247262, 2022837584, 265905162, 114585348, 499347990, 349075736, 736970802, 585122620, 972512814, 821712160, 2595684844, 2478443234, 2293045232, 2174754046, 3196267988, 3079546586, 2895723464, 2777952454, 3537852828, 3687994002, 3234156416, 3385345166, 4142626212, 4293295786, 3841024952, 3992742070, 174567692, 57326082, 410887952, 292596766, 777231668, 660510266, 1011452712, 893681702, 1108339068, 1258480242, 1343618912, 1494807662, 1715193156, 1865862730, 1948373848, 2100090966, 2701949495, 2818666809, 3004591147, 3122358053, 2235061775, 2352307457, 2535604243, 2653899549, 3915653703, 3764988233, 4219352155, 4067639125, 3444575871, 3294430577, 3746175075, 3594982253, 836553431, 953270745, 600235211, 718002117, 367585007, 484830689, 133361907, 251657213, 2041877159, 1891211689, 1806599355, 1654886325, 1568718495, 1418573201, 1335535747, 1184342925]
    dword_6 = [3328402341, 4168907908, 4000806809, 4135287693, 4294111757, 3597364157, 3731845041, 2445657428, 1613770832, 33620227, 3462883241, 1445669757, 3892248089, 3050821474, 1303096294, 3967186586, 2412431941, 528646813, 2311702848, 4202528135, 4026202645, 2992200171, 2387036105, 4226871307, 1101901292, 3017069671, 1604494077, 1169141738, 597466303, 1403299063, 3832705686, 2613100635, 1974974402, 3791519004, 1033081774, 1277568618, 1815492186, 2118074177, 4126668546, 2211236943, 1748251740, 1369810420, 3521504564, 4193382664, 3799085459, 2883115123, 1647391059, 706024767, 134480908, 2512897874, 1176707941, 2646852446, 806885416, 932615841, 168101135, 798661301, 235341577, 605164086, 461406363, 3756188221, 3454790438, 1311188841, 2142417613, 3933566367, 302582043, 495158174, 1479289972, 874125870, 907746093, 3698224818, 3025820398, 1537253627, 2756858614, 1983593293, 3084310113, 2108928974, 1378429307, 3722699582, 1580150641, 327451799, 2790478837, 3117535592, 0, 3253595436, 1075847264, 3825007647, 2041688520, 3059440621, 3563743934, 2378943302, 1740553945, 1916352843, 2487896798, 2555137236, 2958579944, 2244988746, 3151024235, 3320835882, 1336584933, 3992714006, 2252555205, 2588757463, 1714631509, 293963156, 2319795663, 3925473552, 67240454, 4269768577, 2689618160, 2017213508, 631218106, 1269344483, 2723238387, 1571005438, 2151694528, 93294474, 1066570413, 563977660, 1882732616, 4059428100, 1673313503, 2008463041, 2950355573, 1109467491, 537923632, 3858759450, 4260623118, 3218264685, 2177748300, 403442708, 638784309, 3287084079, 3193921505, 899127202, 2286175436, 773265209, 2479146071, 1437050866, 4236148354, 2050833735, 3362022572, 3126681063, 840505643, 3866325909, 3227541664, 427917720, 2655997905, 2749160575, 1143087718, 1412049534, 999329963, 193497219, 2353415882, 3354324521, 1807268051, 672404540, 2816401017, 3160301282, 369822493, 2916866934, 3688947771, 1681011286, 1949973070, 336202270, 2454276571, 201721354, 1210328172, 3093060836, 2680341085, 3184776046, 1135389935, 3294782118, 965841320, 831886756, 3554993207, 4068047243, 3588745010, 2345191491, 1849112409, 3664604599, 26054028, 2983581028, 2622377682, 1235855840, 3630984372, 2891339514, 4092916743, 3488279077, 3395642799, 4101667470, 1202630377, 268961816, 1874508501, 4034427016, 1243948399, 1546530418, 941366308, 1470539505, 1941222599, 2546386513, 3421038627, 2715671932, 3899946140, 1042226977, 2521517021, 1639824860, 227249030, 260737669, 3765465232, 2084453954, 1907733956, 3429263018, 2420656344, 100860677, 4160157185, 470683154, 3261161891, 1781871967, 2924959737, 1773779408, 394692241, 2579611992, 974986535, 664706745, 3655459128, 3958962195, 731420851, 571543859, 3530123707, 2849626480, 126783113, 865375399, 765172662, 1008606754, 361203602, 3387549984, 2278477385, 2857719295, 1344809080, 2782912378, 59542671, 1503764984, 160008576, 437062935, 1707065306, 3622233649, 2218934982, 3496503480, 2185314755, 697932208, 1512910199, 504303377, 2075177163, 2824099068, 1841019862, 739644986]
    dword_7 = [2781242211, 2230877308, 2582542199, 2381740923, 234877682, 3184946027, 2984144751, 1418839493, 1348481072, 50462977, 2848876391, 2102799147, 434634494, 1656084439, 3863849899, 2599188086, 1167051466, 2636087938, 1082771913, 2281340285, 368048890, 3954334041, 3381544775, 201060592, 3963727277, 1739838676, 4250903202, 3930435503, 3206782108, 4149453988, 2531553906, 1536934080, 3262494647, 484572669, 2923271059, 1783375398, 1517041206, 1098792767, 49674231, 1334037708, 1550332980, 4098991525, 886171109, 150598129, 2481090929, 1940642008, 1398944049, 1059722517, 201851908, 1385547719, 1699095331, 1587397571, 674240536, 2704774806, 252314885, 3039795866, 151914247, 908333586, 2602270848, 1038082786, 651029483, 1766729511, 3447698098, 2682942837, 454166793, 2652734339, 1951935532, 775166490, 758520603, 3000790638, 4004797018, 4217086112, 4137964114, 1299594043, 1639438038, 3464344499, 2068982057, 1054729187, 1901997871, 2534638724, 4121318227, 1757008337, 0, 750906861, 1614815264, 535035132, 3363418545, 3988151131, 3201591914, 1183697867, 3647454910, 1265776953, 3734260298, 3566750796, 3903871064, 1250283471, 1807470800, 717615087, 3847203498, 384695291, 3313910595, 3617213773, 1432761139, 2484176261, 3481945413, 283769337, 100925954, 2180939647, 4037038160, 1148730428, 3123027871, 3813386408, 4087501137, 4267549603, 3229630528, 2315620239, 2906624658, 3156319645, 1215313976, 82966005, 3747855548, 3245848246, 1974459098, 1665278241, 807407632, 451280895, 251524083, 1841287890, 1283575245, 337120268, 891687699, 801369324, 3787349855, 2721421207, 3431482436, 959321879, 1469301956, 4065699751, 2197585534, 1199193405, 2898814052, 3887750493, 724703513, 2514908019, 2696962144, 2551808385, 3516813135, 2141445340, 1715741218, 2119445034, 2872807568, 2198571144, 3398190662, 700968686, 3547052216, 1009259540, 2041044702, 3803995742, 487983883, 1991105499, 1004265696, 1449407026, 1316239930, 504629770, 3683797321, 168560134, 1816667172, 3837287516, 1570751170, 1857934291, 4014189740, 2797888098, 2822345105, 2754712981, 936633572, 2347923833, 852879335, 1133234376, 1500395319, 3084545389, 2348912013, 1689376213, 3533459022, 3762923945, 3034082412, 4205598294, 133428468, 634383082, 2949277029, 2398386810, 3913789102, 403703816, 3580869306, 2297460856, 1867130149, 1918643758, 607656988, 4049053350, 3346248884, 1368901318, 600565992, 2090982877, 2632479860, 557719327, 3717614411, 3697393085, 2249034635, 2232388234, 2430627952, 1115438654, 3295786421, 2865522278, 3633334344, 84280067, 33027830, 303828494, 2747425121, 1600795957, 4188952407, 3496589753, 2434238086, 1486471617, 658119965, 3106381470, 953803233, 334231800, 3005978776, 857870609, 3151128937, 1890179545, 2298973838, 2805175444, 3056442267, 574365214, 2450884487, 550103529, 1233637070, 4289353045, 2018519080, 2057691103, 2399374476, 4166623649, 2148108681, 387583245, 3664101311, 836232934, 3330556482, 3100665960, 3280093505, 2955516313, 2002398509, 287182607, 3413881008, 4238890068, 3597515707, 975967766]
    dword_8 = [1671808611, 2089089148, 2006576759, 2072901243, 4061003762, 1807603307, 1873927791, 3310653893, 810573872, 16974337, 1739181671, 729634347, 4263110654, 3613570519, 2883997099, 1989864566, 3393556426, 2191335298, 3376449993, 2106063485, 4195741690, 1508618841, 1204391495, 4027317232, 2917941677, 3563566036, 2734514082, 2951366063, 2629772188, 2767672228, 1922491506, 3227229120, 3082974647, 4246528509, 2477669779, 644500518, 911895606, 1061256767, 4144166391, 3427763148, 878471220, 2784252325, 3845444069, 4043897329, 1905517169, 3631459288, 827548209, 356461077, 67897348, 3344078279, 593839651, 3277757891, 405286936, 2527147926, 84871685, 2595565466, 118033927, 305538066, 2157648768, 3795705826, 3945188843, 661212711, 2999812018, 1973414517, 152769033, 2208177539, 745822252, 439235610, 455947803, 1857215598, 1525593178, 2700827552, 1391895634, 994932283, 3596728278, 3016654259, 695947817, 3812548067, 795958831, 2224493444, 1408607827, 3513301457, 0, 3979133421, 543178784, 4229948412, 2982705585, 1542305371, 1790891114, 3410398667, 3201918910, 961245753, 1256100938, 1289001036, 1491644504, 3477767631, 3496721360, 4012557807, 2867154858, 4212583931, 1137018435, 1305975373, 861234739, 2241073541, 1171229253, 4178635257, 33948674, 2139225727, 1357946960, 1011120188, 2679776671, 2833468328, 1374921297, 2751356323, 1086357568, 2408187279, 2460827538, 2646352285, 944271416, 4110742005, 3168756668, 3066132406, 3665145818, 560153121, 271589392, 4279952895, 4077846003, 3530407890, 3444343245, 202643468, 322250259, 3962553324, 1608629855, 2543990167, 1154254916, 389623319, 3294073796, 2817676711, 2122513534, 1028094525, 1689045092, 1575467613, 422261273, 1939203699, 1621147744, 2174228865, 1339137615, 3699352540, 577127458, 712922154, 2427141008, 2290289544, 1187679302, 3995715566, 3100863416, 339486740, 3732514782, 1591917662, 186455563, 3681988059, 3762019296, 844522546, 978220090, 169743370, 1239126601, 101321734, 611076132, 1558493276, 3260915650, 3547250131, 2901361580, 1655096418, 2443721105, 2510565781, 3828863972, 2039214713, 3878868455, 3359869896, 928607799, 1840765549, 2374762893, 3580146133, 1322425422, 2850048425, 1823791212, 1459268694, 4094161908, 3928346602, 1706019429, 2056189050, 2934523822, 135794696, 3134549946, 2022240376, 628050469, 779246638, 472135708, 2800834470, 3032970164, 3327236038, 3894660072, 3715932637, 1956440180, 522272287, 1272813131, 3185336765, 2340818315, 2323976074, 1888542832, 1044544574, 3049550261, 1722469478, 1222152264, 50660867, 4127324150, 236067854, 1638122081, 895445557, 1475980887, 3117443513, 2257655686, 3243809217, 489110045, 2662934430, 3778599393, 4162055160, 2561878936, 288563729, 1773916777, 3648039385, 2391345038, 2493985684, 2612407707, 505560094, 2274497927, 3911240169, 3460925390, 1442818645, 678973480, 3749357023, 2358182796, 2717407649, 2306869641, 219617805, 3218761151, 3862026214, 1120306242, 1756942440, 1103331905, 2578459033, 762796589, 252780047, 2966125488, 1425844308, 3151392187, 372911126]
    dword_9 = [1667474886, 2088535288, 2004326894, 2071694838, 4075949567, 1802223062, 1869591006, 3318043793, 808472672, 16843522, 1734846926, 724270422, 4278065639, 3621216949, 2880169549, 1987484396, 3402253711, 2189597983, 3385409673, 2105378810, 4210693615, 1499065266, 1195886990, 4042263547, 2913856577, 3570689971, 2728590687, 2947541573, 2627518243, 2762274643, 1920112356, 3233831835, 3082273397, 4261223649, 2475929149, 640051788, 909531756, 1061110142, 4160160501, 3435941763, 875846760, 2779116625, 3857003729, 4059105529, 1903268834, 3638064043, 825316194, 353713962, 67374088, 3351728789, 589522246, 3284360861, 404236336, 2526454071, 84217610, 2593830191, 117901582, 303183396, 2155911963, 3806477791, 3958056653, 656894286, 2998062463, 1970642922, 151591698, 2206440989, 741110872, 437923380, 454765878, 1852748508, 1515908788, 2694904667, 1381168804, 993742198, 3604373943, 3014905469, 690584402, 3823320797, 791638366, 2223281939, 1398011302, 3520161977, 0, 3991743681, 538992704, 4244381667, 2981218425, 1532751286, 1785380564, 3419096717, 3200178535, 960056178, 1246420628, 1280103576, 1482221744, 3486468741, 3503319995, 4025428677, 2863326543, 4227536621, 1128514950, 1296947098, 859002214, 2240123921, 1162203018, 4193849577, 33687044, 2139062782, 1347481760, 1010582648, 2678045221, 2829640523, 1364325282, 2745433693, 1077985408, 2408548869, 2459086143, 2644360225, 943212656, 4126475505, 3166494563, 3065430391, 3671750063, 555836226, 269496352, 4294908645, 4092792573, 3537006015, 3452783745, 202118168, 320025894, 3974901699, 1600119230, 2543297077, 1145359496, 387397934, 3301201811, 2812801621, 2122220284, 1027426170, 1684319432, 1566435258, 421079858, 1936954854, 1616945344, 2172753945, 1330631070, 3705438115, 572679748, 707427924, 2425400123, 2290647819, 1179044492, 4008585671, 3099120491, 336870440, 3739122087, 1583276732, 185277718, 3688593069, 3772791771, 842159716, 976899700, 168435220, 1229577106, 101059084, 606366792, 1549591736, 3267517855, 3553849021, 2897014595, 1650632388, 2442242105, 2509612081, 3840161747, 2038008818, 3890688725, 3368567691, 926374254, 1835907034, 2374863873, 3587531953, 1313788572, 2846482505, 1819063512, 1448540844, 4109633523, 3941213647, 1701162954, 2054852340, 2930698567, 134748176, 3132806511, 2021165296, 623210314, 774795868, 471606328, 2795958615, 3031746419, 3334885783, 3907527627, 3722280097, 1953799400, 522133822, 1263263126, 3183336545, 2341176845, 2324333839, 1886425312, 1044267644, 3048588401, 1718004428, 1212733584, 50529542, 4143317495, 235803164, 1633788866, 892690282, 1465383342, 3115962473, 2256965911, 3250673817, 488449850, 2661202215, 3789633753, 4177007595, 2560144171, 286339874, 1768537042, 3654906025, 2391705863, 2492770099, 2610673197, 505291324, 2273808917, 3924369609, 3469625735, 1431699370, 673740880, 3755965093, 2358021891, 2711746649, 2307489801, 218961690, 3217021541, 3873845719, 1111672452, 1751693520, 1094828930, 2576986153, 757954394, 252645662, 2964376443, 1414855848, 3149649517, 370555436]
    LIST_6B0 = [4089235720, 1779033703, 2227873595, 3144134277, 4271175723, 1013904242, 1595750129, 2773480762, 2917565137, 1359893119, 725511199, 2600822924, 4215389547, 528734635, 327033209, 1541459225]
    ord_list = [77, 212, 194, 230, 184, 49, 98, 9, 14, 82, 179, 199, 166, 115, 59, 164, 28, 178, 70, 43, 130, 154, 181, 138, 25, 107, 57, 219, 87, 23, 117, 36, 244, 155, 175, 127, 8, 232, 214, 141, 38, 167, 46, 55, 193, 169, 90, 47, 31, 5, 165, 24, 146, 174, 242, 148, 151, 50, 182, 42, 56, 170, 221, 88]
    rodata = [3609767458, 1116352408, 602891725, 1899447441, 3964484399, 3049323471, 2173295548, 3921009573, 4081628472, 961987163, 3053834265, 1508970993, 2937671579, 2453635748, 3664609560, 2870763221, 2734883394, 3624381080, 1164996542, 310598401, 1323610764, 607225278, 3590304994, 1426881987, 4068182383, 1925078388, 991336113, 2162078206, 633803317, 2614888103, 3479774868, 3248222580, 2666613458, 3835390401, 944711139, 4022224774, 2341262773, 264347078, 2007800933, 604807628, 1495990901, 770255983, 1856431235, 1249150122, 3175218132, 1555081692, 2198950837, 1996064986, 3999719339, 2554220882, 766784016, 2821834349, 2566594879, 2952996808, 3203337956, 3210313671, 1034457026, 3336571891, 2466948901, 3584528711, 3758326383, 113926993, 168717936, 338241895, 1188179964, 666307205, 1546045734, 773529912, 1522805485, 1294757372, 2643833823, 1396182291, 2343527390, 1695183700, 1014477480, 1986661051, 1206759142, 2177026350, 344077627, 2456956037, 1290863460, 2730485921, 3158454273, 2820302411, 3505952657, 3259730800, 106217008, 3345764771, 3606008344, 3516065817, 1432725776, 3600352804, 1467031594, 4094571909, 851169720, 275423344, 3100823752, 430227734, 1363258195, 506948616, 3750685593, 659060556, 3785050280, 883997877, 3318307427, 958139571, 3812723403, 1322822218, 2003034995, 1537002063, 3602036899, 1747873779, 1575990012, 1955562222, 1125592928, 2024104815, 2716904306, 2227730452, 442776044, 2361852424, 593698344, 2428436474, 3733110249, 2756734187, 2999351573, 3204031479, 3815920427, 3329325298, 3928383900, 3391569614, 566280711, 3515267271, 3454069534, 3940187606, 4000239992, 4118630271, 1914138554, 116418474, 2731055270, 174292421, 3203993006, 289380356, 320620315, 460393269, 587496836, 685471733, 1086792851, 852142971, 365543100, 1017036298, 2618297676, 1126000580, 3409855158, 1288033470, 4234509866, 1501505948, 987167468, 1607167915, 1246189591, 1816402316]
    list_9C8 = []

    def encrypt(self, data):
        headers = [31, 139, 8, 0, 0, 0, 0, 0, 0, 0]
        data = gzip.compress(bytes(data.encode("latin-1")), compresslevel=9, mtime=0)
        data = list(data)
        self.setData(data)
        for i in range(len(headers)):
            self.__content[i] = headers[i]
        list_0B0 = self.calculate(self.list_9C8) + self.ord_list
        list_5D8 = self.calculate(list_0B0)
        list_378 = []
        list_740 = []
        for i in range(0x10):
            list_378.append(list_5D8[i])
        list_378Array = self.dump_list(list_378)
        for i in range(0x10, 0x20):
            list_740.append(list_5D8[i])
        list_8D8 = self.calculate(self.__content)
        list_AB0 = list_8D8 + self.__content
        list_AB0List = self.convertLongList(list_AB0)
        differ = 0x10 - len(list_AB0) % 0x10
        for i in range(differ):
            list_AB0List.append(differ)
        list_AB0 = list_AB0List
        list_55C = self.hex_CF8(list_378Array)
        final_list = self.hex_0A2(list_AB0, list_740, list_55C)
        final_list = (self.begining + self.list_9C8) + final_list
        final_list = self.changeLongArrayTobytes(final_list)
        return bytes(i % 256 for i in final_list).hex()

    def decrypt(self, data):
        data = bytearray.fromhex(data)
        data = list(data)
        self.setData(data)
        self.__content = self.__content_raw[38:]
        self.list_9C8 = self.__content_raw[6:38]
        self.__content = self.changeByteArrayToLong(self.__content)
        list_0B0 = self.calculate(self.list_9C8) + self.ord_list
        list_5D8 = self.calculate(list_0B0)
        list_378 = []
        list_740 = []
        for i in range(0x10):
            list_378.append(list_5D8[i])
        list_378Array = self.dump_list(list_378)
        for i in range(0x10, 0x20):
            list_740.append(list_5D8[i])
        key_longs = self.hex_list(list_378Array)
        decrypted = self.aes_decrypt(bytes(key_longs), bytes(self.__content))
        decryptedByteArray = ([0] * 16) + list(decrypted)
        toDecompress = decryptedByteArray[64:]
        result = gzip.decompress(bytes(toDecompress))
        return result.decode()

   

    def bytearray_decode(self, arrays):
        out = []
        for d in arrays:
            out.append(chr(d))
        return "".join(out)

    def changeLongArrayTobytes(self, array):
        result = []
        for i in range(len(array)):
            if array[i] > 127:
                result.append(array[i] - 256)
            else:
                result.append(array[i])
        return result

    def hex_0A2(self, content, list_740, list_55C):
        result = []
        l55cl = len(list_55C)
        lens = len(content)
        end = lens // 16
        for i in range(end):
            for j in range(16):
                list_740[j] = list_740[j] ^ content[16 * i + j]
            tmp_list = self.dump_list(list_740)
            R6 = tmp_list[3]
            LR = tmp_list[0]
            R8 = tmp_list[1]
            R12 = tmp_list[2]
            R5 = list_55C[0]
            R4 = list_55C[1]
            R1 = list_55C[2]
            R2 = list_55C[3]
            R11 = 0
            v_334 = 0
            R2 = R2 ^ R6
            v_33C = R2
            R1 = R1 ^ R12
            v_338 = R1
            R4 = R4 ^ R8
            R12 = R5 ^ LR
            for j in range(5):
                R3 = v_33C
                R9 = R4
                R0 = int(self.UBFX(R12, 0x10, 8))
                R1 = R3 >> 0x18
                R1 = self.dword_6[R1]
                R0 = self.dword_7[R0]
                R0 = R0 ^ R1
                R1 = int(self.UBFX(R4, 8, 8))
                R8 = v_338
                R1 = self.dword_8[R1]
                LR = list_55C[8 * j + 6]
                R0 = R0 ^ R1
                R1 = int(self.UTFX(R8))
                R1 = self.dword_9[R1]
                R0 = R0 ^ R1
                R1 = list_55C[8 * j + 4]
                v_334 = R1
                R1 = list_55C[8 * j + 5]
                v_330 = R1
                R1 = list_55C[8 * j + 7]
                R11 = R0 ^ R1
                R1 = int(self.UBFX(R3, 0x10, 8))
                R0 = R8 >> 24
                R0 = self.dword_6[R0]
                R1 = self.dword_7[R1]
                R0 = R0 ^ R1
                R1 = int(self.UBFX(R12, 8, 8))
                R1 = self.dword_8[R1]
                R0 = R0 ^ R1
                R1 = int(self.UTFX(R9))
                R1 = self.dword_9[R1]
                R0 = R0 ^ R1
                R1 = int(self.UBFX(R8, 0x10, 8))
                R6 = R0 ^ LR
                R0 = R9 >> 24
                R0 = self.dword_6[R0]
                R1 = self.dword_7[R1]
                R0 = R0 ^ R1
                R1 = int(self.UBFX(R3, 8, 8))
                R1 = self.dword_8[R1]
                R0 = R0 ^ R1
                R1 = int(self.UTFX(R12))
                R1 = self.dword_9[R1]
                R0 = R0 ^ R1
                R1 = v_330
                LR = R0 ^ R1
                R0 = int(self.UTFX(R3))
                R0 = self.dword_9[R0]
                R4 = R12 >> 24
                R1 = int(self.UBFX(R8, 8, 8))
                R4 = self.dword_6[R4]
                R5 = int(self.UBFX(R9, 16, 8))
                R1 = self.dword_8[R1]
                R5 = self.dword_7[R5]
                R5 = R5 ^ R4
                R1 = R1 ^ R5
                R0 = R0 ^ R1
                R1 = v_334
                R1 = R1 ^ R0
                R0 = R1 >> 0x18
                v_334 = R0
                if j == 4:
                    break
                else:
                    R4 = int(self.UBFX(R1, 16, 8))
                    R5 = R11 >> 24
                    R10 = R6
                    R5 = self.dword_6[R5]
                    R4 = self.dword_7[R4]
                    R5 = R5 ^ R4
                    R4 = int(self.UBFX(LR, 8, 8))
                    R4 = self.dword_8[R4]
                    R5 = R5 ^ R4
                    R4 = int(self.UTFX(R10))
                    R4 = self.dword_9[R4]
                    R5 = R5 ^ R4
                    R4 = list_55C[8 * j + 11]
                    R0 = R5 ^ R4
                    v_33C = R0
                    R4 = int(self.UBFX(R11, 16, 8))
                    R5 = R10 >> 24
                    R5 = self.dword_6[R5]
                    R4 = self.dword_7[R4]
                    R5 = R5 ^ R4
                    R4 = int(self.UBFX(R1, 8, 8))
                    R0 = list_55C[8 * j + 9]
                    R9 = list_55C[8 * j + 8]
                    R1 = int(self.UTFX(R1))
                    R4 = self.dword_8[R4]
                    R1 = self.dword_9[R1]
                    R5 = R5 ^ R4
                    R4 = int(self.UTFX(LR))
                    R4 = self.dword_9[R4]
                    R5 = R5 ^ R4
                    R4 = list_55C[8 * j + 10]
                    R4 = R4 ^ R5
                    v_338 = R4
                    R5 = int(self.UBFX(R10, 16, 8))
                    R4 = LR >> 24
                    R4 = self.dword_6[R4]
                    R5 = self.dword_7[R5]
                    R4 = R4 ^ R5
                    R5 = int(self.UBFX(R11, 8, 8))
                    R5 = self.dword_8[R5]
                    R4 = R4 ^ R5
                    R1 = R1 ^ R4
                    R4 = R1 ^ R0
                    R0 = v_334
                    R1 = int(self.UBFX(LR, 16, 8))
                    R5 = int(self.UBFX(R10, 8, 8))
                    R0 = self.dword_6[R0]
                    R1 = self.dword_7[R1]
                    R5 = self.dword_8[R5]
                    R0 = R0 ^ R1
                    R1 = int(self.UTFX(R11))
                    R1 = self.dword_9[R1]
                    R0 = R0 ^ R5
                    R0 = R0 ^ R1
                    R12 = R0 ^ R9
            R2 = R11 >> 24
            R3 = int(self.UBFX(R1, 16, 8))
            R10 = R6
            R0 = R10 >> 24
            R2 = self.dword_0[R2]
            R2 = int(self.parseLong(self.toHex(R2) + "000000", 10, 16))
            R9 = R10
            R3 = self.dword_0[R3]
            R3 = int(self.parseLong(self.toHex(R3) + "0000", 10, 16))
            R0 = self.dword_0[R0]
            R0 = int(self.parseLong(self.toHex(R0) + "000000", 10, 16))
            R2 = R2 ^ R3
            v_350 = R2
            R2 = int(self.UBFX(R11, 0x10, 8))
            R2 = self.dword_0[R2]
            R2 = int(self.parseLong(self.toHex(R2) + "0000", 10, 16))
            R0 = R0 ^ R2
            R2 = int(self.UBFX(R1, 8, 8))
            R1 = int(self.UTFX(R1))
            R2 = self.dword_0[R2]
            R2 = int(self.parseLong(self.toHex(R2) + "00", 10, 16))
            R1 = self.dword_0[R1]
            R0 = R0 ^ R2
            R2 = int(self.UTFX(LR))
            R2 = self.dword_0[R2]
            R12 = R0 ^ R2
            R0 = list_55C[l55cl - 2]
            R10 = list_55C[l55cl - 3]
            R12 = R12 ^ R0
            R2 = list_55C[l55cl - 1]
            R0 = LR >> 24
            v_34C = R2
            R2 = int(self.UBFX(R9, 0x10, 8))
            R0 = self.dword_0[R0]
            R0 = int(self.parseLong(self.toHex(R0) + "000000", 10, 16))
            R2 = self.dword_0[R2]
            R2 = int(self.parseLong(self.toHex(R2) + "0000", 10, 16))
            R0 = R0 ^ R2
            R2 = int(self.UBFX(R11, 8, 8))
            R2 = self.dword_0[R2]
            R2 = int(self.parseLong(self.toHex(R2) + "00", 10, 16))
            R0 = R0 ^ R2
            R0 = R0 ^ R1
            R1 = R0 ^ R10
            R0 = v_334
            R2 = int(self.UBFX(LR, 0x10, 8))
            R0 = self.dword_0[R0]
            R0 = int(self.parseLong(self.toHex(R0) + "000000", 10, 16))
            R2 = self.dword_0[R2]
            R2 = int(self.parseLong(self.toHex(R2) + "0000", 10, 16))
            R0 = R0 ^ R2
            R2 = int(self.UBFX(R9, 8, 8))
            R2 = self.dword_0[R2]
            R2 = int(self.parseLong(self.toHex(R2) + "00", 10, 16))
            R0 = R0 ^ R2
            R2 = int(self.UTFX(R11))
            R2 = self.dword_0[R2]
            R0 = R0 ^ R2
            R2 = int(self.UTFX(R9))
            R2 = self.dword_0[R2]
            R3 = int(self.UBFX(LR, 8, 8))
            R3 = self.dword_0[R3]
            R3 = int(self.parseLong(self.toHex(R3) + "00", 10, 16))
            R5 = v_350
            R6 = list_55C[l55cl - 4]
            R3 = R3 ^ R5
            R2 = R2 ^ R3
            R3 = v_34C
            R0 = R0 ^ R6
            R2 = R2 ^ R3
            list_740 = self.hex_list([R0, R1, R12, R2])
            result = result + list_740
        return result

    def calculate(self, content):
        hex_6A8 = 0
        tmp_list = []
        length = len(content)
        list_6B0 = self.LIST_6B0.copy()
        for item in content:
            tmp_list.append(item)

        divisible = length % 0x80
        tmp = 0x80 - divisible
        if tmp > 0x11:
            tmp_list.append(0x80)
            for i in range(tmp - 0x11):
                tmp_list.append(0)
            for j in range(16):
                tmp_list.append(0)
        else:
            tmp_list.append(128)
            for i in range(128 - 16 + tmp + 1):
                tmp_list.append(0)
            for j in range(16):
                tmp_list.append(0)
        tmp_list_size = len(tmp_list)
        d = tmp_list_size // 0x80
        for i in range(tmp_list_size // 0x80):
            if (tmp_list_size // 128 - 1) == i:
                ending = self.handle_ending(hex_6A8, divisible)
                for j in range(8):
                    index = tmp_list_size - j - 1
                    tmp_list[index] = ending[7 - j]
            param_list = []
            for j in range(32):
                tmpss = ""
                for k in range(4):
                    tmp_string = self.toHex(tmp_list[0x80 * i + 4 * j + k])
                    if len(tmp_string) < 2:
                        tmp_string = "0" + tmp_string
                    tmpss = tmpss + tmp_string
                param_list.append(int(self.parseLong(tmpss, 10, 16)))
            list_3B8 = self.hex_27E(param_list)
            list_6B0 = self.hex_30A(list_6B0, list_3B8)
            hex_6A8 += 0x400
        list_8D8 = self.hex_C52(list_6B0)
        return list_8D8

    def convertLongList(self, content):
        if len(content) == 0:
            return []
        result = []
        for i in content:
            result.append(i)
        return result

    def dump_list(self, content):
        size = len(content)
        ssize = size // 4
        result = []
        for index in range(ssize):
            tmp_string = ""
            for j in range(4):
                tmp = self.toHex(content[4 * index + j])
                if len(tmp) < 2:
                    tmp = "0" + tmp

                tmp_string = tmp_string + tmp
            i = int(self.parseLong(tmp_string, 10, 16))
            result.append(int(i))
        return result

    def hex_CF8(self, param_list):
        list_388 = []
        list_378 = param_list
        for i in range(0xA):
            R3 = list_378[0]
            R8 = list_378[1]
            R9 = list_378[2]
            R5 = list_378[3]
            R6 = int(self.UBFX(R5, 8, 8))
            R6 = self.dword_0[R6]
            R6 = int(self.parseLong(self.toHex(R6) + "0000", 10, 16))
            R4 = int(self.UBFX(R5, 0x10, 8))
            R11 = self.dword_1[i]
            R4 = self.dword_0[R4]
            R4 = int(self.parseLong(self.toHex(R4) + "000000", 10, 16))
            R3 = R3 ^ R4
            R4 = int(self.UTFX(R5))
            R3 = R3 ^ R6
            R4 = self.dword_0[R4]
            R4 = int(self.parseLong(self.toHex(R4) + "00", 10, 16))
            R3 = R3 ^ R4
            R4 = R5 >> 24
            R4 = self.dword_0[R4]
            R3 = R3 ^ R4
            R3 = R3 ^ R11
            R2 = R8 ^ R3
            R4 = R9 ^ R2
            R5 = R5 ^ R4
            list_378 = [R3, R2, R4, R5]
            list_388 = list_388 + list_378
        l388l = len(list_388)
        list_478 = []
        for i in range(0x9):
            R5 = list_388[l388l - 8 - 4 * i]
            R4 = int(self.UBFX(R5, 0x10, 8))
            R6 = R5 >> 0x18
            R6 = self.dword_2[R6]
            R4 = self.dword_3[R4]
            R6 = R6 ^ R4
            R4 = int(self.UBFX(R5, 8, 8))
            R5 = int(self.UTFX(R5))
            R4 = self.dword_4[R4]
            R5 = self.dword_5[R5]
            R6 = R6 ^ R4
            R6 = R6 ^ R5
            list_478.append(R6)
            R6 = list_388[l388l - 7 - 4 * i]
            R1 = int(self.UBFX(R6, 0x10, 8))
            R4 = R6 >> 0x18
            R4 = self.dword_2[R4]
            R1 = self.dword_3[R1]
            R1 = R1 ^ R4
            R4 = int(self.UBFX(R6, 8, 8))
            R4 = self.dword_4[R4]
            R1 = R1 ^ R4
            R4 = int(self.UTFX(R6))
            R4 = self.dword_5[R4]
            R1 = R1 ^ R4
            list_478.append(R1)
            R1 = list_388[l388l - 6 - 4 * i]
            R6 = int(self.UBFX(R1, 0x10, 8))
            R4 = R1 >> 0x18
            R4 = self.dword_2[R4]
            R6 = self.dword_3[R6]
            R4 = R4 ^ R6
            R6 = int(self.UBFX(R1, 8, 8))
            R1 = int(self.UTFX(R1))
            R6 = self.dword_4[R6]
            R1 = self.dword_5[R1]
            R4 = R4 ^ R6
            R1 = R1 ^ R4
            list_478.append(R1)
            R0 = list_388[l388l - 5 - 4 * i]
            R1 = int(self.UTFX(R0))
            R4 = int(self.UBFX(R0, 8, 8))
            R6 = R0 >> 0x18
            R0 = int(self.UBFX(R0, 0x10, 8))
            R6 = self.dword_2[R6]
            R0 = self.dword_3[R0]
            R4 = self.dword_4[R4]
            R1 = self.dword_5[R1]
            R0 = R0 ^ R6
            R0 = R0 ^ R4
            R0 = R0 ^ R1
            list_478.append(R0)
        list_468 = param_list + list_388
        return list_468

    def handle_ending(self, num, r0):
        s = self.toHex(num)
        r1 = None
        r2 = None
        if len(s) <= 8:
            r1 = num
            r2 = 0
        else:
            num_str = self.toHex(num)
            length = len(num)
            r1 = self.parseLong(num_str[: length - 8], 10, 16)
            r2 = self.parseLong(num_str[2 : length - 8], 10, 16)
        r1 = self.ADDS(r1, r0 << 3)
        r2 = self.ADC(r2, r0 >> 29)
        a = self.hex_list([r2, r1])
        return self.hex_list([r2, r1])

    def UTFX(self, num):
        tmp_string = self.toBinaryString(num)
        start = len(tmp_string) - 8
        return self.parseLong(tmp_string[start:], 10, 2)

    def hex_27E(self, param_list):
        r6 = param_list[0]
        r8 = param_list[1]
        for i in range(0x40):
            r0 = param_list[2 * i + 0x1C]
            r5 = param_list[2 * i + 0x1D]
            r4 = self.LSRS(r0, 0x13)
            r3 = self.LSRS(r0, 0x1D)
            lr = r4 | self.check(r5) << 13
            r4 = self.LSLS(r0, 3)
            r4 = r4 | self.check(r5) >> 29
            r3 = r3 | self.check(r5) << 3
            r4 = r4 ^ self.check(r0) >> 6
            lr = lr ^ r4
            r4 = self.LSRS(r5, 6)
            r4 = r4 | self.check(r0) << 26
            r9 = r3 ^ r4
            r4 = self.LSRS(r5, 0x13)
            r0 = r4 | self.check(r0) << 13
            r10 = param_list[2 * i + 0x12]
            r3 = param_list[2 * i + 0x13]
            r5 = param_list[2 * i + 0x2]
            r4 = param_list[2 * i + 0x3]
            r0 = r0 ^ r9
            r3 = self.ADDS(r3, r8)
            r6 = self.ADC(r6, r10)
            r8 = self.ADDS(r3, r0)
            lr = self.ADC(lr, r6)
            r6 = self.LSRS(r4, 7)
            r3 = self.LSRS(r4, 8)
            r6 = r6 | self.check(r5) << 25
            r3 = r3 | self.check(r5) << 24
            r3 = int(self.EORS(r3, r6))
            r6 = self.LSRS(r5, 1)
            r0 = int(self.RRX(r4))
            r0 = int(self.EORS(r0, r3))
            r3 = r6 | self.check(r4) << 31
            r6 = self.LSRS(r5, 8)
            r0 = int(self.ADDS(r0, r8))
            r6 = r6 | self.check(r4) << 24
            r8 = r4
            r6 = r6 ^ self.check(r5) >> 7
            r3 = r3 ^ r6
            r6 = r5
            r3 = self.ADC(r3, lr)
            param_list = param_list + [r3, r0]
        return param_list

    def hex_30A(self, param_list, list_3B8):
        v_3A0 = param_list[7]
        v_3A4 = param_list[6]
        v_374 = param_list[5]
        v_378 = param_list[4]
        LR = param_list[0]
        R12 = param_list[1]
        v_39C = param_list[2]
        v_398 = param_list[3]
        v_3AC = param_list[11]
        v_3A8 = param_list[10]
        R9 = param_list[12]
        R10 = param_list[13]
        R5 = param_list[9]
        R8 = param_list[8]
        R4 = param_list[15]
        R6 = param_list[14]
        for index in range(10):
            v_384 = R5
            R3 = self.rodata[0x10 * index]
            R1 = self.rodata[0x10 * index + 2]
            R2 = self.rodata[0x10 * index + 1]
            R3 = self.ADDS(R3, R6)
            R6 = self.check(R8) >> 14
            v_390 = R1
            R6 = R6 | self.check(R5) << 18
            R1 = self.rodata[0x10 * index + 3]
            R0 = self.rodata[0x10 * index + 4]
            v_36C = R0
            R0 = self.ADC(R2, R4)
            R2 = self.LSRS(R5, 0x12)
            R4 = self.LSRS(R5, 0xE)
            R2 = R2 | self.check(R8) << 14
            R4 = R4 | self.check(R8) << 18
            R2 = self.EORS(R2, R4)
            R4 = self.LSLS(R5, 0x17)
            R4 = R4 | self.check(R8) >> 9
            v_38C = R1
            R2 = self.EORS(R2, R4)
            R4 = self.check(R8) >> 18
            R4 = R4 | self.check(R5) << 14
            R6 = self.EORS(R6, R4)
            R4 = self.LSRS(R5, 9)
            R4 = R4 | self.check(R8) << 23
            v_354 = R8
            R6 = self.EORS(R6, R4)
            R3 = self.ADDS(R3, R6)
            R0 = self.ADCS(R0, R2)
            R2 = list_3B8[0x10 * index + 1]
            R2 = self.ADDS(R2, R3)
            R3 = list_3B8[0x10 * index + 3]
            R6 = list_3B8[0x10 * index]
            v_358 = R10
            R6 = self.ADCS(R6, R0)
            R0 = v_3AC
            v_360 = R3
            R0 = R0 ^ R10
            R3 = list_3B8[0x10 * index + 2]
            R0 = self.ANDS(R0, R5)
            R1 = list_3B8[0x10 * index + 5]
            R4 = R0 ^ R10
            R0 = v_3A8
            v_364 = R1
            R0 = R0 ^ R9
            R1 = v_374
            R0 = R0 & R8
            R8 = v_39C
            R0 = R0 ^ R9
            v_35C = R3
            R10 = self.ADDS(R2, R0)
            R0 = v_398
            R11 = self.ADC(R6, R4)
            R3 = v_378
            R2 = R0 | R12
            R6 = R0 & R12
            R2 = self.ANDS(R2, R1)
            R1 = R0
            R2 = self.ORRS(R2, R6)
            R6 = R8 | LR
            R6 = self.ANDS(R6, R3)
            R3 = R8 & LR
            R3 = self.ORRS(R3, R6)
            R6 = self.check(R12) << 30
            R0 = self.check(R12) >> 28
            R6 = R6 | self.check(LR) >> 2
            R0 = R0 | self.check(LR) << 4
            R4 = self.check(LR) >> 28
            R0 = self.EORS(R0, R6)
            R6 = self.check(R12) << 25
            R6 = R6 | self.check(LR) >> 7
            R4 = R4 | self.check(R12) << 4
            R0 = self.EORS(R0, R6)
            R6 = self.check(R12) >> 2
            R6 = R6 | self.check(LR) << 30
            R3 = self.ADDS(R3, R10)
            R6 = R6 ^ R4
            R4 = self.check(R12) >> 7
            R4 = R4 | self.check(LR) << 25
            R2 = self.ADC(R2, R11)
            R6 = self.EORS(R6, R4)
            v_37C = R12
            R5 = self.ADDS(R3, R6)
            R6 = self.ADC(R2, R0)
            R0 = R6 | R12
            R2 = R6 & R12
            R0 = self.ANDS(R0, R1)
            R3 = self.LSRS(R6, 0x1C)
            R0 = self.ORRS(R0, R2)
            R2 = self.LSLS(R6, 0x1E)
            R2 = R2 | self.check(R5) >> 2
            R3 = R3 | self.check(R5) << 4
            R2 = self.EORS(R2, R3)
            R3 = self.LSLS(R6, 0x19)
            R3 = R3 | self.check(R5) >> 7
            R4 = self.LSRS(R5, 0x1C)
            R3 = self.EORS(R3, R2)
            R2 = self.LSRS(R6, 2)
            R2 = R2 | self.check(R5) << 30
            R4 = R4 | self.check(R6) << 4
            R2 = self.EORS(R2, R4)
            R4 = self.LSRS(R6, 7)
            R4 = R4 | self.check(R5) << 25
            R12 = R6
            R2 = self.EORS(R2, R4)
            R4 = R5 | LR
            R4 = R4 & R8
            R6 = R5 & LR
            R4 = self.ORRS(R4, R6)
            v_388 = R5
            R5 = self.ADDS(R2, R4)
            R0 = self.ADCS(R0, R3)
            v_398 = R1
            R4 = R9
            v_350 = R0
            R0 = v_3A4
            R1 = v_3A0
            v_380 = LR
            LR = self.ADDS(R0, R10)
            R9 = self.ADC(R1, R11)
            R0 = v_3AC
            R6 = self.check(LR) >> 14
            R1 = v_384
            R3 = self.check(R9) >> 18
            R2 = self.check(R9) >> 14
            R3 = R3 | self.check(LR) << 14
            R2 = R2 | self.check(LR) << 18
            R2 = self.EORS(R2, R3)
            R3 = self.check(R9) << 23
            R3 = R3 | self.check(LR) >> 9
            R6 = R6 | self.check(R9) << 18
            R2 = self.EORS(R2, R3)
            R3 = self.check(LR) >> 18
            R3 = R3 | self.check(R9) << 14
            v_39C = R8
            R3 = self.EORS(R3, R6)
            R6 = self.check(R9) >> 9
            R6 = R6 | self.check(LR) << 23
            R8 = v_354
            R3 = self.EORS(R3, R6)
            R6 = R0 ^ R1
            R6 = R6 & R9
            v_370 = R12
            R6 = self.EORS(R6, R0)
            R0 = v_3A8
            R1 = R0 ^ R8
            R1 = R1 & LR
            R1 = self.EORS(R1, R0)
            R0 = v_358
            R1 = self.ADDS(R1, R4)
            R6 = self.ADCS(R6, R0)
            R0 = v_390
            R1 = self.ADDS(R1, R0)
            R0 = v_38C
            R6 = self.ADCS(R6, R0)
            R0 = v_360
            R1 = self.ADDS(R1, R0)
            R0 = v_35C
            R6 = self.ADCS(R6, R0)
            R1 = self.ADDS(R1, R3)
            R3 = self.ADC(R6, R2)
            R2 = v_350
            R0 = self.ADDS(R5, R1)
            R5 = v_37C
            R4 = self.ADC(R2, R3)
            v_390 = R4
            R2 = R4 | R12
            R6 = R4 & R12
            R2 = self.ANDS(R2, R5)
            R5 = self.LSRS(R4, 0x1C)
            R10 = R2 | R6
            R2 = self.LSLS(R4, 0x1E)
            R2 = R2 | self.check(R0) >> 2
            R5 = R5 | self.check(R0) << 4
            R2 = self.EORS(R2, R5)
            R5 = self.LSLS(R4, 0x19)
            R5 = R5 | self.check(R0) >> 7
            R6 = self.LSRS(R0, 0x1C)
            R12 = R2 ^ R5
            R2 = self.LSRS(R4, 2)
            R2 = R2 | self.check(R0) << 30
            R6 = R6 | self.check(R4) << 4
            R2 = self.EORS(R2, R6)
            R6 = self.LSRS(R4, 7)
            R4 = v_388
            R6 = R6 | self.check(R0) << 25
            R5 = v_380
            R2 = self.EORS(R2, R6)
            R6 = R0 | R4
            R4 = self.ANDS(R4, R0)
            R6 = self.ANDS(R6, R5)
            v_38C = R0
            R4 = self.ORRS(R4, R6)
            R6 = LR ^ R8
            R0 = self.ADDS(R2, R4)
            v_3A4 = R0
            R0 = self.ADC(R12, R10)
            v_3A0 = R0
            R0 = v_378
            R10 = self.ADDS(R1, R0)
            R0 = v_374
            R6 = R6 & R10
            R1 = self.ADC(R3, R0)
            R5 = self.check(R10) >> 14
            R0 = v_384
            R6 = R6 ^ R8
            R3 = self.LSRS(R1, 0x12)
            R4 = self.LSRS(R1, 0xE)
            R3 = R3 | self.check(R10) << 14
            R4 = R4 | self.check(R10) << 18
            R3 = self.EORS(R3, R4)
            R4 = self.LSLS(R1, 0x17)
            R4 = R4 | self.check(R10) >> 9
            R5 = R5 | self.check(R1) << 18
            R11 = R3 ^ R4
            R3 = self.check(R10) >> 18
            R3 = R3 | self.check(R1) << 14
            v_378 = R1
            R3 = self.EORS(R3, R5)
            R5 = self.LSRS(R1, 9)
            R5 = R5 | self.check(R10) << 23
            R3 = self.EORS(R3, R5)
            R5 = R9 ^ R0
            R5 = self.ANDS(R5, R1)
            R1 = v_3A8
            R5 = self.EORS(R5, R0)
            R0 = v_36C
            R4 = self.ADDS(R0, R1)
            R2 = self.rodata[0x10 * index + 5]
            R0 = v_3AC
            R2 = self.ADCS(R2, R0)
            R0 = v_364
            R4 = self.ADDS(R4, R0)
            R12 = list_3B8[0x10 * index + 4]
            R0 = v_3A4
            R2 = self.ADC(R2, R12)
            R6 = self.ADDS(R6, R4)
            R2 = self.ADCS(R2, R5)
            R3 = self.ADDS(R3, R6)
            R11 = self.ADC(R11, R2)
            R1 = self.ADDS(R0, R3)
            R0 = v_3A0
            R6 = v_390
            R4 = self.check(R1) >> 28
            R0 = self.ADC(R0, R11)
            R5 = v_370
            R2 = R0 | R6
            R6 = self.ANDS(R6, R0)
            R2 = self.ANDS(R2, R5)
            R5 = self.LSRS(R0, 0x1C)
            R12 = R2 | R6
            R6 = self.LSLS(R0, 0x1E)
            R6 = R6 | self.check(R1) >> 2
            R5 = R5 | self.check(R1) << 4
            R6 = self.EORS(R6, R5)
            R5 = self.LSLS(R0, 0x19)
            R5 = R5 | self.check(R1) >> 7
            R4 = R4 | self.check(R0) << 4
            R6 = self.EORS(R6, R5)
            R5 = self.LSRS(R0, 2)
            R5 = R5 | self.check(R1) << 30
            v_3AC = R0
            R5 = self.EORS(R5, R4)
            R4 = self.LSRS(R0, 7)
            R0 = v_38C
            R4 = R4 | self.check(R1) << 25
            R2 = v_388
            R5 = self.EORS(R5, R4)
            R4 = R1 | R0
            v_3A8 = R1
            R4 = self.ANDS(R4, R2)
            R2 = R1 & R0
            R2 = self.ORRS(R2, R4)
            R0 = self.ADDS(R5, R2)
            v_3A4 = R0
            R0 = self.ADC(R6, R12)
            v_3A0 = R0
            R0 = v_39C
            R2 = v_398
            R0 = self.ADDS(R0, R3)
            v_39C = R0
            R11 = self.ADC(R11, R2)
            R4 = self.LSRS(R0, 0xE)
            R3 = self.check(R11) >> 18
            R6 = self.check(R11) >> 14
            R3 = R3 | self.check(R0) << 14
            R6 = R6 | self.check(R0) << 18
            R3 = self.EORS(R3, R6)
            R6 = self.check(R11) << 23
            R6 = R6 | self.check(R0) >> 9
            R4 = R4 | self.check(R11) << 18
            R1 = self.EORS(R3, R6)
            R6 = self.LSRS(R0, 0x12)
            R6 = R6 | self.check(R11) << 14
            R3 = R10 ^ LR
            R6 = self.EORS(R6, R4)
            R4 = self.check(R11) >> 9
            R3 = self.ANDS(R3, R0)
            R4 = R4 | self.check(R0) << 23
            R5 = R6 ^ R4
            v_398 = R1
            R3 = R3 ^ LR
            R1 = v_378
            R6 = self.rodata[0x10 * index + 6]
            R12 = self.rodata[0x10 * index + 7]
            R4 = R1 ^ R9
            R0 = v_384
            R6 = self.ADDS(R6, R8)
            R4 = R4 & R11
            R12 = self.ADC(R12, R0)
            R4 = R4 ^ R9
            R8 = list_3B8[0x10 * index + 7]
            R2 = list_3B8[0x10 * index + 6]
            R6 = self.ADDS(R6, R8)
            R0 = v_398
            R2 = self.ADC(R2, R12)
            R3 = self.ADDS(R3, R6)
            R2 = self.ADCS(R2, R4)
            R6 = self.ADDS(R3, R5)
            R12 = self.ADC(R2, R0)
            R0 = v_3A4
            R4 = v_390
            R1 = self.ADDS(R0, R6)
            R0 = v_3A0
            v_384 = R1
            R5 = self.ADC(R0, R12)
            R0 = v_3AC
            R8 = self.check(R1) >> 28
            R2 = R5 | R0
            R3 = R8 | self.check(R5) << 4
            R2 = self.ANDS(R2, R4)
            R4 = R5 & R0
            R0 = R2 | R4
            R4 = self.LSLS(R5, 0x1E)
            R2 = self.LSRS(R5, 0x1C)
            R4 = R4 | self.check(R1) >> 2
            R2 = R2 | self.check(R1) << 4
            v_3A0 = R0
            R2 = self.EORS(R2, R4)
            R4 = self.LSLS(R5, 0x19)
            R4 = R4 | self.check(R1) >> 7
            R0 = v_3A8
            R2 = self.EORS(R2, R4)
            R4 = self.LSRS(R5, 2)
            R4 = R4 | self.check(R1) << 30
            R8 = R5
            R3 = self.EORS(R3, R4)
            R4 = self.LSRS(R5, 7)
            R4 = R4 | self.check(R1) << 25
            R5 = v_38C
            R3 = self.EORS(R3, R4)
            R4 = R1 | R0
            R4 = self.ANDS(R4, R5)
            R5 = R1 & R0
            R4 = self.ORRS(R4, R5)
            v_36C = R8
            R0 = self.ADDS(R3, R4)
            v_3A4 = R0
            R0 = v_3A0
            R0 = self.ADCS(R0, R2)
            v_3A0 = R0
            R0 = v_380
            R2 = v_37C
            R0 = self.ADDS(R0, R6)
            R5 = self.ADC(R12, R2)
            v_37C = R5
            R4 = self.LSRS(R0, 0xE)
            v_380 = R0
            R2 = self.LSRS(R5, 0x12)
            R3 = self.LSRS(R5, 0xE)
            R2 = R2 | self.check(R0) << 14
            R3 = R3 | self.check(R0) << 18
            R2 = self.EORS(R2, R3)
            R3 = self.LSLS(R5, 0x17)
            R3 = R3 | self.check(R0) >> 9
            R4 = R4 | self.check(R5) << 18
            R1 = R2 ^ R3
            R3 = self.LSRS(R0, 0x12)
            R3 = R3 | self.check(R5) << 14
            v_398 = R1
            R3 = self.EORS(R3, R4)
            R4 = self.LSRS(R5, 9)
            R1 = v_378
            R4 = R4 | self.check(R0) << 23
            R12 = R3 ^ R4
            R3 = list_3B8[0x10 * index + 9]
            R4 = R11 ^ R1
            R4 = self.ANDS(R4, R5)
            R4 = self.EORS(R4, R1)
            R1 = v_39C
            R5 = R1 ^ R10
            R5 = self.ANDS(R5, R0)
            R5 = R5 ^ R10
            R2 = self.rodata[0x10 * index + 8]
            R0 = self.ADDS(R2, LR)
            R2 = self.rodata[0x10 * index + 9]
            R2 = self.ADC(R2, R9)
            R0 = self.ADDS(R0, R3)
            R3 = list_3B8[0x10 * index + 8]
            R2 = self.ADCS(R2, R3)
            R0 = self.ADDS(R0, R5)
            R2 = self.ADCS(R2, R4)
            R1 = self.ADDS(R0, R12)
            R0 = v_398
            R3 = v_3AC
            R4 = self.ADC(R2, R0)
            R0 = v_3A4
            R6 = self.ADDS(R0, R1)
            R0 = v_3A0
            v_3A4 = R6
            R0 = self.ADCS(R0, R4)
            v_3A0 = R0
            R2 = R0 | R8
            R2 = self.ANDS(R2, R3)
            R3 = R0 & R8
            LR = R2 | R3
            R8 = R6
            R3 = self.LSLS(R0, 0x1E)
            R5 = self.LSRS(R0, 0x1C)
            R3 = R3 | self.check(R8) >> 2
            R5 = R5 | self.check(R8) << 4
            R3 = self.EORS(R3, R5)
            R5 = self.LSLS(R0, 0x19)
            R5 = R5 | self.check(R8) >> 7
            R2 = self.check(R8) >> 28
            R12 = R3 ^ R5
            R5 = self.LSRS(R0, 2)
            R5 = R5 | self.check(R8) << 30
            R2 = R2 | self.check(R0) << 4
            R2 = self.EORS(R2, R5)
            R5 = self.LSRS(R0, 7)
            R3 = v_384
            R5 = R5 | self.check(R8) << 25
            R6 = v_3A8
            R2 = self.EORS(R2, R5)
            R5 = R8 | R3
            R5 = self.ANDS(R5, R6)
            R6 = R8 & R3
            R5 = self.ORRS(R5, R6)
            R0 = self.ADDS(R2, R5)
            v_398 = R0
            R2 = v_388
            R12 = self.ADC(R12, LR)
            R0 = v_370
            R3 = self.ADDS(R1, R2)
            R1 = v_380
            R8 = self.ADC(R4, R0)
            R0 = R3
            R2 = self.check(R8) >> 18
            R3 = self.check(R8) >> 14
            R2 = R2 | self.check(R0) << 14
            R3 = R3 | self.check(R0) << 18
            R2 = self.EORS(R2, R3)
            R3 = self.check(R8) << 23
            R3 = R3 | self.check(R0) >> 9
            R4 = self.LSRS(R0, 0xE)
            LR = R2 ^ R3
            R3 = self.LSRS(R0, 0x12)
            R3 = R3 | self.check(R8) << 14
            R4 = R4 | self.check(R8) << 18
            R3 = self.EORS(R3, R4)
            R4 = self.check(R8) >> 9
            R4 = R4 | self.check(R0) << 23
            R2 = R0
            R0 = v_37C
            R3 = self.EORS(R3, R4)
            v_388 = R2
            R4 = R0 ^ R11
            R0 = v_39C
            R4 = R4 & R8
            R5 = R1 ^ R0
            R4 = R4 ^ R11
            R5 = self.ANDS(R5, R2)
            R5 = self.EORS(R5, R0)
            R6 = self.rodata[0x10 * index + 10]
            R1 = self.ADDS(R6, R10)
            R6 = self.rodata[0x10 * index + 11]
            R0 = v_378
            R6 = self.ADCS(R6, R0)
            R2 = list_3B8[0x10 * index + 11]
            R1 = self.ADDS(R1, R2)
            R2 = list_3B8[0x10 * index + 10]
            R0 = v_398
            R2 = self.ADCS(R2, R6)
            R1 = self.ADDS(R1, R5)
            R2 = self.ADCS(R2, R4)
            R1 = self.ADDS(R1, R3)
            R4 = self.ADC(R2, LR)
            R6 = v_3A0
            R0 = self.ADDS(R0, R1)
            R9 = self.ADC(R12, R4)
            R3 = v_36C
            R2 = R9 | R6
            R5 = self.check(R9) >> 28
            v_374 = R9
            R2 = self.ANDS(R2, R3)
            R3 = R9 & R6
            R10 = R2 | R3
            R3 = self.check(R9) << 30
            R3 = R3 | self.check(R0) >> 2
            R5 = R5 | self.check(R0) << 4
            R3 = self.EORS(R3, R5)
            R5 = self.check(R9) << 25
            R5 = R5 | self.check(R0) >> 7
            R6 = self.LSRS(R0, 0x1C)
            R12 = R3 ^ R5
            R5 = self.check(R9) >> 2
            R5 = R5 | self.check(R0) << 30
            R6 = R6 | self.check(R9) << 4
            R5 = self.EORS(R5, R6)
            R6 = self.check(R9) >> 7
            R3 = v_3A4
            R6 = R6 | self.check(R0) << 25
            R2 = v_384
            R5 = self.EORS(R5, R6)
            R6 = R0 | R3
            R6 = self.ANDS(R6, R2)
            R2 = R0 & R3
            R2 = R2 | R6
            R2 = self.ADDS(R2, R5)
            v_398 = R2
            R2 = self.ADC(R12, R10)
            v_378 = R2
            R2 = v_38C
            R12 = self.ADDS(R1, R2)
            R1 = v_390
            LR = self.ADC(R4, R1)
            R4 = self.check(R12) >> 14
            R1 = self.check(LR) >> 18
            R2 = self.check(LR) >> 14
            R1 = R1 | self.check(R12) << 14
            R2 = R2 | self.check(R12) << 18
            R1 = self.EORS(R1, R2)
            R2 = self.check(LR) << 23
            R2 = R2 | self.check(R12) >> 9
            R4 = R4 | self.check(LR) << 18
            R1 = self.EORS(R1, R2)
            R2 = self.check(R12) >> 18
            R2 = R2 | self.check(LR) << 14
            v_390 = R1
            R2 = self.EORS(R2, R4)
            R4 = self.check(LR) >> 9
            R1 = v_37C
            R4 = R4 | self.check(R12) << 23
            R10 = R2 ^ R4
            R2 = v_388
            R4 = R8 ^ R1
            R4 = R4 & LR
            R4 = self.EORS(R4, R1)
            R1 = v_380
            R5 = R2 ^ R1
            R2 = v_39C
            R5 = R5 & R12
            R5 = self.EORS(R5, R1)
            R6 = self.rodata[0x10 * index + 12]
            R3 = self.rodata[0x10 * index + 13]
            R6 = self.ADDS(R6, R2)
            R3 = self.ADC(R3, R11)
            R1 = list_3B8[0x10 * index + 13]
            R1 = self.ADDS(R1, R6)
            R6 = list_3B8[0x10 * index + 12]
            R3 = self.ADCS(R3, R6)
            R1 = self.ADDS(R1, R5)
            R3 = self.ADCS(R3, R4)
            R5 = self.ADDS(R1, R10)
            R1 = v_390
            R2 = self.ADC(R3, R1)
            R1 = v_398
            R3 = v_3A0
            R10 = self.ADDS(R1, R5)
            R1 = v_378
            v_378 = R0
            R11 = self.ADC(R1, R2)
            R6 = self.check(R10) >> 28
            R1 = R11 | R9
            v_398 = R11
            R1 = self.ANDS(R1, R3)
            R3 = R11 & R9
            R9 = R1 | R3
            R3 = self.check(R11) << 30
            R4 = self.check(R11) >> 28
            R3 = R3 | self.check(R10) >> 2
            R4 = R4 | self.check(R10) << 4
            R6 = R6 | self.check(R11) << 4
            R3 = self.EORS(R3, R4)
            R4 = self.check(R11) << 25
            R4 = R4 | self.check(R10) >> 7
            R1 = v_3A4
            R3 = self.EORS(R3, R4)
            R4 = self.check(R11) >> 2
            R4 = R4 | self.check(R10) << 30
            v_39C = R10
            R4 = self.EORS(R4, R6)
            R6 = self.check(R11) >> 7
            R6 = R6 | self.check(R10) << 25
            R4 = self.EORS(R4, R6)
            R6 = R10 | R0
            R6 = self.ANDS(R6, R1)
            R1 = R10 & R0
            R1 = self.ORRS(R1, R6)
            R10 = LR
            R0 = self.ADDS(R4, R1)
            v_390 = R0
            R0 = self.ADC(R3, R9)
            v_38C = R0
            R0 = v_3A8
            R9 = R12
            R4 = self.ADDS(R5, R0)
            R0 = v_3AC
            v_3A8 = R4
            R0 = self.ADCS(R0, R2)
            R3 = self.LSRS(R4, 0xE)
            v_3AC = R0
            R1 = self.LSRS(R0, 0x12)
            R2 = self.LSRS(R0, 0xE)
            R1 = R1 | self.check(R4) << 14
            R2 = R2 | self.check(R4) << 18
            R1 = self.EORS(R1, R2)
            R2 = self.LSLS(R0, 0x17)
            R2 = R2 | self.check(R4) >> 9
            R3 = R3 | self.check(R0) << 18
            R11 = R1 ^ R2
            R2 = self.LSRS(R4, 0x12)
            R2 = R2 | self.check(R0) << 14
            R2 = self.EORS(R2, R3)
            R3 = self.LSRS(R0, 9)
            R3 = R3 | self.check(R4) << 23
            R2 = self.EORS(R2, R3)
            R3 = LR ^ R8
            R3 = self.ANDS(R3, R0)
            R0 = v_388
            LR = R3 ^ R8
            R5 = R12 ^ R0
            R5 = self.ANDS(R5, R4)
            R3 = R0
            R5 = self.EORS(R5, R0)
            R4 = self.rodata[0x10 * index + 14]
            R6 = self.rodata[0x10 * index + 15]
            R0 = v_380
            R4 = self.ADDS(R4, R0)
            R0 = v_37C
            R6 = self.ADCS(R6, R0)
            R0 = list_3B8[0x10 * index + 14]
            R1 = list_3B8[0x10 * index + 15]
            R1 = self.ADDS(R1, R4)
            R0 = self.ADCS(R0, R6)
            R1 = self.ADDS(R1, R5)
            R0 = self.ADC(R0, LR)
            R1 = self.ADDS(R1, R2)
            R2 = v_390
            R0 = self.ADC(R0, R11)
            R4 = R8
            LR = self.ADDS(R2, R1)
            R2 = v_38C
            R6 = R3
            R12 = self.ADC(R2, R0)
            R2 = v_384
            R8 = self.ADDS(R1, R2)
            R2 = v_36C
            R5 = self.ADC(R0, R2)
        list_638 = [
            self.check(LR),
            self.check(R12),
            self.check(v_39C),
            self.check(v_398),
            self.check(v_378),
            self.check(v_374),
            self.check(v_3A4),
            self.check(v_3A0),
            self.check(R8),
            self.check(R5),
            self.check(v_3A8),
            self.check(v_3AC),
            self.check(R9),
            self.check(R10),
            self.check(R6),
            self.check(R4),
        ]
        for i in range(8):
            R0 = param_list[2 * i]
            R1 = param_list[2 * i + 1]
            R0 = self.ADDS(R0, list_638[2 * i])
            R1 = self.ADCS(R1, list_638[2 * i + 1])
            param_list[2 * i] = R0
            param_list[2 * i + 1] = R1
        return param_list

    def hex_C52(self, list_6B0):
        list_8D8 = []
        for i in range(8):
            tmp = self.hex_list([list_6B0[2 * i + 1], list_6B0[2 * i]])
            list_8D8 = list_8D8 + tmp
        return list_8D8

    def toHex(self, num):
        return format(int(num), "x")

    def check(self, tmp):
        ss = ""
        if tmp < 0:
            ss = self.toHex(4294967296 + int(tmp))
        else:
            ss = self.toHex(tmp)
        if len(ss) > 8:
            size = len(ss)
            start = size - 8
            ss = ss[start:]
            tmp = int(self.parseLong(ss, 10, 16))
        return tmp

    def ADDS(self, a, b):
        c = self.check(a) + self.check(b)
        if len(self.toHex(c)) > 8:
            self.CF = 1
        else:
            self.CF = 0
        result = self.check(c)
        return result

    def ANDS(self, a, b):
        return self.check(a & b)

    def EORS(self, a, b):
        return self.check(a ^ b)

    def ADC(self, a, b):
        c = self.check(a) + self.check(b)
        d = self.check(c + self.CF)
        return d

    def ADCS(self, a, b):
        c = self.check(a) + self.check(b)
        d = self.check(c + self.CF)
        if len(self.toHex(c)) > 8:
            self.CF = 1
        else:
            self.CF = 0
        return d

    def LSLS(self, num, k):
        result = self.bin_type(num)
        self.CF = result[k - 1]
        return self.check(self.check(num) << k)

    def LSRS(self, num, k):
        result = self.bin_type(num)
        self.CF = result[len(result) - k]
        return self.check(self.check(num) >> k)

    def ORRS(self, a, b):
        return self.check(a | b)

    def RRX(self, num):
        result = self.bin_type(num)
        lenght = len(result)
        s = str(self.CF) + result[: lenght - 1 - 0]
        return self.parseLong(s, 10, 2)

    def bin_type(self, num):
        result = ""
        num = self.check(num)
        lst = self.toBinaryString(num)
        for i in range(32):
            if i < len(lst):
                result += str(lst[i])
            else:
                result = "0" + result
        return result

    def UBFX(self, num, lsb, width):
        tmp_string = self.toBinaryString(num)
        while len(tmp_string) < 32:
            tmp_string = "0" + tmp_string
        lens = len(tmp_string)
        start = lens - lsb - width
        end = start - lsb
        a = int(self.parseLong(tmp_string[start : end - start], 10, 2))

        return int(self.parseLong(tmp_string[start : end - start], 10, 2))

    def UFTX(self, num):
        tmp_string = self.toBinaryString(num)
        start = len(tmp_string) - 8
        return self.parseLong(tmp_string[start:], 10, 2)

    def toBinaryString(self, num):
        return "{0:b}".format(num)

    def setData(self, data):
        self.__content_raw = data
        self.__content = data
        self.list_9C8 = self.hex_9C8()

    def hex_9C8(self):
        result = []
        for i in range(32):
            result.append(self.chooice(0, 0x100))
        return result

    def chooice(self, start, end):
        return int(random.uniform(0, 1) * (end + 1 - start) + start)

    def s2b(self, data):
        arr = []
        for i in range(len(data)):
            arr.append(data[i])
        return arr

    def hex_list(self, content):
        result = []
        for value in content:
            tmp = self.toHex(value)
            while len(tmp) < 8:
                tmp = "0" + tmp
            for i in range(4):
                start = 2 * i
                end = 2 * i + 2
                ss = tmp[start:end]
                result.append(int(self.parseLong(ss, 10, 16)))
        return result

    def parseLong(self, num, to_base=10, from_base=10):
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return self.parseLong(n // to_base, to_base) + alphabet[n % to_base]

    def byteArray2str(self, b):
        return binascii.hexlify(bytes(b)).decode()

    def changeByteArrayToLong(self, bytes):
        result = []
        for byte in bytes:
            if byte < 0:
                result.append(byte + 256)
            else:
                result.append(byte)
        return result
    


http=["7421185094760040198:7421184511113283078:c3df63f5fd02a9ac:786100e9-614d-49ec-a222-f3b8a172f7d0:1727879356",
"7421185246433249030:7421184490586916358:df9927f682881622:72d4de88-de4e-49c8-9488-5edab7baeb0c:1727879386",
"7421185447612729094:7421184864579339781:acdc20f90d571ef7:5a7127ab-52cd-4e31-8f93-d862dd5b2ac8:1727879429",
"7421185585094772486:7421185030787073541:7645f439e35a2fcc:26398c55-60f1-435a-b052-1fb07b103cc7:1727879467",
"7421220394336782086:7421219778851079685:775a547275d8b50e:6d5d76a4-00c4-4176-9bc1-52990d4ee70e:1727887576",
"7421221929799927558:7421221200468985349:2e32c6cc7f608e33:0026cb8d-9e37-4227-b3ec-f1b5505bb71a:1727887932",
"7421222595683616517:7421222413256443398:c6222b8abc4facf8:fd98317c-6a1c-4a6d-9264-f778f0f0ba42:1727887969",
"7421222154584508166:7421221501062202886:b838a367df56ef64:e5bf517a-e811-4ded-8b80-40f69cb15cff:1727887982",
"7421222280589575941:7421221460021151238:1daaa99c79906d91:8824b20e-f1e0-46a1-a8ba-68169f396dc9:1727888008",
"7421228740006692614:7421228270014727685:1bb106048070f753:038d808a-1c24-4180-98f4-a23058f51050:1727889513",
"7421233187554166534:7421232395834557957:d7ec8b037a373001:0cc517b6-be77-4e02-8307-60edfce4d961:1727890550",
"7421233501587179270:7421232995996190214:ae4d2aea45af4bcf:e4104809-e6cb-42f3-8b37-bb515d802c50:1727890634",
"7421233746747066117:7421232949918893574:10351a0a0e7c68dd:d5e23f94-22dd-4587-b74d-68d664ec10ac:1727890681",
"7421234253407897350:7421233744084354565:d335dfde581fe089:bb477b21-76da-43fd-8d84-e370f47095a1:1727890809",
"7421234293274101510:7421233668583130629:d7189a98af5b21fd:fe8161d4-5bf6-4afa-a696-47bc8945717b:1727890813",
"7421234361310660357:7421233797612766726:0b613623aac63d47:8df737f6-07f6-427f-8719-50040cc9f9a9:1727890834",
"7421234386950096646:7421233782525150726:e94b652538f08246:f9d21955-3d92-4cbf-849c-f2c6426dfdb2:1727890837",
"7421234448572188422:7421233887927944710:473b0e2fa04ff0c7:244a0dcc-bcb5-4406-a877-6d87b9385d9e:1727890845",
"7421234442222700294:7421233943531423238:003bc4ee00bcf315:f3f15e8d-a49c-4b13-b172-b2729de03675:1727890849",
"7421234467979757317:7421233879107339782:ba588ed0bb056851:a053f33b-e486-47ea-9430-6a71fb1c48b9:1727890853",
"7421234491375175429:7421233993800140294:20d16ea59ae3ddb1:5a8c54d3-296a-4df1-9c73-8762a1c799db:1727890857",
"7421234499104753414:7421233943531816454:0ac3c8786ae27008:0ed6225b-8785-4a9a-92b9-bfda2b712d1b:1727890861",
"7421234561805190917:7421233866088318470:f6ef5e8e473f1693:43d162be-dfb8-4488-bc2a-5879c4d1658e:1727890865",
"7421234667402479365:7421234100533331462:9069a8545a892ead:4b0c8a5e-221d-44f9-8317-4e43689d5ff0:1727890903",
"7421234688084395782:7421234212336420357:61d059b66f9e03eb:18589dec-f872-4393-9b70-fc8e2469b0e3:1727890907",
"7421234718719805189:7421234173769942534:98effa6b1aea537a:47b48c6f-4acf-4e49-b16a-673a2631dc9d:1727890913",
"7421234762935256837:7421234265230870022:4e0e4f9c97efa84f:26c29fc5-1d0f-4120-93e8-1214664d420e:1727890918",
"7421234747069122310:7421234160990569989:ab4955b21813e201:7dc6efc4-d262-492a-943e-8781be43b002:1727890922",
"7421234799291270918:7421234212337124869:39e99742569f7de7:0a2702d0-d6de-4449-9076-4595990bddfa:1727890927",
"7421234800219195142:7421234351000208902:aa528a0df66b9816:2acdc97c-72e6-4f6e-a895-6ed9ae8497c5:1727890931",
"7421234809450497797:7421234323489277446:eff6a0473b98f7e9:bc97a2cd-61ee-4c49-9683-f0bb75fe653b:1727890935",
"7421234819000895238:7421234228237649413:2969cf4a7c43332d:74ef15ac-c59f-43ef-bd93-ccac9b5cf715:1727890940",
"7421234868534986501:7421234276701947398:87cfc3deeba07f4b:837fffa5-41c6-4997-bcff-03837c84b2b9:1727890944",
"7421234997766096646:7421234477793723909:8fd8b03d60e2e445:a3813587-8633-4c67-958c-cf4d7a1726b2:1727890974",
"7421234998856992518:7421234415017985542:cd061b90d29e9375:df0d1b9a-1faf-429d-bc11-2ff38933bc5e:1727890977",
"7421235052035802886:7421234593665435142:9ccdbfa5581142ab:340b8964-857f-4715-b89d-c2aca4c5a5fe:1727890985",
"7421235081686599430:7421234589861627398:cdd21fdbc546806a:985702f0-605d-4898-b1c4-f43b282b8e17:1727891004",
"7421235151260714758:7421234468936304133:111837d25536769f:982a4eb5-721f-4495-8f88-67622f3ea56b:1727891010",
"7421235150278985477:7421234598347179525:b897c1c7f372b16e:5b994c61-c72e-4249-8554-7ad7aeb04dd9:1727891014",
"7421235141794744070:7421234641913267717:081f1802d1e65e50:6a741af6-5924-44e1-8dea-aa69c27b9b70:1727891018",
"7421235185096525573:7421234575144486405:1af97fc7014ef2cf:ee677129-1abc-4190-bc6a-f5b30f54c772:1727891022",
"7421235293636511493:7421234857143518726:c90a944ce69b65ec:9ddbe3f9-8342-48c5-b168-7fe640a36349:1727891045",
"7421235358051927813:7421234792399881733:e9b929561b53ec3f:2cf54559-28a1-486f-8239-1595474bc4a2:1727891051",
"7421235358052845317:7421234792807384581:33c4604e27ce8df7:26ed1e9a-a643-4707-9dc6-00f3cbf4eb3f:1727891056",
"7421235371885430533:7421234822020810246:a80e755f063cca0b:c6c7db0c-c44e-4bd4-b24b-d5a3ea4c92e5:1727891060",
"7421235452461713158:7421234958917993990:b4b627c943f1c4a9:4b46144e-b2fd-4651-8124-521a6e4f705f:1727891075",
"7421235463689701126:7421234940077950470:f88336fe499263d3:a74b8aed-a88c-495b-9935-222e67109ef1:1727891080",
"7421235475858392838:7421234980015244806:a462aa6259a701e2:a4ceaa41-d420-41bf-b858-6e4c70ed3ff3:1727891089",
"7421235507097749254:7421234908788934150:026e98128e3e882c:b904ad69-e614-4f79-a271-ac5acd3e403e:1727891097",
"7421235617034143493:7421235144226244101:45ccda3f3c298b94:3840b9c1-ee09-4237-84ec-9463ce0f4a1a:1727891123",
"7421235631672952581:7421235009389364742:fdbf7b92e829a6e5:533da564-4770-4a59-b1d6-da2d55f57f8b:1727891128",
"7421235698675730182:7421235170903524870:52fbe04f788e93ae:e72579fa-ee16-4ecb-b1ee-b965ba50b710:1727891135",
"7421235725556926214:7421235165479159302:55c15726977f48a6:85e9dde5-fc21-4001-855c-d1e8c1bc2add:1727891141",
"7421235739110000390:7421235111512212997:e467f46c08cd0732:e790c4e3-8f49-426f-96e7-8325a66f402d:1727891148",
"7421235807488313093:7421235190935209478:9e2cd3f00138e4dc:a2eb14f2-04fb-4ed5-b647-59b8d82139fa:1727891154",
"7421235785523644165:7421235203869640197:68f8039fab78f57c:1ce9fdcd-24d1-4c55-a3f9-976b5376f587:1727891161",
"7421235829551433478:7421235330755823110:cf912c13a55bdef8:4fad9de3-6a8a-4179-b84d-aafd3c8992a3:1727891172",
"7421235851940448005:7421235414520481285:e795bd585b2b640f:1ddd8a78-f8b0-46c5-b075-e42f74505ceb:1727891177",
"7421237369850119942:7421236822397175302:013b5511b67c623b:e8e9f2a4-5f9b-4617-a2fd-e388ed1a5cec:1727891522",
"7421240600186521349:7421240520838563334:cdace06219a4e021:71c88ee5-7471-4062-adfc-54c116f0b22c:1727892200",
"7421248601710593797:7421248367743813126:877cb50a4863afc6:39aa3913-0d6d-4b95-8ed3-766b10246cff:1727893995",
"7421248571645822725:7421248556722374150:aeffbdaf0f463b59:0666a725-834e-4a25-ba03-dc060fbed09c:1727894031",
"7421249629201368837:7421248960600524293:957f6ccca9c54ec8:56992f0f-b73e-4879-8ecf-b16db4ac5992:1727894385",
"7421249672364328709:7421249151578818053:6a6e44c025171c2f:7f5b00c1-c53a-4d86-9d2d-cf95bf162cc0:1727894389",
"7421249643135125254:7421248890513507845:78f2ccf83d0a4315:9677e99f-52bd-494e-9902-749886ea3b94:1727894393",
"7421249654954788614:7421249171786728966:b7db7de626723e7d:e29463c3-342f-4227-8ba3-c8d9e68eac95:1727894397",
"7421249686894429958:7421249065386804742:a29f9a6757eeb376:5ee13e6e-284b-4b1b-8032-5991286dc3c5:1727894401",
"7421249715486689030:7421249255811237381:1945ba9e37ab9ea3:c995ba4b-c015-4893-9a24-0ae361207248:1727894405",
"7421249735803586309:7421249095224870405:5e17a637be0977eb:96995443-2f82-4024-9120-08728cd805aa:1727894409",
"7421249747937494790:7421249151579424261:b1658b91ad04cd65:d7fe4074-212f-4503-9c5b-5b87c3ce64aa:1727894412",
"7421249761268008709:7421249090531493381:779075efa0f0d801:bd7ba514-facd-4789-888d-6a61636d156d:1727894417",
"7421249758683907846:7421249253034575365:ad8fcc03ab5d0821:a81dcc32-a255-48d9-b36a-0eb7123aa1ca:1727894421",
"7421251109677876998:7421250449805100550:b88e74971bfc975d:c0b1e4eb-b429-4b3a-af54-a1b8975783f1:1727894737",
"7421252907527702278:7421252418056537606:4212648de60077bf:75544aef-1daf-44e4-bf2c-81fb5dd0cb28:1727895149",
"7421255132400109317:7421254373538334214:fbd0a99eaa34f680:a2affd89-c69d-4161-b3d9-f4464d5c3271:1727895660",
"7421256040593950469:7421255974130894342:147273151eac8f36:79f39ce8-01e0-49ad-a7d0-ef86dea9bcdc:1727895795",
"7421256015427618566:7421255447351051781:f3f3a3c0f3f2cbe8:31e72d52-a037-4d3f-b77c-2b73548c9c4a:1727895866",
"7421256948039485190:7421256257539999237:3cf038fa57eb0a02:eefe4f71-e134-4fc8-9f9d-5556f4465f58:1727896087",
"7421258814920607493:7421258042468173318:36c4a79831675d6b:3c4ac023-c8bf-41c8-a240-61571f43f8da:1727896531",
"7421260024703600390:7421259301715904006:d8d4738a33f0abd7:c6547d4d-2b9f-493a-9508-4c69bb7088bd:1727896801",
"7421260056412997381:7421259566282851846:92a9c4f1d0f35e8c:8707ca3a-9c47-4323-b58c-e8c21454e351:1727896812",
"7421260098045167366:7421259390504781318:8ac767abe3653427:38c80ae4-3b55-4ba1-8e4e-bf226c218457:1727896816",
"7421260344402659077:7421259691025974790:919328196283e505:0a073ceb-da7a-4be7-9b62-3baeceb84503:1727896881",
"7421267367366362885:7421266777986696709:29872f48b421ec24:5c2f1c07-14af-4aac-b805-544bfae38e5a:1727898527",
"7421269077514061574:7421268615062259205:149924d1c97410b6:6c38363a-7596-47fe-a7b7-13bfa6eeb9fd:1727898923",
"7421269225492514565:7421268633907332613:d0d788aa7cab3548:66a20dd4-09de-4e9f-81ba-d37d4d5d8416:1727898939",
"7421269177334662918:7421268469461911046:ee01e21df8455858:a9566903-f192-4729-a5c5-0c514d414814:1727898943",
"7421270430298965765:7421269896715519493:fa715a29c3562d52:a6773d79-dad2-4d2e-b0f0-3a42d5bf527e:1727899239",
"7421272829621110533:7421272909186942470:292db6e1d4427507:0f93e07f-6e29-4aa3-b2cd-1c2203344cec:1727899682",
"7421273074434246405:7421273218424587782:fdb00ea352688beb:286f8c11-8811-401a-9f63-72bc49270c85:1727899753",
"7421272780635719430:7421272216546903558:dd8fd6fe711d5d30:831a7dc3-96a7-46d4-89b7-30164cb845f3:1727899780",
"7421274173945874181:7421274270691575302:9e097ec5ca6e9816:5220d541-d5d2-4246-b7ad-9ad3807dd4f3:1727899967",
"7421273585501603590:7421272889495094790:1efdb05256f3c7a0:cfb18e29-45f7-48d4-8533-976c4a7258af:1727899972",
"7421274562535606021:7421274119192413702:ac2f224dd4ca0daa:40ff1c5b-6922-48b8-99c3-f267ecdc39fe:1727900201",
"7421275545771853573:7421274801426580998:4062269a3111c5db:1c094499-6348-4c0f-8a93-b9aadf5e71d0:1727900424",
"7421275598355465989:7421275012440720902:082b14881ec5e7d8:1657d52d-9d7e-4148-9171-c5796865659f:1727900427",
"7421275578147391238:7421274937149179397:8844995fd16f19a0:37e2bed9-8a69-42f7-893d-d6673d51c236:1727900431",
"7421275561236629253:7421274893382485509:684693c17e29b2b3:ec348255-890f-4cc8-8171-eee1e02a611f:1727900434",
"7421275627409557254:7421275018204399109:ac872113da8c94f3:270bfdcd-4145-4645-8961-b67779c151ec:1727900439",
"7421275646963795718:7421274906187580933:8a2bbaa031b8e2ba:8f85c0fa-c847-48b6-94ad-c8e27a8f4aef:1727900442",
"7421275633063511813:7421275115188471302:15f9928b38d3f54c:a22f4be7-7adf-4749-adaa-7576f55d7e19:1727900446",
"7421275629344458501:7421274911178475013:370365fe7a264ecd:a174545d-77bd-401b-b075-3b772a6e3308:1727900449",
"7421275679784306438:7421275072499680773:c6972c168d7389ed:3730bfe0-ee63-46b3-a70c-05018f67d2dd:1727900452",
"7421278881333659397:7421278174397564421:9d639b83c9b41e75:b7650240-0e1d-4bb2-b516-a5491a7c2f52:1727901196",
"7421278871968139013:7421278174397613573:c4dc110efc9e52bb:9b30bb0d-0441-401b-9bec-431303329dd8:1727901199",
"7421278823940409093:7421278196623050246:82bb191c1fe2b616:674b37b8-e085-486b-bc12-9af0130362b0:1727901202",
"7421278909351675653:7421278301543974406:f46e5018c0ba2d70:e19d94dd-6122-4ac8-b82e-f8e70f63009d:1727901207",
"7421278913319864069:7421278119024690694:7871a60dcfb8f196:5b76939d-90d1-41a7-b2dc-4954d8e3b026:1727901210",
"7421278862032979718:7421278312100431365:5be3740734e077f8:0383b22e-76e2-4cf2-9058-640723bdd172:1727901213",
"7421278948589979397:7421278373336958469:6a9d517ed54eb95d:6116cb1d-da4c-487a-844d-f0bcdc3be013:1727901216",
"7421278935894263557:7421278248464745990:fdda93a81b4e1796:3b5bb1df-cc53-4ca1-a69f-d69856726160:1727901220",
"7421278955020273414:7421278314243393030:ff7aefc2aa36521c:b5933692-2081-4dd1-832d-d08e8ed62459:1727901225",
"7421278991371618053:7421278438511904261:139a51f43e412670:322fb0aa-5bd3-4b01-963e-6eb554ce2f5d:1727901228",
"7421279089988257542:7421278373337892357:6fa8236c2e9db76c:6b1fac23-1547-4a55-a8e7-7e8927f63b3a:1727901255",
"7421279137614071558:7421278351217083909:b55698a57f85ba50:58e9b437-6b67-4c25-8517-6b46cb7f0ec9:1727901258",
"7421279130454951686:7421278510545421830:c993de23a028e0f4:8c0c5b9e-04d1-4570-9d3d-4cf3af958188:1727901261",
"7421279189377042181:7421278378479977989:5012d2b057d96f26:f3d6942c-b8e9-4c20-b8b6-adfedfa2d640:1727901271",
"7421279225640011526:7421278477503432198:81d887adb4be3b90:63c2942c-b900-447a-a376-10352f46ab85:1727901281",
"7421279204719806213:7421278556892792326:cc43151ac27e911c:28c20162-229e-47c4-8e97-d501a25383b0:1727901285",
"7421279264647153413:7421278763222205957:5658363976ab56e5:2c3eb3d8-7d98-4aa9-b892-7dcb7e91637d:1727901289",
"7421279275145266950:7421278763222287877:0db08c57d95be568:806f04f1-d50e-4864-b2e3-d870b70a1b8b:1727901293",
"7421279246797195014:7421278578699322885:b07ef442bbfd9254:88f06a14-9b48-495f-b3f2-a539e9d1612f:1727901298",
"7421279305198831365:7421278854569854470:7f3133a85c5b4230:a5b09148-3824-446d-b927-23c4cee88dc5:1727901302",
"7421279284567164677:7421278652845557253:64b70086f449ccf9:30db1647-9b5c-44d6-8150-660a6ba99172:1727901305",
"7421279307253761798:7421278566212961798:b0ac374a0a53fc01:120062ca-47b2-4a18-9cb0-a0381a1c4e24:1727901309",
"7421279363200714501:7421278569010120198:081380b8b27573f5:361b360c-1fae-4241-a5d1-4b50cedd872d:1727901313",
"7421279344281175813:7421278622722737669:09eaf34a1ceeb43d:82b9291f-2464-4aaf-8602-f8ff5f0be788:1727901317",
"7421279401118271238:7421278818671527429:1d5823c53955420f:d3ba678e-73d9-4175-a581-22377dbca255:1727901328",
"7421279397364352773:7421278852506797573:dd5cb4be708dff58:ffbca56b-8270-4bf6-9ba2-d58df40d65c8:1727901333",
"7421279471212480262:7421278601830876678:19619522bea26a48:516e3b97-b13d-499b-bfa2-8f77d31606cf:1727901336",
"7421279460316202758:7421278843749664261:56cde0683e7e6ddf:605773da-74a8-4d4b-92ef-0f4a102dafe0:1727901340",
"7421279510282307334:7421278883053749765:feaa62687c35c826:638f5af6-f09e-4c6f-b848-4fa550cd4f1b:1727901343",
"7421279486790469381:7421279029208385030:532634fcd9bf234e:856ea366-cfed-4294-b477-98744bc321d0:1727901347",
"7421279477068957445:7421278935532717574:1f3369ac5c84d506:af6d824a-6c41-4ba1-9de5-3cb9fbbf50f2:1727901351",
"7421279550908368646:7421278944768771589:0945562abd6b690b:7dd54a70-2a15-4bf5-ba56-2caf8d87a945:1727901354",
"7421279543585982213:7421278953379661318:43205f7b8e566b2c:5f620cc0-19e8-4cc4-aa77-838d4e1b20c9:1727901361",
"7421279581896230661:7421278935969367558:5db225a81aaa036c:a3345979-b843-4b57-a9fa-afa9c4c03ebc:1727901366",
"7421279594865870598:7421278994064164357:e5c0cd561b6996e4:14d37196-aeae-461e-b501-18754a349075:1727901371",
"7421279646534731525:7421279032228627974:162b42d57419028d:52560d9a-c5e3-4292-8280-4457d9ea9657:1727901377",
"7421279640667326213:7421279062922659334:935b1d4384209069:32b8ce44-6ad2-40a8-8c06-cd385140736f:1727901381",
"7421279637378483974:7421279005699933702:eb9894a7988e67c9:5d966490-35bd-46ae-98e5-f5fbb981fd96:1727901385",
"7421279687261030149:7421279037924410885:c96c21b918dd6005:9df11db9-04ef-44ba-9f98-c56dc68ca41e:1727901389",
"7421279669432272646:7421278920329381382:ce7dc5533c0b5e46:3bd3198f-426d-4314-bcbe-36fc40569363:1727901392",
"7421279664239642374:7421278884945856005:1bd41cceec0f3a4a:c3427cf6-f66a-46a5-bdfe-7603a8a39708:1727901396",
"7421279706027312901:7421279032400774661:a9b1ea31f16cf282:61d096fa-870f-4e37-94f3-315af4a5bd75:1727901400",
"7421279742428743429:7421279005700474374:559ed414f3780fd3:64cb3f71-b9a1-4ca7-925a-856a57d675ca:1727901403",
"7421279763488671494:7421279060284802566:07acbdae1ef8e3d7:0d3e46c5-a4a4-4552-92b4-2882e3ba8e16:1727901407",
"7421279835995670277:7421279360012830214:162656d8e28d3168:3859d7f0-efe5-4d8e-b943-f469cbf5f1d5:1727901419",
"7421279794762270469:7421279310977254918:5a183b9707c54fd6:3ef0e2be-7405-4419-844a-c75f8d2064cc:1727901424",
"7421279857688348421:7421279299153921541:2259e92b2314b24a:70018021-be0d-4997-9e10-8d8112fc3c7a:1727901428",
"7421279804740568838:7421279248621143557:ea6658935566ef7d:630413c1-bc0b-40fd-b735-8ee9ae9a7075:1727901431",
"7421279873391494918:7421279217881253382:0668d780ff936359:944e8c90-de35-4d33-8b26-95ff8e076ed3:1727901435",
"7421279884612126470:7421279232020432389:35292b856d1b78c7:ee1ea228-61cd-4cf0-a4b6-df125f140c3e:1727901439",
"7421279873581516549:7421279274441852421:6728634d7e0b6978:5eb7fccb-64fb-465e-83fc-f6e10db041ab:1727901442",
"7421279898977945350:7421279268003776006:41d85c5c5519da46:d04c5386-787a-48cc-8da1-2cc58a62efb7:1727901445",
"7421279928496834309:7421279375469266438:3053a1836a671b82:eefc0835-7bf9-447e-8afa-95bc48daec35:1727901448",
"7421279914375202565:7421279216346285573:eefd25928076dae8:78ff595f-8e24-4b59-8681-99a729854609:1727901451",
"7421279972158883589:7421279424202950150:f2a1ee216a6c3dbd:6f83bfb6-2b48-4fb0-b296-c62624e2e437:1727901455",
"7421279985305208581:7421279214496957957:fce0065b0e70729c:adc5db33-4325-4f94-b339-427fc061d294:1727901463",
"7421279991671752453:7421279311481406982:58fb572149bb077b:44d04767-fc39-45b1-9a88-1e2fb188f861:1727901468",
"7421280037699929861:7421279312752215558:05fbe2bcf7a52ad7:d63bfbf0-aab0-4559-b3e4-497ee50b9ea8:1727901472",
"7421280065583171334:7421279384395040262:33d2ea03857e289e:ad6fef79-1175-4d69-acb9-dd821984b25d:1727901476",
"7421280062294738694:7421279404221728262:97b128758b093d9d:ce968a1e-c00c-4ff6-9f6f-0b8c5ec1dada:1727901479",
"7421280105894266630:7421279525789353478:f045e8b2cd6627fd:be3dd4f5-7e52-4932-a51f-b9f7a8cabbf5:1727901482",
"7421280090921649926:7421279415387489798:4db47a445d99bc85:350241df-9f7c-43f7-8091-c1b2d6476547:1727901486",
"7421280133090330373:7421279525789550086:b7f186e1bece686f:a15f92b6-b735-40cb-85df-047e742c52e4:1727901489",
"7421280118284584710:7421279578226230790:12038e36e181fddd:f3ac579a-2a31-48ce-aabc-036b1aaade7e:1727901492",
"7421280114594465541:7421279652322313733:74a6b199041353c2:99517db7-8037-47ff-a91e-2c209e2d1723:1727901496",
"7421280143501166342:7421279562178561542:bafb58fe389bfb84:6a5b94d5-933d-47b3-beea-a299f087cfa2:1727901499",
"7421280152720033542:7421279637671888390:75cfa63ab2648285:b6ec1489-bb5a-4c30-98b3-c1eedb5a3df6:1727901508",
"7421280193262405381:7421279658387490309:9885f92e23847f7f:cf77f97f-c26f-4ddc-8968-950a48d29ff7:1727901512",
"7421280238929430277:7421279561453749765:725650b446c1a3b3:480edcf8-42b0-4d27-9233-61b747e35381:1727901516",
"7421280263595935493:7421279676146337286:c45457702681359e:5f90e1b8-2b3d-4041-830d-9076da3ae93b:1727901519",
"7421280261050566405:7421279643326137862:07bfdaa96cde8a7d:d7fb2ef2-e183-447f-a386-28fb5d265ff7:1727901523",
"7421280269732693765:7421279590096799237:5aa03a0b8ee67ac8:6d9043ac-75d3-46b4-8fb2-16b517b744ce:1727901526",
"7421280266339993350:7421279588145661445:29b3a9312aacc75e:f66e9214-0dd4-41a5-87dd-5ce03a00017c:1727901529",
"7421280291199190789:7421279545549342214:b3e3eeabe8b0469a:b2eca5e0-ea58-400e-8049-a169fa1d93fd:1727901532",
"7421280723771000581:7421280893531145734:98e2bf41dcfb17af:11563cb6-a63a-4303-9063-a4f0ecceadfc:1727901535",
"7421280312506500870:7421279756974540293:0042747937fa7f32:ec7447fd-cb33-4892-aeab-88b276924a0a:1727901539",
"7421280318513170181:7421279647943919110:441600da2a4425a1:e66121c5-ea44-4ced-9184-f80d2635e1eb:1727901542",
"7421280332714739462:7421279864977884678:d803a67bde91c04e:6b6f50d6-6dfc-40c5-b76b-f3e4bbb5c586:1727901545",
"7421280392642332421:7421279844282926597:7bf9700205c0de7a:505c7c96-afb2-4281-b1f0-b90c9f344e3a:1727901554",
"7421280399790507782:7421279591988610566:234c1887435a5aab:fb899321-dcb0-4729-9d13-1e82c8678e3a:1727901559",
"7421280389140399878:7421279756975293957:f5bd092b8ca6c662:62cd9436-ad0d-40c6-b990-5b11a469db4b:1727901565",
"7421280458678028037:7421279807881577989:b03feea460a47acd:6768f41b-006b-4439-a421-f10a3b24980b:1727901568",
"7421280487773406982:7421279733390771718:d2c6dbe8552dabe8:2f0907ee-2359-43c5-bf6f-5b83c5818d0f:1727901574",
"7421280470438921990:7421279756975785477:37be450c3a7517c7:711b9f5a-d12d-46fc-b022-a51a99aff62c:1727901580",
"7421280504009967365:7421279901297034758:df8951102567216f:cbc58ca2-624c-4c7a-a975-b411c9adc5a3:1727901583",
"7421280526135035654:7421279762331305478:08ca3a4108791495:258e4473-7e45-4219-b7c0-c66f9dbf4657:1727901588",
"7421280556795135749:7421279901297559046:ee36d3b192ce7f5c:202d7ab4-fc05-4008-bde8-b2724a723e2d:1727901597",
"7421280575451285253:7421280003889808902:ef4bae0b017c747d:80f590c6-0b04-49df-bb72-64aebfdb0cba:1727901600",
"7421280610478180102:7421279949947061766:110497b8ae82de9f:f9301b8d-1a4c-4ced-be2e-68c510e0d2d5:1727901607",
"7421280620578162438:7421279994662929926:dcc19e8917cd32e3:ba94483a-05ea-417f-a96d-2aec9b4480bc:1727901611",
"7421280625841866502:7421280144964634117:e82a51e0b063d7cb:19f278d8-f8b1-4db1-b927-21441f84a2c8:1727901613",
"7421280668052997894:7421280200757069318:7904108b450f3f8c:aa68f3dc-7375-4203-a2ed-cf5b6cbefc73:1727901617",
"7421280684129421061:7421279974358074886:9ca9de157dbc30c0:b18d2d7c-b061-4ada-bdd5-51bffce1e0ec:1727901620",
"7421280676164814598:7421279901100508678:6c1a70bc51d560a0:d4a13a0a-7246-4996-bc42-0baa8a050341:1727901623",
"7421280691545999110:7421280113880761861:5ab7ba9775d30fa6:56bbf632-9158-4e22-93a7-fbdd4292e980:1727901626",
"7421280673443694341:7421280061670163973:6f379fe18a9287e7:89a15bb6-c0dc-4328-ae07-b548b29e8b32:1727901630",
"7421280697128945414:7421280007359088133:34357db73377408e:3e5a56d2-87ce-4887-9de2-727f55dc4363:1727901633",
"7421280707480323846:7421280118099740166:694fecde4aef8951:e7bbfb51-67b4-4f71-a787-b52acca4a558:1727901636",
"7421280833404684038:7421280258773157381:761697ad5febc994:2ec02be9-3793-4f5e-898a-0fb075c860f6:1727901651",
"7421280758802007814:7421280285049849349:f1dcf10cae114620:d4927bd7-4e80-4798-a7c1-3b03b58f4b4c:1727901654",
"7421280815953528581:7421280102972343813:2ae9d66a1004a82d:a96823bb-8260-41d9-80a6-11a6a05ebbdb:1727901657",
"7421280818348033798:7421280263860389382:2202a4cdf0b47f33:b4261ea8-2424-4049-9ebe-5d2fea38ab02:1727901661",
"7421280824278828806:7421280269631653381:eda11eade9c0b667:975ecbd4-4849-4d03-ab85-6b5893eec4a0:1727901664",
"7421280867349808902:7421280219287832070:3b8d9a25abebec33:bcd5416d-ed0a-411c-9baa-e05ee2864a0c:1727901667",
"7421280896542181125:7421280171888625157:142056a0f96d8105:baeb5fe9-08ee-4c32-a645-4a916936e0f4:1727901671",
"7421280855002646278:7421280270080460293:5f6ef80ad6d117de:d0ede889-32f7-4e1a-bdd0-3c6aa6e5d2e9:1727901674",
"7421280897331267333:7421280219288192518:37193f7bbf15ce98:bb272f4f-6874-44d6-a6ea-f8a2b94b6e91:1727901678",
"7421281565584590597:7421281636560487942:4e0ade5761ccf4bc:6ce736b2-b889-45ab-ad63-2cc9e08ef50b:1727901700",
"7421281072557098758:7421280494567998982:087c4f59b53650bc:dfc7a4f2-a375-4fe0-973e-8aa3815e8492:1727901719",
"7421281108636108549:7421280546196096518:9c3e7f552b8ff10d:8fe91149-4e6d-49f4-bb4f-9dde658fe75d:1727901723",
"7421281179246167814:7421280416164972037:cbc5524a209ee23e:c448043c-42a2-4d33-b8de-74f71038942d:1727901728",
"7421281127313491717:7421280580169778693:8103a0e5c259ae2c:1007157e-9532-486e-8b07-bc42726a314d:1727901732",
"7421281130061006598:7421280496431121926:d936bfc8675c41dd:78344ca4-8092-4516-9411-fe03ca4ffa6b:1727901735",
"7421281200897656581:7421280554588800518:27f7fbf71163dee0:82f9447d-67ec-45a0-b407-ba13f131a740:1727901739",
"7421281172900988678:7421280505105139205:af61293a00034cbf:f98c7564-53c9-4380-88d8-1eee1f13feed:1727901744",
"7421281213686499077:7421280644317332997:854cc083ea06c3ac:61c9133e-b977-490b-bd42-950d0e7253e2:1727901749",
"7421281218002618118:7421280494568736262:7a652b113d697326:047e4be4-c7d9-48c5-a39b-3382b39cfcf4:1727901752",
"7421281215515363078:7421280534104540677:765de6e85619362d:b0d61783-cc95-4bc6-8b13-879f03df91a7:1727901757",
"7421281413512070918:7421280866171504134:46b25b478ac1b142:f8a91409-ab77-4536-ba6f-744d883c6b41:1727901806",
"7421281471863162630:7421280893937321478:d4cbd677d1f562c7:2490d5e0-8bb2-40af-a2ec-10b26d86684b:1727901815",
"7421281488199436038:7421280968528922117:1b234ac0c5c72dbf:882f921c-352e-495f-b5a3-7ac86abcc55e:1727901818",
"7421281508684465926:7421280693261993477:48161f6a7c48d04d:ae10aede-a807-4f33-bc93-31e71a57b75f:1727901822",
"7421281544683816710:7421280953433277958:53d5cebf2fab36f7:7a4f69bf-085a-42b0-b9c3-deee32e8c797:1727901825",
"7421281569786365702:7421280775445022213:781de2718e15a093:1e6f14f5-4c5a-4ddf-a0fb-f0612f924aa4:1727901829",
"7421282252779357957:7421282285100549638:aaf5a637624bfa7b:fbf4706d-4bbf-47de-9ed8-b3d988a30e1a:1727901831",
"7421281602904360709:7421280866657961477:5794d74569e7450e:a8b28ab8-9278-44ae-9f59-ccf379d457c8:1727901835",
"7421281606440503045:7421280791958177286:5bcc2dbb2f22df92:c42aa254-c371-4553-8297-3dbee06acc69:1727901839",
"7421281637583308550:7421281037336921606:7e0fa15b7261ca6e:61325c08-24a2-4478-acd5-93c1477882a5:1727901842",
"7421281632403130118:7421281105338385926:df06d4586c781ae1:fd4c7c63-c0fd-49e1-bf7a-377fc5b0fe11:1727901845",
"7421281744982705925:7421281283139077638:66e77275e546bbcb:126bfdb6-5b18-4db8-9262-c6057dd2c7dc:1727901869",
"7421281711265580806:7421281031381403141:e85afcb0f40145f3:e99ab81b-42a6-4cac-870b-985f15366cb1:1727901872",
"7421281761609598725:7421281236145997318:898a0ecd6cf899fd:79a2e1a5-e128-4967-8ff5-be68dbaf118a:1727901877",
"7421281797004494598:7421281011139692037:2f4b49949ae14d40:64dcf3c8-485a-41f0-9450-d719d0ab6767:1727901880",
"7421281829590173446:7421281314529281542:31e122b5abcd8d8b:d9067f8a-a81a-464f-9fcd-990e03754e5e:1727901884",
"7421281809650435846:7421281046501754373:ac3d11c4f52d2f7a:382346de-cc4c-485f-9d74-57078d5c2e8b:1727901887",
"7421281828768417541:7421281203871352326:e92ee624e3653fff:2aecbfa4-da33-4d2b-9cc3-95011c94b2dc:1727901890",
"7421281811391121157:7421281353456469509:c8662a46a394f2f2:806c8616-78e7-428d-b096-1aaaf32d83cc:1727901894",
"7421281842085529349:7421281294300333574:1ccd1e91bae3b27c:774801dc-d5bc-4c9a-a0a4-885d502befa7:1727901897",
"7421281847764944646:7421281274709231110:03effad7bee2a266:a77a37fe-2c05-4961-b3dd-a75bd14236f6:1727901901",
"7421283484138931973:7421282943358371333:3c3475bd3eafa784:75bf2530-c3cf-4e4e-9137-093379fd15e9:1727902283",
"7421283506939545349:7421282841533957638:f1e1a2a9c1c3e1e8:0c59592a-6fbe-4e7a-abb1-604025506cb3:1727902286",
"7421283528741144326:7421282909909272070:9e511b2b848706ff:8c410e3e-47a0-4394-923c-3c54e816ee5e:1727902290",
"7421283539982255878:7421282812123514373:01e4af541c11d362:e4261033-6ef7-468a-b704-cc96296dd4e8:1727902295",
"7421283579307689733:7421283027018155526:37cf7e795ff3a616:30dedf81-8a0a-4393-96a4-d9ed66dbe887:1727902298",
"7421283585297188613:7421282880859768326:21102ad4b09761ae:35be267e-b0e3-411d-a337-70776aaf3cdf:1727902302",
"7421283607240918789:7421282966079096325:4bd56241bf5ae023:f4d5fe47-5e3c-42bb-8d47-720ed761050b:1727902305",
"7421283601151248134:7421282941525984773:8c5863433707f10a:b1ecec37-24b7-46a4-882d-41547fa84f01:1727902309",
"7421283667924043525:7421282947657647621:08b0a83f14703c1b:25c0c372-a658-438b-b87f-416beb4c2448:1727902312",
"7421283628494391045:7421283025885709829:89a309050f095b05:0031d6eb-e269-415f-abe0-6c0250a16ac0:1727902317",
"7421283665429120773:7421282957464618502:8f63162facdbf86d:683cf347-6444-4f40-801d-2b6afcf1dfbd:1727902325",
"7421283688544044806:7421283107209496070:261075f15e95f16c:d042015b-917e-491e-861c-09deac8810fb:1727902331",
"7421283699898369797:7421283025886283269:59d0bcda85bd791f:e942cce9-637f-4e0d-aa52-838127c118d3:1727902335",
"7421283746107033350:7421283288821679621:0bff35e26351ea6b:34493a53-c3ce-4afe-af47-5e0e1c75cb29:1727902341",
"7421283765278803717:7421283230193894918:d73e06435b11e122:725200a3-8db0-4c9d-8d76-23d53086bf77:1727902347",
"7421283794655102726:7421283188251837957:bd0453e66db58816:d0f2f21b-ef5a-4980-aaf1-e05ad71e460b:1727902351",
"7421283853081593606:7421283131750647302:2f083979c81750a0:43419cb4-c494-40b5-818a-5bbadf02a6ce:1727902354",
"7421283837328344837:7421283308174640645:453d3845f186525b:3b3939c9-f4a6-4eca-acf2-cd6f0b117a96:1727902357",
"7421283826838783749:7421283360561038854:8b9116d8c706f4ba:8a575714-a4df-4190-af9a-dca7363c21e2:1727902361",
"7421283905380222725:7421283294127785478:4dbedf488025fbdd:1b73a8ec-2410-484b-b3c1-91be4a8ccf52:1727902367",
"7421283903761581829:7421283293440574981:f5945227163c524d:fbe9e8c1-b86f-48a3-88eb-581021275b9c:1727902370",
"7421283942571968261:7421283353627887110:ab616a90d85f79d1:c40ae32e-269c-4878-aef2-2325bb68bc65:1727902384",
"7421283966190536454:7421283464714323461:a28ca2d018b00538:a3833cdf-9845-4aaf-b5c3-cdeb83f9a217:1727902387",
"7421284022929819397:7421283300432217606:9f8c13a8f7bcb21d:1a44a51b-719c-41aa-81a8-6f2e1039b659:1727902391",
"7421283999580718853:7421283263413913093:b5097d8e3e616ee5:8c481a80-0077-4359-86c5-046c667454c6:1727902397",
"7421284026457589509:7421283436227020293:da22aa061e73899f:27f6a477-57da-44f2-a7e8-1f63a3a86957:1727902400",
"7421284066303428357:7421283477569603077:7836d3fcac5140eb:920be601-a0be-49d8-8199-9b6c63894973:1727902404",
"7421284092215461637:7421283392116098566:29e2e9b32c12bea8:76e4dbf2-8e6d-4ae0-a61e-9595aa1073e8:1727902408",
"7421284068623009542:7421283365377508870:5924b59f4576c1bb:652a4ca4-f1d3-4802-892e-6c0fcc3aa96b:1727902412",
"7421284068363208453:7421283460109698565:9d258b9d87c5478d:6d074b20-68c9-4d04-9f9c-0a07c75ddd06:1727902416",
"7421284079830714118:7421283454325556742:d5ef8754ceee36c7:cd2d207e-0efc-4d59-9782-d6b599704ed6:1727902420",
"7421284158959306502:7421283513301337605:e06aea78eae998b3:0ade6053-de7b-4f18-9ec4-f7b945cb9da1:1727902426",
"7421284109145097990:7421283459606038022:0050f65a0a6c6845:9ec5e712-3ae7-401d-bd66-65ec7e1c4e66:1727902430",
"7421284179197789958:7421283431291045381:8d23fc707c25a341:e145e680-19ad-4c94-90f4-026f05f07d5c:1727902443",
"7421284238747666181:7421283648592823814:a3355ad8e3085656:c1a4aa0e-f609-42d0-8fe1-0f47a80ca6c7:1727902448",
"7421284235090511622:7421283733388641798:7bd2154209e5442c:5af5dcee-a4f5-410c-9eca-f480017d2d94:1727902451",
"7421284234940352262:7421283537746544134:57f3192fef128c1d:d94772c6-2c48-49a2-9526-cb6b8415503b:1727902455",
"7421284284989703941:7421283509493679621:488cea25cd7c59de:41d218a3-46ae-46c2-8d75-6db196ed3473:1727902459",
"7421284306565449478:7421283798643443206:cd00feb05153609b:1390c48a-be41-4d6f-82b5-b25f600950f1:1727902463",
"7421284319592843014:7421283737650087429:c0b0a8b869829008:db9c863c-ce62-4dd5-b1a2-e93d5f66e6dd:1727902467",
"7421284324895131398:7421283611355776518:06b740b4c9722e44:1576a2b3-be13-46e3-969a-f18c62df47bc:1727902470",
"7421284327529039621:7421283762853660166:f66405253756c562:48d1938f-ddbc-4c10-8d0e-287f49507e44:1727902474",
"7421284357274420997:7421283756146984453:35d0f57a1df05018:0a725740-534a-494e-b3ab-0dc49b475d31:1727902477",
"7421284367429093126:7421283838351033861:dcc33afb13e4b6f3:c53c5f17-64c2-443f-91c3-d77b9736bde0:1727902480",
"7421284367706818309:7421284003694528006:ad1b64cf138ce9ee:b01e0d3a-6657-416c-9964-cb48982c8a88:1727902489",
"7421284439319676677:7421283877882250757:3537e2758f8313d7:504c6a2b-8a5b-4f35-9d7b-7318563be451:1727902494",
"7421284436916487942:7421283754206332422:d1ea4a82f5492b72:e226e968-68c0-425d-978a-c5c4130216a0:1727902498",
"7421284427689264902:7421283782521947654:5afc946c94f51a7d:0e90d5fc-5cab-4fa7-8222-20a71f178178:1727902501",
"7421284440566400774:7421283813668439558:10a6173028932fc9:975e0b26-ad2b-4d83-a059-73d3e8815111:1727902505",
"7421284499625068294:7421283877882627589:bea3fa81d7155289:98a63df0-a81c-49c0-801c-64675fe091bf:1727902508",
"7421284530612537093:7421283820933121541:c3e33c0da43fcc30:efe64bff-ac71-4b44-9a35-f6b0dc13eaf6:1727902518",
"7421284611902228229:7421284073437398534:1e6b73f3dc1a47e3:c22a947e-e588-4ed5-86fe-71255c722222:1727902529",
"7421284606319560454:7421284003904718341:87004863263db16f:59c64f3b-bd6a-4233-8e7e-1675247722ed:1727902537",
"7421284671620712198:7421283977565324805:4e097cca538da691:ea215870-e39d-4c2c-b09a-7daae7cf2244:1727902546",
"7421284698582058757:7421284013137184262:d16dd3b163c5d038:4d5f845f-2411-4801-aa93-4f30515596c1:1727902554",
"7421284691628869381:7421284203408033286:16f683102d44b781:b658b899-f793-4e43-8bf5-ad317f7cf54f:1727902563",
"7421284733638592261:7421284113498129926:28b1f6b3e0a20aa9:2cd99073-15c4-4f40-b2c7-1f1841fe86a5:1727902571",
"7421284789728397061:7421284247408870917:53a568b68f97ddd9:a67246af-0311-434b-8bc1-5ff155fa87ec:1727902578",
"7421284781964707590:7421284153092359686:3405cbc52675bb09:e4baf07b-7da0-4de0-917a-8c833be28f0f:1727902582",
"7421284836444702470:7421284254161765894:ad96c9f984cb831f:c90cdc69-094c-48ac-9d98-a0e31ce68934:1727902591",
"7421284885064730373:7421284328908539398:cc8c06b59a59f75e:03f4fbcc-921b-4009-9a18-c6e218e835e5:1727902595",
"7421284824064231174:7421284458567009797:f930e45b3ac98303:d17d95cf-7e09-4726-a4b1-0cbc566ac0d8:1727902600",
"7421284918506096390:7421284276047889925:ff2c54305571b876:8a413095-e2c6-4638-873c-7e576f96f751:1727902610",
"7421284946407753477:7421284348278294022:ca058f1d96c6c076:5f9e5db0-4167-4d92-890f-ed47754ea8dc:1727902625",
"7421285036361533190:7421284444922856965:b6234089e0a4a149:f5e7d08d-1af6-4bca-bba4-3971e6e88842:1727902630",
"7421285013532477190:7421284334541637125:e69d472d2578d744:26350f97-776d-4ef4-b0ff-9cd6b6ee742d:1727902633",
"7421285030641207046:7421284408382703109:2735f3e2d3e8c303:4d0b9d4b-2b07-497f-8665-0756eb6e1e67:1727902637",
"7421285052115830534:7421284448098338310:fb0a4fb5c7210925:e5855e5a-a720-4fae-bf83-f4d72a85796c:1727902640",
"7421285035360159494:7421284334541981189:6f253fc8fa517d10:e0ef7368-ccf6-4cb2-a933-6f340e665b4d:1727902643",
"7421285043228608262:7421284376929781253:cd083ba725253e9d:8e454e68-e3da-4321-b550-b37526d4efbe:1727902647",
"7421285123116648198:7421284404498957829:d6e97211aaea0e88:8cc58204-8179-4717-b9be-8f19c8e3f4f8:1727902650",
"7421285117383313157:7421284461994558982:202677d431dd2ded:4a05dc6f-6cb8-4663-80c8-a8a55437086b:1727902654",
"7421285125289985798:7421284448098878982:da7595f81e2081e5:f1640589-fcd8-489d-a235-eff555885aac:1727902658",
"7421285171323127558:7421284494005913093:dd7757818127e7ae:32d9b31a-4b5c-41f9-a250-2ee9cfba3b0f:1727902679",
"7421285191283656453:7421284664104699398:e123ebc4c7c71c55:2f4ec39c-9087-46e7-94a1-9886323cd24f:1727902683",
"7421285257405875973:7421284701316744710:7760d5742a74218c:2b43f871-25dd-4210-bf7d-9214fd605570:1727902687",
"7421285255003653894:7421284688272082438:871bfc0b4ff8bde5:c12430a8-9dc9-42fb-a050-009cb29f0455:1727902692",
"7421285330273289990:7421284463202600454:556417d0398124d1:46c97ab3-0117-4779-a6bd-25fc7c12d8de:1727902697",
"7421285327530215173:7421284659793593862:dec3ffb2b685df03:be208534-c4be-4252-bb4b-2f508d1aa23f:1727902701",
"7421285310057531142:7421284463202960902:d4d3259b31de8fac:21572d73-e8e8-4bd2-b27b-05d4d9775d65:1727902706",
"7421285366874015494:7421284691682919941:03ef76d114ce1898:9811855e-bd87-4928-b4b9-b16c1eed9ecb:1727902711",
"7421285367310010117:7421284764345107973:9f37fd056e135079:20a8738d-fc7c-4d8c-ac2c-409925e62df0:1727902715",
"7421285364797277957:7421284782535214597:d2a278cded625c17:22769157-1054-46e0-a4eb-b33a77e6eccb:1727902719",
"7421285430953379589:7421284729100355077:a576dcb8cf37f578:8efaca4e-1f8f-40ec-b788-906930f0954e:1727902723",
"7421285435915339526:7421284719163475462:08b29e8b712951dc:69f342f0-dc46-41a6-a1df-f9260689376f:1727902728",
"7421285425174546182:7421284664106026502:1351827042d3f7a0:20766ecd-d0b1-4780-8fbb-76f853766dd3:1727902731",
"7421285548692637446:7421284935200065030:2b71a67694c0395e:4e2a065f-5dc9-4b7c-a4b9-5af54fcdf020:1727902762",
"7421285589930592005:7421284795190396421:0b9766267cc1e84b:4c1dc271-f62d-4e6c-ae6e-ecf94da4d1a8:1727902766",
"7421285610792912646:7421284849418110469:03d9f0d86ed035f3:3a872d4c-3378-48e7-875d-d0eb8636d085:1727902770",
"7421285645013976837:7421285012702414341:6ec6b21f13c543b4:214e6198-9643-4cda-970a-423776c58341:1727902775",
"7421285616631645957:7421285012702545413:a004df41e4796203:8913a70c-986c-44e9-b419-fa8f26c86e7b:1727902778",
"7421285656154162949:7421284889067570693:1eb42559446ba09c:fb684057-3cac-4701-80be-a295c5248cc5:1727902781",
"7421285646222542597:7421285144402806278:f202084b82e2e40a:70d270f0-31ec-4dc7-9592-aad67ade6a7a:1727902784",
"7421285693437626118:7421284999422887429:7193982d4d3b739b:6a7634a7-cea7-4393-adc9-a79be1dfce87:1727902788",
"7421285672865056518:7421284917311555077:6d2d22bff07da93b:03fb6693-4903-4fd7-818e-b9ca81cd3dbd:1727902792",
"7421285702942066438:7421284849418733061:80bf89ec16fcfc38:7e91f0da-bb14-40b2-a841-b8afa7ab272b:1727902795",
"7421285703969867526:7421284984353211909:780bfb570db44c33:508cea46-75f5-4dee-b8cb-0dbd73cc2a5f:1727902798",
"7421285754859489030:7421285095489160709:d54ee0859cac6aa8:1209bba5-51e2-406a-8e80-533ef27fafef:1727902809",
"7421285772173248262:7421285298744591878:c0ba74af0fbf718d:3f40a154-34f8-486f-8a4c-415b32ab67e8:1727902812",
"7421285807120385798:7421285130654238214:f5f4eb33c4d53f3b:96a694f9-cb0a-4cb1-b826-efe0b180e3d5:1727902817",
"7421285850535118597:7421285143799203334:90d70859c2f649fd:788832c5-563d-45b3-9676-075d30cef197:1727902825",
"7421285846559033093:7421285008085026309:7d73e473e9142428:b7d6f3dc-0df3-44da-b518-5e64fe9217f8:1727902829",
"7421285854088464134:7421285148333868549:8c4651d31e252487:1211159b-f222-4489-a39e-a3b6baa3023c:1727902833",
"7421285924220585733:7421285129816229381:852f5ed5f6550ca9:369901bf-91c3-4e1d-b001-2caef8f35e12:1727902837",
"7421285868177213190:7421285362116691462:bb32cc6b4e3a444c:29d291cf-f18c-4e6f-b374-afd750384b39:1727902841",
"7421285928112834309:7421285167132329478:583e4f34be96313e:f6019dfc-1600-4b13-b368-acbdb9fdb452:1727902846",
"7421285990783846149:7421285401056298501:9df8fd60786234b8:00b7e104-ff8d-475a-8e9b-bfa3faacd4ed:1727902850",
"7421285978817955590:7421285360690382342:692e1d417dab9f80:b5ac238a-d4bc-47a5-ad56-70c0cadc8484:1727902854",
"7421285962389440262:7421285447068222981:47033ddab0ae505f:69b3fbd1-173d-4283-92b1-df8f89258b15:1727902858",
"7421286053547640582:7421285520996746758:f43aa6038e674422:35982676-9f48-4faa-a11c-d726341c43d1:1727902868",
"7421286014143153926:7421285368366761477:15411f3aee619e85:c430f10d-46ed-41e9-8ee1-6a8e7d45768b:1727902872",
"7421286069415347973:7421285275282851334:97112a8856c5314d:a8da8f19-467e-4a97-a068-22b0447cc0ed:1727902875",
"7421286107771438854:7421285469268739590:4f301baccb481a98:04e61d00-7793-44fd-adb0-291b106eadf4:1727902878",
"7421286099328386821:7421285435223754246:05039f2478ebcbae:cc88e294-68f9-410b-b999-7bb278f6f2bc:1727902882",
"7421286101656930053:7421285441531954694:4f71b472bc320923:a1248ffc-bc88-45b2-a1b3-3fe758b94c7b:1727902885",
"7421286130165122821:7421285526726247941:0d3c7cac2e2ca308:29fc63bc-3983-4837-8380-4bb410c9ad8e:1727902888",
"7421286102852536069:7421285355981473286:d34484afe6fccd40:e7954c12-11ce-43ee-b222-eac7bffe517f:1727902892",
"7421286277615650565:7421285712345368070:878af5967ad26858:582a7063-2e62-4487-8e7c-c021ad851cec:1727902922",
"7421286262068168454:7421285627381270022:5d443dd9cab45949:f2773731-da41-47c7-a7ab-f01cc9fadd1f:1727902925",
"7421286321924802310:7421285660675900933:92f7e69d9611e65e:441e803d-c7d7-40f9-8d68-3e46f4c94bed:1727902932",
"7421286320096102149:7421285744389457413:5ebdf3d66f768298:68b288a4-b6d5-44f2-acb9-4805efa6ecd7:1727902935",
"7421286362940344069:7421285732247143941:ddf965185ac4c97e:07a9aaaa-699c-4292-949b-48d368fcda8f:1727902938",
"7421286335816369925:7421285593387173382:f81eff2b7f776df7:57f26dbb-ef16-4daf-ae55-e50ccb1d0854:1727902943",
"7421286376568440582:7421285694414898693:0d19be2e45b027d5:953ee4af-6585-49fb-86dd-116b0d65e08b:1727902946",
"7421286348353505029:7421285605907334662:fc0b8702d8afa429:adf3ec9b-7ffe-4d9e-bd9a-be5ee543d394:1727902949",
"7421286396314289926:7421285590790866438:ce0077cf77ed7e99:988ed004-3340-47a7-961f-bd2b583b4b73:1727902953",
"7421286403223045893:7421285593387501062:bdef76f63bfbcd8b:868afb06-24ed-4504-8c0f-2be404fa50f4:1727902956",
"7421286497980729094:7421285712010577413:60e2c3854e420a8e:e450b0ae-fb6e-49ef-8acf-5f7d4ef1c1ad:1727902977",
"7421286507174790917:7421285747616089605:80eb2d4086cd6597:bab8045f-b194-464f-ac3d-98cafbb9203f:1727902981",
"7421286543396472582:7421285970047649285:7cb62febe2b2089a:94bf0580-6715-4d16-8ab9-b09e63180f2d:1727902984",
"7421286530252031750:7421285841014130181:4a4e0d378dd9f90b:bc82041d-c4c5-42db-a13e-1b8f58419c00:1727902988",
"7421286528930907910:7421285993560507909:f20358af71b2c530:100d1975-485c-4ecb-8b5d-2713cd3f83c6:1727902992",
"7421286610827888389:7421285965580961286:98527febc7896612:462d48ae-33e8-4c57-bc6e-0eb4caf70d89:1727902995",
"7421286544013526790:7421285689579570693:b4e6aed14966e23a:e855984f-cdd7-4bac-a89c-a1ce0d08b97a:1727902999",
"7421286614162556677:7421285938854594053:12ef8863595e5128:e364b068-e5c4-4a92-8490-537d8fa0caf8:1727903002",
"7421286563072902917:7421286005372077573:262eebde6c8fe08e:f7e5d191-9e1a-4fa1-a0a3-eeffc9bba43d:1727903005",
"7421286626657912581:7421285983343396358:7c77e690702471b6:83f145f5-40c4-4850-8f33-4f00c7e45f86:1727903009",
"7421286674896013061:7421285879338092038:ee3af327d3e12cd7:7219f29a-e667-49a7-a7ef-5e9616b63406:1727903018",
"7421286718571300613:7421286107058636293:e94046cd99b655f2:db1183dc-56d4-465b-be6a-194056d4070b:1727903022",
"7421286689392576262:7421285902008567302:423e57523053572b:8bae52e2-9609-455c-9eec-155333b46bfa:1727903025",
"7421286741413660422:7421286104915002885:e5dd00ccba653209:3b7cb7f8-839b-4f9c-8760-973e823b0696:1727903029",
"7421286699018569478:7421286129108125189:9b2dc36fbe6cc340:feb2862e-56c0-40eb-aa1a-a61485ea1c5c:1727903032",
"7421286750700521221:7421285993561638405:08f1e69f6ae3c29c:12e2fb2b-7776-428f-a225-4acc8b474b8b:1727903036",
"7421286769708680965:7421286259844285958:f876b7640ce3dc80:f3e081fd-ef70-40e8-aabe-37e768dffdfc:1727903039",
"7421286747697628933:7421286047320311301:ad205e5e42c833fb:7a03ed1f-2f99-4da0-a01c-2d7c4c111dd3:1727903042",
"7421286780672706310:7421286168870077958:1e7671c48a57a6de:ceb449f4-20f0-4409-87e9-7b30f88e6c08:1727903045",
"7421286799324563205:7421286107059389957:ee764dfb0690d1d6:3e537d99-881a-42b4-b75e-cd13d06c38f3:1727903048",
"7421286830525630213:7421286123311891974:bd613bb42cf0220f:c37cec9c-fff6-4f1e-bde1-a421f2599a02:1727903052",
"7421286847835703045:7421286236880979461:f823430fd9ac85e6:2065e1d0-f6dd-4d43-a30d-ad134bdfff0f:1727903059",
"7421286849006847750:7421286178047460870:431e097621643e8f:92dbbd08-f370-4fac-8c4e-feadb3c70f95:1727903064",
"7421286906354435846:7421286115922085382:c96b412d8b83407e:62d127a5-4442-4286-91c8-f2647675b9eb:1727903068",
"7421286916220159750:7421286129109255685:0dd1d0c234cb75dd:24635b89-c28a-400a-a645-282328e00d00:1727903072",
"7421286936465606406:7421286304967198213:fe692d3c3b587c65:e761844a-ed51-4262-bb42-c730cfaa7ef1:1727903076",
"7421286902509537029:7421286347161683462:2c6c536f9f8c8cc3:9e19f955-a0c2-403e-b293-c07fb0d73a81:1727903079",
"7421286913716553477:7421286206422091269:d219fc3556102fac:c55d3c50-b6a3-43ad-a253-af59ee7931c4:1727903082",
"7421286990878115589:7421286438257493510:71a544ff0d0a1e89:def921fc-320d-4352-b9e1-b9777e772250:1727903088",
"7421286971434436357:7421286361854100998:0d75660e602de69e:31a8fca8-3710-4a61-88b2-03cdf385a409:1727903092",
"7421286979344549637:7421286391881352709:489bfa77a5af6307:d4a47deb-f07d-4513-b4c2-7eca19e39d11:1727903096",
"7421287021015156486:7421286206422582789:00a1c991398e4d76:5a614c5c-d3b4-4a89-a0c6-515a81e39fe9:1727903099",
"7421286966757967621:7421286375774963206:03c1ea670de35983:8156f296-4882-4089-9704-48ad7b5aff89:1727903102",
"7421287048940537605:7421286502271075845:7506f85a8d71a20f:4d764737-8d39-46b9-8f8a-e6a038a5b64b:1727903105",
"7421287087267317510:7421286245295506950:09edb153cde3c7b5:e308b580-44c5-46cc-9458-59579567f96e:1727903109",
"7421287053651396357:7421286365177316870:b626019a36b53df8:9a61185d-6cc4-4aca-bed8-cb83a559a349:1727903113",
"7421287090598463237:7421286326601352710:448d8e088d9fac3d:cad812cd-b4c7-450d-a564-c2cc98680884:1727903117",
"7421287099267614469:7421286385712399877:0a94256d7cb49b32:9c0c5971-45ba-4e22-86ba-b9b96220ae95:1727903120",
"7421287089587914501:7421286443891000838:ddaf0e77c16627dd:8d582413-c0cf-4582-949d-ebc894832a6d:1727903126",
"7421287164425570054:7421286438258525702:84acbdae7677ce04:b8224cb6-96a3-4f65-b038-e3f7da47641b:1727903131",
"7421287177558755078:7421286387373622789:d2f9c530ab0e664b:7c7410b1-8c46-4ca4-a8ad-bfa2d68cf236:1727903135",
"7421287198781458182:7421286651529266693:b4c5346e7d2564d9:f217f39c-1bda-4d75-a7e6-fb1711ec1496:1727903139",
"7421287168231393030:7421286624069371398:9073dacd4bd32957:c60a56b1-04f6-40bc-8448-b6c717645b12:1727903143",
"7421287249519920902:7421286584391435782:fcaf3ed9e70aeaac:3865459a-fdbe-44d5-a4ff-05ac8aab0d70:1727903146",
"7421287210895689478:7421286555798849030:9ee08e20fedfbd25:53c760ae-6deb-42c3-841c-934969ebbeb0:1727903150",
"7421287201387251461:7421286480000304645:14b233ba0cfa2fad:c12a2a57-c5b0-4036-845b-ebb8fa860b07:1727903154",
"7421287252821739269:7421286578276451845:9f053ac72c3257cf:0a0c60aa-282b-4280-8e16-c2a4f9801190:1727903157",
"7421287295929681669:7421286578276566533:500f5d94c96b077e:26de9b52-e24c-48a0-9a59-4b7156949119:1727903160",
"7421287313458104069:7421286613207025157:4235b4a9b58bc370:320211a5-3a6f-4b85-96b6-bfabb21eeb1b:1727903167",
"7421287288020633350:7421286782588945926:9bfafdd861f73504:6af8a96d-a2c9-4e36-9346-b9527f9e976e:1727903172",
"7421287313945462534:7421286668143838726:6d5a0fbbc6d6bbec:37ba667d-73f0-4450-86ff-da6e545ccb7a:1727903175",
"7421287331325708037:7421286587307509253:bb4e9e119992d1b8:940aca9a-b437-49c5-8545-56ae5a10f60d:1727903179",
"7421287375978710789:7421286720152831494:60ca813d8ce1996f:dc5992d6-eb0a-45bd-b8b5-dcc64af4645b:1727903182",
"7421287413827815173:7421286699785782790:0a378d0889451e34:ad05f3ea-382b-44cf-8c90-ddeff83bfcc5:1727903187",
"7421287434049029893:7421286684640478725:f37af6255af36cb1:6fa91a25-969e-4e3c-b212-939cf573ed92:1727903191",
"7421287392336889605:7421286816738903558:a5357b7c1c24aba9:f36b0481-bc2e-4720-bd1d-b4b44e561a1a:1727903194",
"7421287414315239174:7421286745424201222:ab16f054e04e9358:ae4fca5f-47e3-4dcb-a09a-a89945e8b9da:1727903200",
"7421287474300897030:7421286872573969926:2e316bf026dfd6c8:5de167b8-a0ec-4f35-8d99-101664f5a6cf:1727903203",
"7421287487584405253:7421286728923661829:effdc7ca0224042c:68fa5886-3b01-415c-8279-47571b640cf7:1727903209",
"7421287511991666438:7421286898737612294:60aba06892244a21:6aa84277-b277-4719-9064-3fab11285a44:1727903213",
"7421287518052386566:7421286690864891397:122e7482c3fa0f83:5ff0ae73-8884-42ef-b035-f44a99c80ce9:1727903218",
"7421287521827866374:7421286825202992645:8eb509b9296a8a0d:6678f3f4-a17c-426f-aae0-80d804673c44:1727903221",
"7421287533659637509:7421286996641154566:e7566cef37286aa8:23f77487-522f-400f-830d-1156e3961e2c:1727903226",
"7421287585735886598:7421286638994032134:6a148fb9fc92b134:e039bf3c-8021-4683-8d91-6e118bda7818:1727903229",
"7421287602231838469:7421286949727815173:b737d3eaef46fe60:c1aacaed-2fbd-437b-bd63-0d20f3032dde:1727903234",
"7421287668996114182:7421287052236654086:9f01a95f571b1453:9f7f96a5-a52e-4e8c-8675-823461514cb8:1727903238",
"7421287630279444229:7421287053457131014:245fa7426c657c36:6c667629-63ce-4f81-8c6e-5771dde0dde3:1727903242",
"7421287652005840645:7421286991461352966:8508f9c5f536738e:37a3cd58-52a1-4a79-a963-aa17979b6956:1727903246",
"7421287672544888581:7421287003704788486:aa2eb30361402518:e7b27157-66c9-48a5-9a34-cc329cff314c:1727903250",
"7421287749875091206:7421286904174773765:4a1e5a0ff1593800:43154472-b29f-4a52-9583-b59d43b0686f:1727903254",
"7421287751276152581:7421287094129526278:070a085c122d0ecc:d3a73b47-1b71-45b3-9e18-0a30af113b2b:1727903264",
"7421287729236231942:7421286995782436357:90186a01f776c7f1:9f69b1b5-d309-4db0-8fcc-285f778fe997:1727903268",
"7421287765412136709:7421287089633805830:223cf4185094270a:0bebf6d6-fb26-422a-92ef-ce5c3d57bca9:1727903272",
"7421287787133290245:7421287204397401606:759a40f2044c6258:6780ca6a-4472-4199-843e-6f5744decbb1:1727903276",
"7421287806587242246:7421287250539234822:27ceda7bcc865494:c4c23dfa-d34e-42f7-b745-af899266f63b:1727903281",
"7421287807518148357:7421287106284750341:e35976b46929c835:b68a8837-9104-4def-b335-85fb223a9742:1727903285",
"7421287792331081477:7421287063226648070:f34d33848664c439:395c0d97-3896-435c-b8ff-133449c18419:1727903291",
"7421287874157102853:7421287138648507909:56de51fa828d93b7:68f9d1ad-6516-4fde-a00d-fc2c72e711bc:1727903295",
"7421287848378926854:7421287141974558214:969b3b2ee233bceb:4aa17f3e-6fab-4fd4-80ab-0b84162839ae:1727903299",
"7421287889688217350:7421287361675380229:794e044fd0484d86:3eeb0fa1-5930-4569-8c66-91eb97b26019:1727903303",
"7421287958906406661:7421287115383162373:6f28a1aa89ffc8d1:385772be-a8fe-4aae-8567-b9a6e1e07ebb:1727903306",
"7421287918985840390:7421287147511137798:e143899f47d4cf4c:b9e7c440-bdf8-4b62-b281-a31232122b75:1727903310",
"7421287907070248709:7421287250540283398:6a1a4a37341683ec:cb865a3a-9452-4368-817d-8f3447b71714:1727903314",
"7421287966734206725:7421287293569107462:7dbd3ffc724d54f2:577e3c4f-adb6-47d7-8f18-5ca206b4fce1:1727903323",
"7421287975877576454:7421287215416854022:be72a7cb827fdf7c:cc3ce758-4b81-4476-ac4b-da8cd7ff8404:1727903328",
"7421288005631641350:7421287188241860102:5053ab23bb159cc7:2eb6bb86-779a-4b59-8b8b-4dd5068b7c3b:1727903331",
"7421287979724343046:7421287366155355654:4ac77ce5a485c3c5:48d459ee-c30b-4a56-9825-56a39d046042:1727903334",
"7421288024367908613:7421287207229785605:eea418375993bad6:08f204e1-c287-49ac-930b-2b06c7f6669d:1727903338",
"7421288031259182854:7421287405841368582:b89e07734481a3c6:7fbe6da5-44c3-475a-821f-3a31280ae9c5:1727903341",
"7421288084530579205:7421287293548758534:6fea40c6b1b3df49:0819aa0f-7f8d-4563-ad4c-037909913c77:1727903344",
"7421288099789948678:7421287410635720197:8c56ec61eab54604:7a401d26-484c-41f8-9255-5c825d7f506a:1727903350",
"7421288099375122181:7421287331024242182:ab4a65a44d51ce08:89d291b8-8280-49d3-961a-f42ba8159063:1727903355",
"7421288069163468550:7421287340386059781:fba40789c48695ec:78b06f00-4486-49af-9432-efde97cf27bd:1727903359",
"7421288151970891525:7421287538880660997:fe913732bb460716:882a84e6-c657-4ce6-a439-22ce864b97b4:1727903363",
"7421288213442660102:7421287426746107397:956c8f66fdfd3993:f117c3a5-c02d-4313-b666-8415a7960130:1727903377",
"7421288234912925445:7421287453992961541:ef3a115f70cf77a8:95b5da9e-5807-4b44-aec0-5f08ad795e9b:1727903382",
"7421288220623718150:7421287426746304005:550884698d8dd3a9:205365d8-049b-4dc0-a16b-d5dba79d5448:1727903385",
"7421288216576526085:7421287598049773061:5108aaa246d89d8c:b7590017-9adf-435d-936f-3775c9779e46:1727903388",
"7421288268483806981:7421287448636966405:560dc422b3fd8dfa:c159714f-0ff1-4f14-ae8f-06a8150fc158:1727903391",
"7421288234603284229:7421287551624070662:25c1d7be2621992e:b7494887-bb3c-49c2-9e0a-ae22ded0b79f:1727903395",
"7421288312981751557:7421287717054744070:fa1245884051b17b:761c2c25-eca9-4af9-af53-e5986c2c9f35:1727903400",
"7421288319553963781:7421287774399022598:8136d289fd9811fa:8050cefe-fdb7-42d1-b47f-82f7165c0c34:1727903404",
"7421288364449662725:7421287757492438534:4c9a2bad8d6489bf:6cc4ebb6-1034-4962-8842-ee37cabdefd0:1727903408",
"7421288349128918789:7421287545685149189:3ebc34118d6528f0:fbd30739-6211-4a44-9204-3954a2a0d98d:1727903411",
"7421288325879760646:7421287538881906181:0583e0e962f99089:8a029589-c206-4198-9b79-0e98154b9a49:1727903414",
"7421289253576050437:7421289109803582982:3f1905c759d033ce:44362132-f3cf-4714-987f-aca42737c6f8:1727903482",
"7421294482191353606:7421293807013266949:238f646403b1826a:ef58a6fa-325d-4103-a872-3a85093c1603:1727904846",
"7421294524221622022:7421293911756293637:a7c98f1e681e25e4:fdcca8e3-c8ef-4a23-95e2-8339b2c76658:1727904849",
"7421294523386676998:7421293669645829637:92521acf81eaa1cf:e66dfa31-08f8-4c90-9cbd-f40f303af10d:1727904852",
"7421294523519371014:7421293872892642822:866bd6ec2f00df74:a1cda43b-7839-4ce9-a87c-a2592327a14c:1727904855",
"7421294523519633158:7421293565987816965:21a4325beb1aba66:f1128c5f-3b44-436b-9eb7-bda0ee989511:1727904858",
"7421294553750472453:7421293995638244870:25f3a8cebeb7e79c:53fac2b7-1f1a-4175-9364-d07ce5dbade8:1727904861",
"7421294632589674245:7421293883424785926:00a99263832fc180:60788345-1827-486d-9ca5-0afdf749c10d:1727904864",
"7421294621185607430:7421293736112784902:7559e81f0ee2ce9f:bf6c4748-8a89-44b2-ba03-65a9311cf8af:1727904868",
"7421294621186033414:7421293920048891398:630e26ec73b2fd21:de26d6f7-d137-47c7-80d9-63882da6c68c:1727904872",
"7421294594590426886:7421294029008373253:199a8b026ff45fe8:0f43f62a-6624-4982-8269-7ff082ea69fa:1727904875",
"7421295406572914438:7421294753670596102:f0102547750e4055:1629e536-ab74-4ea6-a781-f40a1a6409df:1727905054",
"7421295442560452357:7421294601171338757:fb18d15e06f72fbc:62eaf263-bcd0-4380-8fb0-2cd6e6db5707:1727905058",
"7421295455897732869:7421294789242504709:a4d8ad215cfdde87:cfc790f4-37ed-4217-96e1-fcde5f0f7e95:1727905062",
"7421295442771019526:7421294672486057478:a32db89e82c4019c:e7ec5eb4-2bcd-48cc-82aa-d11d60eafd72:1727905065",
"7421295489808713477:7421294823476577798:9b31a6ede25f596c:904e6705-dff3-4f01-9b45-721395cabd82:1727905069",
"7421295453164422917:7421294627196798470:9959d78c836e131c:2c85e4d5-3699-457a-8298-4a0efc7b45e9:1727905072",
"7421295530154379013:7421294719471126021:0150be8248dcab6c:519894ce-66e5-437f-b0d2-326987bb85e5:1727905076",
"7421295480314267398:7421294672486368774:8bdd0262c356e021:0956d8fe-2c44-4b8a-9021-159a45cfcb7f:1727905079",
"7421295535501641477:7421294863800747526:0ddf55ea4d938832:9b83ab97-aae9-436b-a57e-e398697e9a10:1727905083",
"7421295531995956997:7421294753671415302:d288dac4c411fb6f:30c00440-44f0-4cfd-a129-b420f420600b:1727905086",
"7421295557350852357:7421294794293265926:0d2bb6dfc45642a0:afd83985-4fdf-4f63-800a-4052d7fd703e:1727905096",
"7421295627650909958:7421294986236855814:f324646075469ba5:83f62525-4364-4c95-9a04-47c3b8b5ecae:1727905102",
"7421295633749624582:7421294874027099654:d256e1df5aa5f00e:a8240a1d-7282-435c-b170-d7056f2c12f2:1727905106",
"7421295673406064389:7421295002124453381:a5974fcf38186fff:c41ae1ab-a47d-4eb3-be89-3b3bee20b5fb:1727905112",
"7421295695556658950:7421295022034847238:8c9d6548e69a2863:c4083272-c852-4c6c-b796-6f5e795fef18:1727905118",
"7421295702338881285:7421294911843173893:3b313d3c39c5f940:decaddda-b7f5-4be6-976f-a356c1c3cb2b:1727905121",
"7421295722634561286:7421295037663282694:0c800531247e2ab0:8cb04ff5-0ff1-4dd1-a740-7768acf25de3:1727905126",
"7421295725085263621:7421294973025666566:8d9918e0222001f8:00749947-29cc-41f1-9e10-64b9b57be75f:1727905131",
"7421295787319133957:7421295210527032837:92e5299af5f0747f:315ee12f-3ba5-44b8-824c-55bf5d81148d:1727905136",
"7421295794345215750:7421295121389684230:38babb90a0ad1ed1:f23d2a96-ca1d-4eb6-892b-24f7812ba80f:1727905141",
"7421295793749673734:7421294960157656581:015c107e25a4ab28:f87f102e-cefd-4e9d-984f-d959c37f9bf6:1727905147",
"7421295808086296325:7421295111172982277:1cc39276c18addf3:37456c9c-a6bb-42ce-9f91-30ffa1c4aac1:1727905152",
"7421295785835677445:7421294930000250374:e2bdaf584bd82611:476316a3-7c4a-4746-9384-bc52c62071d6:1727905156",
"7421295866986956550:7421295016742766085:712bcd508575936b:a37fb0af-a8ca-4c3e-8d2d-d901311ab85d:1727905161",
"7421295926305670917:7421295002125682181:1fb8151d439996fc:1fa928a0-2822-47d9-b88a-d9cf53d6e289:1727905165",
"7421295897629984517:7421295241447622149:7a129b04e8015133:9fe318d5-5368-49ce-9c40-5e7407cf64bb:1727905170",
"7421295892933019397:7421294990788560390:ffa6884d3a76189b:40884818-89d9-4160-a012-db1e7b0397fe:1727905173",
"7421295904425232134:7421295223239902726:9aab962e2280e55e:f1839e6c-ad13-4c17-bc94-e055a8ada0f0:1727905177",
"7421295978881468165:7421295269516215814:f6c0542ead8a97b2:9b6db837-a7c3-4c8b-8dea-82755419c15d:1727905181",
"7421295945474295557:7421295343750497797:21399ef1b48363b8:b14dc4bc-1ba1-447f-bfd8-7474901f7ae2:1727905184",
"7421296003812165381:7421295343750710789:f5e973c8ac7af0ef:b2ebb761-2e5d-4e3a-845f-11640b99042c:1727905189",
"7421295983005845254:7421295398775457285:0b2735e4fd0d2385:e8379dc1-1207-4c87-8e77-98c4df371e1f:1727905192",
"7421296047374567174:7421295211517707781:6eca24dc2eb8ce54:a9e12edb-d819-4bf6-8578-1b262c1dbadf:1727905196",
"7421296122272745222:7421295483232290309:5d42c41a4e3afd56:6b98c3a6-a230-4fdc-8697-2e960cd2d7cb:1727905225",
"7421296176517580549:7421295450185876998:ff285117ba9f29f2:0b2b06fd-41cd-4ab1-9c33-875a02fcc085:1727905233",
"7421296176518072069:7421295615532860933:8bf450c67508d7fa:1123463d-8d63-40df-bfbb-2290c1acf550:1727905237",
"7421296219731347205:7421295332334437893:3438d5e9896def13:ccb8595e-00b3-4b85-8783-cd8eac616f6e:1727905241",
"7421296270511326981:7421295572231112198:4cc6e062422cf15c:b8eff776-a99c-4890-9988-8c6e3e7cf292:1727905245",
"7421296211032606470:7421295462802916870:418b9eb2af983616:ebfb63b4-e652-46ff-b97e-f5af1b581335:1727905249",
"7421296245304264453:7421295321618564613:fcad01fef73d512c:02e78c47-5cc5-437e-94c7-32f28b85642e:1727905253",
"7421296323627927302:7421295535783577093:4919d9d0b9e4d278:87dc474f-995f-48fc-97f6-7481c5109507:1727905262",
"7421296349503211270:7421295535783675397:7e520c017cc23561:48d418a8-c4a6-4a96-998d-8fef52bb05ba:1727905267",
"7421296327520503557:7421295572378568197:299fcaf80e6ab3ac:1b0c9929-d2ee-479f-a660-0f31baeff071:1727905270",
"7421296369581246214:7421295748505323013:a29e9723bfcd8f2c:f7b17e03-6b9f-44d5-a6d4-bccc326b4eeb:1727905273",
"7421296376967251717:7421295612039988741:0a60200f853666cd:f4c10149-ee4e-4201-8f5f-355298fdaa5f:1727905277",
"7421296380314765061:7421295836656748038:debf85004965e1f4:222d174b-9524-4cd4-907f-3a482320d4d0:1727905283",
"7421296354260322054:7421295624157529606:af02e36628cd5b7f:65e54627-1bf9-4660-83fb-68ee990ff220:1727905286",
"7421296410341820165:7421295634467423750:fb41e7b09f4ecc44:c9fcd895-10f9-4fa4-b26d-589f22e13767:1727905289",
"7421296441962301189:7421295751856555526:3cd689e0ecb52e6e:a202fcaa-b7b8-4b38-9b2c-accf70ff5a97:1727905292",
"7421296421444372229:7421295711608784390:bf42765365464a73:936b53ce-2062-4713-9ce6-fa21b3cc2565:1727905295",
"7421296421444667141:7421295500954027526:f884300f837afc06:d0098518-661b-480d-831b-453dc941d844:1727905298",
"7421296441963202309:7421295672106993158:1ac4d5062cb6b0a6:05697ddf-62f3-429a-84f2-fd328978e8b3:1727905302",
"7421296544009766661:7421295822996653574:6576985695c2359a:238c3f3a-ce6f-4c8b-bd7b-25cc714fd341:1727905317",
"7421296523672274693:7421295723864311302:6cb18250ad46875c:a001e15b-4445-48dc-a0e7-b8e0ff0e2574:1727905321",
"7421296547583559429:7421295966412178949:5f39c297e5369b60:7b9fcc4d-271f-4d6f-85dd-3c6cdff97fce:1727905324",
"7421296586296379142:7421295988670924293:f6b6d2e64e525899:47eb0beb-ca05-4ad5-a039-77a341792d74:1727905328",
"7421296575643502341:7421295818139502085:70d97676c5d489e6:6db9089d-7555-4c09-8ef7-a9a1019f3bfd:1727905331",
"7421296608908199685:7421296031406589446:0cf93dd875dfa694:022f3a1c-caf4-4899-a635-57a3e2c7688c:1727905334",
"7421296642483521285:7421295934460184069:1cf3dca4c758241b:031a458d-5672-4b8f-9782-12851e6519d9:1727905340",
"7421296647458293509:7421296010645292550:9a7210f358259aee:01ae6585-bf44-4847-80fd-c157285894ce:1727905343",
"7421296681846769414:7421296054399747589:57699c13b75fd080:a2e7293e-0933-42fe-8030-d5ad2cdaca5a:1727905349",
"7421296720547628806:7421296053435270661:ef8550dd47ae3f42:084febd6-c297-43e2-90ae-eb89f451847e:1727905353",
"7421296756417251078:7421295816223311366:0668a3ecaa472bc4:c2679054-69c0-4d4d-93be-52c06586c579:1727905359",
"7421296689741760262:7421295844836410885:20dfb115dc519eaa:4949ce90-aa83-44fc-9ec9-246fc1b152fe:1727905362",
"7421296716547344133:7421296048779937285:3a41c0f451f80031:590cc32b-7564-4ba2-80b0-f2b1d862d0a6:1727905365",
"7421296748314543878:7421296031407556102:a691fc12f76db677:c27a999e-dafb-4bc6-a874-ff9a84785b9b:1727905368",
"7421296751112374022:7421296019491210757:95340e03476d5131:537da36b-0a6a-4054-a163-85bd4a77d140:1727905372",
"7421296750940292870:7421295844836640261:735a4649acdef7f4:2ce47407-819e-4e2d-b154-8c3ec8cb6a3b:1727905375",
"7421296773199382278:7421296055541122565:366f972e50dc1c89:3e580339-4985-43ac-a8be-ba17315984d5:1727905378",
"7421296827976959749:7421296054400517637:e91498fb15767fa8:f505d3f1-97a4-4cc0-a8bd-6abdde8a078d:1727905381",
"7421296805210638085:7421295883491739141:72e8860931ce4c31:79df474a-f358-4fa7-8f57-c0d08586b1e6:1727905384",
"7421296892905441030:7421296175480899078:6b0f61c458343f53:2480da1f-678e-4197-9309-2c716cff5888:1727905404",
"7421296901607786246:7421296091209991685:a3b61f7dfcd5775b:6bae69f7-6ab2-4c56-a4f7-3127a3e6d639:1727905408",
"7421296970322724613:7421296084964902405:388a51ce6e0de042:4c657bb5-b52e-464c-922f-07498e8ae1cb:1727905413",
"7421296924224259846:7421296230842091014:a2c67c4f1f4c1207:3e86d156-d1af-40ee-bae0-21dfdd669c97:1727905416",
"7421296983941891846:7421296238568900101:1d2777c87b8b588b:673be655-d327-434f-a929-46ba581d3075:1727905421",
"7421297035682301702:7421296096646202885:1c20195b118378b5:0b14d7e8-3b64-4fbd-8e16-7e404dd70c54:1727905424",
"7421296996370450181:7421296165885609477:b347a5225a67ddbc:f86d5bb9-de76-415b-8ca6-d7bbc2a15a9a:1727905428",
"7421297051155793669:7421296321372521989:737c217ea82b5365:800b01b5-8953-4a3c-a4a2-8dc6d1d3dc88:1727905434",
"7421297059137619717:7421296464598582790:65cffeec66ed95d7:d0f518bb-2321-4ebc-a0e2-886c660a39f4:1727905437",
"7421297106066884358:7421296364829132293:e8146f90e340f042:f41c4e7d-d299-4c64-8453-a7f696cc007b:1727905441",
"7421297083309737734:7421296314950665733:cc7337bfaa633e49:7843de71-2517-48dc-ada4-0eb2504637fb:1727905445",
"7421297218663433990:7421296577865795078:aea91ae4a7a734c7:ac6b4442-e5d2-40bd-957d-c57dc80a207c:1727905471",
"7421297187249047302:7421296620530550277:a2ec3e38040b35d1:0f673dea-a9dd-4974-a6f6-67c0d36c3317:1727905475",
"7421297217250526981:7421296643074590214:47b57a9610b8165b:f4470ad6-b015-4c0f-8524-0a7552566c07:1727905479",
"7421297220497458950:7421296581091116549:55177027afdeceff:04244f43-dc23-4ac2-8941-9a0ac208535f:1727905482",
"7421297287374669574:7421296577866188294:3b5a12ff12612435:7f5c3478-c857-49e3-90b4-66b51fca6d16:1727905489",
"7421297309546055430:7421296375206774278:d9fef3c5409e01e2:747a5f59-e49a-4eef-a3dd-39848ba26595:1727905495",
"7421297317770168070:7421296528495576582:3f5cda10a596ac04:a2db133c-7af1-4193-b9c3-ec1f81534d46:1727905498",
"7421297313757333253:7421296620531189253:e6ef9c8002c57930:b6ab0c44-94ab-4084-973e-47b37f758034:1727905501",
"7421297298028463878:7421296799971100165:118936de4d639e35:12bc9d0e-5545-4fcb-8dc1-477c1607d435:1727905505",
"7421297317771527942:7421296723164972550:60f63965f95bbebb:3a8a20fb-8ada-4bef-b1f2-14512e0362df:1727905509",
"7421297374599677701:7421296736679527942:453bc82a99fcae1b:ad8eb618-d9d0-426c-b324-187a9c9dbb35:1727905512",
"7421297587430590213:7421296838672188933:ed39fa16f0669349:c37b6f2c-a355-48d1-ac89-c187d2cf7aa8:1727905557",
"7421297580079286021:7421297078195979781:6715718415f418a5:ddaf6fe2-836c-4033-9a18-a11f46cec405:1727905562",
"7421297615826175749:7421297072349578757:6a396d7d9895bfa0:19382962-05ac-4c23-8186-2bec8ad7b4f5:1727905566",
"7421297629437445894:7421296840803436037:bdf9a633a38012b8:d7dd1ae3-2b7c-426b-9996-216dbf891d32:1727905570",
"7421297629894248197:7421296743802062341:6d9a1b8a730ec5cc:2fd27075-d93b-401c-b3d5-4f16f8beed96:1727905573",
"7421297672218937093:7421296707949135365:2573a481ee27431a:5c6de08d-013f-41c6-9896-457454ec7343:1727905578",
"7421297706150168325:7421296942829143558:75f0f86219bacb9e:a0659479-d436-410d-abd5-3464517346fe:1727905581",
"7421297672221296389:7421297055324734982:84974c59d19b94bd:83a819db-9a9f-456b-a77a-cadedaab41d4:1727905585",
"7421297711872313094:7421297091634546181:0fda01deb68ba5f8:0b683934-cc7a-4a46-ab28-3a2b9e7b7d1e:1727905588",
"7421297718234007302:7421297017601869318:b6d6c3081a713af8:ed80394a-f949-4a45-851b-59ad17a0192e:1727905592",
"7421297748949370630:7421296836223682053:b4170765f3aea80e:afa26459-88af-4c72-8529-9fe2df5cbc8b:1727905596",
"7421297788685731590:7421297169012049414:abc835c5f4480f8f:2efa8351-6acc-4e53-a1dc-8380d0168403:1727905612",
"7421297801425323782:7421297169012262406:170c5a54ec80e5ce:82afc787-92c7-4598-96c9-345fe356717e:1727905617",
"7421297862195775237:7421297407817745925:8d8a07dc61fee928:93088c4d-20ef-483b-9cc1-1d90e05c0e2d:1727905622",
"7421297844159891206:7421297172072891910:f0a44b33ec96ef01:53669430-acb5-48e9-93a0-ed428608e3fc:1727905625",
"7421297855677810438:7421297156823107078:f557db0b78abe266:fafddecb-58e1-41a0-909e-867694a2196e:1727905629",
"7421297862968329990:7421297110425716230:99ded624021a3c7c:29923299-19ed-4ec7-bc72-8bce97f0be6b:1727905633",
"7421297893757929221:7421297177085838854:2613a09f43042cbf:5d7377a8-84f8-4708-bc41-919d3119af4a:1727905636",
"7421297911583934213:7421297234983699974:70f936b85a1d2c94:077a01c2-c5ba-448c-9a41-2a9b362916a3:1727905641",
"7421297971087918853:7421297251223766534:137f4a7d9ec5387b:443811ed-e5d3-4044-b25d-2aec8723581e:1727905646",
"7421297968517416710:7421297365941847558:07972aa771f8404b:33267031-fe6f-46fd-9ae3-838291c0c6ef:1727905649",
"7421297962197223174:7421297278424204806:dabbabe3e6d70b8c:943ab64b-80fe-43b4-a5e0-3e6658e1138b:1727905653",
"7421298015624267525:7421297447529645573:0c9b9a89413c493b:4ce59918-c12d-4c1a-8e10-618926338241:1727905673",
"7421298101249656582:7421297307545355781:9c081521fc9400c3:71108884-adb8-47ee-adc5-faee2fd3f2f8:1727905677",
"7421298080861898501:7421297315422504454:14e3daa0f4c371c7:d6deac33-8357-4d2b-bee4-29f4a3dafd70:1727905682",
"7421298126256080645:7421297320648558085:f00a06df7c460f99:30fc5c1a-010d-4102-afc3-5197c4197878:1727905690",
"7421298112260704006:7421297496779097605:6922eba12e7a8ed6:6cfb53b2-8363-497c-995e-965cff9fed48:1727905694",
"7421298158071170822:7421297407432869381:4aee6d9f5dc2699e:23cd7d80-13e9-4015-a693-390b1f6583d9:1727905698",
"7421298165326939910:7421297357432440325:f4c63abae2d1e5ad:ac78ff44-b8a3-4181-b062-b11d032bd748:1727905703",
"7421298219100964614:7421297561207965189:dcec126be6b29a7f:48e3bb3e-b726-4792-bb13-d77427f6d94a:1727905707",
"7421298189524027141:7421297503301535238:65c93b47d8e0d6be:25e063a9-4739-43b9-a24f-ddbd78248b58:1727905710",
"7421298268988491525:7421297549028099590:20c6dc20144b39c3:1105c5e0-2b5a-45dc-81e7-161e1ae0c0de:1727905715",
"7421298220633294598:7421297637778982406:d4ade5c87b448066:0b08f964-ffb4-4b6d-bcc6-3e63b0d926e0:1727905719",
"7421298280157644550:7421297588156679685:bde73674820e3548:016c9369-dedd-4924-886e-fc599c5e1e3e:1727905723",
"7421298320419047174:7421297441117324806:31555ff6c61eea69:656e854d-1b06-498c-ba7e-8522ecc39edd:1727905730",
"7421298353935566598:7421297503302059526:b602a7b1681da3c4:638e129e-2081-4385-b21c-fe2ac1b892ef:1727905736",
"7421298376093927174:7421297532755002885:26b08079cd3db3f5:dabcf4be-55c1-4f8d-b419-fa40f56cb248:1727905739",
"7421298348815353605:7421297712244819462:c95b0e4b6c74bee8:6bfdbc83-d22b-49cf-a175-d4c245ed1eae:1727905742",
"7421298378245801734:7421297692225603077:1d8e50d5d2327521:9453bcad-a226-4d2b-b7ac-22997c934a9c:1727905746",
"7421298403495298821:7421297712244983302:5dc0db03a318cba8:00ca5cfd-795a-480f-8118-c0da7c70e169:1727905749",
"7421298362656769798:7421297704984512005:be46a81b5b41735b:45a26326-3fb5-4741-b519-50ad43ea3712:1727905753",
"7421298434055636742:7421297646251378182:85c643b37f76cfef:3452859c-bdd1-49b0-b236-6ca238d9fbda:1727905758",
"7421298434362263301:7421297733589550598:806294c12c981a52:19bc8f73-c153-4f45-b187-a486b8319c48:1727905762",
"7421298458197509893:7421297616594519557:ffbfdb7af7eb496e:921a4a5b-9ee4-45d6-84b9-f2e7ad3ac30f:1727905765",
"7421298448748906246:7421297721837258246:3425fe8feded0c81:ff50bbd5-8a85-488a-97df-8b581be1c614:1727905769",
"7421298530335328005:7421297873423386117:b686d65dffb75d40:b635f898-ca11-422e-8ea0-bcadc5a85a98:1727905775",
"7421298547665995526:7421297575893321222:84593af3fa7636f9:65b55f15-42f2-4f3b-9af9-cf74335df3e8:1727905780",
"7421298523273348870:7421297710161511941:5f8132606f5d2346:bf4460b2-2a72-4615-839d-72a0eb7dd41c:1727905783",
"7421298569246246662:7421297575893452294:68ba63859a42d879:4539108b-6147-4749-b062-16bcea71068c:1727905787",
"7421298552763320069:7421297893566318086:cbe4464442323b76:0e9ece96-7a6b-4c96-9db8-231830e1026e:1727905791",
"7421298591304599302:7421297821745808902:bc421655347a7ef4:ec59c865-cf56-4b7d-a6a2-e13f94ad4a3c:1727905796",
"7421298593925351174:7421297809108354565:94f057ab5b20048f:bc7d2014-9652-4a4f-b9eb-dc3ecc9a6e77:1727905799",
"7421298577568466694:7421297767811565061:8e0e8fcb498df580:3aad5f12-6181-474b-9df9-d83abcd23447:1727905803",
"7421298666125707014:7421297877588444678:1b045f66261b97fd:200e0a75-38ae-4e45-bafc-7cd9bdac637c:1727905807",
"7421298661139351301:7421298040025302534:01384d3c6f31b8cf:9083ea97-ea5e-4d63-8113-20af0805ad27:1727905814",
"7421298680156833541:7421298040830739973:4f49c71380b8922e:4c7a312f-9796-4eaf-b71a-d455418b27bb:1727905818",
"7421298759428032262:7421298099764626950:b27852a934a2dbae:6d69ca9c-6b23-469a-acfd-a952aa8b22c1:1727905825",
"7421298729652864774:7421297821893133830:57089b6900ec182b:ace86f76-e89c-4f01-9a67-333a3e9990fc:1727905828",
"7421298719792842501:7421297920153486853:7d21cae31d1a34aa:d047a8f5-3e25-4f99-b2ea-c3356f5c89f5:1727905832",
"7421298808413374214:7421298014432413190:7f9f56cef59547ef:5d8f6658-f105-4364-a6f3-b019a65bff52:1727905838",
"7421298784787498758:7421297924399482374:e969c38cdb7e62d4:c8e92021-3546-4104-9bc5-bd3aabea5f90:1727905841",
"7421298777334728453:7421298053657003526:5bba66aa6a547c41:a119479b-6d39-4da6-b1bf-9d334f930f8f:1727905847",
"7421298765640484614:7421298069252326918:8fe740ffadaa8edd:091eed31-d9fc-4d4b-83c8-3b0a722dbc9b:1727905849",
"7421298823610517254:7421298030186612229:5a1b49c54299e704:623247d2-b316-474b-8a42-069e30358149:1727905853",
]


def tt_encrypt(data) -> str:
  return AFRITON().encrypt(json.dumps(data).replace(" ", ""))
def device_register() -> dict:
      _rticket,ts,ts1,icket=tim()
      openudid = hexlify(random.randbytes(8)).decode()
      cdid = str(uuid4())
      google_aid = str(uuid4())
      clientudid = str(uuid4())
      req_id = str(uuid4())
      url = f"https://log-va.tiktokv.com/service/2/device_register/?ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=170404&version_name=17.4.4&device_platform=android&ab_version=17.4.4&ssmix=a&device_type=SM-G611M&device_brand=samsung&language=en&os_api=28&os_version=9&openudid={openudid}&manifest_version_code=2021704040&resolution=720*1280&dpi=320&update_version_code=2021704040&_rticket={icket}&_rticket={_rticket}&storage_type=2&app_type=normal&sys_region=US&appTheme=light&pass-route=1&pass-region=1&timezone_name=Europe%252FBerlin&cpu_support64=false&host_abi=armeabi-v7a&app_language=en&ac2=wifi&uoo=1&op_region=US&timezone_offset=3600&build_number=17.4.4&locale=en&region=US&ts={ts}&cdid={cdid}"
      
      payload = {"magic_tag":"ss_app_log","header":{"display_name":"TikTok","update_version_code":2021704040,"manifest_version_code":2021704040,"app_version_minor":"","aid":1233,"channel":"googleplay","package":"com.zhiliaoapp.musically","app_version":"17.4.4","version_code":170404,"sdk_version":"2.12.1-rc.5","sdk_target_version":29,"git_hash":"050d489d","os":"Android","os_version":"9","os_api":28,"device_model":"SM-G611M","device_brand":"samsung","device_manufacturer":"samsung","cpu_abi":"armeabi-v7a","release_build":"e1611c6_20200824","density_dpi":320,"display_density":"xhdpi","resolution":"1280x720","language":"en","timezone":1,"access":"wifi","not_request_sender":0,"mcc_mnc":"26203","rom":"G611MUBS6CTD1","rom_version":"PPR1.180610.011","cdid":cdid,"sig_hash":"e89b158e4bcf988ebd09eb83f5378e87","gaid_limited":0,"google_aid":google_aid,"openudid":openudid,"clientudid":clientudid,"region":"US","tz_name":"Europe\\/Berlin","tz_offset":7200,"oaid_may_support":False,"req_id":req_id,"apk_first_install_time":1653436407842,"is_system_app":0,"sdk_flavor":"global"},"_gen_time":1653464286461}
      
      headers = {
        "Host": "log-va.tiktokv.com",
        "accept-encoding": "gzip",
        "sdk-version": "2",
        "passport-sdk-version": "17",
        "content-type": "application/octet-stream",
        "user-agent": "okhttp/3.10.0.1"
      }
      response = request("POST", url, headers=headers, data=bytes.fromhex(tt_encrypt(payload))).json()

      try:
       install_id = response["install_id_str"]
       device_id = response["device_id_str"]
       ti=response['server_time']
       return install_id,device_id,openudid,cdid,ti
      except:
        rfr=random.choice(http)
        install_id=rfr.split(':')[0]
        device_id=rfr.split(':')[1].split(':')[0]
        openudid=rfr.split(':')[2].split(':')[0]
        cdid=rfr.split(':')[3].split(':')[0]
        ti=rfr.split(':')[4]
      
        return install_id,device_id,openudid,cdid,ti


class Xgorgon:
    def __init__(self, params: str, data: str) -> None:

        self.params = params
        self.data = data
        self.cookies = None

    def hash(self, data: str) -> str:
        _hash = str(hashlib.md5(data.encode()).hexdigest())

        return _hash

    def get_base_string(self) -> str:
        base_str = self.hash(self.params)
        base_str = (
            base_str + self.hash(self.data) if self.data else base_str + str("0" * 32)
        )
        base_str = (
            base_str + self.hash(self.cookies)
            if self.cookies
            else base_str + str("0" * 32)
        )

        return base_str

    def get_value(self) -> json:
        base_str = self.get_base_string()

        return self.encrypt(base_str)

    def encrypt(self, data: str) -> json:
        unix = int(time.time())
        len = 0x14
        key = [
            0xDF,
            0x77,
            0xB9,
            0x40,
            0xB9,
            0x9B,
            0x84,
            0x83,
            0xD1,
            0xB9,
            0xCB,
            0xD1,
            0xF7,
            0xC2,
            0xB9,
            0x85,
            0xC3,
            0xD0,
            0xFB,
            0xC3,
        ]
        param_list = []
        for i in range(0, 12, 4):
            temp = data[8 * i : 8 * (i + 1)]
            for j in range(4):
                H = int(temp[j * 2 : (j + 1) * 2], 16)
                param_list.append(H)

        param_list.extend([0x0, 0x6, 0xB, 0x1C])

        H = int(hex(unix), 16)

        param_list.append((H & 0xFF000000) >> 24)
        param_list.append((H & 0x00FF0000) >> 16)
        param_list.append((H & 0x0000FF00) >> 8)
        param_list.append((H & 0x000000FF) >> 0)

        eor_result_list = []

        for A, B in zip(param_list, key):
            eor_result_list.append(A ^ B)

        for i in range(len):

            C = self.reverse(eor_result_list[i])
            D = eor_result_list[(i + 1) % len]
            E = C ^ D

            F = self.rbit_algorithm(E)
            H = ((F ^ 0xFFFFFFFF) ^ len) & 0xFF
            eor_result_list[i] = H

        result = ""
        for param in eor_result_list:
            result += self.hex_string(param)

        return {"X-Gorgon": ("0404b0d30000" + result), "X-Khronos": str(unix)}
    def rbit_algorithm(self, num):
        result = ""
        tmp_string = bin(num)[2:]

        while len(tmp_string) < 8:
            tmp_string = "0" + tmp_string

        for i in range(0, 8):
            result = result + tmp_string[7 - i]

        return int(result, 2)

    def hex_string(self, num):
        tmp_string = hex(num)[2:]

        if len(tmp_string) < 2:
            tmp_string = "0" + tmp_string

        return tmp_string

    def reverse(self, num):
        tmp_string = self.hex_string(num)

        return int(tmp_string[1:] + tmp_string[:1], 16)