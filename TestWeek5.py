from gpiozero import LED
from time import sleep

orange = LED(18)

class students:
        def __init__(self, name, age, home):
                self.name = name
                self.age = age
                self.home = home
        def displayfamily(self):
                print("naam: ", self.name, " age: ", self.age, " living at home :", self.home)

inputkeuze = 0
lijst = []

while inputkeuze !=3:
        print("\n\n\n\n\n")
        print("Menu\n------------------------\n1)Add family member\n2)See the family\n3)quit")
        inputkeuze = int(input("Geef je keuze in: "))
        print("\n\n\n\n\n")
        if inputkeuze == 1:
                while True:
                        naam = input("Geef een naam in: ")
                        if naam != "q":
                                leeftijd = int(input("Geef de leeftijd in: "))
                                home = input("Woon je nog thuis? True of False: ")
                                if home == "False" or home == "True" or home == "false" or home == "true":
                                        lijst.append(students(naam, leeftijd, home))
                                        orange.on()
                                        sleep(1)
                                        orange.off()
                                else:
                                        print("Foute input \nGebruik False of True\n")
                                        continue
                        else:
                                break
        elif inputkeuze == 2:
                for obj in lijst:
                        obj.displayfamily()
        elif inputkeuze == 3:
                break
        else:
                print("Geef uw juiste keuze in!")
else:
        print("end of program")
