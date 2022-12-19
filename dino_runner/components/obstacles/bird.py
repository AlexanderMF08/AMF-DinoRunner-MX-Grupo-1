from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0 
        super().__init__(image, self.type)
        self.fly_index = 0
    
    def draw(self, screen):
        if self.fly_index >= 10:
            self.fly_index = 0
        screen.blit(self.image[self.fly_index//5], self.rect)
        self.fly_index +=1     
    
