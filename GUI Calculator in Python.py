#GUI Calculator in Python
import tkinter as tk #imports tkinter for GUI
import math #imports math for sqrt

#Creating main window
root = tk.Tk()            #creates window
root.title("Calculator")    #title of window
root.resizable(False, False) #makes window not resizeable

#Creating calculator screen/display
display = tk.Entry(root,width=30,
                    font=("Arial", 18),
                      justify="right")   #creates input widget, justify aligns text to right
display.grid(row=0, column=0,  #row and column places grid at top,
             columnspan=4,   #stretches across 4 columns
               padx=10, pady=10)

#Button Functions
def button_click(text):                       #function called when any button is pressed
  current_text = display.get()                #sees what is currently on the screen
  print(f"Current Text: {current_text}")       #prints to terminal for debugging
  print(f"Button Clicked: {text}")        #prints whatever button was clicked

  if text == "C":                   #if CLEAR button pressed
      display.delete(0, tk.END)     #delete everything from display

  elif text =="\u232B":                            #the erase button symbol #if ERASE button pressed
      display.delete(len(current_text)-1, tk.END)    #delete only the last character

  elif text == "CE":             #if CE button pressed
      display.delete(0, tk.END)   #clear everything like C

  elif text == "=":                  #if EQUAL button pressed
      try:                          #try to calculate
          result= eval(current_text)  #eval function does math
          display.delete(0, tk.END)   #clear the screen
          display.insert(tk.END, str(result))  #show result
          print(f"Result: {result}")             
      except Exception as e:       #if math fails i.e wrong input
          display.delete(0, tk.END)   #clear screen
          display.insert(tk.END, "Error")   #show Error
          print(f"Error: {e}")  
  elif text == "\u221A":          #if SQUARE ROOT button pressed
      try:                
          result = math.sqrt(float(current_text))   #calculate sqrt and convert text to number first
          display.delete(0, tk.END)         #clear screen
          display.insert(tk.END, str(result))  #show result
          print(f"Square Root: {result}")
      except Exception as e:               #if it fails
          display.delete(0, tk.END)         #clear screen
          display.insert(tk.END, "Error")   #show Error
          print(f"Error:, {e}")
  else: 
      display.insert(tk.END, text)      #for any other button it is displayed to screen
  
#Creating buttons layout 
buttons = [       #the list of buttons, only creating a list so no 'Button'
    ("C", 1, 0), ("CE", 1, 1), ("\u232B", 1, 2), ("/", 1, 3), 
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4",3 , 0), ("5",  3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4 ,0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("\u221A", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3)
]
for (text, row, col) in buttons: #loop through all bttons
    tk.Button(root,       #creates each button, tkinter is creating button so 'Button' 
    text=text,              #button label
     width=7,
     height=2,
     font=("Arial", 14),
     command=lambda t=text: button_click(t)  #when clicked call button_click
    ).grid(row=row,   #place in grid
          column=col,    
          padx=5, pady=5)   #space between buttons   
root.mainloop()     #keeps window open and running