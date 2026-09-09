Ability_List=[]
def damage(Health):
    Health-=10
    return Health
CharName=input("Enter your character's name: ")
Ability_Num=int(input("Enter the number of abilities this character has: "))
for i in range(0,Ability_Num):
    Ability=input("Enter an ability: ")
    Ability_List.append(Ability)
print(CharName,"Has:",Ability_List)
Health=int(input("Enter health: "))
print(CharName, "has", Health,"HP")
Attack=input("Attack?")
if Attack=="yes":
    print(damage(Health))



