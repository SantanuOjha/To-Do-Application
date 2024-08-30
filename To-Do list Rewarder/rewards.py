class RewardSystem:
    def __init__(self, todo_list):
        self.todo_list = todo_list

    def add_reward(self):
        self.todo_list.data['rewards'] += 1
        self.todo_list.save_data()

    def get_rewards(self):
        return self.todo_list.data['rewards']

    def redeem_rewards(self, amount):
        if self.todo_list.data['rewards'] >= amount:
            self.todo_list.data['rewards'] -= amount
            self.todo_list.save_data()
            return True
        return False
