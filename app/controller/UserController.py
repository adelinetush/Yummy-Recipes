from app.models.User import User

class UserController:
    global users

    def __init__(self):
        print('ini self')
        self.users = []

    def login(self, username, password):
        if(len(self.users)==0):
            user = User(username,password)
            self.users.append(user)
            return self.users

        for user in self.users:
            if(user.name!= username and user.password!=password):
                    user = User(username,password)
                    self.users.append(user)
                    return self.users
        return self.users
    
