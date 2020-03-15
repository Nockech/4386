from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView

#Config.set("graphics", "resizable",0)
Config.set("graphics", "width", 500)
Config.set("graphics", "height", 500)

class GButton(Button):
    def __init__(self, *args, **kwargs):
        super(GButton, self).__init__(*args, **kwargs)
        self.side = 0

class MainApp(App):
    def build(self):
        self.title = 'Tic tac toe(Hleb edition)'
        self.winner = None
        self.turn = True

        main_layout = BoxLayout(orientation='vertical')
        play_grid = GridLayout(cols=3, rows=3, spacing=5)

        self.btn1 = GButton(on_release=self.move_bind, text="1")
        self.btn2 = GButton(on_release=self.move_bind, text="2")
        self.btn3 = GButton(on_release=self.move_bind, text="3")
        self.btn4 = GButton(on_release=self.move_bind, text="4")
        self.btn5 = GButton(on_release=self.move_bind, text="5")
        self.btn6 = GButton(on_release=self.move_bind, text="6")
        self.btn7 = GButton(on_release=self.move_bind, text="7")
        self.btn8 = GButton(on_release=self.move_bind, text="8")
        self.btn9 = GButton(on_release=self.move_bind, text="9")

        play_grid.add_widget(self.btn1)
        play_grid.add_widget(self.btn2)
        play_grid.add_widget(self.btn3)
        play_grid.add_widget(self.btn4)
        play_grid.add_widget(self.btn5)
        play_grid.add_widget(self.btn6)
        play_grid.add_widget(self.btn7)
        play_grid.add_widget(self.btn8)
        play_grid.add_widget(self.btn9)

        self.cells = [self.btn1, self.btn2, self.btn3, self.btn4,self.btn5, self.btn6, self.btn7, self.btn8, self.btn9,]

        main_layout.add_widget(Button())
        main_layout.add_widget(play_grid)
        main_layout.add_widget(Button())

        return main_layout

    def move_bind(self, button):
        if self.turn and int(button.side) != (1 and -1):
            button.background_color = [1, 0, 0, 1]
            button.side = 1
            self.turn = False
            self.check_game()
        elif not self.turn and int(button.side) != (1 and -1):
            button.background_color = [0, 1, 0, 1]
            button.side = -1
            self.turn = True
            self.check_game()

    def check_game(self):
        sums = [
            sum([self.btn1.side, self.btn2.side], self.btn3.side),
            sum([self.btn4.side, self.btn5.side], self.btn6.side),
            sum([self.btn7.side, self.btn8.side], self.btn9.side),

            sum([self.btn1.side, self.btn4.side], self.btn7.side),
            sum([self.btn2.side, self.btn5.side], self.btn8.side),
            sum([self.btn3.side, self.btn6.side], self.btn9.side),

            sum([self.btn1.side, self.btn5.side], self.btn9.side),
            sum([self.btn7.side, self.btn5.side], self.btn3.side),
            ]

        if 3 in sums:
            self.winner = "X win"
        elif -3 in sums:
            self.winner = "O win"
        elif 0 not in sums:
            self.winner = "Draw"
        else:
            return
        self.win()
    
    def win(self):
        popup = ModalView(size_hint=(0.75, 0.5))
        victory_label = Label(text=self.winner, font_size=50)
        popup.add_widget(victory_label)
        popup.bind(on_dismiss=self.reset)
        popup.open()
    
    def reset(self, *args):
        global winner
        winner = None
        for i in self.cells:
            i.side = 0
            i.background_color = [1, 1, 1, 1]

MainApp().run()