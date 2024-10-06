import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name) as f:
        while f.readline() != '':
            all_data.append(f.readline())
    print(name, 'прочитан')

if __name__ == "__main__":

    file_names = ["file 1.txt", "file 2.txt", "file 3.txt", "file 4.txt"]

    time_0 = time.time()
    for f in file_names:
        read_info(f)
    time_1 = time.time()
    print(time_1 - time_0)

    time_0 = time.time()
    with multiprocessing.Pool(processes=2) as p:
        p.map(read_info, file_names)
    time_1 = time.time()
    print(time_1 - time_0)
