class Members:
    def __init__(self, member_id, name):
        self.id = member_id
        self.name = name
        self.directory = {self.id: self.name}

    def check_in(self):
        pass


# Single club members
class Single(Members):
    def __init__(self, member_id, name, membership,
                 assigned_club):  # passes their membership version and specific club (prob don't need membership)
        super().__init__(member_id, name)
        self.membership = membership
        self.club = assigned_club

    def check_in(self):
        # TODO add loop to make sure user input is correct based on instructions
        self.club = input("Please input your club or input Cancel to end the check in process.\n").title()

    def home_club(self, club):
        while True:
            if self.club == club or self.club == 'Cancel':  # welcome customer if club they're at is their assigned club
                print(f"Welcome to {self.club}")
                break
            else:
                print(f"This is not your club")
                self.check_in()


# Multi club members
class Multi(Members):
    # counter for member points
    member_points = 0

    def __init__(self, member_id, name, membership):
        super().__init__(member_id, name)
        self.membership = membership
        self.club = None

    def check_in(self):
        self.member_points += 1

