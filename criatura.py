
class Criatura:

    def __init__(self, sprite, pos_x, pos_y, velocidade=20):
        self.sprite = sprite
        self.rect = sprite.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocidade = velocidade

    def move_left(self):
        
        if self.rect.x > -20: 
            self.rect.x -= self.velocidade
        

    def move_right(self):
        
        if self.rect.x < 1380:
            self.rect.x += self.velocidade 
    

    def shot(self):
        pass
    
    def move_down(self):
        pass
