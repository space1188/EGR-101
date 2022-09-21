# Brian Diosan in class ten

def main() :
    filename = "inClassAssignments/InClassTen/pi_million_digits.txt"
    try :
        with open(filename) as file:
            lines = file.readlines()
            pi_string = ''
            for line in lines:
                pi_string += line.strip()
            print(f"{pi_string[:52]}...")
            print(len(pi_string))

            birthday = input("Enter your birthday, in form mmddyy: ")
            if birthday in pi_string:
                print("Your birthday does appear in the first million digits of pi!")
            else :
                print("Your birthday does not appear in the first million digits of pi.")
        
    except FileNotFoundError:
        print("File Is Not Found")

main()