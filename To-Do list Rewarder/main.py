from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from todo import TodoList
from rewards import RewardSystem

class ToDoApp(App):
    task_input = ObjectProperty(None)
    task_list = ObjectProperty(None)
    reward_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.todo_list = TodoList()
        self.rewards = RewardSystem(self.todo_list)

    def build(self):
        return self.root

    def add_task(self):
        task = self.task_input.text
        if task:
            self.todo_list.add_task(task)
            self.task_input.text = ''
            self.update_task_list()

    def complete_task(self):
        task_buttons = self.task_list.children
        for button in task_buttons:
            if button.state == 'down':
                task = button.text
                if self.todo_list.complete_task(task):
                    self.rewards.add_reward()
                    self.update_task_list()
                    self.update_rewards()
                    break

    def update_task_list(self):
        self.task_list.clear_widgets()
        for task in self.todo_list.list_tasks():
            button = Button(text=task, size_hint_y=None, height=40)
            self.task_list.add_widget(button)

    def update_rewards(self):
        self.reward_label.text = str(self.rewards.get_rewards())

    def redeem_rewards(self):
        amount = 1  # Set this as needed or prompt the user
        if self.rewards.redeem_rewards(amount):
            self.update_rewards()

if __name__ == '__main__':
    ToDoApp().run()
