import plotly.express as px
import pandas as pd

# Assuming tesla_data is already fetched
fig = px.line(tesla_data, x=tesla_data.index, y='Close', title='Tesla Stock Price')
fig.show()
