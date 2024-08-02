import time as tm
import keyboard

def play(title, limit, time):
    print(f"Чтобы остановить воспроизведение <{title}>, нажмите esc")
    while time < limit:
        if keyboard.is_pressed('esc'):
            print("Воспроизведение остановлено")
            break
        else:
            print(time)
            tm.sleep(1)
            time += 1
    if time == limit:
        print ("Конец видео")
        time = 0
    return (time)

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f"Ник {self.nickname}, хэш-пароль {self.password}, возраст {self.age}"

class Video:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False

    def ask_permission(self):
        self.adult_mode = True

    def __len__(self):
        return self.duration


class UrTube:

    def __init__(self, users, videos):
        self.users = users
        self.videos = videos
        self.current_user = None

    def user_list(self):
        return (list(user.nickname for user in self.users))

    def video_list(self):
        return (list(video.title for video in self.videos))


    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                return(f"Пользователь {nickname} авторизован. Добро пожаловать!")
        return ('Логин или пароль введен неверно, вход не выполнен')

    def register(self, nickname, password, age):
        for n in self.user_list():
             if nickname == n:
                 print(f"Пользователь {nickname} уже существует")
                 break
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print(f"Пользователь {nickname} зарегистрирован. Добро пожаловать!")
        self.current_user = new_user

    def log_out(self):
        if self.current_user != None:
            print(f"Пользователь {self.current_user.nickname} выходит...")
        self.current_user = None

    def add(self, array):
        for v in array:
            if not isinstance(v, Video):
                print('Несоответствие типа данных')
                break
            self.videos.append(v)

    def get_videos(self, request):
        result = []
        for v in self.video_list():
            if request in v:
                result.append(v)
        return (f"Видео по запросу <{request}>: {result}")

    def watch_video(self, request):
        if self.current_user == None:
            return ("Войдите в аккаунт, чтобы смотреть видео")
        for video in self.videos:
            if request == video.title:
                if video.adult_mode == True:
                    print (f"Видео по запросу <{request}> содержит контент для взрослых")
                    if self.current_user.age < 18:
                        return ("Вам нет 18 лет, пожалуйста покиньте страницу")
                video.time_now = play(video.title, video.duration, video.time_now)
                return ("")
        return (f"Видео по запросу <{request}> не найдено")

ajumo = User("ajumo", hash("qwerty"), 41)
baburo = User("baburo", hash("йцукен"), 28)
lesson1 = Video("Python Lesson 1", 300)
lesson2 = Video("Python Lesson 2", 250)
lesson3 = Video("Python Lesson 3", 350)
cute_cats = Video("Милые котики", 25)
cringe_case = Video('Кринжовый случай с программистом', 180)
cringe_case.ask_permission()
array = [cringe_case]
old_UrTube = UrTube([ajumo], [lesson1, lesson2, lesson3, cute_cats])
print(old_UrTube.log_in("ajumo", hash("qwerty")))
print(old_UrTube.get_videos("Python"))
print(old_UrTube.watch_video("Python guru"))
print(old_UrTube.log_out())
print(old_UrTube.log_in("petrushka", hash("12345")))
new_UrTube = UrTube(old_UrTube.users, old_UrTube.videos)
new_UrTube.add([cringe_case])
new_UrTube.register("petrushka", hash("12345"), 17)
print(new_UrTube.watch_video("Милые котики"))
print(new_UrTube.watch_video("Кринжовый случай с программистом"))