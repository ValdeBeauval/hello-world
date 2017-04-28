import turtle

def koch_string (iteration, pattern='AGADAGA', start='A'):
    current = start
    if iteration < 0:
        raise Exception('itération doit être supérieur à 0')

    for i in range (iteration):
        current = current.replace(start, pattern)

    return current

def draw_koch (iterations, pattern='AGADAGA', start='A'):
    ks = koch_string(iterations, pattern, start)

    turtle.setup(800, 600)
    window = turtle.Screen()
    turtle.up
    turtle.backward(400)
    turtle.down()

    for car in ks:
        if car == 'A':
            turtle.forward(400 / (3 ** (iterations -1)))
        elif car == 'G':
            turtle.left(60)
        elif car == 'D':
            turtle.right(120)
        else:
            raise Exception('Bad letter')    
            
    window.exitonclick()

if __name__ == '__main__':
    print (draw_koch(3))




