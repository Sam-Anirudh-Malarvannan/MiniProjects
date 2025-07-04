from User import User

class UserManager:
    __Users = []

    @classmethod
    def AddUser(cls, userObj):
        if any(user.MailId == userObj.MailId for user in cls.__Users):
            print("Email already registered!")
            return False
        if isinstance(userObj, User):
            cls.__Users.append(userObj)
            return True
        print("Invalid User")
        return False

    @classmethod
    def FindUser(cls, mail, pwd):
        for user in cls.__Users:
            if user.MailId == mail and user.Password == pwd:
                return user
        return None