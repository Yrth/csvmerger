import csv
import array
import os

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
myfile = open('final.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
path = os.path.dirname(os.path.abspath(__file__))
subdirectories = get_immediate_subdirectories(path)
keys_drawed = False
for key in subdirectories:
    subpath = path+'/'+key
    archivos = os.listdir(subpath)
    for x in archivos:
        if "csv" in x and "transposed" not in x:
            archivo = x
            with open(subpath+'/'+archivo) as f:
                r = csv.reader(f, delimiter=',')
                counter = 0
                dict_f_t = {}
                for row in r:
                    print row
                    if counter==0 and (not keys_drawed):
                        counter = 1
                        keys_drawed = True
                    if counter==0 and keys_drawed:
                        counter = 1
                        continue
                    wr.writerow(row)