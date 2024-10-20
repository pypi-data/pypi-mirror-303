# SF3 - Secure File Encryption and Execution Tool
# Created by CODESF3 (@c_ega on Telegram)
# Copyright (c) 2023 CODESF3. All rights reserved.

import marshal
import base64
import zlib
import types
import sys

def encrypt_and_compile(code: str) -> bytes:
    compiled_code = compile(code, '<string>', 'exec')
    marshalled = marshal.dumps(compiled_code)
    compressed = zlib.compress(marshalled)
    encoded = base64.b85encode(compressed)
    return encoded

def decrypt_and_run(encrypted_code: bytes):
    g = globals().copy()
    l = lambda f: f()
    e = lambda x: exec(x, g)
    d = lambda x: base64.b85decode(x)
    z = lambda x: zlib.decompress(x)
    m = lambda x: marshal.loads(x)
    c = lambda x: types.FunctionType(x, g)
    s = lambda x: sys.modules[x]
    
    l(lambda: e(m(z(d(encrypted_code)))))

# مثال على الاستخدام
if __name__ == "__main__":
    print("SF3 - Secure File Encryption and Execution Tool")
    print("Created by CODESF3 (@c_ega on Telegram)")
    
    sample_code = """
print("هذا مثال على كود مشفر باستخدام SF3")
for i in range(5):
    print(f"العدد: {i}")
"""
    
    encrypted = encrypt_and_compile(sample_code)
    print("الكود المشفر:", encrypted)
    
    print("\nتنفيذ الكود المشفر:")
    decrypt_and_run(encrypted)
