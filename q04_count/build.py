# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    for k in data['innings'][0]['1st innings']['deliveries']:
        for y,x in k.items():
            if x['batsman']== 'RT Ponting':
                count=count+1
    return count
