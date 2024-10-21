from setuptools import setup
from pathlib import Path
import os

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

if __name__ == "__main__":
  long_description = read_file('./README.md')
  this_directory = Path(__file__).parent
  setup(
    packages = ['together_forever'],
    long_description=long_description,
    long_description_content_type='text/markdown'
  )
