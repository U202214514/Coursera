# Assuming gamestop_data is already fetched
fig = px.line(gamestop_data, x=gamestop_data.index, y='Close', title='GameStop Stock Price')
fig.show()
