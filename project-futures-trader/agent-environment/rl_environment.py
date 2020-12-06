import rl_const as ct
from rl_data_man import DataMan


class Environment:

    def __init__(self, start_date=ct.START_DATE, end_date=ct.END_DATE):
        self.data_man = DataMan(start=start_date, end=end_date)
        self.chart_data = self.data_man.chart_data()
        self.train_data = self.data_man.train_data()

        self.trading_unit = 1  # 거래 단위
        self.delayed_reward_threshold = 0.012  # 지연보상 임계치

        self.init_balance = 50000000  # 초기 자본금
        self.min_margin = 5000000 # 유지 증거금

        self.observe_chart = None
        self.observe_train = None
        self.observe_state = None
        self.data_idx = -1

        self.balance = 0  # 현재 잔고, 예탁금
        self.contract_cnt = 0  # 보유 계약 수
        self.contract_pt = 0.0 # 계약 포인트
        self.contract_pos = 0 # 계약 포지션, 0:empty, 1:long, 2:short

        self.long_cnt = 0     # 매수 포지션 횟수
        self.short_cnt = 0    # 매도 포지션 횟수
        self.holding_cnt = 0  # 보유 횟수
        self.clearing_cnt = 0  # 포지션 청산 횟수

        # 매수 포지션: balance + (contract_cnt * (현재 선물 포인트 - contract_pt) / TICK_POINT * TICK_PRICE)
        # 매도 포지션: balance + (contract_cnt * (contract_pt - 현재 선물 포인트) / TICK_POINT * TICK_PRICE)
        # 포지션 없음: balance
        self.position_value = 0  # 포지션 손익 현황
        self.portfolio_value = self.balance + self.position_value  # balance + 포지션 손익 현황
        self.base_portfolio_value = self.portfolio_value  # 직전 학습 시점의 PV
        self.profitloss = 0.0 # 현재 손익
        self.base_profitloss = 0.0  # 직전 지연 보상 이후 손익
        self.immediate_reward = 0  # 즉시 보상
        self.ratio_portfolio_value = 0.0  # 포트폴리오 가치 비율, portfolio_value / base_portfolio_value


    def reset(self):
        self.observe_chart = None
        self.observe_train = None
        self.observe_state = None
        self.data_idx = -1

        self.balance = self.init_balance
        self.contract_cnt = 0
        self.contract_pt = 0.0
        self.contract_pos = 0

        self.long_cnt = 0
        self.short_cnt = 0
        self.holding_cnt = 0
        self.clearing_cnt = 0

        self.position_value = 0
        self.portfolio_value = self.balance + self.position_value
        self.base_portfolio_value = self.portfolio_value
        self.profitloss = 0.0
        self.base_profitloss = 0.0
        self.immediate_reward = 0
        self.ratio_portfolio_value = 0.0


    def account_status(self):
        self.ratio_portfolio_value = self.portfolio_value / self.base_portfolio_value
        return [self.contract_cnt, self.contract_pos, self.ratio_portfolio_value]


    def next_state(self):
        if len(self.chart_data) <= self.data_idx + 1:
            return None

        self.data_idx += 1
        self.observe_chart = self.chart_data.iloc[self.data_idx]
        self.observe_train = self.train_data.iloc[self.data_idx]

        self.observe_state = self.observe_train.to_list()
        self.observe_state.extend(self.account_status())
        return self.observe_state


    def cur_close_point(self):
        if self.observe_chart is None:
            return None

        return self.observe_chart[ct.CLOSE_IDX]


    def calc_position_value(self):
        if self.contract_pos == ct.EMPTY_POSITION:
            return 0

        close_point = self.cur_close_point()
        delta = close_point - self.contract_pt
        delta = delta if self.contract_pos == ct.LONG_POSITION else -delta
        return int(self.contract_cnt * delta / ct.TICK_POINT * ct.TICK_PRICE)


    def step(self, action):
        close_point = self.cur_close_point()
        if close_point is None:
            return

        if action == ct.ACTION_ENTRY_BUY:
            if self.contract_cnt >= 1:
                print('ACTION_ENTRY_BUY error!!')

            self.position_value = self.calc_position_value()
            self.contract_cnt = 1
            self.contract_pt = self.cur_close_point()
            self.contract_pos = ct.LONG_POSITION
            self.long_cnt += 1
            self.balance -= ct.TRADING_CHARGE

        elif action == ct.ACTION_ENTRY_SELL:
            if self.contract_cnt >= 1:
                print('ACTION_ENTRY_SELL error!!')
            
            self.position_value = self.calc_position_value()
            self.contract_cnt = 1
            self.contract_pt = self.cur_close_point()
            self.contract_pos = ct.SHORT_POSITION
            self.short_cnt += 1
            self.balance -= ct.TRADING_CHARGE

        elif action == ct.ACTION_CLEARING:
            if self.contract_cnt <= 0:
                print('ACTION_CLEARING error!!')

            self.position_value = self.calc_position_value()
            self.contract_cnt = 0
            self.contract_pt = 0.0
            self.contract_pos = ct.EMPTY_POSITION
            self.clearing_cnt += 1
            self.balance = self.balance + self.position_value - ct.TRADING_CHARGE

        else: # ACTION_HOLDING
            self.position_value = self.calc_position_value()
            self.holding_cnt += 1

        # update portfolio_value
        self.portfolio_value = self.balance + self.position_value
        self.profitloss = \
            (self.portfolio_value - self.init_balance) / self.init_balance
        self.base_profitloss = \
            (self.portfolio_value - self.base_portfolio_value) / self.base_portfolio_value

        # 즉시 보상, 수익률
        self.immediate_reward = self.profitloss

        # 지연 보상, 익절 손절 기준
        delayed_reward = 0
        base_profitloss_abs = abs(self.base_profitloss)
        if base_profitloss_abs > self.delayed_reward_threshold:
            self.base_portfolio_value = self.portfolio_value
            delayed_reward = self.immediate_reward

        # 유지 증거금 보다 작아질때 거래 종료
        done = bool(self.min_margin > self.portfolio_value)

        return (self.immediate_reward, delayed_reward, done)


if __name__ == "__main__":
    env = Environment()
    env.reset()
    print('inti environment!!')