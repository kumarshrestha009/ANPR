import sonar
import database
import servo
import time

a = sonar.display()
print(type(a))
d = database.read_table()
for i in d:
    for j in i:
        if j == a:
            print("Match Found")
            print("Please Wait")
            print("Opening the gate")
            servo.move()
            break
        else:
            print("No Match Found")
            print("Match found")
            print("Please Wait .......")
            print("opening the gate")
            
            servo.move()
            break
        break
    break

