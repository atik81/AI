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
        if self.a < len(environment):
            self.a +=1
            self.clean(environment)#there have two attributes "self.a" and "self.clean(), its takes argument "environment"
            # i used this one for moving one unit  to down 
    def clean(self,environment):
        if environment[self.a-1][self.b-1] == "dirt  ":
            environment[self.a-1][self.b-1] = "Clean " # change the current cell state to clean
            # i used this one for checking the cell if it is dirty , its clean the cell by updaing it's value to "clean"
    def get_environment_with_cleaner(self, environment):
        new_environment = [row.copy() for row in environment]
        new_environment[self.a-1][self.b-1] += "*"
        return new_environment
    # i used this one for marked the current position of vaccum cleaner with(*)

#///////////////////////////////////////////(       CLASS MANUAL AGENT            )///////////////////////////////////////////////////#
class ManualAgent:
    def get_action(self): 
        action = input("Enter action (left, right, up, down, clean): ")
        return action
    #method is get_action then returns the string by the user

#///////////////////////////////////////////(       CLASS AUTOAGENT           )////////////////////////////////////////////////////#
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
            if value == 'q':
                return value
            a, b = map(int, value.split(","))
            if a > 0 and b > 0:
                return a, b
        except ValueError:
            print("Sorry, invalid value. Enter a positive coordinates in the format a,b.")
            # for a,b formet user need to put > 0 and for quit entering user can press"q" anytime 
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
        
def create_environment(n):
    environment = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append("clean ")
        environment.append(row)
    return environment
   # each "n" cells with string value "clean" .it's returns  the fully initialized environment.
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def mark_dirt(environment, a, b): # mark cell at row a, column b as "dirt"
    environment[a-1][b-1] = "dirt  "
     
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

def display_environment(environment):
    n = len(environment)
    # Print the top border of the table
    print("+{}+".format("--" * (n * 3 + n + 1)))
    # Print each row of the table
    for row in environment:
        for col in row:
           
         print("| {:^2}".format(col), end=" ") # it's centers value within a 2-character  wide space for each column 
        print("|")
        print("+{}+".format("--" * (n * 3 + n + 1)))
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

n = get_integer_input("Enter the size of the  environment: ")
environment = create_environment(n) # for create environment size from user
while True: # this loop for get dirt location untill user put q
    dirt_location = get_coordinate_input("Enter the location of the dirt (use a,b int formet or type 'q' to stop): ")
    if dirt_location == "q": # if user put "q" it's break the loop
        break
    mark_dirt(environment, dirt_location[0], dirt_location[1]) # it's used for marking the dirt
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

display_environment(environment) # it's showed current state of environment
agent_type = input("Enter agent type (manual or auto): ") # user need to select manual or auto
if agent_type == "manual":
 agent = ManualAgent()
elif agent_type == "auto":
    agent = AutoAgent()
else:
    print("Invalid input. Please enter 'manual' or 'auto'.")
    exit()
    # for invalid input i used this one
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

start_location = get_coordinate_input("Enter start location of the cleaner: ") # this one for start location of cleaner user need to select 
Cleaner = cleaner(start_location[0], start_location[1])

while not is_goal_state(environment): # loop for  goal state reched
    display_environment(Cleaner.get_environment_with_cleaner(environment)) # displays the current state of the environmennt with cleaner position
    if isinstance(agent, ManualAgent):     #user need slect movement untill goals state reached for manual
        action = agent.get_action()
    elif isinstance(agent, AutoAgent): # it will take autp action .
        action = agent.get_action(environment, Cleaner)
    else:
        print("Invalid agent type.")
        exit()
    if action == "left":
        Cleaner.move_left(environment)
        print("Cleaner moved left.")
    elif action == "right":
        Cleaner.move_right(environment)
        print("Cleaner moved right.")
    elif action == "up":
        Cleaner.move_up(environment)
        print("Cleaner moved up.")
    elif action == "down":
        Cleaner.move_down(environment)
        print("Cleaner moved down.")
        Cleaner.move_left(environment)
    elif action == "clean":
        Cleaner.clean(environment)
        print("Clean")
   
    else:
        print("Invalid action. Try again.")


print(" all task is clean !")
display_environment(environment)
#////////////////////////////////////////////// (          END       )//////////////////////////////////////////////////////////////////////////#