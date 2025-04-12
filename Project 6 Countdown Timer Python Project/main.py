import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = f"{mins:02d}:{secs:02d}"
        print(timer_format, end="\r")
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!")

# User se input lena
seconds = int(input("Enter countdown time in seconds: "))
countdown_timer(seconds)