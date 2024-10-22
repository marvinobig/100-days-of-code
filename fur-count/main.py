import pandas as pd


squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_fur_count = squirrel_data['Primary Fur Color'][squirrel_data['Primary Fur Color'] == 'Gray'].count()
black_fur_count = squirrel_data['Primary Fur Color'][squirrel_data['Primary Fur Color'] == 'Black'].count()
cinnamon_fur_count = squirrel_data['Primary Fur Color'][squirrel_data['Primary Fur Color'] == 'Cinnamon'].count()

fur_color_count = {
    'Fur Color': ['Cinnamon', 'Black', 'Gray'],
    'Count': [cinnamon_fur_count, black_fur_count, gray_fur_count],
}

fur_color_count_df = pd.DataFrame(fur_color_count)

fur_color_count_df.to_csv('./fur-color-count.csv')

