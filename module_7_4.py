team1_num = 5
team2_num = 6
print("В команде Мастера кода %s участников" %team1_num)
print("В команде Волшебники данных %s участников" %team2_num)
print("Значит, количественный состав сегодняшней битвы: %s против %s" % (team1_num, team2_num))
score_1 = 40
team1_time = 16937
score_2 = 42
team2_time = 18015.2
print('Команда Мастера Кода решила {} задач за {} секунд'.format(score_1, team1_time))
print('Команда Волшебники данных решила {} задач за {} секунд'.format(score_2, team2_time))
print(f"Скорость решения задач по командам: {score_1 / team1_time} и {score_2 / team2_time} задач в секунду")
challenge_result = "Мастера кода"
print(f"Результат битвы: победа команды {challenge_result}!")
print(f"Сегодня было решено {score_1 + score_2} задач, в среднем по {(team1_time + team2_time) / (score_1 + score_2)} секунды на задачу")

