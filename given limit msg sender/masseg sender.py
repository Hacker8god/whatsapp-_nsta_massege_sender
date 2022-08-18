import pyautogui as pt
import time

from pygments import highlight
limit=input("enter limit : ")
massage=input("enter msg : ") 
print("click in typebox within 10 sec...")
i=1
time.sleep(1)
while i<int(limit):
    pt.typewrite(massage)
    pt.press("enter")
    i+=1
   