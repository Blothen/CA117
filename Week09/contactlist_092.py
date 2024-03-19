class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def __str__(self):
        return f'{self.name} {self.phone} {self.email}'
    

class Contactlist:
    def __init__(self):
        self.d = {}
        
    def add(self, c):
        self.d[c.name] = c
        return self

    def remove(self, name):
        if name in self.d:
            del(self.d[name])
        
    def get(self, name):
        return self.d.get(name)

    def __str__(self):
        output = "Contact list\n------------\n"
        contacts = sorted([str(c) for c in self.d.values()])
        return output + "\n".join(contacts)
