import mlbgame

def main():
    game = mlbgame.day(2020, 8, 27, home='Padres')[0]
    score = mlbgame.box_score(game.game_id)
    print(score.print_scoreboard())

if __name__ == '__main__':
    main()