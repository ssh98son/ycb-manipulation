import os
from setuptools import setup, find_packages

setup_py_dir = os.path.dirname(os.path.realpath(__file__))
need_files = []
datadir = "ycb_manipulation"

hh = setup_py_dir + "/" + datadir

for root, dirs, files in os.walk(hh):
  for fn in files:
    ext = os.path.splitext(fn)[1][1:]
    if ext and ext in 'urdf sdf xml stl ini obj mtl png'.split(
    ):
      fn = root + "/" + fn
      need_files.append(fn[1 + len(hh):])


setup(
  name="ycb_manipulation",
  version="0.1",
  author="Sanghyeon Son",
  description="Selected YCB objects for manipulation tasks.",
  license="MIT",
  python_requires='>=3',
  keywords="urdf model object simulation pybullet",
  packages=find_packages(),
  package_dir={'': '.'},
  package_data={'ycb_manipulation': need_files},
  url="https://github.com/ssh98son/ycb-manipulation",
)