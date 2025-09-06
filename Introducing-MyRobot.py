class Robot:
    def __init__(self, name, model, purpose, creator):
        self.name = name
        self.model = model
        self.purpose = purpose
        self.creator = creator

    def introduction(self):
        print(f"Hello! I am {self.name}, a robot designed for {self.purpose}.")
        print(f"My model is {self.model}, and I was created by {self.creator}.")

    def abilities(self):
        print("I can assist with tasks, learn from interactions, and evolve with updates.")
        print("I also love making humans smile 😄")

    def farewell(self):
        print(f"Thank you for meeting me! {self.name} signing off. Beep bop ✨")

# Create your robot object
my_robot = Robot(
    name = "J-Bot 3000",
    model = "XLR-9",
    purpose = "helping Jeremy learn and explore coding",
    creator = "Jeremy Esotu"
)

# Call the robot's methods
my_robot.introduction()
my_robot.abilities()
my_robot.farewell()