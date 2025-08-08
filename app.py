import streamlit as st
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
import pickle
import time

# Title
col = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']

st.title('California Housing Price Prediction')

st.image('https://imgs.search.brave.com/2QlH1jW1D7Aw038DVg1Qwcqh7dim4PdItrsAEPdsSao/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS12ZWN0b3Iv/ZmxhdC1kZXNpZ24t/cmVhbHRvci1hc3Np/c3RhbmNlLWlsbHVz/dHJhdGlvbndpdGgt/d29tYW5fMjMtMjE0/ODY1MTE5Mi5qcGc_/c2VtdD1haXNfaHli/cmlkJnc9NzQw')

st.header('The project aims at building a model of housing prices to predict median house values in California using the provided dataset.',divider=True)

st.subheader('''User Must Enter Given Values To Predict The Price
['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']''')

st.sidebar.title('Select House Feature 🏠')

st.sidebar.image('https://imgs.search.brave.com/IVfAaQIp_cykZu1l7lqmacXyaGKUFtLSCGiNtXLYNNQ/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/aG91c2VwbGFucy5u/ZXQvdXBsb2Fkcy9z/ZWFyY2hlcy8xMi0y/ODguanBnP3Y9MDgw/NDI1MTExOTQ4')
# read_data
temp_df = pd.read_csv('california.csv')

random.seed(52)

all_values = []

for i in temp_df[col]:
    min_value, max_value = temp_df[i].agg(['min','max'])

    var =st.sidebar.slider(f'Select {i} value', int(min_value), int(max_value),
                      random.randint(int(min_value),int(max_value)))

    all_values.append(var)

ss = StandardScaler()
ss.fit(temp_df[col])

final_value = ss.transform([all_values])

with open('house_price_pred_ridge_model.pkl','rb') as f:
    chatgpt = pickle.load(f)

price = chatgpt.predict(final_value)[0]

st.write(pd.DataFrame(dict(zip(col, all_values)),index = [1]))

progress_bar = st.progress(0)
placeholder = st.empty()
placeholder.subheader('Predicting Price')

if price>0:

    for i in range(100):
        time.sleep(0.05)
        progress_bar.progress(i + 1)

    body = f'Predicted Median House Price: ${round(price,2)} Thousand Dollars'
    placeholder.empty()
    # st.subheader(body)

    st.success(body)
else:
    body = 'Invalid House features Values'
    st.warning(body)
