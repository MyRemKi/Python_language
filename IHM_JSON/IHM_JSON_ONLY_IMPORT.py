from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import filedialog
import json

#define event Buttons ...
def Event_Button_Enter(event):
    event.widget.config(bg="#75F058")
def Event_Button_Leave(event):
    event.widget.config(bg="#EAFFE5")
#end event

IHM = tk.Tk()

IHM.geometry("1000x400")
IHM.resizable(False,False)
IHM.title("PYSON")

#Settings Frames

#Frame Settings JSON
frame_settings = tk.Frame(IHM,bg = "lightblue",width = 1000,height = 20)
frame_settings.place(x = 0,y = 0)
frame_settings.pack()

#Frame Print Datas
frame_json = tk.Frame(IHM,bg = "#648A5B",width = 1000,height = 360)
frame_json.place(x = 0,y = 20)
frame_json.pack()

#Settings Label to import datas
custom_font = ("Cambria", 11, "bold")
label = tk.Label(frame_json,text = "",bg = "#648A5B",font=custom_font,width = 1000,height = 360)

#Settings Buttons

#Button in frames_settings
button_import = tk.Button(frame_settings,bg = "#EAFFE5",text = "Import",command = lambda : From_Bouton_Import(frame_json),width = 70,height = 2)
button_import.place(x = 0,y = 0)
button_import.pack(side="left")

#Button in frames_settings
button_init = tk.Button(frame_settings,bg = "#EAFFE5",text = "Init",command = lambda : From_Bouton_Init(frame_json),width = 70,height = 2)
button_init.place(x = 251,y = 0)
button_init.pack(side="left")

#Event Buttons
button_import.bind("<Enter>", Event_Button_Enter)
button_init.bind("<Enter>", Event_Button_Enter)

button_import.bind("<Leave>", Event_Button_Leave)
button_init.bind("<Leave>", Event_Button_Leave)
#end Event Buttons

#This Function allow to import json datas ONLY WITHOUT KEYS
def From_Bouton_Import(frame):

    LabelIsEmpty = (label.cget("text") == "")

    if LabelIsEmpty :

        #a way to retrieve a JSON file in GUI
        """
        file_location = askstring("Input", "Enter the location of your file")
        file_name = askstring("Input", "Enter the name of your json file")

        if (file_location == "" or file_name == "") or (file_location is None) or (file_name is None) :
            messagebox.showwarning("Error","Your both answers is invalid")
            return

        try:

            file = file_location + "\\" + file_name + ".json"
            with open(file,encoding = "utf-8",newline = '') as F :
                datas = json.load(F)

            label.pack()

        except FileNotFoundError :
            messagebox.showwarning("Error","invalid file location !")
            return

        except json.JSONDecodeError:
            messagebox.showwarning("Error","invalid file datas, check your file syntax ! (ONLY WITHOUT KEYS)")
            return
        """
        #end of the way

        #Another way to retrieve a JSON file in GUI
        #"""
        file_location = filedialog.askopenfilename()

        if (file_location == "") or (file_location is None):
            messagebox.showwarning("Error","Your answer is invalid")
            return

        try:

            file = file_location
            with open(file,encoding = "utf-8",newline = '') as F :
                datas = json.load(F)

            label.pack()

        except FileNotFoundError :
            messagebox.showwarning("Error","invalid file location !")
            return

        except json.JSONDecodeError:
            messagebox.showwarning("Error","invalid file datas, check your file syntax !")
            return
        #"""
        #End of Another way

        #Import JSON datas without keys
        list_keys = datas[0].keys()
        items = ""

        for key in list_keys:
                items = items + key + "   "
        label.config(text = items + "\n")

        for data in datas:
            request=""

            for key in list_keys:
                request = request+str(data[key]) + " " +(" "*(10-len(str(data[key]))))

            label.config(text = label.cget("text") + str(request + "\n"))



    else :
        messagebox.showwarning("Error","Label not empty ! Please click on 'Init' button to empty your label")

def From_Bouton_Init(frame):

    LabelIsEmpty = (label.cget("text") == "")

    if LabelIsEmpty != True :
        label.config(text = "")
        label.pack_forget()

    else:
        messagebox.showwarning("Error","Label already empty")

IHM.mainloop()