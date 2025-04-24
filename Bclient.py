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