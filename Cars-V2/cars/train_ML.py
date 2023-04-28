import pandas as pd
import pickle
from sklearn.covariance import EllipticEnvelope

EE = EllipticEnvelope(contamination=0.10)
df = pd.read_pickle('data/out_ML.pkl')

X = df.drop(columns=['manufacturer','model1']).to_numpy()
EE.fit(X)

pickle.dump(EE, open("trained_models/ML_model.pkl", 'wb'))