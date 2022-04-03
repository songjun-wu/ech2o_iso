import numpy as np
line1 = '# no comments'
line2 = str(3650)
tmp = np.linspace(1,3650,3650).tolist()
line3 = ' '.join([str(int(x)) for x in tmp])

output_name_list = ['Precip', 'Tavg', 'Tmax', 'Tmin', 'windspeed', 'RH', 'sdown', 'ldown', 'LAI_1', 'LAI_2']

for output_name in output_name_list:
    with open('./' + output_name + '.txt', 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line1 + '\n' + line2 + '\n' + line3 + '\n' + content)
