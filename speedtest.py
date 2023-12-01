import random
import time
import tkinter as tk
from tkinter import messagebox

class TypingTestGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Test")
        self.master.geometry("400x300")

        self.user_name = tk.StringVar()
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("medium")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Welcome to the Speed Typing Test!").pack(pady=10)

        tk.Label(self.master, text="Enter your name:").pack()
        tk.Entry(self.master, textvariable=self.user_name).pack(pady=5)

        tk.Label(self.master, text="Select difficulty:").pack()
        tk.OptionMenu(self.master, self.difficulty_var, "easy", "medium", "hard").pack(pady=5)

        tk.Button(self.master, text="Start Test", command=self.start_typing_test).pack(pady=10)

    def start_typing_test(self):
        user_name = self.user_name.get()
        difficulty_level = self.difficulty_var.get()

        if not user_name:
            messagebox.showinfo("Error", "Please enter your name.")
            return

        self.master.destroy()  # Close the GUI window

        typing_test(user_name, difficulty_level)

def load_words_from_file(filename):
    with open(filename, 'r') as file:
        words = [line.strip() for line in file]
    return words

def typing_test(user_name, difficulty='medium'):
    word_list = load_words_from_file("word_list.txt")

    # Customize test duration and number of words based on difficulty
    difficulty_levels = {'easy': (30, 3), 'medium': (60, 5), 'hard': (90, 7)}
    test_duration, num_words = difficulty_levels.get(difficulty, (60, 5))

    print(f"\nWelcome, {user_name}! Type the following {num_words} words as fast as you can:")

    random.shuffle(word_list)
    word_list = word_list[:num_words]

    start_time = time.time()

    correct_words = 0
    total_words = len(word_list)

    for word in word_list:
        user_input = input(f"{word}: ")
        if user_input == word:
            correct_words += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    wpm = (correct_words / elapsed_time) * 60
    accuracy = (correct_words / total_words) * 100
    score = int(wpm * accuracy / 100)

    print(f"\nTest completed in {elapsed_time:.2f} seconds.")
    print(f"You typed {correct_words}/{total_words} words correctly.")
    print(f"Your typing speed is {wpm:.2f} WPM.")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Score: {score}")

    update_score(user_name, score)

def update_score(user_name, score):
    # You can implement a score tracking system here (e.g., store scores in a file or database).
    print(f"\n{user_name}'s Score: {score}")

if __name__ == '__main__':
    root = tk.Tk()
    typing_test_gui = TypingTestGUI(root)
    root.mainloop()
