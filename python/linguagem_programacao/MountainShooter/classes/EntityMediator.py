from classes.Const import SCREEN_WIDTH
from classes.Enemy import Enemy
from classes.EnemyShot import EnemyShot
from classes.PlayerShot import PlayerShot

class EntityMediator:
    @staticmethod
    def __verify_collision_screen(entity):
        if isinstance(entity, Enemy):
            if entity.rect.right <= 0:
                entity.health = 0

        if isinstance(entity, PlayerShot):
            if entity.rect.left >= SCREEN_WIDTH:
                entity.health = 0

        if isinstance(entity, EnemyShot):
            if entity.rect.right <= 0:
                entity.health = 0
    
    @staticmethod
    def verify_collision(entity_list: list):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_screen(entity1)

    @staticmethod
    def verify_health(entity_list: list):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)