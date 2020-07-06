import winsound
import time

fr=1000
d=900

ar=2000
a=900
count=0
print("sound started")
for i in range(5):
 
    winsound.Beep(fr,d)
    count=count+1
    print(count)
    winsound.Beep(ar,a)
    
print("sound ended")


    