class wepon:
   def __init__(self, wepon_name):
       self.name = wepon_name
       self.description = None


   #method to get the description of the wepon:
   def get_description(self):
       return self.description


   #method to set the description of the wepon:
   def set_description(self, wepon_description):
       self.description = wepon_description


   #method to get the name of the wepon:
   def get_name(self):
       return self.name


   #method to set the name of the wepon:
   def set_name(self, wepon_name):
       self.name = wepon_name


   def describe(self):
       print("The [" + self.name + "] is here - " + self.description)

