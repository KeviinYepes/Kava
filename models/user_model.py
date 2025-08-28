class User:
    #El método __init__ es el constructor de la clase
    #Se ejecuta cada vez que creamos un nuevo usuario
   class User:
    def __init__(self, id, username, password, role, fullname=None, document=None):
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
        self.document = document
        self.role = role
