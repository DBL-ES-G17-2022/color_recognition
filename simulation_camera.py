import os
from pipes import Pipes
import numpy as np

class SimulationCamera():


    def __init__(self) -> None:
        self.pipe = Pipes(os.getenv("RIOL_PIPE_DIRECTORY") + "ColorCamera")
        self.x = 300
        self.y = 300
        self.size = self.x * self.y * 12
    
    def get_frame(self) -> None:
        data = self.pipe.read_pipe(self.size)
        scalled_data = (np.array(data) * 255).astype(np.uint8)
        reshaped_data = scalled_data.reshape(self.x, self.y, 3)
        return np.array(list(reshaped_data[::-1,:,::-1]))


