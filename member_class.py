class Members:
    def __init__(self, member_id, name):
        self.id = member_id
        self.name = name

    def check_in(self):
        pass


# Single club members
class Single(Members):
    def __init__(self, member_id, name, assigned_club=None):  # passes their membership version and specific club (prob don't need membership)
        super().__init__(member_id, name)
        self.assigned_club = assigned_club
        self.checkin_club = None
        self.directory = {
            self.id: {'name': self.name, 'club': self.assigned_club}  # dict for saving users info and club location
        }

    # gets user to enter the club they want to check into and makes sure it's on the list of clubs
    def check_in(self):
        while True:
            self.checkin_club = input("Please input your club or input Cancel to end the check in process.\n").title()
            if self.checkin_club in self.directory[self.id].values() or self.checkin_club == 'Cancel':
                print(self.directory)
                print(self.checkin_club)
                break
            else:
                print("That is not a valid entry")

    # checks if this is customers correct gym
    def home_club(self):

        while True:
            self.check_in()
            if self.checkin_club == self.assigned_club:  # welcome customer if club they're at is their assigned club
                print(f"Welcome to {self.checkin_club}")
                break
            elif self.checkin_club == 'Cancel':
                print("Have a nice day!")
                break
            else:
                print(f"This is not your club")


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


singles = Single(1, "Mike", 'Power Workout')
singles.home_club()
