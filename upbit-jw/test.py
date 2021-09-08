import pyupbit
import time


access = "z2mHQKCNtJUeHgvc8nIW5DYFGCCrNQGfh9ipd3Az"          # 본인 값으로 변경
secret = "SGVXHE7ITVvhSZWvunxpQXFPjqhxA0gwlHlxUYsP"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    # print(balances)
    for b in balances:
        if b['currency'] == 'K  RW':
            if b['balance'] is not None:
                print(b['balance'])
            else:
                return 0
    return 0

for _ in range(5):
    time.sleep(5)
    get_balance("KRW-XRP")

    # print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
    # print(upbit.get_balance("KRW"))         # 보유 현금 조회
    


