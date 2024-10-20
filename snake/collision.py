from snake import Snake


class Collision(Snake):
    def snake_food_collision(self, food, increment):
        if self.snake_segments[0].distance(food) < 20:
            increment()
            self.generate_food(food)
            self.grow_body(self.snake_segments)

    def snake_body_collision(self):
        for segment in self.snake_segments[1:]:
            if self.snake_segments[0].distance(segment) < 10:
                return True

        return False

    def snake_wall_collision(self):
        left, right = -(self.WIDTH // 2) + 20, (self.WIDTH // 2) - 20
        up, down = (self.HEIGHT // 2) - 20, -(self.HEIGHT // 2) + 20
        snake_head = self.snake_segments[0]

        if snake_head.xcor() < left or snake_head.xcor() > right:
            return True
        elif snake_head.ycor() > up or snake_head.ycor() < down:
            return True

        return False