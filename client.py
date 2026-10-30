import socket

IP_ROBOT = "192.168.1.112"  
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP_ROBOT, PORT))

print("W avanti, S indietro, A sinistra, D destra, X stop, Q esci (poi premi Invio)")

try:
    while True:
        tasto = input("> ").lower()

        if tasto == "q":
            break
        if tasto in ("w", "a", "s", "d", "x"):
            client.send(tasto.encode())
finally:
    client.send(b"x")  
    client.close()