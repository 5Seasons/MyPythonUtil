import pandas as pd

pddata=pd.read_csv('pddata.csv')
pddata.describe()
pddata.columnspd
pddata.coordX
features=['coordX', 'coordY', 'coordZ']
x=pddata[features]
x.head()
from sklearn.tree import DecisionTreeRegressor
# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)
y=pddata.diameter_mm
melbourne_model.fit(x, y)
melbourne_model.predict(x.head())
import SimpleITK as sitk
