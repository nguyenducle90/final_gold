import os
import pickle
import sklearn
import streamlit as st

FILEPATH = os.path.join('H:\python project\program\python nang cao\demo\models\gold.model.pkl')
def forecast(spx:float, uso: float, slv:float, eur_usd: float)->float:
    model = pickle.load(open(FILEPATH, 'rb'))
    results = model.predict([[spx, uso, slv, eur_usd]])
    return results[0]


spx = st.slider('SPX', min_value=676.0, max_value=2873.0, step=0.1)
uso = st.slider('USO', min_value=7.0, max_value=118.0, step=0.1)
slv = st.slider('SLV', min_value=8.0, max_value=48.0, step=0.1)
eur_usd = st.slider('EUR/USD', min_value=1.0, max_value=1.6, step=0.1)
result = forecast(spx, uso, slv, eur_usd)
st.write('Predicted: %s' % result)