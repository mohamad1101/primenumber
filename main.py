from math import sqrt
import time
import matplotlib.pyplot as plt


def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step


def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))


start_num = 1000000000
end_num =   2000000000
data_ = []
start_time = time.time()
for i in range(start_num, end_num):
    if is_prime(i):
        data_.append(i)
        # print(data_)

end_time = time.time()
print(f"execution time:{end_time - start_time}")

plt.hist(data_, bins=40, color='gold')
plt.grid(True)
plt.xlabel('points')
plt.title("Histogram")
plt.show()
