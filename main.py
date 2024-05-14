from tkinter import *
import random as rd

randomNumber = rd.randint(1, 101)
trueAns = int(randomNumber)

nowMin = 1
nowMax = 100

answerHistory = []

def checkAnswer():

  global trueAns, nowMin, nowMax

  try:
    userAnswer = int(gameAnswerInput.get())
  except ValueError:
    statusText.configure(text=f"Please enter a valid number between {nowMin} and {nowMax}.")
    return

  userAnswer = int(gameAnswerInput.get())

  if userAnswer < nowMin:
    statusText.configure(text=f"Please answer between {nowMin}-{nowMax}")
    return
  if userAnswer > nowMax:
    statusText.configure(text=f"Please answer between {nowMin}-{nowMax}")
    return

  if userAnswer > trueAns:
    statusText.configure(text="Your answer is more than true answer.")
    nowMax = userAnswer - 1
  elif userAnswer < trueAns:
    statusText.configure(text="Your answer is less than true answer.")
    nowMin = userAnswer + 1
  else:
    statusText.configure(text="Congratulation!, Your answer is correct!")
    StartNewGameButton.pack()
    
  if (int(nowMax) - int(nowMin) != 0):
    gameAnswerShow.configure(text=f"{nowMin}-{nowMax}")
  else:
    gameAnswerShow.configure(text=f"{trueAns}")
    gameAnswerInput.configure(state="disabled")
    statusText.configure(text="Game over! Please restart for start new game")
    StartNewGameButton.pack()

def startNewGame():

  global trueAns, nowMin, nowMax
  newRandomNumber = rd.randint(1, 101)
  trueAns = newRandomNumber
  nowMin = 1
  nowMax = 100
  gameAnswerInput.configure(state="normal")
  gameAnswerInput.delete(0, END)
  gameAnswerShow.configure(text=f"{nowMin}-{nowMax}")
  statusText.configure(text="Please select number between 1-100.")
  StartNewGameButton.forget()
  

root = Tk()
root.geometry('700x700')
root.resizable(False, False)
root.title("Number Guessing Game")
root.configure(background='lightgreen')

gameTitle = Label(root, text="Number Guessing Game", font=("Kozuka Mincho Pro R", 25))
gameTitle.pack(pady=25)

gameAnswerTitle = Label(root, text="Range is : ", font=("Kozuka Mincho Pro R", 15))
gameAnswerTitle.pack(pady=25)
gameAnswerShow = Label(root, text="1-100", font=("Kozuka Mincho Pro R", 25))
gameAnswerShow.pack(pady=25)

gameAnswerInput = Entry(root, width='30', font=("Kozuka Mincho Pro R", 18), state="normal")
gameAnswerInput.pack(pady=25)

gameAnswerSubmit = Button(root, text="Submit Answer", command=checkAnswer, width='30', height='3', font=("Kozuka Mincho Pro R", 12))
gameAnswerSubmit.pack(pady=10)

statusText = Label(root, text="Please select number between 1-100.", font=("Kozuka Mincho Pro R", 18))
statusText.pack(pady=50)

StartNewGameButton = Button(root, text="Restart", command=startNewGame, width='30', height='2', font=("Kozuka Mincho Pro R", 12))

root.mainloop()