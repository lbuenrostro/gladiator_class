from random import randint


class Gladiator:
    """Gladiator fighter."""

    def __init__(self, name, health, rage, damage_low, damage_high):
        """(Gladiator) -> NoneType
        creates a gladiator named name and it has health, rage, damage_low, damage_high"""
        self.name = name
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def __str__(self):
        """ (Gladiator) -> string
        returns a string representation of gladiator"""
        return 'name: {}, health: {}, rage: {}, damage_low: {}, damage_high: {}'.format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high)

    def attack(self, other_g):
        '''(Gladiator, Gladiator) -> '''
        normal = randint(self.damage_low, self.damage_high)
        if randint(1, 100) >= self.rage:
            other_g.health -= normal * 2
            self.rage = 0
        else:
            other_g.health = other_g.health - normal
            other_g.rage += 15

    def heal(self):
        '''Gladiator -> Gladiator'''
        if self.rage >= 10:
            self.health = min(100, self.health + 5)
            self.rage = max(0, self.rage - 10)

    def kamehameha(self, other_g):
        '''Gladiator -> Gladiator'''
        mega_attack = randint(30, 50)
        normal = randint(self.damage_low, self.damage_high)
        if [self.rage] >= 30:
            defender[self.health] = defender[self.health] - mega_attack
            [self.rage] = 0
        else:
            defender[self.health] = defender[self.health] - normal
            self.rage += 15

    def is_dead(self):
        '''Gladiator -> bool
        returns True if gladiator
        has no health'''
        if self.health <= 0:
            return True