import pgzrun

WIDTH = 600
HEIGHT = 450

bullets_List = []
bugs = []

g = Actor("galaga")
g.x = 300
g.y = 360

for t in range(3):
    for i in range(4):    
        u = Actor("bug")
        u.x = 60 + i*60
        u.y = 50 + t*50
        bugs.append(u)

def draw():
    screen.fill("black")    
    g.draw()
    for b in bullets_List:
        b.draw()
    for i in bugs:
        i.draw()
    

def update():
    if keyboard.left:
        if g.x > 0:
            g.x = g.x - 10
    if keyboard.right:
        if g.x < 600:
            g.x = g.x + 10
    for b in bullets_List:
        b.y = b.y - 3
        if b.y < 0:
            bullets_List.remove(b)
    for u in bugs:
        u.x = u.x + 5
    if bugs[-1].x >= 600:
        for u in bugs:
            u.y = u.y + 20
def on_key_down(key):
    if key == keys.SPACE:
        b = Actor("bullet")
        b.x = g.x
        b.y = g.y - 45
        bullets_List.append(b)

pgzrun.go()