def main():
    return input("Which club do you want to join or do you want to be a multi-club member?:")


class Club:
    def __init__(self, name, address):
        self.name = name
        self.address = address


c1 = Club("Power Workout", "122 Kings St Miami, FL 33012")
c2 = Club("Protein Punch", "245 Main St Seattle, WA 98122")
c3 = Club("Work Life Balance", "967 West Ave Brooklyn, New York 11201")
c4 = Club("Sweat & Grit", "480 Park Ave San Diego, California 92101")

print(f"1.{c1.name}")
print(f"2.{c2.name}")
print(f"3.{c3.name}")
print(f"4.{c4.name}")
print(main())