class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}"

class Team:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        print(f"Игрок {player.name} добавлен в команду {self.team_name}")

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            print(f"Игрок {player.name} удален из команды {self.team_name}")
        else:
            print(f"Игрок {player.name} не найден в команде {self.team_name}")

    def list_players(self):
        print(f"\nКоманда: {self.team_name}")
        print(f"Главный тренер: {self.coach}")
        print("Состав команды:")
        for player in self.players:
            print(player)
            print("-" * 20)

# Пример использования
if __name__ == "__main__":
    # Создаем игроков
    player1 = Player("Иванов", 25, "Нападающий")
    player2 = Player("Петров", 30, "Полузащитник")
    player3 = Player("Сидоров", 28, "Защитник")

    # Создаем команды
    team1 = Team("Красные", "Краснов")
    team2 = Team("Синие", "Синёв")

    # Добавляем игроков в команды
    team1.add_player(player1)
    team1.add_player(player2)
    team2.add_player(player3)

    # Выводим список игроков в командах
    team1.list_players()
    team2.list_players()

    # Удаляем игрока из команды
    team1.remove_player(player2)

    # Выводим обновленный список игроков
    team1.list_players()