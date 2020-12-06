import numpy as np
from collections import deque
import rl_const as ct
from rl_q_network import QNetwork as qnet


class Agent:

    def __init__(self, state_size=ct.STATE_SIZE, \
        action_size=ct.ACTION_SIZE, model_path=None):
        self.state_size = state_size
        self.action_size = action_size

        self.discount_factor = 0.9
        self.learning_rate = 0.001
        self.epsilon = ct.INIT_EPSILON

        self.batch_size = 0
        self.memory = deque(maxlen=3000)

        self.model = qnet(input_dim=state_size, \
            output_dim=action_size, model_path=model_path)
        # self.target_model = qnet(input_dim=state_size, output_dim=action_size)
        # self.update_target_model()


    def reset(self):
        self.epsilon = ct.INIT_EPSILON
        self.batch_size = 0
        self.memory.clear()


    def set_epsilon(self, cur_epoch):
        self.epsilon = \
            ct.INIT_EPSILON * (1.0 - float(cur_epoch) / float(ct.MAX_EPOCHES - 1))
        self.epsilon = max(self.epsilon, 0.001)


    # 타깃 모델을 모델의 가중치로 업데이트
    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())


    def save_model(self, model_path):
        self.model.save_model(model_path)


    # 입실론 탐욕 정책으로 액션 선택
    def get_action(self, state):
        # state에서 포지션 보유 상태 파악
        # 가능한 행동만 선택하도록 처리
        holding_position = bool(state[ct.CONTRACT_CNT_IDX] >= 1)
        able_actions = ct.HOLDING_ACTIONS if holding_position else ct.ENTRY_ACTIONS
        select_action = ct.ACTION_HOLDING

        preds = self.model.predict(state)

        if np.random.rand() <= self.epsilon:
            select_action = np.random.choice(able_actions)
        else:
            able_preds = preds[able_actions]
            select_action = able_actions[np.argmax(able_preds)]

        return select_action, preds


    # 샘플 <state, action, reward, next_state>을 리플레이 메모리에 저장
    # 최신 정보가 앞으로 오도록 저장
    def append_sample(self, state, action, reward, values, done):
        self.memory.appendleft((state, action, reward, values, done))
        self.batch_size += 1


    def get_batch(self, batch_size, delayed_reward):
        if len(self.memory) == 0:
            return None, None

        batch_memory = list(self.memory)[:batch_size]
        x_train = np.zeros((batch_size, 1, ct.STATE_SIZE))
        y_value = np.zeros((batch_size, ct.ACTION_SIZE))
        value_max_next = 0
        reward_next = self.memory[0][2]
        for i, (state, action, reward, value, done) in enumerate(batch_memory):
            x_train[i] = state
            y_value[i] = value
            r = (delayed_reward + reward_next - reward * 2) * 100
            y_value[i, action] = r + self.discount_factor * value_max_next
            value_max_next = value.max()
            reward_next = reward
        return x_train, y_value


    def train_model(self, delayed_reward, full=False):
        batch_size = len(self.memory) if full else self.batch_size
        if batch_size == 0:
            return

        x_train, y_value = self.get_batch(batch_size, delayed_reward)
        self.model.train_on_batch(x_train, y_value)
        self.batch_size = 0


if __name__ == "__main__":
    agent = Agent()
    agent.reset()
    print('init agent!!')

