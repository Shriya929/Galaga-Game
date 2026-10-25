import pgzrun

WIDTH = 600
HEIGHT = 450

bullets_List = []
bugs = []
remove_bullets = []
remove_bugs = []

g = Actor("galaga")
g.x = 300
g.y = 360

direction = 1
score = 0 
game_over = False
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
    screen.draw.text("Score =" + str(score), (0,400))
    if game_over:
        screen.fill("blue")
        screen.draw.text("Game Over! Your score is" + str(score), (300,225))
    

def update():
    global direction,score,game_over
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
            if b.colliderect(u):
                #bugs.remove(u)  
                #bullets_List.remove(b)
                remove_bugs.append(u)
                remove_bullets.append(b)
                score = score + 5
    for u in remove_bugs:
        if u in bugs:
            bugs.remove(u)

    for b in remove_bullets:
        if b in bullets_List:
            bullets_List.remove(b)
    if bugs:
        for u in bugs:
            u.x = u.x + 5*direction
        if bugs[-1].x >= 600:
            direction = -1
            for u in bugs:
                u.y = u.y + 20
        if bugs[0].x <= 0:
            direction = 1
            for u in bugs:
                u.y = u.y + 20
    else:
        game_over = True

def on_key_down(key):
    if key == keys.SPACE:
        b = Actor("bullet")
        b.x = g.x
        b.y = g.y - 45
        bullets_List.append(b)

pgzrun.go()