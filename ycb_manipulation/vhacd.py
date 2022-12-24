import pybullet as pb
import os

pb.connect(pb.DIRECT)

dirs = os.listdir("./")
for d in dirs:
    if not '0' in d:
        continue
    

    name_in = os.path.join("./", d, "google_16k", "textured.obj")
    name_out = os.path.join("./", d, "google_16k", "vhacd.obj")
    name_log = os.path.join("./", d, "google_16k", "log.txt")

    pb.vhacd(name_in, name_out, name_log)

