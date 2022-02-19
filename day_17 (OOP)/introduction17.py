class User:
    #Atributes
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    #Methods
    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("123", "Frander Calvo.")
user2 = User("456", "Luis Franco. ")
user1.follow(user2)
user2.follow(user1)
print(user1.followers, user2.followers, user1.following, user2.following)


#user1 = User("001002", "Frander Calvo Rodríguez.")
#print(user1.id, user1.username, user1.followers)



