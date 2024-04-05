import json
from my_function import build_person, build_experiment

if __name__ == "__main__":
    print()
    print("Welcome to the experiment builder!")
    print("Please enter the following information about the experiment")
    print()
    experiment_name = input("Enter the experiment name: "),
    experiment_date = input("Enter the date(dd-mm-yyyy): ")
    while True:
        check = input("Do you want to enter new supervisor information? (y/n): ")

        if check == "y":
            print()
            print("Please enter the following information about the experiment supervisor!")
            supervisor = build_person(
                input("Enter the supervisor's first name: "),
                input("Enter the supervisor's last name: "),
                input("Enter the supervisor's gender: "),
                int(input("Enter the supervisor's age: "))
            )
            break
        elif check == "n":
            supervisor = build_person("Alexander", "Kometer", "male", 27)
            break
        else: 
            print("Please enter a valid input!")
        
#test
    
    print()
    print("Please enter the following information about the experiment subject!")
    print()
    subject = build_person(
        input("Enter the subject's first name: "),
        input("Enter the subject's last name: "),
        input("Enter the subjects gender: "),
        int(input("Enter the subjects age: "))
        )
        
    
    experiment = build_experiment(
        experiment_name,
        experiment_date,
        supervisor,
        subject
    )
    print(experiment)


with open("experiment.json", "w") as outfile:
        json.dump(experiment, outfile, indent=4)
        print("Experiment saved to experiment.json")
        
