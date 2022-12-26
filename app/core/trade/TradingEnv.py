


class Market:
    def __init__(self, price_data):
        self.bot = BotTrader()
        self.price_data = price_data
        self.reset()

    def reset(self):
        self.total_profit = 0
        self.bot.reset()
        self.step_count = 0
        self.done = False
        self.new_observation = self.price_data.iloc[self.step_count]

    def step(self, action):
        reward = 0

        if action == 1:
            self.bot.buy(self.price_data.iloc[self.step_count]['Close'])
        elif (action == 2) and (self.bot.position_status == 1):
            self.bot.sell(self.price_data.iloc[self.step_count]['Close'])
            self.total_profit += self.bot.profit
            reward = self.bot.profit
            self.bot.position_status = 0
        if reward > 0:
            reward = 1
        else:
            reward = -1

        self.step_count += 1

        if self.step_count >= len(self.price_data)
            self.done = True
        else:
            self.new_observation = self.price_data.iloc[self.step_count]

        return self.done, self.new_observation, reward

class BotTrader:
    def __init__(self):
        self.reset()

    def reset(self):
        self.position_price = 0
        self.position_status = 0
        self.profit = 0

    def buy(self, current_price):
        self.position_price = current_price
        self.position_status = 1

    def sell(self, current_price):
        self.profit = (current_price - self.position_price) * 100 / self.position_price
        self.position_status = 0
