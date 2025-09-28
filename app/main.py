class Animal:
    alive = list()

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False) -> None:
        self.name = name
        self.hidden = hidden
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}"
                f"}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = False if self.hidden else True


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                self.alive.remove(herbivore)
