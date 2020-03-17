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
Config.set("graphics", "height", 700)


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

        self.count_label = Label(text=f'[color=8999A3]X: {self.count[0]}   |   O: {self.count[1]}[/color]', size_hint = [1,.2], markup = True, font_size = 40)
        self.small_label = Label(size_hint = [1,.1], font_size = 20, markup = True)
        restart_btn = Button(text="Next round", on_press=self.reset, size_hint = [1,.13], center_x=.25)
        
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

        main_layout = MainLayout()
        play_grid = GridLayout(cols=3, rows=3, spacing=5)
        empty_label = Label(size_hint = [1,.1])
        
        for i in self.cells:
            play_grid.add_widget(i)

        main_layout.add_widget(self.count_label)
        main_layout.add_widget(self.small_label)
        main_layout.add_widget(play_grid)
        main_layout.add_widget(empty_label)
        main_layout.add_widget(restart_btn)

        return main_layout

    def move_bind(self, button):
        if self.turn and button.side != 1 and button.side != -1 and button.side != 1000:
            button.text = "X"
            button.side = 1
            self.turn = False
        elif not self.turn and button.side != 1 and button.side != -1 and button.side != 1000:
            button.text = "O"
            button.side = -1
            self.turn = True
        else:
            return
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
        self.count_label.text = f'[color=8999A3]X: {self.count[0]}   |   O: {self.count[1]}[/color]'
        self.small_label.text = f'[color=7289DA]{self.winner}[/color]'
        for i in self.cells:
            if i.side == 0:
                i.side = 1000
                print(i.side)
                i.text = '-'

    def reset(self, *args):
        for i in self.cells:
            i.side = 0
            i.text = ""
MyApp().run()