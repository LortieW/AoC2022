class Node:
    def __init__(self, parent) -> None:
        self.parent = parent
        self.folders = {}
        self.files = {}
    
    def files_size(self):
        return sum(self.files.values())
    
    def folders_size(self):
        return sum([folder.size() for folder in self.folders.values()])
    
    def size(self):
        return self.files_size() + self.folders_size()

class Directory:
    def __init__(self) -> None:
        self.root: Node = Node(None)
        self.head: Node = None
    
    def create(self, path):
        self.head = self.root
        with open(path, "r") as f:
            for line in f:
                match line.split():
                    case ['$', arg, val] if 'cd' in arg:
                        self.move_head(val)
                        continue
                    case [arg, val] if arg.isnumeric(): # arg is file size
                        self.add_file(filename=val, size=int(arg))
                        continue
    
    def add_file(self, filename, size):
        self.head.files.setdefault(filename, size)
       
    def move_head(self, value):
        match value:
            case '/':
                self.head = self.root
            case '..':
                self.head = self.head.parent
            case _:
                self.head = self.head.folders.setdefault(value, Node(self.head))

class DirectoryParser:
    def __init__(self, directory: Directory) -> None:
        self.directory = directory
        self.memo = 70000000 - directory.root.size() # get unused space
        self.required = 30000000 - self.memo
    
    # Find the smallest directory that,
    # if deleted, would free up enough space
    # on the filesystem to run the update
    def find(self):
        self.parse(self.directory.root)
        return self.memo
    
    def parse(self, node: Node):
        files = node.files_size()
        folders = sum([self.parse(folder) for folder in node.folders.values()])
        size = folders + files
        if size >= self.required:
            self.memo = min(size, self.memo)
        return size
    
def main():
    directory = Directory()
    directory.create("./input.txt")
    directory_parser = DirectoryParser(directory)
    print(directory_parser.find())
        
if __name__ == '__main__':
    main()