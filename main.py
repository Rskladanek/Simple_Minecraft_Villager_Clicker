# Program działa na pełym ekranie !!!
import turtle
from playsound import playsound  #pobrałem tą biblioteke z https://pypi.org/project/playsound/#description wersja (1.2.2)
import winsound
import random

def playmusic1():
    winsound.PlaySound(r'MincecraftVillagerRemix.wav',winsound.SND_ASYNC)
def playmusic2():
    winsound.PlaySound(r'MinecraftC418.wav', winsound.SND_ASYNC)
def playmusic3():
    winsound.PlaySound(r'megalovillager.wav', winsound.SND_ASYNC)

a=(random.randint(1,3))


wn = turtle.Screen()
wn.title("Cookie Cliker by Remigiusz S(bo rodo)")
wn.bgpic("Wioska.png")

wn.register_shape("VillagerLeb.gif")


Villager = turtle.Turtle()
Villager.shape("VillagerLeb.gif")
Villager.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("Black")
pen.penup()
pen.goto(0, 350)
pen.write(f"Clicks: {clicks}", align="center", font=("Impact", 64, "bold"))


def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Impact", 64, "bold"))
    playsound('Villager_DMG_sound.wav')




Villager.onclick(clicked)



if(a==1):
    playmusic1()
elif(a==2):
    playmusic2()
else:
    playmusic3()



wn.mainloop()