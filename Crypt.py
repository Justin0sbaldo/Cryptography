cachetools:

python
from cryptography.fernet import Fernet
from cachetools import cached, TTLCache

# Генерация ключа для шифрования
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Кэш с TTL (временем жизни) в секундах
cache = TTLCache(maxsize=100, ttl=300)

# Функция для шифрования данных
def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Функция для дешифрования данных
def decrypt_data(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode()

# Декоратор для кэширования результатов функции с использованием ключа
@cached(cache)
def get_encrypted_data(key, data):
    encrypted_data = encrypt_data(data)
    return encrypted_data

# Пример использования функций
data = "Hello, world!"

encrypted_data = get_encrypted_data(key, data)
print("Encrypted data:", encrypted_data)

decrypted_data = decrypt_data(encrypted_data)
print("Decrypted data:", decrypted_data)
