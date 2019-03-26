import sonar2
import servo2
import time

a = sonar2.display()
print(type(a))
if a <= 15:
    servo2.move()
 
