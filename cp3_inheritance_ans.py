class Info:
    def __init__(self, given_name, surname, nation, bday):
        self.given_name = given_name
        self.surname = surname
        self.nation = nation
        self.bday = bday
    def get_result(self):
        return f"Given name：{self.given_name}\nSurname：{self.surname}\nNationality：{self.nation}\nBirthday：{self.bday}"
class PersonOne(Info):
    def __init__(self, given_name, surname, nation, bday):
        super().__init__(given_name, surname, nation, bday)

class PersonTwo(Info):
    def __init__(self, given_name, surname, nation, bday):
        super().__init__(given_name, surname, nation, bday)
def main():
    # personOne = PersonOne("Kizuki", "Yagi", "Japan", "4/10")
    # personTwo = PersonTwo("Dongfei", "Cheng", "Taiwan", "12/22")

    personOne = PersonOne("Audrey", "Boucher", "France", "1/14")
    personTwo = PersonTwo("Yuliya", "Sidorova", "Russia", "12/12")
   
    print("Person 1: ")
    print(personOne.get_result())
    print("Person 2: ")
    print(personTwo.get_result())

if __name__ == "__main__":
    main()
