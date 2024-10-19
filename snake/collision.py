from snake import Snake


class Collision(Snake):
    def snake_food_collision(self, food, increment):
        if self.snake_segments[0].distance(food) < 20:
            increment()
            self.generate_food(food)
            self.grow_body(self.snake_segments)

    def snake_body_collision(self):
        for segment in range(1, len(self.snake_segments) - 1):
            if self.snake_segments[0].distance(self.snake_segments[segment]) < 20:
                return True

        return False