from turtle import *

color('red', 'black')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
forward(200)
backward(200)
shape('square')
end_fill()
done()