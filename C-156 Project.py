from tkinter import *
import random
from PIL import ImageTk, Image
root=Tk()

root.title("Endless Pokemon Game")
root.geometry("600x400")

root.configure(background = "Yellow")

img=ImageTk.PhotoImage(Image.open ("button.jpg"))

player1 = Label(root, text = "Player 1", bg = "CadetBlue1", fg = "black")
player1.place(relx = 0.1, rely = 0.3 , anchor =  CENTER)

player2 = Label(root, text = "Player 2", bg = "CadetBlue1", fg = "black")
player2.place(relx = 0.9, rely = 0.3 , anchor =  CENTER)

player_1_score_label = Label(root , bg = "CadetBlue1", fg = "black")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor =  CENTER)

player_2_score_label = Label(root , bg = "CadetBlue1", fg = "black")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor =  CENTER)

pokemon_list = ["Pikachu","Squirtle","Rattata","Persian","Paras","Nidoking","Meowth","Kadabra","Jigglypuff","Ivysuar","Charander","Bulbasaur","Abra"]
pokemon_power_list = [200,50,40,70,40,90,60,70,70,100,50,60,30]

label = Label(root)
label.place(relx = 0.5, rely = 0.5 , anchor =  CENTER)

player1_score = 0
def player1():
    global player1_score
    random_no1 = random.randint(0,12)
    random_pokemon = pokemon_list[random_no1]
    Label["Image"]= random_pokemon
    pokemon_power = pokemon_power_list[random_no1]
    player1_score = player1_score + pokemon_power
    player_1_score_label["text"] = str(player1_score)
    
player2_score = 0
def player2():
    global player2_score
    random_no2 = random.randint(0,12)
    random_pokemon = pokemon_list[random_no2]
    Label["Image"]= random_pokemon
    pokemon_power = pokemon_power_list[random_no1]
    player2_score = player2_score + pokemon_power
    player_2_score_label["text"] = str(player2_score) 
    
player_1_btn = Button(root, image = img, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor =  CENTER)
player_2_btn = Button(root, image = img, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6 , anchor =  CENTER)


root.mainloop()

    

