class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name} \n{self.last_name} \n{self.email} \n{self.age} \n{self.is_rewards_member} \n{self.gold_card_points}")
        
        return self
        
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

        return self

    def spend_points(self, amount=0):
        if self.gold_card_points - amount >= 0:
            self.gold_card_points -= amount
        else:
            print("You don't have enough gold points to spend")

        return self
    
user = User("Vincent", "Guerena", "starbucks@coffee.com", 30)
user.display_info().enroll().enroll().spend_points(50).display_info().spend_points(270)