import pandas as pd

url = 'https://www.cwb.gov.tw/V8/C/W/OBS_Station.html?ID=46691'

dfs = pd.read_html(url)
print(len(dfs))