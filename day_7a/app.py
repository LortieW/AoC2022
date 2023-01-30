class Node:
    def __init__(self, parent) -> None:
        self.parent = parent
        self.childs = {}
        self.files = {}
    
    def sum_of_files(self):
        return sum(self.files.values())

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
                self.head = self.head.childs.setdefault(value, Node(self.head))

class DirectoryParser:
    def __init__(self) -> None:
        self.memo = 0
    
    # Get at most 100 000
    def get_at_most(self, root: Node):
        self.memo = 0
        self.parse(root)
        return self.memo

    def parse(self, node: Node):
        files_size = node.sum_of_files()
        childs_size = sum([self.parse(child) for child in node.childs.values()])
        size = files_size + childs_size
        if size <= 100000:
            self.memo += size
        return size

def main():
    directory = Directory()
    directory.create("./day_7a/input.txt")
    total_size = DirectoryParser().get_at_most(directory.root)
    print(total_size)
        
if __name__ == '__main__':
    main()