import rl_const as ct
from rl_environment import Environment
from rl_agent import Agent


class FuturesTrader():
    def __init__(self):
        self.env = Environment(start_date='2020/10/30', end_date='2020/11/09')
        self.agent = Agent(model_path=ct.MODEL_PATH)


    def reset(self):
        self.env.reset()
        self.agent.reset()
        self.agent.epsilon = 0.0


    def begin_trade(self):
        self.reset()
        result = self.next_trade()
        return result


    def next_trade(self):
        state = self.env.next_state()
        if state is None:
            return self.make_result()

        action, preds = self.agent.get_action(state)
        immediate_reward, _, done = self.env.step(action)
        self.agent.append_sample(state, action, immediate_reward, preds, done)

        result = self.make_result(action)
        return result


    def make_result(self, agent_action):
        chart = self.env.observe_chart
        result = {
            'chartDate': chart[0],
            'chartTime': chart[1],
            'chartOpen': chart[2],
            'chartHigh': chart[3],
            'chartLow': chart[4],
            'chartClose': chart[5],
            'chartVolume': chart[6],
            'contractCount': self.env.contract_cnt,
            'contractPoint': self.env.contract_pt,
            'contractPosition': self.env.contract_pos,
            'positionValue': self.env.position_value,
            'initBalance': self.env.init_balance,
            'balance': self.env.balance,
            'profitLoss': self.env.profitloss,
            'agentAction': agent_action
        }
        return result


if __name__ == "__main__":
    ft = FuturesTrader()
    print('init FuturesTrader!!')
    result = ft.begin_trade()
    print(result)

