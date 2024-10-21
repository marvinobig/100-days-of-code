from os import path
from snake import Snake


class Score(Snake):
    current_score = 0
    high_score = 0

    def increment(self):
        self.current_score += 1

    def display_scores(self, score):
        if path.exists("snake_data.txt"):
            with open("snake_data.txt") as snake:
                self.high_score = int(snake.read())

        score.clear()
        score.hideturtle()
        score.penup()
        score.color('white')
        score_position = (-(Snake.WIDTH // 2) + 40, (Snake.HEIGHT // 2) - 70)
        score.setpos(score_position)
        score.write(f"Current Score: {self.current_score}\nHighest Score: {self.high_score}", font=('Helvetica', 20, 'bold'))

    def update_highscore(self, score):
        if self.current_score > self.high_score:
            self.high_score = self.current_score

            with open("snake_data.txt", mode="w") as snake:
                snake.write(f"{self.high_score}")


            score.clear()
            score.hideturtle()
            score.write(f"Current Score: {self.current_score}\nHighest Score: {self.high_score}",
                        font=('Helvetica', 20, 'bold'))

        self.current_score = 0
