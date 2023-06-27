#!python

import os
import subprocess


def main():
    path = os.path.dirname(__file__)
    subprocess.run(["jupyter", "notebook", f"--notebook-dir={path}"])
