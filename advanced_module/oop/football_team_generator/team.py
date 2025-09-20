from advanced_module.oop.football_team_generator.player import Player


class Team:
    def __init__(self, name:str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player.name in [p.name for p in self.__players]:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        player_to_remove = None

        for player in self.__players:
            if player.name == player_name:
                player_to_remove = player
                break

        if player_to_remove:
            self.__players.remove(player_to_remove)
            return str(player_to_remove)
        else:
            return f"Player {player_name} not found"


p = Player("Pall", 1, 3, 5, 7)

print("Player name:", p.name)
print("Points sprint:", p._Player__sprint)
print("Points dribble:", p._Player__dribble)
print("Points passing:", p._Player__passing)
print("Points shooting:", p._Player__shooting)

print("\ncalling the __str__ method")
print(p)

print('\nAbout the team')
t = Team("Best", 10)

print("\nTeam name:", t._Team__name)
print("Team points:", t._Team__rating)
print("Team players count:", len(t._Team__players))

print(t.add_player(p))
print(t.add_player(p))  # Attempt to add the same player again

print("Team players:", len(t._Team__players))


print(t.remove_player("Pall"))
print(t.remove_player("Pall"))  # Attempt to remove the same player again
