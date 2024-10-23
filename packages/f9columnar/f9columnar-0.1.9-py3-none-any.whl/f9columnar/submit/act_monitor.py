import datetime
import os
import time

import pandas as pd


def read_act_state():
    os.system("act stat -a > logs/act_stat.txt")
    df = pd.read_csv("logs/act_stat.txt", delimiter=r"\s+")
    os.system("rm -f logs/act_stat.txt")
    return df


def act_monitor(rate=5):
    while True:
        df = read_act_state()
        state, act_state = df["State"], df["arcstate"]

        print(26 * "=")
        print(datetime.datetime.now())
        print(26 * "=")
        print(state.value_counts())
        print(26 * "-")
        print(act_state.value_counts())
        print(26 * "=" + "\n")

        time.sleep(rate)


if __name__ == "__main__":
    # need to pip install pandas in act_venv
    act_monitor()
