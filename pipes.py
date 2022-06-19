import os, sys

class Pipes:
    def __init__(self, path):
        self.path = path

    def write_pipe(self, data):
        with open(self.path, "wb") as file:
            file.write(bytes(data))  
    
    def read_pipe(self, data_length):
        with open(self.path, "rb") as file:
            data = file.read(data_length)
        return int.from_bytes(data, "big")