import struct
import os

class Pipes:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(path):
            mode = 0o600
            os.mkfifo(path, mode)

    def write_pipe(self, data):
        with open(self.path, "wb") as file:
            file.write(bytes(data))  
    
    def read_pipe(self, data_length):
        with open(self.path, "rb") as file:
            data = file.read(data_length)
        return struct.unpack(">" + str(int(data_length / 4)) + "f", data)