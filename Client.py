import socket 

host = "localhost"
port = 7777

def auto(low, high):
    return str((low + high) // 2)

def get_range(difficulty):
    if difficulty == 1:
        return 1, 10
    elif difficulty == 2:
        return 1, 50
    return 1, 100

s = socket.socket()
s.connect((host, port))

data = s.recv(1024)
print(data.decode().strip())

manual_inputs = 0
low, high = 0, 0
difficulty = None
last_guess = None

while True:
    try:
        if manual_inputs < 1:
            user_input = input("").strip()
            if manual_inputs == 0:
                difficulty = int(user_input)
                low, high = get_range(difficulty)
        else:
            user_input = auto(low, high)
            print(user_input)
            last_guess = int(user_input)

        s.sendall(user_input.encode())

        reply = s.recv(1024).decode().strip()

        if "CORRECT!" in reply:
            print(reply)
            break
        if "Lower" in reply:
            high = last_guess - 1
        elif "Higher" in reply:
            low = last_guess + 1

        manual_inputs += 1
        print(reply)
        continue
    except ConnectionAbortedError as e:
        reply = s.recv(1024).decode().strip()
        print(reply)
        break

s.close()