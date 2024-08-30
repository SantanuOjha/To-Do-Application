import json

class TodoList:
    def __init__(self, data_file='data.json'):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {"tasks": [], "completed": [], "rewards": 0}
            self.save_data()

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_task(self, task):
        self.data['tasks'].append(task)
        self.save_data()

    def remove_task(self, task):
        if task in self.data['tasks']:
            self.data['tasks'].remove(task)
            self.save_data()

    def complete_task(self, task):
        if task in self.data['tasks']:
            self.data['tasks'].remove(task)
            self.data['completed'].append(task)
            self.save_data()
            return True
        return False

    def list_tasks(self):
        return self.data['tasks']

    def list_completed_tasks(self):
        return self.data['completed']
