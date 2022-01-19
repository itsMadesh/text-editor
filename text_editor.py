# PROJECT SIMPLE TEXT EDITOR
# 14. Create a simple text editor that stores and displays a string of characters. Your editor 
# should support the following operations: 
# • left: Move pointer left one character (do nothing if at beginning). 
# • right: Move pointer right one character (do nothing if at end). 
# • insert c: Insert the character c just after the pointer. 
# • delete: Delete the character just after the pointer (do nothing at end).

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class text_editor:
    def __init__(self):
        self.directory = "C:/Users/mades/Documents/workspace/python-lab-programs/Project/"
        self.filepath = self.directory + input("Enter filename : ")
        self.reset()
        self.load()
    def reset(self):
        self.head = None
        self.pos = None

    def store(self):
        content = ""
        temp = self.head
        while temp is not None:
            content += temp.data
            temp = temp.next
        with open(self.filepath, "w+") as fp:
            fp.write(content)

    def load(self):
        try:
            with open(self.filepath, "r") as fp:
                for c in fp.read():
                    self.insert(c)
        except:
            pass

    def insert(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.pos = newnode
        elif self.pos == None and self.head:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            self.pos = newnode
        else:
            newnode.next = self.pos.next
            if self.pos.next:
                self.pos.next.prev = newnode
            self.pos.next = newnode
            newnode.prev = self.pos
            self.pos = newnode

    def delete(self):
        if self.pos == None and self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif self.head is None or self.pos.next is None:
            return
        else:
            temp = self.pos.next
            self.pos.next = temp.next
            if temp.next:
                temp.next.prev = self.pos

    def backspace(self):
        if self.head is None or self.pos is None:
            return
        elif self.head == self.pos and self.head.next is None:
            self.head = None
            self.pos = None
        elif self.head == self.pos:
            self.head = self.head.next
            self.head.prev = None
            self.pos = None
        else:
            temp = self.pos
            if temp.next is not None:
                self.pos.prev.next = temp.next
                temp.next.prev = self.pos.prev
            else:
                self.pos.prev.next = temp.next
            self.pos = self.pos.prev
            temp = None

    def left(self):
        if self.pos.prev is not None:
            self.pos = self.pos.prev
        else:
            self.pos = None

    def right(self):
        if self.pos == None and self.head:
            self.pos = self.head
        elif self.pos.next is not None:
            self.pos = self.pos.next

    def print_text(self):
        print("content - ", end="")
        temp = self.head
        if self.pos == None:
            print("|", end="")
        while temp:
            print(temp.data, end="")
            if self.pos == temp:
                print("|", end="")
            temp = temp.next
        print("")
        print("=" * 32)


text = text_editor()
print("=" * 32)
print("Operations:(Simple Text editor):")
print("i-Insert")
print("d-Delete")
print("b-Backspace")
print("l-Move left")
print("r-Move right")
print("s-save content")
print("c-clear content")
print("e-Exit")
print("=" * 32)
while 1:
    text.print_text()
    c = input("\nEnter your choice(i/d/b/l/r/s/c/e):")
    if c == "i":
        data = input("Enter character to insert:")
        for i in data:
            text.insert(i)
    elif c == "d":
        text.delete()
    elif c == "b":
        text.backspace()
    elif c == "l":
        text.left()
    elif c == "r":
        text.right()
    elif c == "s":
        text.store()
        print("")
    elif c == "c":
        text.reset()
    elif c == "e":
        break
    else:
        print("Invalid choice")
