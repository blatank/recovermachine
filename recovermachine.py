#! /usr/bin/python3
import time
import pyautogui

cycle = 1
cycle_recover = 30
count_th = 30

count = 0
# Ctrl+Cまで終了しない
while 1:
  while count < count_th:
    # 一定周期毎に左クリックする
    pyautogui.click()
    count = count + 1
    time.sleep(cycle)

  # MP回復待ち
  # ToDo:Autoまで移動してAutoをクリック
  time.sleep(cycle_recover)  
  count = 0
