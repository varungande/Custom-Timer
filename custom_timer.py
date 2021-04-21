# Varun Gande


import time
from win10toast import ToastNotifier


# Custom Timer
def timer():
    
    print("Please enter the information in whole numbers. For example, enter '2' or '3' rather than '2.7' or '3.4'")
    time.sleep(0.5)

    act_user = int(input("Enter in minutes, the duration: "))
    break_user = int(input("Enter in minutes, the duration of your break: "))
    toaster = ToastNotifier()
    print("Timer Starts Now")
    toaster.show_toast("Timer Starts Now", "You may start your activity now!", duration = 3)
    ptime = (act_user)*60

    while ptime:
        minutes = ptime // 60
        seconds = ptime % 60
        timer = "{:02d}:{:02d}".format(minutes, seconds)
        print(timer, end = "\r")
        time.sleep(1)
        ptime -= 1
        
        if ptime == 0:
            btime = (break_user)*60
            print("Break Starts Now")
            toaster.show_toast("Break Starts Now", "Take a break, you've earned it!", duration = 3)

            while btime:
                minutes = btime // 60
                seconds = btime % 60
                timer = "{:02d}:{:02d}".format(minutes, seconds)
                print(timer, end = "\r")
                time.sleep(1)
                btime -= 1

                if btime == 0:
                    print("Timer Over")
                    toaster.show_toast("Time Over", "Your break has ended", duration = 3)
                    break
                    
timer()

