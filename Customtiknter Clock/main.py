
import customtkinter
from datetime import datetime
from threading import Thread
from time import sleep

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.title('Customtkinter - Clock')
root.geometry('420x220')
root.resizable(width = False, height = False)

clock_font = customtkinter.CTkFont('digital-7', 80)

clock_label = customtkinter.CTkLabel(
    root,
    width=400,
    height=150,
    text = '3:50:50: PM',
    font = clock_font,
    text_color = 'red'
)

clock_label.place(x = 10, y = 25)

def update_clock():
    clock = datetime.now()
    h = int(clock.hour)
    m = clock.minute
    s = clock.second
    
    am_pm = clock.strftime('%p')
    
    time_string = f'{h}:{m}:{s} {am_pm}'
    clock_label.configure(text = time_string)
    sleep(1)
    update_clock()

# start new Thread
t = Thread(target=update_clock)
t.start()

root.mainloop()