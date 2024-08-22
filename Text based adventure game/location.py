
class Location:
   def __init__(self, location_name):  # constructor
       self.name = location_name
       self.description = None
       self.linked_locations = {}  # creates an empty dictionary
       self.character = None
       self.wepon = None

   # Here is a method to get the description of the location :
   def get_description(self):
       return self.description

   # Here is a method to set the description of the location:
   def set_description(self, location_description):
       self.description = location_description

   # Will print out the object's description when it is called
   def describe(self):
       print(self.description)

   # Here is a method to get the name of the location:
   def get_name(self):
       return self.name

   # Here is a method to set the name of the location:
   def set_name(self, location_name):
       self.name = location_name

   def describe(self):
       print(self.description)

   # Add link_ method here
   def link_location(self, location_to_link, direction):
       self.linked_locations[direction] = location_to_link

   def get_details(self):
       for direction in self.linked_locations:
           location = self.linked_locations[direction]
           print("The " + location.get_name() + " is " + direction)

   def move(self, direction):
       if direction in self.linked_locations:
           return self.linked_locations[direction]
       else:
           print("You can't go that way")
           return self

   # Here is a method to get the character in a location:
   def get_character(self):
       return self.character

   # Here is a method to set the character in a location:
   def set_character(self, _character):
       self.character = _character

   # Here is a method to get the wepon in a location:
   def get_wepon(self):
       return self.wepon

   # Here is a method to set the wepon in a location:
   def set_wepon(self, location_wepon):
       self.wepon = location_wepon

   

