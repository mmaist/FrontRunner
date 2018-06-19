import time
import random
import json
import requests

BANCOR_CHANGER = '0xb72a0fa1e537c956dfca72711c468efd81270468'
CHANGE_METHOD = '0x5e5144eb'
QUICKBUY_METHOD = '0x7758c4f8'
QUICKCHANGE_METHOD = '0xa93d7c72'
BANCOR_TOKEN = '0x1f573d6fb3f13d689ff844b4ce37794d79a7ff1c'
ETH_ERC20_TOKEN = '0xc0829421c1d260bd3cb3e0f06cfe2d52db2ce315'
BUY_THRESHOLD = int(200e18)  # 200 ETH
BUY_AMOUNT = int(5e18)  # 5 ETH


def log(*args):
  print('-' * 40)
  print(time.ctime())
  print(args)


