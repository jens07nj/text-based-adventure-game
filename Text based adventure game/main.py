

from location import Location
from character import Enemy, Friend
#from character import
from wepon import wepon


saltysprings = Location("saltysprings")
saltysprings.set_description("A small town where many battles were fought ")


tiltedtowers = Location("tiltedtowers")
tiltedtowers.set_description("A city with one large tower in the middle")




lootlake = Location("lootlake")
lootlake.set_description("A small lake with a house in the middle ")

dustydepot = Location("dustydepot")
dustydepot.set_description("A abandoned depot that got hit by a meteor")

junkjunction = Location ("junkjunction")
junkjunction.set_description("A old junk yard where rust Lord runs his shop")

pleasantpark = Location ("pleasantpark")
pleasantpark.set_description("A town surrounding a large soccer feild")

riskyreels = Location ("riskyreels")
riskyreels.set_description("A drive in theater that hasen't been used for many years")



saltysprings.link_location(tiltedtowers, "south")
lootlake.link_location(tiltedtowers, "east")
tiltedtowers.link_location(lootlake, "west")
tiltedtowers.link_location(saltysprings, "north")
tiltedtowers.link_location(dustydepot, "south")
dustydepot.link_location(tiltedtowers, "north")
lootlake.link_location(junkjunction, "west")
junkjunction.link_location(lootlake, "east")
dustydepot.link_location(pleasantpark, "east")
pleasantpark.link_location(dustydepot, "west")
pleasantpark.link_location(riskyreels, "north")
riskyreels.link_location(pleasantpark, "south")
riskyreels.link_location(saltysprings, "west")
saltysprings.link_location(riskyreels,"east")


Peely = Enemy("Peely", "a FNCS tourniment winner")
Peely.set_conversation("battle me for the victory royal you noob, or are you too scared??")
Peely.set_weakness("pumpshotgun")
dustydepot.set_character(Peely)


brightbomber = Friend("brightbomber", "A friendly bot")
brightbomber.set_conversation("Gidday, you look lost. if you wanna get this victory royal, remember use the pumpshotgun on peely, sniper on fishsticks and smg to kill dark knight")
saltysprings.set_character(brightbomber)

fishsticks = Enemy("fishsticks", "A sneaky bot who camps on the top of the island")
fishsticks.set_weakness("sniper")
lootlake.set_character(fishsticks)

darknight = Enemy("darknight", "A streamer who loves to snipe")
darknight.set_weakness("smg")
pleasantpark.set_character(darknight)

smg = wepon("smg")
smg.set_description(" rust lord offers it to you, 'you will need it fight fight darknight' he says")
junkjunction.set_wepon(smg)


pumpshotgun = wepon("pumpshotgun")
pumpshotgun.set_description("Peely's worst nightmare")
lootlake.set_wepon(pumpshotgun)
torch = wepon("sniper")
torch.set_description("great for long distance fights especially bots who camp on roofs")
riskyreels.set_wepon(torch)
inventory = []

print("****************************************")

print ("        Fortnite Battle royal")

print("****************************************")


print("how to play:")
print("- Move locations by typing: north , south, east or west")
print("- Interact with characters by typing: talk , dance , fight")
print("- Add items to your inventory by typing: take")
print("- eliminate all 3 enemys to win")
print("- before you fight anyone, collect wepons and find brightbomber, she has some valuable advice")
print("")
print("")





current_Location = tiltedtowers
dead = False
while dead == False:
   print("\n")





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
           if fight_with in inventory:
               if inhabitant.fight(fight_with) == True:
                   # What happens if you win?
                   print("Bravo, gamer you won the fight!")
                   print( str(Enemy.enemies_to_defeat)  + " enemys remain")
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
           inventory.append(wepon.get_name())
           current_Location.set_wepon(None)


