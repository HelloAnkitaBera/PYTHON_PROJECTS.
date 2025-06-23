import tkinter as tk
from tkinter import ttk, messagebox


questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Paris", "C. Madrid", "D. Rome"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {    "question": "What is the capital of Japan?",
        "options": ["A.Tokyo ", "B. Kyoto", "C. Osaka", "D. Yokohama"],
        "answer": "A"
        
    }
]


class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Page Quiz")
        self.geometry("500x300")
        self.resizable(False, False)
        self.answers = {}  
        self.frames = {}
        self.current_index = 0
        self.show_question_frame(0)

        

    def show_question_frame(self, index):
        if index < len(questions):
            frame = QuestionFrame(self, index)
            self._switch_frame(frame)
        else:
            self._switch_frame(SummaryFrame(self))

    def _switch_frame(self, new_frame):
        if hasattr(self, 'current_frame') and self.current_frame:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)


class QuestionFrame(tk.Frame):
    def __init__(self, app, q_index):
        super().__init__(app)
        self.app = app  # app is the QuizApp instance
        self.q_index = q_index
        self.selected = tk.StringVar()

        question_data = questions[q_index]
        tk.Label(self, text=f"Question {q_index + 1} of {len(questions)}",
                 font=("Arial", 12)).pack(pady=(10, 5))

        tk.Label(self, text=question_data["question"],
                 font=("Arial", 14)).pack(pady=(5, 15))

     
        for opt in question_data["options"]:
            ttk.Radiobutton(self, text=opt, variable=self.selected,
                            value=opt[0]).pack(anchor="w", padx=20)

       
        tk.Button(self, text="Next", command=self.next_question, background="green").pack(pady=20)

    def next_question(self):
        choice = self.selected.get()
        if not choice:
            messagebox.showwarning("Selection Required", "Please select an answer before continuing.")
            return
        self.app.answers[self.q_index] = choice
        self.app.show_question_frame(self.q_index + 1)


class SummaryFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        score = 0

        tk.Label(self, text="Quiz Summary", font=("Arial", 16, "bold")).pack(pady=10)

        summary_frame = tk.Frame(self)
        summary_frame.pack(pady=5, padx=10, fill="both", expand=True)

        for i, q in enumerate(questions):
            correct = q["answer"]
            user = master.answers.get(i, "No Answer")
            is_correct = user == correct
            color = "green" if is_correct else "red"
            if is_correct:
                score += 1

            result = f"Q{i+1}: {q['question']}\n  Your Answer: {user}   |   Correct Answer: {correct}"
            tk.Label(summary_frame, text=result, justify="left", fg=color).pack(anchor="w", pady=4)

        tk.Label(self, text=f"Your Score: {score} / {len(questions)}", font=("Arial", 14)).pack(pady=15)

        tk.Button(self, text="Exit", command=self.master.destroy).pack()


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
