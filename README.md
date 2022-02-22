#Wordle Helper Project

##Commands:
- **sure C i**: when you know a letter's position for sure, enter "sure" followed by the letter C in capital case followed by i from 1 to 5 indicating its position. (correspond to GREEN in wordle)
- **ctn C i j**: when you know a letter is contained, enter "ctn" followed by the letter in capital case C, the minimum number of occurance of this letter denoted by i (typically 1), and the position to be eliminated j. (correspond to YELLOW in wordle)
- **elim [C]**: when you know a letter is not contained, enter "elim" followed by a list of letters in capital cases C. (correspond to GREY in wordle)
- **reset**: reset the program for a new game
- **exit**: exit the program
- **search all**: look up all the words based on the current limitations set
- **search unique**: look up all the words based on the current limitations set, and all words have unique or non-repeating letters
- **search adv**: look up all the words based on the current limitations set, and all words have unique or non-repeating letters, and these words are scored based on how often the letter appears based on the histogram, and the highest scored word is returned.

##Procedure:
- Start the game with any word
- Look at the result.
  - For all green letters: use sure command, only need to use it once for each letter in each game
  - For all yellow letters: use ctn command, think about if the minimum number of occurrence of letter is 1 or more, and enter its position so that the position is eliminated (yellow stands for contained by incorrect position)
  - For all grey letters: use elim command, only need to use it once for each letter in each game
- To obtain the optimal next word to guess,
  - use search adv or sa first
  - if result from sa is none or invalid, use search unique or su
  - depending on the situation, can use search all or s

After more testing, my program certainly helps me a lot in beating this game. However, it also allows me to see some issues with the program and also better understand the game.
- For the game, I'm still figuring in out if in certain situation the game is unwinnable through pure logic and all comes down to luck. For instance, there are about 10 words that end with "ight" like fight, might, sight, tight, dight, etc. A potential improvement to the program can be to incorporate a search method that look up words to quickly eliminate all the initial letters because there's not enough attempts to guess through all of them and it would come down to luck. Yet of course, if there's no such word, then in combination with a unlucky first word seems to make it impossible to guarantee a win in some situations.
- Some potential improvements with my program:
  - biggest problem/limitation: multiple of the same letters. I've been ignoring this in the development of the program because initially in every game, guessing words with duplicate letters does not seem efficient to eliminate more letters. When it comes down to the remaining words, however, duplicate letters play a greater part. My eliminate and contain operations may have issues with duplicate letters, and my search adv operation is based solely on words with non-repetitive letters.
  - Can improve user input detection, which is highly unstable right now since this is just a quick program.
