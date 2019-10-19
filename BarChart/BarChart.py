'''Module to Show the way of presenting data using Bar Chart'''
import os
import yaml
import plotly.graph_objects as pg
def get_team_list(path):
    '''Get Team List from all Yaml files'''
    all_teams = []
    unique_teams = []
    uniq_team_count = []
    winners = {}
    temp = 0
    print("Wait Getting Teams List")
    for root, direc, files in os.walk(path):
        for filer in files:
            print(temp)
            temp += 1
            try:
                with open(root + "/"+filer) as file_obj:
                    data = yaml.load(file_obj, Loader=yaml.FullLoader)
                    for team in data['info']['teams']:
                        all_teams.append(team.strip())
                    if data['info']['toss']['winner'] not in winners.keys():
                        winners[data['info']['toss']['winner']] = 1
                    else:
                        winners[data['info']['toss']['winner']] = \
                              winners[data['info']['toss']['winner']] + 1
            except:
                print("File Type Not Supported or Data not Exists")
    print("Collected Teams Details")
    unique_teams = sorted(list(set(all_teams)))
    for team in unique_teams:
        uniq_team_count.append(all_teams.count(team))
    winner_tup = []
    winner_list = []
    winner_count = []
    for (team, count) in winners.items():
        winner_tup.append((team, count))
    winner_tup.sort(key=lambda x: x[0])
    for tup in winner_tup:
        winner_list.append(tup[0])
        winner_count.append(tup[1])
    print(winner_tup)
    print(winner_list)
    print(winner_count)
    return (unique_teams, uniq_team_count, winner_list, winner_count)

PATH = str(input("Enter Path of YAML DataSet: "))
TEAMS_TUPLE = get_team_list(PATH)
'''Two Seperate Bar Graphs
bar_chart1 = pg.Figure(data=pg.Bar(x=TEAMS_TUPLE[0],y=TEAMS_TUPLE[1]))
bar_chart1.write_html('Unique_Teams.html',auto_open=True)
bar_chart2 = pg.Figure(data=pg.Bar(x=TEAMS_TUPLE[2],y=TEAMS_TUPLE[3]))
bar_chart2.write_html('Winner_Teams.html',auto_open=True)
'''
BAR_CHART = pg.Figure()
BAR_CHART.add_trace(pg.Bar(x=TEAMS_TUPLE[0],\
	y=TEAMS_TUPLE[1], name='Played Matches', marker_color='indianred'))
BAR_CHART.add_trace(pg.Bar(x=TEAMS_TUPLE[2],\
	y=TEAMS_TUPLE[3], name='Won Matches', marker_color='lightsalmon'))
BAR_CHART.update_layout(title='Winning Statistics of Various countries for 1445 Matches',\
xaxis=dict(title="Countries", titlefont_size=16),\
yaxis=dict(title="Number of Matches", titlefont_size=16),\
)
BAR_CHART.write_html('Bar_Chart.html', auto_open=True)
