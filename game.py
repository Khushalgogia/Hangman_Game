import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.target_word = ""
        self.guesses_left = 6
        self.guessed_letters = set()
        self.word_in_progress = []
        self.guess_counter = 0
        self.same_length_list = []

    def choose_word(self):
        self.target_word = random.choice(self.word_list)
        self.word_in_progress = ["_"] * len(self.target_word)

    def display_word(self):
        return " ".join(self.word_in_progress)
    
    def guess_here(self):
        
        
        #Calculating Entrophy function
        
        
        def entrophy(letter, position, l1,all_letters):
    
            my_dic = {letter: {position: 0 for position in range(len(l1[0]))} for letter in all_letters}


            for j in all_letters:
                for i in l1:
                    for k in range(len(i)):
                        if j in i[k]:
                            my_dic[j][k] += 1
            probab = my_dic[letter][position]/len(l1)
            if probab == 0:
                return 0  # To avoid math domain error for log(0)
            entropy = -probab * math.log(probab, 2)
            return entropy

        def Predictor(l1):
            all_letters = list(set("".join(l1)))
            my = {letter: {position: 0 for position in range(0,len(l1[0]))} for letter in all_letters}
            for i in all_letters:
                for j in range(0,len(l1[0])):
                    my[i][j] = entrophy(i,j,l1,all_letters) 
            df = pd.DataFrame(list(my.values()))
            df['words'] = list(my)
            df = df.set_index('words')
            max_value = df.max().max()
            row,column = np.where(df.values == df.values.max())
            predicted_alphabets = df.index[row[0]]
            col_index = df.columns[column[0]]
            return predicted_alphabets, col_index

        #Predicting First Alphabet
        if self.guess_counter == 0:
            self.same_length_list = [word for word in self.word_list if len(word) == len(self.word_in_progress)]
            alphabet, col_index = Predictor(self.same_length_list)
            print(f"Target Word: {self.target_word}")
            return alphabet
        
        #Predicting Next Letters based on previous guess
        while len(self.same_length_list) > 1:
            
            alphabet, col_index = Predictor(self.same_length_list)
            # Calculating how many times that predicted alphabet comes in that word,(to eliminate other words for future)
            alphabet_indexes = [index for index, char in enumerate(self.word_in_progress) if char == alphabet]
            
            # If we guessed predcted alphabet right with right index
            if self.word_in_progress[col_index] == alphabet and len(alphabet_indexes) == 1:
                updated_list = [word for word in self.same_length_list if word[col_index] == alphabet]
                print(f"A - Number of words left: {len(self.same_length_list) - len(updated_list)}")
                self.same_length_list = updated_list
                alphabet, col_index = Predictor(self.same_length_list)
                # Once we get to last word
                if len(updated_list) == 1:
                    word = self.same_length_list[0]
                    my_final_guess = [i for i in word if i not in self.guessed_letters]
                    return my_final_guess[-1]
                return alphabet
                

                
            # If we guessed it right with right index but that predcted alphabet is coming twice in that word
            elif self.word_in_progress[col_index] == alphabet and len(alphabet_indexes) > 1:
                updated_list = [word for word in self.same_length_list if word[col_index] == alphabet
                                and all(word[i] == alphabet for i in alphabet_indexes)]
                print(f"B - Number of words left: {len(self.same_length_list) - len(updated_list)}")
                self.same_length_list = updated_list
                alphabet, col_index = Predictor(self.same_length_list)
                if len(updated_list) == 1:
                    word = self.same_length_list[0]
                    my_final_guess = [i for i in word if i not in self.guessed_letters]
                    return my_final_guess[-1]
                return alphabet
                

                
            # If we guessed the letter right but in wrong index
            elif alphabet in "".join(self.word_in_progress) and self.word_in_progress[col_index] != alphabet:
                no_of_char = len(alphabet_indexes)
                updated_list = [word for word in self.same_length_list if word.count(alphabet) == no_of_char
                                and all(word[i] == alphabet for i in alphabet_indexes)]
                print(f"C - Number of words left: {len(self.same_length_list) - len(updated_list)}")
                self.same_length_list = updated_list
                alphabet, col_index = Predictor(self.same_length_list)
                if len(updated_list) == 1:
                    word = self.same_length_list[0]
                    my_final_guess = [i for i in word if i not in self.guessed_letters]
                    return my_final_guess[-1]
                return alphabet
                

            # If predcted alphabet is not in the word
            elif alphabet not in "".join(self.word_in_progress):
                updated_list = [word for word in self.same_length_list if alphabet not in word]
                print(f"D - Number of words left: {len(self.same_length_list) - len(updated_list)}")
                self.same_length_list = updated_list
                alphabet, col_index = Predictor(self.same_length_list)
                if len(updated_list) == 1:
                    word = self.same_length_list[0]
                    my_final_guess = [i for i in word if i not in self.guessed_letters]
                    return my_final_guess[-1]
                return alphabet
                

        # Once we get to last word
            
        if len(self.same_length_list) == 1:
            word = self.same_length_list[0]
            my_final_guess = [i for i in word if i not in self.guessed_letters]
            return my_final_guess[-1]

        

        
        

    def make_guess(self, letter):
        self.guess_counter += 1
        if letter in self.guessed_letters:
            return "You already guessed that letter!"

        self.guessed_letters.add(letter)

        if letter in self.target_word:
            for i in range(len(self.target_word)):
                if self.target_word[i] == letter:
                    self.word_in_progress[i] = letter
            if "_" not in self.word_in_progress:
                
                return "Congratulations! You guessed the word: {}".format(self.target_word)
        else:
            self.guesses_left -= 1
            if self.guesses_left == 0:
                return "Sorry, you ran out of guesses. The word was: {}".format(self.target_word)

        return self.display_word() + f"\nLives left: {self.guesses_left}\nGuessed Word: {letter}\nTarget word: {self.target_word}"

word_list = my_list

total_games = 10  # Set the number of games you want to play
successful_games = 0

for _ in range(total_games):
    custom_hangman = HangmanGame(word_list)
    custom_hangman.choose_word()
    print("Welcome to Hangman!")
    Algorithm_start_time = datetime.now()
    print("Word to guess:", custom_hangman.display_word())

    col_index = 0  # Define col_index before the loop
    result = ""  # Initialize result variable
    while custom_hangman.guesses_left > 0 and "_" in custom_hangman.word_in_progress:
        guess = custom_hangman.guess_here()
        result = custom_hangman.make_guess(guess)
        #print(result)  # Display the result after each guess
        print("Word in progress:", custom_hangman.display_word())  # Display the word_in_progress

    Algorithm_completed_time = datetime.now()

    if "_" not in custom_hangman.word_in_progress:
        successful_games += 1
        print(result)  # Print the winning message here
        #print("Word in progress:", custom_hangman.display_word())  # Display the word_in_progress

    elapsed_time = Algorithm_completed_time - Algorithm_start_time
    minutes = int(elapsed_time.total_seconds() // 60)
    seconds = int(elapsed_time.total_seconds() % 60)
    print(f"Elapsed time: {minutes} minutes and {seconds} seconds")

success_rate = (successful_games / total_games) * 100
print(f"Success rate: {success_rate}%")