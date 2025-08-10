from turtle import Turtle, Screen

class GameOverPrompt:
    def __init__(self,screen):
        self.screen = screen

    def play_again(self,restart_callback):
        #Display "Play again"
        self.prompt =Turtle()
        self.prompt.hideturtle()
        self.prompt.color("Gold")
        self.prompt.penup()
        self.prompt.goto(0,0)
        self.prompt.write("Play Again",align="center",font=("Courier",24,"bold"))


        #Yes button
        self.yes = Turtle()
        self.yes.hideturtle()
        self.yes.color("Blue")
        self.yes.penup()
        self.yes.goto(-40,-10)
        self.yes.write("Yes",align="center",font=("Courier",24,"bold"))

        #NO button
        self.no = Turtle()
        self.no.hideturtle()
        self.no.color("Red")
        self.no.penup()
        self.no.goto(40,-10)
        self.no.write("No",align="center",font=("Courier",24,"bold"))

        #Click detection
        self.screen.onscreenclick(lambda x,y: self.handle_click(x,y,restart_callback))

    def handle_click(self,x,y,restart_callback):
        #YEs area
        if -70 < x<-10 and -20<y<20:
            self.clear_prompt()
            restart_callback()
        #no area
        elif 10 < x<70 and -20 <y <20:
            self.screen.bye()

    def clear_prompt(self):
        self.prompt.clear()
        self.yes.clear()
        self.no.clear()