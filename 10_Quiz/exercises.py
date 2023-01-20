
class User:

    def __init__(self,id_user, username):
        self.id = id_user
        self.username = username
        self.followers = 0
        self.following = 0
    pass

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'one')
# user_1.id = '001'
# user_1.username = 'one'

user_2 = User('002', 'two')

user_1.follow(user_2)

print(user_1.id)
print(user_1.followers)
print(user_1.following)

