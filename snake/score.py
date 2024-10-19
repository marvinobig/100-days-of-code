from turtle import Turtle
from snake import Snake


class Score(Snake):
    current_score = 0

    def increment(self):
        self.current_score += 1

    def display_score(self, score):
        score.clear()
        score.penup()
        score.color('white')
        score_position = (-(Snake.WIDTH // 2) + 40, (Snake.HEIGHT // 2) - 70)
        score.setpos(score_position)
        score.write(self.current_score, font=('Helvetica', 30, 'bold'))