'''Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.

wins get 3 points
draws get 1 point
losses get 0 points

'''


def football(wins, draws, losses):
    """
    :param wins:
    :param draws:
    :param losses:
    :return:
    """
    if wins and draws and losses >= 0:
        result = wins * 3 + draws
        return result


print(football(3, 4, 2))


# other version

def football_points(wins, draws, losses):
    return wins * 3 + draws * 1 + losses * 0
