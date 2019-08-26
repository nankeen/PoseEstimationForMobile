import sys
import json

annFile_foot = sys.argv[1]
annFile_foot_modified = sys.argv[2]

with open(annFile_foot) as f:
    data = json.loads(f.read())
            
    #add additional brackets to categories
    data['categories']=[data['categories']] 
                        
    #add additional brakets to annotations
    for i in range(len(data['annotations'])):
        if type(data['annotations'][i]['segmentation'][0])!=list:
            data['annotations'][i]['segmentation'] = [data['annotations'][i]['segmentation']] #additional brackets
                                                                
            #export
            with open(annFile_foot_modified, 'w+') as ff:
                ff.write(json.dumps(data))
