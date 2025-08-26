from controllers.user_dao import UserDAO

class AuthController:
    @staticmethod #Sirve para crear una clase sin un obj
    def login(username,password):
        user = UserDAO.get_user_by_username(username)

        if user and user.password == password:
            return user #Auth check
        return None #Sin Auth
