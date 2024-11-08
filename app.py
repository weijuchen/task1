import tkinter as tk
from tkinter import ttk
# import pymysql
import sqlite3
import csv
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timezone, timedelta

# D:\D_Download\zap_database

conn = sqlite3.connect("D:\D_Download\zap_database")
cursor = conn.cursor()


def query_info():

    query = "SELECT pm25,temperature,humidity,create_at FROM airqualitydata"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    # for row in data:
    #     print(row)
    # return data

    with open("mj.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([header[0] for header in cursor.description])
        writer.writerows(data)
    print("匯出成功！")


def plot_bar_chart():
    db_data = pd.read_csv("D:\\Work Area\\FINAL\\task1\\mj.csv")

    df = pd.DataFrame(db_data)
    df["create_at"] = pd.to_datetime(df["create_at"], unit="ms")
    df["create_at"] = df["create_at"].dt.strftime("%Y-%m-%d %H %M")
    # df["create_at"] = pd.to_datetime(df["create_at"].astype(int), unit="s")
    # df["create_at"] = pd.to_datetime(df["create_at"].astype(str), format="%Y%m%d%H%M%S")
    # df["create_at"] = pd.to_datetime(df["create_at"], unit="s")
    # df["create_at"] = pd.to_datetime(df["create_at"], format="%Y%m%d%H%M%S")

    X = list(df.iloc[:, 3])
    Y = list(df.iloc[:, 1])

    # Plot the data using bar() method
    plt.bar(X, Y, color="g")
    plt.title("Temperature over time")
    plt.xlabel("Time")
    plt.ylabel("Temperature")

    # Show the plot
    plt.show()
# query_info()
# 查詢表中的所有行
# for row in cur.execute(
#     "SELECT pm25,temperature,humidity,create_at FROM airqualitydata"
# ):
#     print(row)

# conn.close()

# 輸出:
# (1, 'John Doe', 30)


root = tk.Tk()
root.title("GUI Ver1 @v0.02 2024-03-26")
root.geometry("800x800")


notebook = ttk.Notebook(root)


tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="page 1")


button1_1 = tk.Button(
    tab1,
    text="Step 1",
    font=("Arial", 16),
    command=query_info,
    # command=lambda: print("Page 1 按鈕 1 被點擊"),
)
button1_1.pack(pady=20)

button1_2 = tk.Button(
    tab1,
    text="Step 2",
    font=("Arial", 16),
    command=plot_bar_chart,
    # command=lambda: print("Page 1 按鈕 2 被點擊"),
)
button1_2.pack(pady=20)
button1_3 = tk.Button(
    tab1,
    text="Step 3",
    font=("Arial", 16),
    command=lambda: print("Page 1 按鈕 3 被點擊"),
)
button1_3.pack(pady=20)
button1_4 = tk.Button(
    tab1,
    text="Step 4",
    font=("Arial", 16),
    command=lambda: print("Page 1 按鈕 4 被點擊"),
)
button1_4.pack(pady=20)

button1_5 = tk.Button(
    tab1,
    text="Step 5",
    font=("Arial", 16),
    command=lambda: print("Page 1 按鈕 5 被點擊"),
)
button1_5.pack(pady=20)


tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="page2")


button2_1 = tk.Button(
    tab2,
    text="按鈕 2",
    font=("Arial", 16),
    command=lambda: print("Page 2 按鈕 2 被點擊"),
)
button2_1.pack(pady=20)


notebook.pack(expand=True, fill="both")


root.mainloop()
