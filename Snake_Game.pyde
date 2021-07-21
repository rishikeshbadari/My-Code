from random import randint
snake = []
nBubbles = 1
sc = 0.9
food = []
nFood = 1
count = 1
x = 5
y = 5
#creating the "bubbles" in the snake
class Bubble(object):
    def __init__(self):
        self.col = [randint(0,256),randint(0,256), randint(0,256)]
        self.xcor = randint(0,width)
        self.ycor = randint(48,height)
        self.r = 15
    def display(self):
        fill(self.col[0], self.col[1], self.col[2])
        ellipse(self.xcor, self.ycor, self.r, self.r)
#creating the "food" that the snake will eat
class Food(object):
    def __init__(self):
        self.xcor = randint(0,width)
        self.ycor = randint(0,height-50)
        self.r = 15
    def display(self):
        fill(255,255,255)
        ellipse(self.xcor,self.ycor,self.r,self.r)
#sets up the frameRate, size of the screen, as well as creating bubbles and food
def setup():
    frameRate(120)
    size(700,700)
    background(0)
    colorMode(RGB)
    for cnt in range(0, nBubbles):
        snake.append(Bubble())
    for cnt in range(0, nFood):
        food.append(Food())
def draw():
    global count
    global nBubbles
    background(0)
    food[0].display()
    #allowing the snake to move
    if(keyCode == DOWN):
        snake[0].ycor = snake[0].ycor + 1
    elif(keyCode == UP):
        snake[0].ycor = snake[0].ycor - 1
    elif(keyCode == RIGHT):
        snake[0].xcor = snake[0].xcor + 1
    elif(keyCode == LEFT):
        snake[0].xcor = snake[0].xcor - 1
    snake[0].display()
    #drawing the snake and displaying it
    for ind in range(1,nBubbles):
        snake[ind].xcor = snake[ind].xcor + 0.07*(snake[ind-1].xcor - snake[ind].xcor)
        snake[ind].ycor = snake[ind].ycor + 0.07*(snake[ind-1].ycor - snake[ind].ycor)
        snake[ind].display()
    #having the snake add a bubble once it eats a food
    if(abs((food[0].xcor - snake[0].xcor)) < 15 and abs((food[0].ycor - snake[0].ycor)) < 15):
        food[0] = Food()
        count += 1
        nBubbles += 1
        snake.append(Bubble())
        for ind in range(1,nBubbles):
            snake[ind].xcor = snake[ind].xcor + 0.07*(snake[ind-1].xcor - snake[ind].xcor)
            snake[ind].ycor = snake[ind].ycor + 0.07*(snake[ind-1].ycor - snake[ind].ycor)
            snake[ind].display()
    #reroutes the food if it's inside the top rectangle
    if(food[0].xcor > 140 and food[0].xcor < 560 and food[0].ycor > 8 and food[0].ycor < 48):
        food[0] = Food()
    #stops the game if the snake's center leaves the edge of the screen
    if(snake[0].xcor >= 700 or snake[0].ycor >= 650 or snake[0].xcor <= 0 or snake[0].ycor <= 0):
        fill(255,255,255)
        textSize(60)
        text("OUT OF BOUNDS", 350, 300)
        noLoop()
    redraw()
    #stops the game if the snake's center hits the top rectangle
    if(snake[0].xcor >= 140 and snake[0].xcor <= 560 and snake[0].ycor >= 8 and snake[0].ycor <= 48):
        fill(255,255,255)
        textSize(60)
        text("OUT OF BOUNDS", 360, 310)
        noLoop()
    redraw()
    #top rectangle
    fill(255,255,255)
    rect(140,8,420,40)
    #bottom rectangle
    fill(255,255,255)
    rect(10,650,680,40)
    fill(0,0,0)
    textSize(30)
    textAlign(CENTER)
    text("SCORE: ", 350, 680)
    text(count, 415, 680)
    fill(255,195,0)
    text("SNAKE by Rishikesh Badari", 349, 39)
    fill(255,87,51)
    text("SNAKE by Rishikesh Badari", 350, 39)
    fill(199,0,57)
    text("SNAKE by Rishikesh Badari", 351, 39)
