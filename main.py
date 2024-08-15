from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class ToDoApp(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self, orientation='vertical')

        # Initialize widgets
        self.text_input = TextInput(hint_text='Enter new task') #does kv file connect?
        self.add_widget(self.text_input)

        self.add_button = Button(text='Add Task')
        self.add_button.bind(on_press=self.add_task)
        self.add_widget(self.add_button)

        self.task_list = BoxLayout(orientation='vertical')
        self.add_widget(self.task_list)

    def add_task(self, instance):
        task_text = self.text_input.text
        if task_text:
            task_label = Label(text=task_text)
            self.task_list.add_widget(task_label)
            self.text_input.text = ''

class MyApp(App):
    def build(self):
        return ToDoApp()

if __name__ == "__main__":
    MyApp().run()