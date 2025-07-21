def getName(a='fml'):
    return a + "1"


print(getName(str(111)))

y = [1, 2, 5, 6] * 10
print(y)
# x = np.array(y)
# N = len(x)
# fft_x = list()
# for __ in range(N):
#     fft_x.append(abs((x * np.exp(-2j * np.pi * __ * (1 / N) * np.arange(N))).sum()))
# print(fft_x)