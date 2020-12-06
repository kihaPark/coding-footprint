#for data_man
CHART_COLS = ['date', 'time', 'f_open', 'f_high', 'f_low', 'f_close', 'f_vol']

CLOSE_IDX = 5  # 종가의 위치

TRAIN_COLS = [
    'open_lastclose_ratio', 'high_close_ratio', 'low_close_ratio',
    'close_lastclose_ratio', 'vol_lastvol_ratio',
    'close_ma5_ratio', 'vol_ma5_ratio',
    'close_ma10_ratio', 'vol_ma10_ratio',
    'close_ma20_ratio', 'vol_ma20_ratio'
]

START_DATE = '2020/07/18'
END_DATE = '2020/07/22'
# END_DATE = '2020/11/09'

MODEL_PATH = 'models/futures_dqn.h5'

# for environment
TRADING_CHARGE = 3000

TICK_PRICE = 12500
TICK_POINT = 0.05

EMPTY_POSITION = 0
LONG_POSITION = 1
SHORT_POSITION = 2

CONTRACT_CNT_IDX = len(TRAIN_COLS)
CONTRACT_POS_IDX = CONTRACT_CNT_IDX + 1
PORTFOLIO_VAL_IDX = CONTRACT_POS_IDX + 1
ACCOUNT_INFO = [CONTRACT_CNT_IDX, CONTRACT_POS_IDX, PORTFOLIO_VAL_IDX]


# for agent
ACTION_ENTRY_BUY = 0    # 신규매수
ACTION_ENTRY_SELL = 1   # 신규매도
ACTION_HOLDING = 2      # 포지션 보유 혹은 관망
ACTION_CLEARING = 3     # 포지션 청산

ACTIONS = [ACTION_ENTRY_BUY, ACTION_ENTRY_SELL, ACTION_HOLDING, ACTION_CLEARING]  
ENTRY_ACTIONS = [ACTION_ENTRY_BUY, ACTION_ENTRY_SELL, ACTION_HOLDING]
HOLDING_ACTIONS = [ACTION_HOLDING, ACTION_CLEARING]

INIT_EPSILON = 1.0
MAX_BATCH_SIZE = 1000


# for train
MAX_EPOCHES = 100

STATE_SIZE = len(TRAIN_COLS) + len(ACCOUNT_INFO)
ACTION_SIZE = len(ACTIONS)




