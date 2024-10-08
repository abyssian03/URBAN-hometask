import time
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print (f"Завершилась запись в файл {file_name}")

start_functs_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_functs_time = time.time()

print("Время выполнения: ", round(end_functs_time - start_functs_time, 3))

start_threds_time = time.time()
thr_first = Thread(target=write_words, args=[10, 'example5.txt'])
thr_second = Thread(target=write_words, args=[30, 'example6.txt'])
thr_third = Thread(target=write_words, args=[200, 'example7.txt'])
thr_forth = Thread(target=write_words, args=[100, 'example8.txt'])

thr_first.start()
thr_second.start()
thr_third.start()
thr_forth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_forth.join()

end_threds_time = time.time()
print("Время выполнения: ", round(end_threds_time - start_threds_time, 3))