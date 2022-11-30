from abc import ABC, abstractmethod

class Component(ABC):

    @abstractmethod
    def size(self):
        pass

class File(Component):

    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def size(self):
        return self.__size

class Folder(Component):

    def __init__(self, name, components):
        self.__name = name
        self.__components = components

    def size(self):
        total = 0
        for component in self.__components:
            total += component.size()
        return total

    def add(self, component):
        self.__components.append(component)

resume = File("resume.doc", 1024)
cover_letter = File("cover.doc", 2048)
reference = File("reference.pdf", 4096)

documents = Folder("Documents", [resume, cover_letter, reference])

todo = File("todo.txt", 256)
screenshot = File("screenshot.png", 25000)

desktop = Folder("Desktop", [todo, screenshot])

user = Folder("User", [desktop, documents])

print(resume.size())
print(documents.size())
print(desktop.size())
print(user.size())

death_star_plans = File("secret.txt", 512)

user.add(death_star_plans)

print(user.size())

components = [todo, user, screenshot]

for component in components:
    print(component.size())