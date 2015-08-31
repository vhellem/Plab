__author__ = 'Vegard'

import matplotlib.pyplot as plt
import numpy

class Action:
    action = ""

    def __init__(self, action):
        self.action = action

    def __eq__(self, other):
        if self.action == other.action:
            return True
        return False

    def win(self, other):
        if (self.action == "rock"):
            if (other.action == "paper"):
                return False
            else:
                return True
        elif self.action == "paper":
            if other.action == "scissor":
                return False
            else:
                return True
        else:
            if other.action == "rock":
                return False
            return True

    def getAction(self):
        return self.action


class Player:
    won = 0
    name = ""
    act = Action("rock")
    moves = ["rock", "paper", "scissor"]
    beats = {"rock": "paper", "paper": "scissor", "scissor": "rock"}

    def __init__(self, name):
        self.name = name
        self.points = 0

    def pick_action(self, action):
        None

    def getAction(self):
        return self.act

    def get_result(self):
        None

    def getName(self):
        return name

    def point(self):
        self.points += 1

    def getPoints(self):
        return str(self.points)


class Tilfeldig(Player):
    import random

    def pick_action(self):
        self.act = Action(self.moves[random.randint(0, 2)])


class Sekvensiell(Player):
    def __init__(self, name):
        self.counter = 0
        super().__init__(name)

    def pick_action(self):
        self.act = Action(self.moves[self.counter])
        self.counter += 1
        if (counter == 3):
            counter = 0


class MestVanlig(Player):
    import random

    def pick_action(self, history):
        if (len(history) == 0):
            self.act = Action(self.moves[self.random.randint(0, 2)])
            return self.act
        else:

            hist = {"rock": 0, "paper": 0, "scissor": 0}
            for element in history:
                hist[element] += 1
            max = -1
            willC = ""
            for key, number in hist.items():
                if (number > max):
                    max = number
                    willC = key
            self.act = Action(self.beats[willC])
            return self.act


class Historiker(Player):
    import random

    husk = 0

    def __init__(self, name, husk):
        self.husk = husk
        super().__init__(name)

    def pick_action(self, history):
        if len(history) <= self.husk:
            self.act = Action(self.moves[self.random.randint(0, 2)])
            return self.act

        else:
            temp = {"rock": 0, "paper": 0, "scissor": 0}
            seq = len(history) - self.husk
            seque = []
            for i in range(seq, len(history)):
                seque.append(history[i])

            for i in range(seq):
                found = True
                for index, item in enumerate(seque):
                    if (history[i + index] == item):
                        next
                    else:
                        found = False
                if found:
                    temp[history[i + self.husk]] += 1
            mest = -1
            print(temp)
            for key, value in temp.items():
                if value > mest:
                    mest = value
                    willChoose = key
            self.act = Action(self.beats[willChoose])
            return self.act


class ManyGames():
    def __init__(self, spiller1, spiller2, antall_spill):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.antall = antall_spill
        self.history1 = []
        self.history2 = []

    def oneGame(self):
        s1 = self.spiller1.pick_action(self.history2)
        s2 = self.spiller2.pick_action(self.history1)
        if (s1 == s2):
            print("Draw, both played " + s1.getAction())
        elif (s1.win(s2)):
            print("Player 1 wins, played" + s1.getAction() + " against " + s2.getAction())
            self.spiller1.point()
        else:
            self.spiller2.point()
            print("Player 2 wins, played" + s2.getAction() + " against " + s1.getAction())
        self.history1.append(s1.getAction())
        self.history2.append(s2.getAction())
        print(self.history2)

    def tournament(self):
        for i in range(self.antall):
            self.oneGame()
        print("Points player 1: " + self.spiller1.getPoints())
        print("Points player 2: " + self.spiller2.getPoints())

# Import statements
# Disse brukes for Ã¥ hente inn pakker til programmet vÃ¥rt.
# Beskrivelse pÃ¥ wiki om hvordan disse installeres pÃ¥ maskinen og gjÃ¸res tilgjengelig
from tkinter import Tk, BOTH, StringVar
from tkinter.ttk import Frame, Button, Label, Style
import pylab
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




# Kode for Ã¥ generere GUI'et

class GUITournament(Frame):
    # Klassen GUITournament definerer en turnering mellom menneske
    # og en Spiller
    spiller = None
    # Resultater holder resultatet av kampene - for plotting
    resultater = None
    # Denne labelen vil brukes for aa rapportere enkeltspill
    resultat_label = None
    history = []

    def __init__(self, parent, motspiller):
        Frame.__init__(self, parent)
        self.parent = parent
        # Huske hvem vi spiller mot
        self.spiller = motspiller
        # Initiere listen av resultater
        self.resultater = []
        # Foreloepig ikke noe aa rapportere
        self.resultat_label = StringVar()
        self.resultat_label.set("Beskrivelse av siste spill kommer her")
        self.style = Style()
        self.fig = None
        self.history = []


    def arranger_enkeltspill(self, a):
        s1 = self.spiller.pick_action(self.history)
        if (s1 == a):
            lab = ("Draw, both played " + s1.getAction())
            self.resultater.append(0.5)
        elif (s1.win(a)):
            lab = ("Computer wins, played " + s1.getAction() + " against " + a.getAction())
            self.resultater.append(0)

        else:

            lab = ("Player wins, played " + a.getAction() + " against " + s1.getAction())
            self.resultater.append(1)
        self.history.append(a.getAction())
        lab += "\nScore against is " + str(sum(self.resultater)/len(self.resultater)*100) + "%"

        self.resultat_label.set(lab)


        plt.figure(self.fig.figure.number)  # Handle til figuren
        plt.ion()
        plt.plot(range(1, len(self.resultater) + 1),
                 100 * numpy.cumsum(self.resultater) /
                 range(1, len(self.resultater) + 1), 'b-', lw=4)
        plt.ylim([0, 100])
        plt.xlim([1, max(1.1, len(self.resultater))])
        plt.plot(plt.xlim(), [50, 50], 'k--', lw=2)
        plt.grid(b=True, which='both', color='0.65', linestyle='-')
        self.fig.show()

    def setup_gui(self):
        self.parent.title("Stein - Saks - Papir")
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        # Label for rapportering
        label = Label(self.parent, textvariable=self.resultat_label)
        label.place(x=800, y=50)
        # Buttons
        # Disse fyrer av metoden self.arranger_enkeltspill som er
        # definert i klassen. Denne metoden tar aksjonen til mennesket
        # som startup, og gjennomfoerer spillet
        # Samme type oppfoersel for de tre aksjons-knappene
        rock_button = Button(self, text="Stein",
                             command=lambda: self.arranger_enkeltspill(Action("rock")))
        rock_button.place(x=800, y=400)
        scissors_button = Button(self, text="Saks",
                                 command=lambda: self.arranger_enkeltspill(Action("scissor")))
        scissors_button.place(x=900, y=400)
        paper_button = Button(self, text="Papir",
                              command=lambda: self.arranger_enkeltspill(Action("paper")))
        paper_button.place(x=1000, y=400)
        # quit_button avslutter GUI'et naar den trykkes
        quit_button = Button(self, text="Quit", command=self.quit)
        quit_button.place(x=1000, y=450)
        # Embedde en graf i vinduet for aa rapportere fortloepende score
        self.fig = FigureCanvasTkAgg(pylab.figure(), master=self)
        self.fig.get_tk_widget().grid(column=0, row=0)
        self.fig.show()





root = Tk()

root.geometry("1100x500+300+300")


game = GUITournament(root, Historiker("Historiekr", 2))
game.setup_gui()

root.mainloop()

# game = ManyGames(Historiker("Historiker", 2), MestVanlig("Mest Vanlig"), 100)
# game.tournament()
