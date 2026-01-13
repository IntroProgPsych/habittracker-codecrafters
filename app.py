#import all the modules you need, below this line


#write any functions you need, below this line
questions = [
    {"text": "How many days per week do you go to bed at a consistent hour?", "habit": "SleepRoutine"},
    {"text": "How many days per week do you sleep at least 7 hours?", "habit": "SleepRoutine"},
    {"text": "How many days per week do you avoid screens before bed?", "habit": "SleepRoutine"},

    {"text": "How many days per week do you exercise for at least 20 minutes?", "habit": "PhysicalActivity"},
    {"text": "How many days per week do you walk or bike?", "habit": "PhysicalActivity"},
    {"text": "How many days per week do you stretch?", "habit": "PhysicalActivity"},

    {"text": "How many days per week do you eat at least one healthy meal?", "habit": "HealthyEating"},
    {"text": "How many days per week do you eat fruits or vegetables?", "habit": "HealthyEating"},
    {"text": "How many days per week do you drink enough water?", "habit": "HealthyEating"},

    {"text": "How many days per week do you practice mindfulness?", "habit": "Mindfulness"},
    {"text": "How many days per week do you relax without screens?", "habit": "Mindfulness"},
    {"text": "How many days per week do you manage stress well?", "habit": "Mindfulness"},

    {"text": "How many days per week do you spend meaningful time with others?", "habit": "SocialConnection"},
    {"text": "How many days per week do you talk with friends or family?", "habit": "SocialConnection"},
    {"text": "How many days per week do you feel socially supported?", "habit": "SocialConnection"}
]

def interpet_score(score):
    if score >= 12:
        return "High"
    elif score >= 6:
        return "Moderate"
    else:
        return "Low"
def valid_input(question):
     while True:
         try:
             value = int(input(question + "(0-7): "))
             if value <= 0 or value <= 7:
                 return value
             else:
                 print("Please enter a number between 0 and 7")   
                
         except ValueError:
             print("Invalid input. Please enter a number")
            
        
           
        


#use the main() function for your program, define all other functions above main
def main ():
    #use print statements such as this one, to mark important points in the application, to help you with debugging
    print("Starting application...")
    scores={
        "SleepRoutine": 0,
        "PhysicalActivity": 0,
        "HealthyEating": 0,
        "Mindfulness": 0,
        "SocialConnection": 0
    }

    for question in questions:
        text = question["text"]
        habit = question["habit"]

        answer = valid_input(text)
        scores[habit] = scores[habit] + answer

    print("\n--- Habit Tracker Results ---")
    for habit in scores:
        total = scores[habit]
        label = interpet_score(total)
        print(habit + ": Score " + str(total) + " -> " + label)

#please do not change the lines below, they are needed for your tests to work properly
#write all your code in the current file, and all your tests in the tests.py file
if __name__ == "__main__":
    main()
