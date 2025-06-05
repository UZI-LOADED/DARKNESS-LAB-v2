from cryptography.fernet import Fernet
import socket

key = b'your_saved_key_here'  # Save and reuse key from client
cipher = Fernet(key)

s = socket.socket()
s.bind(("0.0.0.0", 4444))
s.listen(1)

conn, addr = s.accept()
data = conn.recv(1024)
print("[RECV] Decrypted Beacon:", cipher.decrypt(data).decode())
