
import os
import sys

class Tree:
    def __init__(self):
        self.dirCount = 0
        self.fileCount = 0

    def register(self, absolute):
        if os.path.isdir(absolute):
            self.dirCount += 1
        else:
            self.fileCount += 1

    def summary(self):
        return str(self.dirCount) + " directories, " + str(self.fileCount) + " files"

    def walk(self, directory, prefix = "", exclude = [], stdout = sys.stdout):
        filepaths = sorted([filepath for filepath in os.listdir(directory)])

        for index in range(len(filepaths)):
            exclude = set(exclude)
            if filepaths[index] in exclude:
                continue
            if filepaths[index][0] == ".":
                continue

            absolute = os.path.join(directory, filepaths[index])
            self.register(absolute)

            if index == len(filepaths) - 1:
                print(prefix + "└── " + absolute, file = stdout, flush=True)
                if os.path.isdir(absolute):
                    self.walk(absolute, prefix + "    ", exclude, stdout)
            else:
                print(prefix + "├── " + absolute, file = stdout, flush=True)
                if os.path.isdir(absolute):
                    self.walk(absolute, prefix + "│   ", exclude, stdout)