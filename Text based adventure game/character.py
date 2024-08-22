class Character():
   def __init__(self, char_name, char_description):
       self.name = char_name
       self.description = char_description
       self.conversation = None


   # Describe this character
   def describe(self):
       print( self.name + " is here!" )
       print( self.description )


   # Set what this character will say when talked to
   def set_conversation(self, conversation):
       self.conversation = conversation


   # Talk to this character
   def talk(self):
       if self.conversation is not None:
           print("[" + self.name + " says]: " + self.conversation)
       else:
           print(self.name + " doesn't want to talk to you")


   # Fight with this character
   def fight(self, combat_wepon):
       print(self.name + " doesn't want to fight with you")
       return True


   def fight(self, combat_wepon):
       if combat_wepon == self.weakness:
           print("You fend " + self.name + " off with the " + combat_wepon)
           return True
       else:
           print(self.name + " swallows you, little wimp")
           return False










class Enemy(Character):
   enemies_to_defeat = 0
   def __init__(self, char_name, char_description):
       super().__init__(char_name, char_description)
       self.weakness = None
       Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1


   # Here is a method to get the weakness of the enemy:
   def get_weakness(self):
       return self.weakness


   # Here is a method to set the weakness of the enemy:
   def set_weakness(self, weakness):
       self.weakness = weakness


   def steal(self):
       print("You steal from " + self.name)


   def fight(self, combat_wepon):
       if combat_wepon == self.weakness:
           Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
           return True
       else:
           print(self.name + " swallows you, little wimp")
           return False








class Friend(Character):
   def __init__(self, char_name, char_description):
       super().__init__(char_name, char_description)
       self.feeling = None
   def dance(self):
       print(self.name + " hits the griddy!")

