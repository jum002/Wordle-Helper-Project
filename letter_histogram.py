word_list = []

file = open("words.txt", "r")

for line in file:
    word_list.extend(line.split())

file.close()

histogram = [0] * 26

for word in word_list:
    for x in range(0, 5):
        ind = ord(word[x]) - ord('A')
        histogram[ind] += 1

for x in range(0, 26):
    print(chr(65+x), ": ", histogram[x])

"""
Result:
*A :  5738
B :  1547
C :  1947
D :  2364
*E :  6441
F :  1071
G :  1576
H :  1682
*I :  3595
J :  270
K :  1426
*L :  3269
M :  1908
*N :  2854
*O :  4248
P :  1945
Q :  104
*R :  4027
*S :  6427
*T :  3206
*U :  2399
V :  661
W :  1013
X :  268
Y :  1992
Z :  412

So most common occuring letters: A, E, I, L, N, O, R, S, T, U
In order from most to least:     E, S, A, O, R, I, L, T, N, U
In order from least to most:     U, N, T, L, I, R, O, A, S, E
"""
