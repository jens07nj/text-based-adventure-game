

from location import Location
from character import Enemy, Friend
#from character import
from wepon import wepon


saltysprings = Location("saltysprings")
saltysprings.set_description("A small town where many battles were fought ")


tiltedtowers = Location("tiltedtowers")
tiltedtowers.set_description("A large city with a ")


lootlake = Location("lootlake")
lootlake.set_description("A small lake with a house in the middle ")


saltysprings.link_location(tiltedtowers, "south")
lootlake.link_location(tiltedtowers, "east")
tiltedtowers.link_location(lootlake, "west")
tiltedtowers.link_location(saltysprings, "north")


Peely = Enemy("Peely", "a FNCS tourniment winner")
Peely.set_conversation("battle me for the victory royal you noob, or are you too scared??")
Peely.set_weakness("pumpshotgun")
tiltedtowers.set_character(Peely)


brightbomber = Friend("brightbomber", "A friendly bot")
brightbomber.set_conversation("Gidday")
lootlake.set_character(brightbomber)


pumpshotgun = wepon("pumpshotgun")
pumpshotgun.set_description("Peely's worst nightmare")
lootlake.set_wepon(pumpshotgun)
torch = wepon("sniper")
torch.set_description("great for long distance fights")
tiltedtowers.set_wepon(torch)
bag = []




current_Location = saltysprings
dead = False
while dead == False:
   print("\n")

   print("****************************************")

   print ("        Fortnite Battle royal")

   print("****************************************")


   print("how to play:")
   print("- Move locations by typing: north , south, east or west")
   print("- Interact with characters by typing: talk , dance , fight")
   print("- Add items to your inventory by typing: take")
   print("")
   print("")
   print("")


   print(f"Currant location: {current_Location.get_name()}")
   current_Location.describe()


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
       print()


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
                       print("**********************************************************")
                       print("")
                       print("                   VICTORY ROYAL")
                       print("")
                       print("**********************************************************")
                       dead = True
               else:
                   print("back to the lobby nerd, you lost the fight.")
                   print("That's the end of the game")
                   dead = True
           else:
               print("You don't have a " + fight_with)
       else:
           print("There is no one here to fight with")


   elif command == "dance":
       if inhabitant is not None:
           if isinstance(inhabitant, Enemy):
               print("I wouldn't do that if I were you...")
           else:
               inhabitant.dance()
       else:
           print("There is no one here to dance with :(")


   elif command == "take":
       if wepon is not None:
           print(wepon.get_name() + " has been added to your inventory")
           bag.append(wepon.get_name())
           current_Location.set_wepon(None)


