import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

execute_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.normpath(os.path.join(execute_dir, '..', '..'))
result_visualize_dir = os.path.normpath(os.path.join(project_root, 'result', 'visualizetion'))
raw_data_dir = os.path.normpath(os.path.join(project_root, 'data', 'raw'))


df = pd.read_csv(os.path.join(raw_data_dir ,'nikkei_stock_average_daily_jp.csv'), encoding='shift_jis')
df = df.iloc[:-1, 0:2]
df.columns = ['date', 'price']

# change data type (date:string → dateformat)
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# plot Price
plt.figure(figsize=[10, 4])
plt.style.use('ggplot')
left = np.array(df['date'])
height = np.array(df['price'])
plt.plot(left, height)
plt.title('nikkei Price')
plt.xlabel('date')
plt.ylabel('price')
plt.savefig(os.path.join(result_visualize_dir, 'plot_price_raw.png'))

