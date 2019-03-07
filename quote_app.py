

from tkinter import Tk, Canvas, Frame, Label, Entry, Button, ttk, font, PhotoImage
HEIGHT = 800
WIDTH = 700
"""Dictionary that retrieves print cost per item.  x stands for the quantity to be quotes.  For a one color print/one side the cost is $.60 per item for 1200 units or more"""
def get_quote():
    x = int(quantity_entry.get()) 
    pricer_a = {  

    0:0,         
    1: .6 if x >= 1200 else .7 if x >= 480 else .75 if x >= 240 else .85 if x >= 180 else .95 if x >= 120 else 1.05 if x >= 60 else 1.2 if x >= 36 else 1.6 if x >= 12 else None,

    2: .75 if x >= 1200 else .85 if x >= 480 else .95 if x >= 240 else 1.05 if x >= 180 else 1.1 if x >= 120 else 1.45 if x >= 60 else 1.60 if x >= 36 else 1.90 if x >= 12 else None,
        
    3: .80 if x >= 1200 else .90 if x >= 480 else 1.05 if x >= 240 else 1.15 if x >= 180 else 1.35 if x >= 120 else 1.75 if x >= 60 else 2.0 if x >= 36 else 2.25 if x >= 12 else None,
           
    4: 1.1 if x >= 1200 else 1.1 if x >= 480 else 1.25 if x >= 240 else 1.4 if x >= 180 else 1.75 if x >= 120 else 2.15 if x >= 60 else 2.5 if x >= 36 else 2.65 if x >= 12 else None,
            
    5: 1.1 if x >= 1200 else 1.2 if x >= 480 else 1.3 if x >= 240 else 1.55 if x >= 180 else 1.85 if x >= 120 else 2.45 if x >= 60 else 2.90 if x >= 36 else None if x >= 12 else None,
           
    6: 1.35 if x >= 1200 else 1.45 if x >= 480 else 1.7 if x >= 240 else 1.85 if x >= 180 else 2.20 if x >= 120 else None if x >= 60 else None if x >= 36 else None if x >= 12 else None
        
    }   
    """Output boxes"""
    output_front = pricer_a[int(front_entry.get())]
    frontcost_label['text'] = f"Front Cost: ${output_front:,.2f}"

    output_back = pricer_a[int(back_entry.get())]
    backcost_label['text'] = f"Back Cost: ${output_back:,.2f}"

    output_totalcost = int(quantity_entry.get()) * (float(price_entry.get()) + output_front + output_back + float(flash_entry.get())) + float(setup_entry.get()) + float(art_entry.get())
    totalcost_label['text'] = f"Total Cost: ${output_totalcost:,.2f}"

    out_totalquote = output_totalcost * (1 + (float(markup_entry.get()))/100)
    totalquote_label['text'] = f"Total Quote: ${out_totalquote:,.2f}"
    totalquote_label['font'] = ('Ariel', 20)

    out_itemquote = out_totalquote/x
    itemquote_label['text'] = f"Quote per Item: ${out_itemquote:,.2f}"
    itemquote_label['font'] = ('Ariel', 20)

    output_totalprofit = out_totalquote - output_totalcost
    totalprofit_label["text"] = f"Total Profit: ${output_totalprofit:,.2f}"

    output_cost = output_totalcost/x
    cost_label['text'] = f'Cost per Item: ${output_cost:,.2f}'

    output_profit = output_totalprofit/x
    profit_label['text'] = f"Profit per Item: ${output_profit:,.2f}"
    
    
root = Tk()
root.title("Quote Maker")


quote_canvas = Canvas(root, height = .8*HEIGHT, width = .8*WIDTH )
quote_canvas.pack()



quote_frame = Frame(quote_canvas, bg="#4a545f", bd=5, pady=10)
quote_frame.place(relx = 0, rely = 0, relwidth=1, relheight=.2)

economics_frame = Frame(quote_canvas, bg="#5f4a54", bd=5)
economics_frame.place(relx = 0, rely = .2, relwidth=1, relheight=.4)

input_frame = Frame(quote_canvas, bg = "#545f4a", bd=5)
input_frame.place(relx = 0, rely = .6, relwidth=1, relheight=.4)

quantity_label = Label(input_frame, text="Quantity to Print", anchor='w',bg = "black", fg = "white")
quantity_label.place(relx = 0, rely = 0, relwidth=.28, relheight= .08)

price_label = Label(input_frame, text="Price of Item", anchor='w',bg = "black", fg = "white")
price_label.place(relx = 0, rely = .1, relwidth=.28, relheight= .08)

front_colors_label = Label(input_frame, text="Front: Number of Colors", anchor='w',bg = "black", fg = "white")
front_colors_label.place(relx = 0, rely = .2, relwidth=.28, relheight= .08)

back_colors_label = Label(input_frame, text="Back: Number of Colors", anchor='w',bg = "black", fg = "white")
back_colors_label.place(relx = 0, rely = .3, relwidth=.28, relheight= .08)

mark_up_label = Label(input_frame, text="Mark-Up %", anchor='w',bg = "black", fg = "white")
mark_up_label.place(relx = 0, rely = .4, relwidth=.28, relheight= .08)

set_up_label = Label(input_frame, text="Set-Up Charge", anchor='w',bg = "black", fg = "white")
set_up_label.place(relx = 0, rely = .5, relwidth=.28, relheight= .08)

art_charge_label = Label(input_frame, text="Art-Charge", anchor='w',bg = "black", fg = "white")
art_charge_label.place(relx = 0, rely = .6, relwidth=.28, relheight= .08)

flash_label = Label(input_frame, text="Flash-Charge", anchor='w',bg = "black", fg = "white")
flash_label.place(relx = 0, rely = .7, relwidth=.28, relheight= .08)

"""Entry Boxes"""
quantity_entry = Entry(input_frame, bg = "white", fg = "black")
quantity_entry.place(relx = .3, rely = 0, relwidth=.1, relheight = .08)

price_entry = Entry(input_frame, bg = "white", fg = "black")
price_entry.place(relx = .3, rely = .1, relwidth=.1, relheight = .08)

front_entry = Entry(input_frame, bg = "white", fg = "black")
front_entry.place(relx = .3, rely = .2, relwidth=.1, relheight = .08)
front_entry.insert(0,0)

back_entry = Entry(input_frame, bg = "white", fg = "black")
back_entry.place(relx = .3, rely = .3, relwidth=.1, relheight = .08)
back_entry.insert(0,0)

markup_entry = Entry(input_frame, bg = "white", fg = "black")
markup_entry.place(relx = .3, rely = .4, relwidth=.1, relheight = .08)
markup_entry.insert(0,45)

setup_entry = Entry(input_frame, bg = "white", fg = "black")
setup_entry.place(relx = .3, rely = .5, relwidth=.1, relheight = .08)
setup_entry.insert(0,20)

art_entry = Entry(input_frame, bg = "white", fg = "black")
art_entry.place(relx = .3, rely = .6, relwidth=.1, relheight = .08)
art_entry.insert(0,0)

flash_entry = Entry(input_frame, bg = "white", fg = "black")
flash_entry.place(relx = .3, rely = .7, relwidth=.1, relheight = .08)
flash_entry.insert(0,.6)

"""Quote Button"""
quote = Button(input_frame, bd = 50, fg ="red", text="CLICK HERE", font= ('Ariel', 20), command = get_quote) 
quote.place(relx=0.7, rely=.5)
quote.config(relief='sunken')

"""Labels"""
cost_label = Label(economics_frame, text="cost",anchor='w', bg='black', fg="white")
cost_label.place(relx = 0, rely = .05, relwidth = .5, relheight = .1)

profit_label = Label(economics_frame, text="profit", anchor='w', bg='black', fg="white" )
profit_label.place(relx=0, rely= .17, relwidth = .5, relheight = .1)

totalcost_label = Label(economics_frame, text="total cost", anchor='w', bg='black', fg="white")
totalcost_label.place(relx=0, rely=.29,relwidth = .5, relheight = .1)

totalprofit_label = Label(economics_frame, text="total profit", anchor='w', bg='black', fg="white")
totalprofit_label.place(relx=0, rely=.41,relwidth = .5, relheight = .1)

frontcost_label = Label(economics_frame, text="front cost", anchor='w', bg='black', fg="white")
frontcost_label.place(relx=0, rely=.53,relwidth = .5, relheight = .1)

backcost_label = Label(economics_frame, text="back cost", anchor='w', bg='black', fg="white")
backcost_label.place(relx=0, rely=.65, relwidth = .5, relheight = .1)

totalquote_label = Label(quote_frame, text="Total Quote", anchor='w', bg='black', fg="white")
totalquote_label.place(relx=0, rely=.05,relwidth = .5, relheight = .4)

itemquote_label = Label(quote_frame, text="Quote per item", anchor='w', bg='black', fg="white")
itemquote_label.place(relx=0, rely=.55, relwidth = .5, relheight = .4)

   

   
   





root.mainloop()






      

