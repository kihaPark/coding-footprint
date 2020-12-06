import locale
import logging
import rl_const as ct
from rl_environment import Environment
from rl_agent import Agent

logger = logging.getLogger(__name__)
locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')

if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    for epoch in range(ct.MAX_EPOCHES):
        env.reset()
        agent.reset()

        agent.set_epsilon(epoch)
        done = False

        while not done:
            state = env.next_state()
            if state is None:
                break

            # 가치 신경망 예측, 신경망 또는 탐험에 의한 행동 결정
            action, preds = agent.get_action(state)

            # 결정한 행동을 수행하고 즉시 보상과 지연 보상 획득
            immediate_reward, delayed_reward, done = env.step(action)

            # 행동 및 행동에 대한 결과를 기억
            agent.append_sample(state, action, immediate_reward, preds, done)

            # 지연 보상 발생된 경우 배치 학습
            if delayed_reward != 0:
                agent.train_model(delayed_reward)

        agent.train_model(env.profitloss, full=True)

        print(f'epoch:{epoch}, port:{int(env.portfolio_value)}, profit:{round(env.profitloss*100,1)}')
        print(f'long:{env.long_cnt}, short:{env.short_cnt}, hold:{env.holding_cnt}, clear:{env.clearing_cnt}')

    agent.save_model(ct.MODEL_PATH)



