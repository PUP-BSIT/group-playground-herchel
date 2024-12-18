class FitnessTracker:
    def __init__(self):
        self.activities = {}

    def log_activity(self, activity_name, minutes):
        if activity_name in self.activities:
            self.activities[activity_name] += minutes
        else:
            self.activities[activity_name] = minutes
            
        print(f"Logged {minutes} minutes for {activity_name}."
              f"\nTotal: {self.activities[activity_name]} minutes.")

    def remove_activity(self, activity_name):
        if activity_name in self.activities:
            del self.activities[activity_name]
            print(f"Activity '{activity_name}' removed from the tracker.")
        else:
            print(f"Activity '{activity_name}' does not exist in the tracker.")

    def display_activities(self):
        if not self.activities:
            print("No activities logged.")
        else:
            print("Current Activities:")
            for activity_name, minutes in self.activities.items():
                print(f"- {activity_name}: {minutes} minutes")

    def check_activity(self, activity_name):
        if activity_name in self.activities:
            print(f"{activity_name}: {self.activities[activity_name]} "
                  f"minutes logged.")
        else:
            print(f"No logs for {activity_name}.")

    def clear_activities(self):
        self.activities.clear()
        print("All activities have been cleared.")

    def display_menu(self):
        while True:
            print("\nFitness Tracker")
            print("1. Log Activity")
            print("2. Remove Activity")
            print("3. Display Activities")
            print("4. Check Activity")
            print("5. Clear All Activities")
            print("6. Return to main menu")

            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    activity_name = input("Enter the activity name: ")
                    minutes = int(input("Enter the number of minutes: "))
                    self.log_activity(activity_name, minutes)
                case "2":
                    activity_name = input("Enter the activity name to remove: ")
                    self.remove_activity(activity_name)
                case "3":
                    self.display_activities()
                case "4":
                    activity_name = input("Enter the activity name to check: ")
                    self.check_activity(activity_name)
                case "5":
                    self.clear_activities()
                case "6":
                    return
                case _:
                    print("Invalid choice. Please try again.")

tracker = FitnessTracker()
tracker.display_menu()