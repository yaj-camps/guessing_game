import socket
import random

host = "localhost"
port = 7777

banner = b"""
====GUESSING GAME===
enter guess:"""

def generate_random(difficulty):
    if difficulty == 1:
        return random.randint(1,10)
    elif difficulty == 2:
        return random.randint(1,50)
    return random.randint(1,100)

def get_difficulty(c):
    difficulty_display = """
    Difficulty
    ==========
    1) easy
    2) medium 
    3) hard
    enter choice:"""
    c.sendall(difficulty_display.encode())
    difficulty = int(c.recv(1024).decode().strip())
    return difficulty

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

print("server is listening in port %s" % (port))

conn = None
guessme = 0

while True:
    if conn is None:
        print("waiting for connection..")
        conn, addr = s.accept()
        print(f"New client : {addr[0]}")
        difficulty = get_difficulty(conn)
        guessme = generate_random(difficulty)
        print(f"Number to guess: {guessme}")
        conn.sendall(banner)
    else:
        client_input = conn.recv(1024)
        guess = int(client_input.decode().strip())
        print(f"user guess attempt: {guess}")
        if guess == guessme:
            conn.sendall(b"CORRECT!")
            conn.close()
            conn = None
            continue
        elif (guess > guessme):
            conn.sendall(b"=Guess Lower\nenter guess: ")
            continue
        elif (guess < guessme):
            conn.sendall(b"=Guess Higher\nenter guess: ")
            continue
s.close()