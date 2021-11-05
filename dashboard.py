import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
from urllib.request import urlopen
import json
import plotly.graph_objects as go 

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})



import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

#Inputs
df_1 = pd.read_csv("2016.csv")
map_values = {'Loan originated':1, 
              'Application approved but not accepted':0,
              'Application denied by financial institution':0,
              'Application withdrawn by applicant':0,
              'File closed for incompleteness':0,
              'Loan purchased by the institution':0,
              'Preapproval request denied by financial institution':0,
              'Preapproval request approved but not accepted':0
            }
df_1["action_taken_name"] = df_1.apply(lambda row: map_values[row["action_taken_name"]], axis=1)
df_fips = pd.read_csv("state_and_county_fips_master.csv")
df_fips = df_fips[df_fips["state"]=="WA"].reset_index(drop=True)
df_1 = df_1.merge(df_fips, left_on="county_name",right_on="name")

df_1.drop(['name','state','applicant_race_name_5', 'applicant_race_name_4' , 'applicant_race_name_3' , 'applicant_race_name_2',], axis=1 , inplace = True)
df_1.drop(['agency_abbr'] , axis = 1 ,inplace = True)
df_1.drop(['as_of_year'], axis = 1 ,inplace = True)
df_1.drop(['co_applicant_race_name_2' , 'state_name'], axis = 1 ,inplace = True)
df_1.drop(['co_applicant_race_name_5', 'co_applicant_race_name_4' , 'co_applicant_race_name_3' ,'state_abbr'], axis=1 , inplace = True)
marks={h : {"label":str(h),"style":{"color":"white"}} for h in range(2011,2017)}


#2011
df_2011 = pd.read_csv("2011.csv")
df_2011["action_taken_name"] = df_2011.apply(lambda row: map_values[row["action_taken_name"]], axis=1)

df_2011 = df_2011.merge(df_fips, left_on="county_name",right_on="name")

df_2011.drop(['name','state','applicant_race_name_5', 'applicant_race_name_4' , 'applicant_race_name_3' , 'applicant_race_name_2',], axis=1 , inplace = True)
df_2011.drop(['agency_abbr'] , axis = 1 ,inplace = True)
df_2011.drop(['as_of_year'], axis = 1 ,inplace = True)
df_2011.drop(['co_applicant_race_name_2' , 'state_name'], axis = 1 ,inplace = True)
df_2011.drop(['co_applicant_race_name_5', 'co_applicant_race_name_4' , 'co_applicant_race_name_3' ,'state_abbr'], axis=1 , inplace = True)

#2012
df_2012 = pd.read_csv("2012.csv")
df_2012["action_taken_name"] = df_2012.apply(lambda row: map_values[row["action_taken_name"]], axis=1)

df_2012 = df_2012.merge(df_fips, left_on="county_name",right_on="name")

df_2012.drop(['name','state','applicant_race_name_5', 'applicant_race_name_4' , 'applicant_race_name_3' , 'applicant_race_name_2',], axis=1 , inplace = True)
df_2012.drop(['agency_abbr'] , axis = 1 ,inplace = True)
df_2012.drop(['as_of_year'], axis = 1 ,inplace = True)
df_2012.drop(['co_applicant_race_name_2' , 'state_name'], axis = 1 ,inplace = True)
df_2012.drop(['co_applicant_race_name_5', 'co_applicant_race_name_4' , 'co_applicant_race_name_3' ,'state_abbr'], axis=1 , inplace = True)

#2013
df_2013 = pd.read_csv("2013.csv")
df_2013["action_taken_name"] = df_2013.apply(lambda row: map_values[row["action_taken_name"]], axis=1)

df_2013 = df_2013.merge(df_fips, left_on="county_name",right_on="name")

df_2013.drop(['name','state','applicant_race_name_5', 'applicant_race_name_4' , 'applicant_race_name_3' , 'applicant_race_name_2',], axis=1 , inplace = True)
df_2013.drop(['agency_abbr'] , axis = 1 ,inplace = True)
df_2013.drop(['as_of_year'], axis = 1 ,inplace = True)
df_2013.drop(['co_applicant_race_name_2' , 'state_name'], axis = 1 ,inplace = True)
df_2013.drop(['co_applicant_race_name_5', 'co_applicant_race_name_4' , 'co_applicant_race_name_3' ,'state_abbr'], axis=1 , inplace = True)

#2014
df_2014 = pd.read_csv("2014.csv")
df_2014["action_taken_name"] = df_2014.apply(lambda row: map_values[row["action_taken_name"]], axis=1)

df_2014 = df_2014.merge(df_fips, left_on="county_name",right_on="name")

df_2014.drop(['name','state','applicant_race_name_5', 'applicant_race_name_4' , 'applicant_race_name_3' , 'applicant_race_name_2',], axis=1 , inplace = True)
df_2014.drop(['agency_abbr'] , axis = 1 ,inplace = True)
df_2014.drop(['as_of_year'], axis = 1 ,inplace = True)
df_2014.drop(['co_applicant_race_name_2' , 'state_name'], axis = 1 ,inplace = True)
df_2014.drop(['co_applicant_race_name_5', 'co_applicant_race_name_4' , 'co_applicant_race_name_3' ,'state_abbr'], axis=1 , inplace = True)

#2015
df_2015 = pd.read_csv("2015.csv")
df_2015["action_taken_name"] = df_2015.apply(lambda row: map_values[row["action_taken_name"]], axis=1)

df_2015 = df_2015.merge(df_fips, left_on="county_name",right_on="name")

df_2015.drop(['name','state','applicant_race_name_5', 'applicant_race_name_4' , 'applicant_race_name_3' , 'applicant_race_name_2',], axis=1 , inplace = True)
df_2015.drop(['agency_abbr'] , axis = 1 ,inplace = True)
df_2015.drop(['as_of_year'], axis = 1 ,inplace = True)
df_2015.drop(['co_applicant_race_name_2' , 'state_name'], axis = 1 ,inplace = True)
df_2015.drop(['co_applicant_race_name_5', 'co_applicant_race_name_4' , 'co_applicant_race_name_3' ,'state_abbr'], axis=1 , inplace = True)


# print(df_1_population)

# App Layout
app.layout = html.Div(children=[
    dbc.NavbarSimple(
    brand="HMDA Analysis",
    brand_href="#",
    color="rgb(30, 30, 30)",
    dark=True,
    ),
    html.Br(),
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card
                    (
                        dbc.CardBody
                        (
                            [
                                dcc.Slider(
                                    id="yearslider",
                                    min=2011,
                                    max=2016,
                                    step=None,
                                    marks=marks
                                ), 

                            ],
                            style={"background-color":"black"}
                        )
                    )
                ],
                width=6   
            ),

            dbc.Col(
                [
                    dbc.Card(
                        dbc.CardBody
                        (
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dcc.Dropdown(
                                                    id='demo-dropdown',
                                                    options=[
                                                        {'label': 'Population', 'value': 'population'},
                                                        {'label': 'Loan Approval', 'value': 'action_taken_name'},
                                                    ],
                                                    placeholder = "Select criteria",
                                                    style={"color":"black"}
                                                ),

                                            ],
                                            width=12,
                                        ),
                                    ]
                                )

                            ],
                            style={"background-color":"black"}
                        )
                    )
                ],
                width=3
            ),
        ]
    ),
    html.Br(),
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody
                            (
                                [
                                    html.H5("County Details", style={"textAlign":"center"}),
                                    html.Div(children=[], id="selectioncriteria", style={"textAlign":"center"}),
                                    html.Div(id="choropleth_map1_div",children=[
                                    dcc.Loading(children = dcc.Graph(id="choropleth_map1", style={"height":"53vh"}) )
                                    ])
                                ],
                                style={"background-color":"black", "height":"65vh"}
                            )
                        ]
                    )
                ],
                width=6,
            ),
            dbc.Col(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Card(
                                        [
                                            dbc.CardBody
                                            (
                                                [
                                                    html.H5("Loan Purpose Vs Rate of Approval(%)", style={"textAlign":"center"}),
                                                    html.Div(children=[], id="selectedregion", style={"textAlign":"center"}),
                                                    dcc.Loading(dcc.Graph(id="lrra", style={"height":"50vh"})),
                                                ],
                                                style={"background-color":"black", "height":"65vh"}
                                            )
                                        ]
                                    )

                                ],
                                width=12,
                            )
                        ]
                    )
                ],
                width=6,
            ),
        ],
        style={"padding-top":"5 px"}
    ),
    html.Br(),
    dbc.Row([
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardBody
                        (
                            [
                                html.H5("Loan Type Name Vs Rate of Approval(%)", style={"textAlign":"center"}),
                                html.Div(children=[], id="selectedregion1", style={"textAlign":"center"}),
                                dcc.Loading(dcc.Graph(id="ltra", style={"height":"50vh"})),
                            ],
                            style={"background-color":"black", "height":"65vh"}
                        )
                    ]
                )
            ],
            width=12,
        )
    ])
])

@app.callback(
    [
    Output('choropleth_map1', 'figure'),
    Output('selectioncriteria','children')
    ],
    [
    Input('yearslider', 'value'),
    Input('demo-dropdown','value')
    ]
    )
def update_figure(sliderdata, ddown):
    year = {
        2011 : df_2011,
        2012 : df_2012,
        2013 : df_2013,
        2014 : df_2014,
        2015 : df_2015,
        2016 : df_1
    }
    if not sliderdata:
        sliderdata = 2011
    
    df_copy = year[sliderdata]   
    if not ddown:
        ddown = "population"
    
    if ddown == "population":
        df_1_down = df_copy.groupby('fips')[ddown].mean().reset_index(name=ddown)

    if ddown == "action_taken_name":
        df_1_down = df_copy.groupby('fips')[ddown].sum().reset_index(name=ddown)
        ddown = "loanapproval"
        df_1_down = df_1_down.rename(columns={"action_taken_name":"loanapproval"})
        #df_1_down = df_1.groupby('fips')[ddown].mean().reset_index(name=ddown)


    fig = px.choropleth_mapbox(df_1_down, geojson=counties, locations='fips', color=ddown,
                           color_continuous_scale="Viridis",
                           range_color=(min(df_1_down[ddown]), max(df_1_down[ddown])),
                           mapbox_style="carto-positron",
                           zoom=5, center = {"lat": 47.751076, "lon": -120.740135},
                           opacity=0.5,
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                            # plot_bgcolor='green',
                            # paper_bgcolor='green'
                    )
    return (fig,html.H6("based on "+ddown))

@app.callback(
    [
    Output('lrra','figure'),
    Output('selectedregion', 'children'),
    Output('ltra','figure'),
    Output('selectedregion1', 'children'),
    ],
    [
    Input('choropleth_map1', 'clickData'),
    Input('yearslider','value'),
    ])
def update_bargraph(selectdata, sliderdata):
    year = {
        2011 : df_2011,
        2012 : df_2012,
        2013 : df_2013,
        2014 : df_2014,
        2015 : df_2015,
        2016 : df_1
    }
    if not sliderdata:
        sliderdata = 2011
    
    df_copy = year[sliderdata]
    print(df_copy)
    region = "Washington"
    if selectdata:
        fips_selected = selectdata["points"][0]["location"]
        df_copy = df_copy[df_copy["fips"]==fips_selected].reset_index(drop=True)
        region = df_copy[df_copy["fips"]==fips_selected]["county_name"].iloc[0]

    # Loan Purpose and rate of Approval
    df_purpose = pd.crosstab(df_copy['loan_purpose_name'],df_copy['action_taken_name'],normalize='index').reset_index()
    print(df_purpose)
    df_purpose = df_purpose.rename(columns={0:"Loan_Rejected",1:"Loan_Approved"})
    df_purpose["Loan_Rejected"] = df_purpose["Loan_Rejected"]*100
    df_purpose["Loan_Approved"] = df_purpose["Loan_Approved"]*100
    fig2 = go.Figure(data=[
        go.Bar(name='Loan Rejected', x=df_purpose["loan_purpose_name"].to_list(), y=df_purpose["Loan_Rejected"].to_list()),
        go.Bar(name='Loan Approved', x=df_purpose["loan_purpose_name"].to_list(), y=df_purpose["Loan_Approved"].to_list())
    ])
    fig2.update_layout(barmode='group', xaxis_title="Loan Purpose",
    yaxis_title="Purpose Rate(%)")

    # Loan Type Name and rate of Approval
    # Loan Purpose and rate of Approval
    df_purpose1 = pd.crosstab(df_copy['loan_type_name'],df_copy['action_taken_name'],normalize='index').reset_index()
    df_purpose1 = df_purpose1.rename(columns={0:"Loan_Rejected",1:"Loan_Approved"})
    df_purpose1["Loan_Rejected"] = df_purpose1["Loan_Rejected"]*100
    df_purpose1["Loan_Approved"] = df_purpose1["Loan_Approved"]*100
    fig3 = go.Figure(data=[
        go.Scatter(mode= 'lines+markers', name='Loan Rejected', x=df_purpose1["loan_type_name"].to_list(), y=df_purpose1["Loan_Rejected"].to_list()),
        go.Scatter(mode= 'lines+markers', name='Loan Approved', x=df_purpose1["loan_type_name"].to_list(), y=df_purpose1["Loan_Approved"].to_list())
    ])
    #fig3 = go.Figure()
    # fig3.add_trace(go.Scatter(x=random_x, y=random_y0,
    #                     mode='lines',
    #                     name='lines'))
    # fig3.add_trace(go.Scatter(x=random_x, y=random_y1,
    #                     mode='lines+markers',
    #                     name='lines+markers'))
    fig3.update_layout(barmode='group', xaxis_title="Loan Type Name",
    yaxis_title="Purpose Rate(%)")

    return (fig2, html.H6(region), fig3, html.H6(region))

if __name__ == '__main__':
    app.run_server(debug=True)