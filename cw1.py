#///////////////////////////////////////////(       CLASS CLEANER             )///////////////////////////////////////////////////#
class cleaner:    # created initialization method in my cleaner class
    def __init__(self, a, b): 
        self.a = a   # self.a is attribute and  the parameter is a
        self.b = b   ## self.a is attribute and  the parameter is a
    
    def move_left(self, environment): # i used this one for moving one unit  move to left position
        if self.b > 1:
            self.b -= 1
            self.clean(environment) #there have two attributes "self.b" and "self.clean(), its takes argument "environment"
           # i used this one for moving one unit  to left position
    def move_right(self, environment): 
        if self.b < len(environment[0]):
            self.b += 1
            self.clean(environment) #there have two attributes "self.b" and "self.clean(), its takes argument "environment"
         # i used this one for moving one unit   to right position
    def move_up(self, environment):
        if self.a > 1:
            self.a -=1
            self.clean(environment)#there have two attributes "self.a" and "self.clean(), its takes argument "environment"
            # i used this one for moving one unit  to up
    def  move_down(self, environment):
        if self.a > 1:
            self.a +=1
            self.clean(environment)#there have two attributes "self.a" and "self.clean(), its takes argument "environment"
            # i used this one for moving one unit  to down 
    def clean(self,environment):
        if environment[self.a-1][self.b-1] == "Dirt  ":
            environment[self.a-1][self.b-1] = "Clean "
            # i used this one for checking the cell if it is dirty , its clean the cell by updaing it's value to "clean"
    def get_environment_with_cleaner(self, environment):
        new_environment = [row.copy() for row in environment]
        new_environment[self.a-1][self.b-1] += "*"
        return new_environment

#///////////////////////////////////////////(       CLASS AUTOAGENT            )///////////////////////////////////////////////////#
class ManualAgent:
    def get_action(self):
        action = input("Enter action (left, right, up, down, clean): ")
        return action
    #method is get_action then returns the string by the user

#///////////////////////////////////////////(       CLASS MANUALAGENT           )////////////////////////////////////////////////////#
class AutoAgent:
    def get_action(self, environment, cleaner):
        if environment[cleaner.a-1][cleaner.b-1] == "dirt  ":
            return "clean"
        else:
            if cleaner.a % 2 == 1:
                if cleaner.b < len(environment[0]):
                    return "right"
                else:
                    return "down"
            else: 
                if cleaner.b > 1:
                    return "left"
                else:
                    return "down"
        # it's move in a zigzag pattern from left to right and down untill all the cells are cleand.
    #method is get_action then returns the string by the user
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def is_goal_state(environment):
    for row in environment:
        if "dirt  " in row:
            return False
    return True
    #its cheak is the environment clean or not clean
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def get_integer_input(prompt): #its takes parametr prompt
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            print("Sorry, invalid value. Enter a positive integer.")
        #  user need to put positive value otherwise it will show valuerror
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def get_coordinate_input(prompt):
    while True:
        try:
            value = input(prompt)
            if value == 'Q':
                return value
            a, b = map(int, value.split(","))
            if a > 0 and b > 0:
                return a, b
        except ValueError:
            print("Sorry, invalid value. Enter a positive coordinates in the format a,b.")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
        
def create_environment(n):
    environment = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append("clean ")
        environment.append(row)
    return environment
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def mark_dirt(environment, a, b):
    environment[a-1][b-1] = "dirt  "
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

def display_environment(environment):
    n = len(environment)
    # Print the top border of the table
    print("+{}+".format("--" * (n * 3 + n + 1)))
    # Print each row of the table
    for row in environment:
        print("| {} |".format(" | ".join(row)))
    # Print the bottom border of the table
    print("+{}+".format("--" * (n * 3 + n + 1)))
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

n = get_integer_input("Enter the size of the  environment: ")
environment = create_environment(n)
while True:
    dirt_location = get_coordinate_input("Enter the location of the dirt (or type 'Q' to stop): ")
    if dirt_location == "Q":
        break
    mark_dirt(environment, dirt_location[0], dirt_location[1])
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

display_environment(environment)
agent_type = input("Enter agent type (manual or auto): ")
if agent_type == "manual":
 agent = ManualAgent()
elif agent_type == "auto":
    agent = AutoAgent()
else:
    print("Invalid input. Please enter 'manual' or 'auto'.")
    exit()
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

start_location = get_coordinate_input("Enter start location of the cleaner: ")
cleaner = cleaner(start_location[0], start_location[1])

while not is_goal_state(environment):
    display_environment(cleaner.get_environment_with_cleaner(environment))
    if isinstance(agent, ManualAgent):
        action = agent.get_action()
    elif isinstance(agent, AutoAgent):
        action = agent.get_action(environment, cleaner)
    else:
        print("Invalid agent type.")
        exit()
    if action == "left":
        cleaner.move_left(environment)
        print("Cleaner moved left.")
    elif action == "right":
        cleaner.move_right(environment)
        print("Cleaner moved right.")
    elif action == "up":
        cleaner.move_up(environment)
        print("Cleaner moved up.")
    elif action == "down":
        cleaner.move_down(environment)
        print("Cleaner moved down.")
        cleaner.move_left(environment)
    elif action == "clean":
        cleaner.clean(environment)
        print("Clean")
        
    else:
        print("Invalid action. Try again.")


print(" All task is clean !")
display_environment(environment)
