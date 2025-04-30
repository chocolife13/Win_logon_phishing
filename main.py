from PIL import Image, ImageTk
import tkinter as tk
import keyboard
import os

def ok():
    pass

menu = tk.Tk()

screen_width = menu.winfo_screenwidth()
screen_height = menu.winfo_screenheight()

menu.title("Login to Windows")


menu.geometry(f"600x700+{(screen_width // 2) - 300}+{(screen_height // 2) - 350}")
menu.resizable(False, False)

def GET_OUT(event):
    print("GET_OUT")
    os.system("start explorer.exe")
    menu.iconify()
    main.destroy()
    

def start():
    global main
    global menu
    
    menu.withdraw()
    os.system("taskkill /f /im explorer.exe")
    
    main = tk.Toplevel(menu)
    main.geometry(f"{screen_width}x{screen_height}+0+0")
    main.overrideredirect(True)
    main.protocol("WM_DELETE_WINDOW", ok)
    main.attributes("-topmost", True)
    

    image = Image.open(os.path.join(os.getcwd(), "BG.png"))
    image = image.resize((screen_width, screen_height))
    image =  ImageTk.PhotoImage(image)

    image_loading = tk.Label(main, image= image)
    image_loading.image = image
    image_loading.pack(fill="both", expand=True)
    
    
    main.bind("d" + "e" + "v", GET_OUT)







bouton = tk.Button(menu, text="Lancer", command = start)
bouton.pack(side="bottom", pady=25)





menu.mainloop()