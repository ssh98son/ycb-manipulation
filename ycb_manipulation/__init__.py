import os


def getDataPath():
  resdir = os.path.join(os.path.dirname(__file__))
  return resdir


def getObjectNames():
  dir = getDataPath()
  names = []
  for name in os.listdir(dir):
    if "0" not in name:
      continue

    names.append(name)

  return names
