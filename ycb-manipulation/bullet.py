import pybullet as pb
import os
import time

pb.connect(pb.GUI)


dirs = os.listdir("./")
for d in dirs:
    if not '0' in d:
        continue
    
    name = os.path.join("./", d, "model.urdf")
    pb.loadURDF(name)

while True:
    pass