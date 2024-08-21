

from location import Location
from character import Enemy, Friend
#from character import
from wepon import wepon


saltysprings = Location("saltysprings")
saltysprings.set_description("A damp and dirty Location ")


tiltedtowers = Location("tiltedtowers")
tiltedtowers.set_description("A large Location with a rack")


lootlake = Location("lootlake")
lootlake.set_description("A small Location with ancient graffiti")


saltysprings.link_location(tiltedtowers, "south")
lootlake.link_location(tiltedtowers, "east")
tiltedtowers.link_location(lootlake, "west")
tiltedtowers.link_location(saltysprings, "north")


Peely = Enemy("Peely", "a FNCS tourniment winner")
Peely.set_conversation("Hangry…Hanggrry")
Peely.set_weakness("pumpshotgun")
tiltedtowers.set_character(Peely)


brightbomber = Friend("brightbomber", "A friendly bot")
brightbomber.set_conversation("Gidday")
lootlake.set_character(brightbomber)


pumpshotgun = wepon("pumpshotgun")
pumpshotgun.set_description("A Wumpuses worst nightmare")
lootlake.set_wepon(pumpshotgun)
torch = wepon("torch")
torch.set_description("A light for the end of the tunnel")
tiltedtowers.set_wepon(torch)
bag = []




current_Location = saltysprings
dead = False
while dead == False:
   print("\n")


   wepon = current_Location.get_wepon()
   if wepon is not None:
       wepon.describe()


   current_Location.get_details()
   inhabitant = current_Location.get_character()
   if inhabitant is not None:
       inhabitant.describe()


   command = input("> ")


   if command in ["north", "south", "east", "west"]:
       current_Location = current_Location.move(command)


   elif command == "talk":
   # Talk to the inhabitant - check whether there is one!
       if inhabitant is not None:
           inhabitant.talk()


   elif command == "fight":
       if inhabitant is not None and isinstance(inhabitant, Enemy):
           # Fight with the inhabitant, if there is one
           print("What will you fight with?")
           fight_with = input()
           if fight_with in bag:
               if inhabitant.fight(fight_with) == True:
                   # What happens if you win?
                   print("Bravo, hero you won the fight!")
                   current_Location.set_character(None)
                   if Enemy.enemies_to_defeat == 0:
                       print("Congratulations, you have survived another adventure!")
                       dead = True
               else:
                   print("Scurry home, you lost the fight.")
                   print("That's the end of the game")
                   dead = True
           else:
               print("You don't have a " + fight_with)
       else:
           print("There is no one here to fight with")


   elif command == "pat":
       if inhabitant is not None:
           if isinstance(inhabitant, Enemy):
               print("I wouldn't do that if I were you...")
           else:
               inhabitant.pat()
       else:
           print("There is no one here to pat :(")


   elif command == "take":
       if wepon is not None:
           print("You put the " + wepon.get_name() + " in your bag")
           bag.append(wepon.get_name())
           current_Location.set_wepon(None)


