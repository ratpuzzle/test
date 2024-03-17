import time
import random
import tkinter as tk

from start_text import hello_text
from shop_run import def_shop
from mine_run import def_main
from prison_run import def_prison
from tavern_run import def_tavern
from lumber_mill_run import def_lumber_mill
from start_loc_file import start_loc, def_killer

window = tk.Tk()
window.title('Поход  в шахту капать-капать')
window.geometry('400x400')
# переменные
gold = 0
hp = 10
pickaxe = None  # ='алмазна'   ='каменная'


start_loc()





text_field = tk.Label(text='Приветствую вас в  деревне....', width=56, height=15, bg='yellow')
text_field.grid(row=5)
time.sleep(0)
text_field = tk.Label(text='Вы играете за персонажа....', width=56, height=15, bg='yellow')
text_field.grid(row=5)
time.sleep(0)

while True:
    if gold <= -5:
        def_killer()
        text_field = tk.Label(text='ВЫ будете арестованы и отправленны в тюрьму до уплаты долгов', width=56, height=15,
                              bg='yellow')
        text_field.grid(row=5)
        time.sleep(2)

        button_prison = tk.Button(text='Поехали', bg='pink', command=lambda: [def_killer(), def_lumber_mill])
        button_prison.grid(column=0, row=4)
        button_prison.bind("<Button-1>", def_prison)
    elif hp <= 0:

        gold -= 10
        hp = 10

    window.mainloop()
