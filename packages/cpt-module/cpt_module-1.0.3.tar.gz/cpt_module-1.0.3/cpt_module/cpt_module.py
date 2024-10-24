import ctypes
import os

_lib = None

def _load_lib():
    """Internal function to load the Rust shared library."""
    global _lib
    if _lib is None:
        lib_path = os.path.join(os.path.dirname(__file__), 'libcpt_module.so')
        _lib = ctypes.CDLL(lib_path)

        _lib.encrypt_data.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
        _lib.encrypt_data.restype = ctypes.POINTER(ctypes.c_ubyte)

        _lib.decrypt_data.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
        _lib.decrypt_data.restype = ctypes.POINTER(ctypes.c_ubyte)

        _lib.free_buffer.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t]

def encrypt_data(data: bytes|str, password: bytes|str) -> bytes:
    """
    Encrypt the given data using the specified password.

    Args:
        data (bytes | str): The data to be encrypted. If a string is provided, it will be encoded to UTF-8.
        password (bytes | str): The password used for encryption. If a string is provided, it will be encoded to UTF-8.

    Returns:
        bytes: The encrypted data in bytes.

    Example:
        >>> from cpt_module import encrypt_data
        >>> data = b"Hello, world!"
        >>> password = b"password123"
        >>> encrypted = encrypt_data(data, password)
        >>> print(encrypted)
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    if isinstance(password, str):
        password = password.encode('utf-8')
    
    _load_lib()
    out_len = ctypes.c_size_t()
    data_ptr = (ctypes.c_ubyte * len(data))(*data)
    pass_ptr = (ctypes.c_ubyte * len(password))(*password)

    encrypted_ptr = _lib.encrypt_data(data_ptr, len(data), pass_ptr, len(password), ctypes.byref(out_len))
    encrypted_data = bytes(ctypes.cast(encrypted_ptr, ctypes.POINTER(ctypes.c_ubyte))[:out_len.value])

    _lib.free_buffer(encrypted_ptr, out_len.value)
    return encrypted_data

def decrypt_data(data: bytes|str, password: bytes|str) -> bytes:
    """
    Decrypt the given data using the specified password.

    Args:
        data (bytes | str): The encrypted data to be decrypted. If a string is provided, it will be encoded to UTF-8.
        password (bytes | str): The password used for decryption. If a string is provided, it will be encoded to UTF-8.

    Returns:
        bytes: The decrypted data as bytes.

    Example:
        >>> from cpt_module import decrypt_data
        >>> encrypted = b"...encrypted bytes here..."
        >>> password = b"password123"
        >>> decrypted = decrypt_data(encrypted, password)
        >>> print(decrypted)
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    if isinstance(password, str):
        password = password.encode('utf-8')
    _load_lib()
    out_len = ctypes.c_size_t()
    data_ptr = (ctypes.c_ubyte * len(data))(*data)
    pass_ptr = (ctypes.c_ubyte * len(password))(*password)

    decrypted_ptr = _lib.decrypt_data(data_ptr, len(data), pass_ptr, len(password), ctypes.byref(out_len))
    decrypted_data = bytes(ctypes.cast(decrypted_ptr, ctypes.POINTER(ctypes.c_ubyte))[:out_len.value])

    _lib.free_buffer(decrypted_ptr, out_len.value)
    return decrypted_data.decode("utf-8")
