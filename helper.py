word_list = []

file = open("words.txt", "r")

for line in file:
    word_list.extend(line.split())

file.close()

exit = False
letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
               'O','P','Q','R','S','T','U','V','W','X','Y','Z']
COMMON_LETTER_LIST = ['U', 'N', 'T', 'L', 'I', 'R', 'O', 'A', 'S', 'E']
ctn_list = [0] * 26
ctn_elim_list = []
for x in range(0,26):
    ctn_elim_list.append([False, False, False, False, False])

sure_list = ['0'] * 5
copy_word_list = word_list[:]

def update_list_sure():
    for x in range(0, 5):
        if sure_list[x] != '0':
            letter = sure_list[x]
            rmv_list = []
            for word in copy_word_list:
                if word[x] != letter:
                    rmv_list.append(word)

            for word in rmv_list:
                copy_word_list.remove(word)


def update_list_ctn():
    for x in range(0, 26):
        if ctn_list[x] != 0:
            letter = chr(65+x)
            min_num = ctn_list[x]
            rmv_list = []
            for word in copy_word_list:
                if word.count(letter) < min_num or ctn_elim_list[x][word.find(letter)] == True:
                    rmv_list.append(word)

            for word in rmv_list:
                copy_word_list.remove(word)


def update_list_elim():
    for x in range(0, 26):
        if letter_list[x] == '0':
            letter = chr(65+x)
            rmv_list = []
            for word in copy_word_list:
                if word.count(letter) > 0:
                    rmv_list.append(word)

            for word in rmv_list:
                copy_word_list.remove(word)


while exit == False:
    user_in = input("Enter command: sure c i, ctn c i j, elim [c], search all / s, search unique / su, search adv / sa, reset, exit\n")

    if user_in == "exit":
        exit = True

    elif user_in == "reset":
        letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                       'O','P','Q','R','S','T','U','V','W','X','Y','Z']
        sure_list = ['0','0','0','0','0']
        ctn_list = [0] * 26
        ctn_elim_list = []
        for x in range(0,26):
            ctn_elim_list.append([False, False, False, False, False])

        copy_word_list = word_list[:]

    elif user_in == "search all" or user_in == "s":
        print("Found ", len(copy_word_list), " matches")
        print(copy_word_list)

    elif user_in == "search unique" or user_in == "su":
        result_list = []
        for word in copy_word_list:
            keep = True
            for x in range(1, 5):
                if word[x:].find(word[x-1]) != -1:
                    keep = False
                    break

            if keep == True:
                result_list.append(word)


        print("Found ", len(result_list), " matches")
        print(result_list)

    elif user_in == "search adv" or user_in == "sa":
        result_list = []
        for word in copy_word_list:
            keep = True
            for x in range(1, 5):
                if word[x:].find(word[x-1]) != -1:
                    keep = False
                    break

            if keep == True:
                result_list.append(word)

        score = [0] * len(result_list)
        for x in range(0, len(result_list)):
            for y in range(0, len(COMMON_LETTER_LIST)):
                if result_list[x].find(COMMON_LETTER_LIST[y]) != -1:
                    score[x] += y

        max_ind = 0
        max_score = 0
        for x in range(0, len(score)):
            if score[x] > max_score:
                max_score = score[x]
                max_ind = x

        if len(result_list) > 0:
            print(result_list[max_ind])
        else:
            print("No result. Use search all.")

    elif user_in[0:4] == "sure":
        letter = user_in[5]
        ind = int(user_in[7]) - 1
        sure_list[ind] = letter
        ind = ord(letter)-ord('A')

        print("Current Sure List: ", sure_list)
        update_list_sure()

    elif user_in[0:4] == "elim":
        temp_elim_list = user_in[5:].split()
        for letter in temp_elim_list:
            ind = ord(letter) - ord('A')
            letter_list[ind] = '0'

        print("Current Letter List: ", letter_list)
        update_list_elim()

    elif user_in[0:3] == "ctn":
        letter = user_in[4]
        ind = ord(letter) - ord('A')
        num = int(user_in[6])
        elim_pos = int(user_in[8])-1
        ctn_list[ind] = num
        ctn_elim_list[ind][elim_pos] = True

        update_list_ctn()

    else:
        print("Invalid command.")
