def save_flashcards(flashcards, filename="flashcards.txt"):
	with open(filename, "w") as file:
		for question, answer in flashcards.items():
			file.write(f"{question} => {answer}\n")
	print(f"\nFlashcards saved to {filename}")
import random
from collections import deque
import os
from datetime import datetime






import random

flashcards = {
	"git": {
		"What does 'git status' do?": "Shows the state of working directory and staging area.",
		"What does 'git as .' do?": "Stages all changes in the current directory.",
		"What does 'git commit -m \"msg\"' do?": "Commits staged changes with a message.",
		"What does 'git push' do?": "Uploads local commits to the remote repository.",
		"What does 'git pull' do?": "Fetches and merges changes from the remote repo to local.",

	},
	"python": {
		"What does 'len()' do?": "Returns the number of items in an object.",
		"What is a list comprehension ?": "A compact way to create lists using a single line of code.",
		"What does 'def' do?": "Defines a new function.",
		"What is a directory?": "A collection of key-value pairs.",
		"What does 'if __name__ \"__main__\"' mean?": "Checks if the script is run directly.",
	},
	"terminal": {
		"What does 'ls' do?": "Lists files in the current directory.",
		"What does 'cd ..' do?": "Moves up one directory level.",
		"What does 'pwd' show you?": "Prints the current working directory.",
		"What does 'mkdir' do?": "Creates a new directory.",
		"What does 'rm filename' do?": "Deletes the file named 'filename'.",
		"What does 'touch file.py' do?": "Creates an empty file named file.py.",
		"What does 'clear' do ?": "Clears the terminal screen.",
		"What does 'man <command>' do?": "Shows the manual for a command.",

    },
    "abbreviations": {
        "What does SMB stand for?": "Server Message Block",
        "What does FTP stand for?": "File Transfer Protocol",
        "What does RDP stand for?": "Remote Desktop Protocol",
        "What does DNS stand for?": "Domain Name Server",
        "What does HTTP stand for?": "Hypertext Transfer Protocol",
        "What does HTTPS stand for?": "Hypertext Transfer Protocol Secure",
        "What does IP stand for?": "Internet Protocol",
        "what does VPN stand for?": "Virtual Private Network"
    }
}

def save_session(topic, score, total, accuracy, best_streak, path="session/log.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    write_headers = not os.path.exists(path)
    ts = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    with open(path, "a", encoding="utf-8") as f:
        if write_header:
            f.write("timestamp,topic,score,total,accuracy, longest_streak/n")
        f.write(f"{ts},{topic},{score},{total},{accuracy:.2f},{best_streak}\n")








def run_flashcards(topic, spaced_repetition=True):
    cards = flashcards.get(topic)
    if not cards:
        print("\nInvalid topic selection")
        return

    keys = list(cards.keys())
    random.shuffle(keys)
    queue = deque(keys)

    score = 0
    total = len(keys)
    streak = 0
    best_streak = 0

    print(f"\n=== {topic.upper()} flashcards ===")
    while queue:
        question = queue.popleft()
        user_answer = input(f"\n{question}\n> ").strip().lower()
        correct_answer = cards[question].strip().lower()

        if user_answer in {"quit", "exit"}:
            break

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
            streak += 1
            best_streak = max(best_streak, streak)
        else:
            print(f"Incorrect. The correct answer is: {cards[question]}")
            if spaced_repetition:
                queue.append(question)
            streak = 0

        answered = score = (total - len(queue) - (0 if spaced_repetition else 0))
        accuracy = (score / max(1, (score + (answered - score)))) * 100

        again = input("\nDo you want another flashcard? (y/n): ").strip().lower()
        if again != "y":
            break

    print(f"\nFinal score: {score}/{total}")
    final_accuracy = (score / total) * 100 if total else 0.0
    print(f"Final accuracy: {final_accuracy:.2f}%")
    print(f"Longest streak: {best_streak}")
    if score < total:
        print("Good session! Keep practicing.")

def main():
    print("Welcome to Terminal Flashcards!")
    print("Available topics: " + ", ".join(flashcards.keys()))

    topic = input("Choose a topic to study: ").strip().lower()
    if topic in flashcards:
        run_flashcards(topic)
    else:
        print("Invalid topic. Please choose from the list above.")

    save_flashcards(flashcards["git"])

if __name__ == "__main__":
    main()
