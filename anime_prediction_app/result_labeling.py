import pandas as pd

# labels consumption status on final_data
# no room for custumization

def lable_result():
    final_data = pd.read_csv('data/final_data.csv')


    list_data = pd.read_csv('data/alist.csv')
    list_data = list_data[['id_ref', 'consumption_status']]

    final_data = final_data.merge(list_data, on='id_ref')

    final_data = final_data.drop('Unnamed: 0', axis=1)

    final_data = final_data[['id_ref', 'name', 'prediction', 'consumption_status']]

    final_data.to_csv('data/final_data_labled.csv')

    print('Finished labeling')
