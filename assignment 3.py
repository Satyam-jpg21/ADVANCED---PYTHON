from functools import wraps

# Decorator to format report output
def report_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 50)
        print("        DYNAMIC REPORT GENERATOR")
        print("=" * 50)
        result = func(*args, **kwargs)
        print("=" * 50)
        return result
    return wrapper


class Report:

    default_title = "Untitled Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Magic Method
    def __str__(self):
        return f"\nTitle : {self.title}\nContent : {self.content}"

    # Magic Method
    def __len__(self):
        return len(self.content)

    # Class Method
    @classmethod
    def create_default_report(cls):
        return cls(cls.default_title, "This is the default report content.")

    @report_decorator
    def display(self):
        print(self)


def main():

    reports = []

    while True:

        print("\n========== MENU ==========")
        print("1. Create New Report")
        print("2. Create Default Report")
        print("3. Display All Reports")
        print("4. Show Report Length")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            title = input("Enter Report Title: ")
            content = input("Enter Report Content: ")

            report = Report(title, content)
            reports.append(report)

            print("\nReport Created Successfully!")

        elif choice == "2":

            report = Report.create_default_report()
            reports.append(report)

            print("\nDefault Report Created Successfully!")

        elif choice == "3":

            if len(reports) == 0:
                print("\nNo Reports Available.")

            else:

                for i, report in enumerate(reports, start=1):
                    print(f"\nReport {i}")
                    report.display()

        elif choice == "4":

            if len(reports) == 0:
                print("\nNo Reports Available.")

            else:

                for i, report in enumerate(reports, start=1):
                    print(f"\nReport {i} Length = {len(report)} characters")

        elif choice == "5":

            print("\nThank You!")
            break

        else:

            print("\nInvalid Choice!")


if __name__ == "__main__":
    main()