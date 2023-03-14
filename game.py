"""task5"""
class Room:
    """class for room"""
    def __init__(self, name: str) -> None:
        """
        stores variables:
        name (of the room)
        """
        self.name = name
        self.description = None
        self.character = None
        self.item = None
        self.dct = {}

    def link_room(self, room: object, direction: str) -> None:
        """
        links two rooms, and specifies direction to a new room
        """
        self.dct[direction] = room

    def set_description(self, description: str) -> None:
        """
        set description of the room
        """
        self.description = description

    def get_details(self) -> str:
        """
        return details of the room
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for direction, room in (self.dct).items():
            print(f"{room.name} is {direction}")

    def set_character(self, character: object) -> None:
        """
        set enemy in the room
        """
        self.character = character

    def set_item(self, item: object) -> None:
        """
        asssign item to a room
        """
        self.item = item

    def get_character(self) -> object:
        """
        return character in the room
        """
        return self.character

    def get_item(self) -> object:
        """
        return an item in the room
        """
        return self.item

    def move(self, command: str) -> None:
        """
        move to another room
        """
        for direction, room in (self.dct).items():
            if command == direction:
                return room


class Enemy:
    """class for enemy"""
    wins = 0
    def __init__(self, name: str, description: str) -> None:
        """
        stores variables:
        name of the enemy
        desciption of the enemy
        """
        self.name = name
        self.description = description
        self.conversation = None
        self.weaknees = None


    def set_conversation(self, conversation: str) -> None:
        """
        set conversation between player and enemy
        """
        self.conversation = conversation

    def set_weakness(self, weakness: str) -> None:
        """
        set weakness for the enemy
        """
        self.weaknees = weakness

    def describe(self) -> str:
        """
        return info about an Enemy
        """
        print(f"{self.name} is here!")
        print(self.description)

    def fight(self, wearpon: str) -> bool:
        """
        return if wearpon is accepted by weaknesses of an enemy
        """
        if wearpon == self.weaknees:
            self.wins += 1
            return True
        return False

    def get_defeated(self) -> int:
        """
        return number of times player defeated enemy
        """
        Enemy.wins += 1
        return Enemy.wins


class Item:
    """class for item"""
    def __init__(self, name: str) -> None:
        """
        stores variables:
        name of the item
        """
        self.name = name
        self.description = None

    def get_name(self) -> str:
        """
        return name of an Item
        """
        return self.name

    def set_description(self, description: str) -> None:
        """
        set description of an item
        """
        self.description = description

    def describe(self) -> str:
        """
        return info about an Enemy
        """
        print(f"The [{self.name}] is here! - {self.description}")
