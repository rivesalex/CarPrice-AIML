from clean import pd
from sklearn.preprocessing import OneHotEncoder
import pickle
OHE = OneHotEncoder(handle_unknown='ignore')

out = pd.read_pickle('data/cleaned_cars_db.pickle')
out_ML = out.sort_values('manufacturer').reset_index()

encoded_df = pd.DataFrame(OHE.fit_transform(out_ML[['manufacturer']]).toarray().astype(int))
encoded_df.columns = out_ML['manufacturer'].unique()

out_ML = out_ML.join(encoded_df).drop(columns='index')
out_ML.to_pickle('data/out_ML.pkl')


brands_list = encoded_df.columns.to_list()
pickle.dump(brands_list, open("data/brands.pkl", 'wb'))
