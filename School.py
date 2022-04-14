def school():
    name = input("What is your Name? ")
    print("Hello " + name)
    age = input("How old are you? ")
    print("Hello " + name + " you are " + age + " years old ")
    school = input("What school do you go to? ")
    print("Hello " + name + " you are " + age + " years old" + " you attend " + school)
    subject = input("What is your favorite school subject? ")
    print("Hello " + name + " you are " + age + " years old" + " you attend " + school + " you love doing " + subject)

def main():
    talk = input("Do you want to talk about school or house? ")
    if talk == "school" or "School":
        school()
        
main()
