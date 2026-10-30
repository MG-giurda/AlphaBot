import socket
from libreria import AlphaBot

HOST = "0.0.0.0"  
PORT = 5000

robot = AlphaBot()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server in ascolto sulla porta {PORT}...")

try:
    while True:
        conn, addr = server.accept()
        print("Client connesso:", addr)

        while True:
            dati = conn.recv(1024).decode().lower()
            if not dati:  
                break

            for comando in dati:
                if comando == "w":
                    robot.forward()
                elif comando == "s":
                    robot.backward()
                elif comando == "a":
                    robot.left()
                elif comando == "d":
                    robot.right()
                elif comando == "x":
                    robot.stop()

        robot.stop()
        conn.close()
        print("Client disconnesso")
finally:
    server.close()
    robot.cleanup()