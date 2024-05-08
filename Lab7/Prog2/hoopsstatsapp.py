"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd
import matplotlib.pyplot as plt

def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("Lab7/rawbrogdonstats.csv")
    MIN = frame["MIN"]
    FG = frame["FG"]
    THREEPT = frame["3PT"]
    FT = frame["FT"]

    FG_make = []
    FG_attempt = []
    THREEPT_make = []
    THREEPT_attempt = []
    FT_make = []
    FT_attempt = []

    for data in FG:
        data = str(data)
        data_split = data.split('-')
        FG_make.append(int(data_split[0]))
        FG_attempt.append(int(data_split[1]))
    
    for data in THREEPT:
        data = str(data)
        data_split = data.split('-')
        THREEPT_make.append(int(data_split[0]))
        THREEPT_attempt.append(int(data_split[1]))
    
    for data in FT:
        data = str(data)
        data_split = data.split('-')
        FT_make.append(int(data_split[0]))
        FT_attempt.append(int(data_split[1]))

    new_frame = pd.DataFrame({
        'FG Make': FG_make,
        'FG Attempt': FG_attempt,
        '3PT Make': THREEPT_make,
        '3PT Attempt': THREEPT_attempt,
        'FT Make': FT_make,
        'FT Attempt': FT_attempt,
    }, index=MIN)

    new_frame.plot(kind='bar', xlabel='MIN', ylabel='Amount', )
    plt.show()
    # HoopStatsView(frame)

if __name__ == "__main__":
    main()
