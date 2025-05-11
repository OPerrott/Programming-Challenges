import keyboard
import mouse
import time


username = "Tenuous"


password = []

while True:
    if keyboard.is_pressed("F4"):
        
        with open('problem_3/passwords.txt', 'r') as file:
            passwords = [line.strip() for line in file]
        
        time.sleep(5)
        
        for password in passwords:
            
            if keyboard.is_pressed("F7"):
                break
            
            
            mouse.click()
            
            keyboard.press("tab")
            
            keyboard.write(username)
            
            time.sleep(0.05)
            
            keyboard.press("tab")

            keyboard.write(password)
            
            time.sleep(0.05)
            
            keyboard.press("tab")
            
            keyboard.press("enter")
            
            