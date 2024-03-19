from my_function import build_person, build_experiment

if __name__ == "__main__":
    supervisor = build_person("Alexander", "Kometer", "male", 27)
    subject = build_person("Max", "Mustermann", "male", 30)
    
    experiment = build_experiment(
        "Heart Rate Response to Exercise",
        "2024-03-18",
        supervisor,
        subject
    )
    
    print(experiment)
