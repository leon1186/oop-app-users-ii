# your User class goes here
class User:
    ISD_location = ("Dallas")
    userPosts = []

    def __init__(self, name, phone_number, email_address, dl_number, age, occupation, points):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.dl_number = dl_number
        self.age_value = age
        self.occupation_value = occupation
        self.points = points
        

    #we want to allow for creation of new user posts, involves class manipulation
    #what type of data structure do we use: 
    #add a class variable that stores post from every user: what data structure should you use?

    def addToUserPosts(self, newUserPost):
            self.userPosts.append(newUserPost)

    def deleteUserPosts(self, deleteUserPost):
            self.userPosts.remove(deleteUserPost)



user_Adam_Smith = User("Adam_Smith", "5055552233", "as@gmail.com", "52345126", 21, "engineer", 10)

user_Adam_Smith.addToUserPosts("hey get outta here")
print(user_Adam_Smith.userPosts)

user_Not_GF = User("Not_GF", "0000000000", "none_ever@gmail.com", "666", 25, "loser", -100)

user_Not_GF.addToUserPosts("No thats my post")
print(user_Not_GF.userPosts)

user_Not_GF.deleteUserPosts("No thats my post")
print(user_Not_GF.userPosts)


#key and value in a dictionary for all posts, enter key to remove with input selection / case-switch access
#acll method by userpost/id, print - take user input, take logice to match key and delete
# -----



#     def contact(self):
#         print(f">> {self.name} is reachable at {self.email_address} or {self.phone_number}")

#     def age(self):
#         print(f">> {self.name} is currently {self.age_value}")

#     def occupation(self):
#         print(f">> {self.name} is currently working as a/an {self.occupation_value}")

#     def driving_record(self):
#         points = 10
#         print(f">> {self.name} has a drivers license number: {self.dl_number} with {self.points} points left")

# user_Adam_Smith = User("Adam_Smith", "5055552233", "as@gmail.com", "52345126", 21, "engineer", 10)
# print(user_Adam_Smith)

# user_Adam_Smith.contact()
# user_Adam_Smith.age()
# user_Adam_Smith.occupation()
# user_Adam_Smith.driving_record()


# user_Coolio = User("Coolio", "123456789", "coolio@gmail.com", "987654321", 55, "rapper", -10)
# print(user_Coolio)

# user_Coolio.contact()
# user_Coolio.age()
# user_Coolio.occupation()
# user_Coolio.driving_record()


# user_Not_GF = User("Not_GF", "0000000000", "none_ever@gmail.com", "666", 25, "loser", -100)
# print(user_Not_GF)

# user_Not_GF.contact()
# user_Not_GF.age()
# user_Not_GF.occupation()
# user_Not_GF.driving_record()