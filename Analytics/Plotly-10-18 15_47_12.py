# Databricks notebook source
# MAGIC %pip install dash plotly pandas
# MAGIC

# COMMAND ----------

# This is just experimental to show how you can make use of Plotly Library for Analytics
# Author and experiemental from Yogananda Muthaiah (SAP Solution Architect)

import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Region": ["North", "South", "East", "West"],
    "Avg_Delay_Days": [2.5, 3.1, 1.8, 4.0]
})

fig = px.bar(df, x="Region", y="Avg_Delay_Days", title="Average Delivery Delay by Region")
fig.show()

# COMMAND ----------

# This is just experimental to show how you can make use of Plotly Library for Analytics
# Author and experiemental from Yogananda Muthaiah (SAP Solution Architect)

import plotly.graph_objects as go

# Sample forecast data
quarters = ["Q1", "Q2", "Q3", "Q4"]
actuals = [100, 120, 130, 150]
forecast = [105, 125, 135, 160]

fig = go.Figure()
fig.add_trace(go.Scatter(x=quarters, y=actuals, mode='lines+markers', name='Actual'))
fig.add_trace(go.Scatter(x=quarters, y=forecast, mode='lines+markers', name='Forecast'))

fig.update_layout(title="Quarterly Revenue Forecast", xaxis_title="Quarter", yaxis_title="Revenue (in M€)")
fig.show()

# COMMAND ----------

import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")

# If you print the figure, you'll see that it's just a regular figure with data and layout
# print(fig)

fig.show()

# COMMAND ----------

from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.update_traces(marker=dict(color="RoyalBlue"),
                  selector=dict(type="bar"))

fig.show()

# COMMAND ----------

import pandas as pd
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 facet_col="species", title="Using update_xaxes() With A Plotly Express Figure")

fig.update_xaxes(showgrid=False)

fig.show()

# COMMAND ----------

import plotly.express as px
df = px.data.iris()
df["e"] = df["sepal_width"]/100
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", error_x="e", error_y="e")
fig.show()

# COMMAND ----------

from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "bar"}, {"type": "barpolar"}],
           [{"type": "pie"}, {"type": "scatter3d"}]],
)

fig.add_trace(go.Bar(y=[2, 3, 1]),
              row=1, col=1)

fig.add_trace(go.Barpolar(theta=[0, 45, 90], r=[2, 3, 1]),
              row=1, col=2)

fig.add_trace(go.Pie(values=[2, 3, 1]),
              row=2, col=1)

fig.add_trace(go.Scatter3d(x=[2, 3, 1], y=[0, 0, 0],
                           z=[0.5, 1, 2], mode="lines"),
              row=2, col=2)

fig.update_layout(height=700, showlegend=False)

fig.show()