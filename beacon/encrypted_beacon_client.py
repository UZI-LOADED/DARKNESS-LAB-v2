from cryptography.fernet import Fernet
import socket

key = Fernet.generate_key()
cipher = Fernet(key)

s = socket.socket()
s.connect(("127.0.0.1", 4444))

msg = b"Status: System breached."
s.send(cipher.encrypt(msg))
s.close()
