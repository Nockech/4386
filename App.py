from kivy.app import App
from kivy.config import Config
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
#from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView

Builder.load_file('my.kv')
#Config.set("graphics", "resizable",0)
Config.set("graphics", "width", 500)
Config.set("graphics", "height", 500)


class GButton(Button):
    def __init__(self, *args, **kwargs):
        super(GButton, self).__init__(*args, **kwargs)
        self.background_color = [0.44, 0.47, 0.51, 1]
        self.background_color_down = [1, 0, 0, 1]
        self.font_size = 40
        self.side = 0

class MainLayout(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(MainLayout, self).__init__(*args, **kwargs)

class MyApp(App):
    def build(self):
        self.title = 'Tic tac toe(Hleb edition)'
        self.winner = None
        self.turn = True
        self.count = [0,0]

        self.btn1 = GButton(on_release=self.move_bind)
        self.btn2 = GButton(on_release=self.move_bind)
        self.btn3 = GButton(on_release=self.move_bind)
        self.btn4 = GButton(on_release=self.move_bind)
        self.btn5 = GButton(on_release=self.move_bind)
        self.btn6 = GButton(on_release=self.move_bind)
        self.btn7 = GButton(on_release=self.move_bind)
        self.btn8 = GButton(on_release=self.move_bind)
        self.btn9 = GButton(on_release=self.move_bind)

        self.count_label = Label(text=f'X: {self.count[0]}   |   O: {self.count[1]}', size_hint = [1,.3], font_size = 40)
        self.restart_btn = Button(text="Next round", on_press=self.reset, size_hint = [1,.1])

        self.cells = [
            self.btn1,
            self.btn2, 
            self.btn3, 
            self.btn4,
            self.btn5, 
            self.btn6, 
            self.btn7, 
            self.btn8, 
            self.btn9,
            ]

        play_grid = GridLayout(cols=3, rows=3, spacing=5)
        main_layout = MainLayout()
        
        for i in self.cells:
            play_grid.add_widget(i)

        main_layout.add_widget(self.count_label)
        main_layout.add_widget(play_grid)
        main_layout.add_widget(self.restart_btn)

        return main_layout

    def move_bind(self, button):
        #button.font_size = 40
        if self.turn and int(button.side) != 1 and int(button.side) != -1:
            button.text = "X"
            button.side = 1
            self.turn = False
        elif not self.turn and int(button.side) != 1 and int(button.side) != -1:
            button.text = "O"
            button.side = -1
            self.turn = True
        self.check_game()

    def check_game(self):
        sums = [
            sum([self.btn1.side, self.btn2.side, self.btn3.side]),
            sum([self.btn4.side, self.btn5.side, self.btn6.side]),
            sum([self.btn7.side, self.btn8.side, self.btn9.side]),

            sum([self.btn1.side, self.btn4.side, self.btn7.side]),
            sum([self.btn2.side, self.btn5.side, self.btn8.side]),
            sum([self.btn3.side, self.btn6.side, self.btn9.side]),

            sum([self.btn1.side, self.btn5.side, self.btn9.side]),
            sum([self.btn7.side, self.btn5.side, self.btn3.side]),
            ]
        if 3 in sums:
            self.count[0] += 1
            self.winner = "X win"
        elif -3 in sums:
            self.count[1] += 1
            self.winner = "O win"
        elif 0 not in [i.side for i in self.cells]:
            self.winner = "Draw"
        else:
            return
        self.win()
    
    def win(self):
        self.count_label.text=f'X:{self.count[0]} O:{self.count[1]}'
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
            i.text = ""
MyApp().run()