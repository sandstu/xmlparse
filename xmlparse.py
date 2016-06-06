# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 10:47:18 2016

@author: stusand
"""
def xmlparse(xml):
    import xml.etree.ElementTree as ET
    import pandas as pd
    tree=ET.parse(xml)
    root=tree.getroot()
    act=root.getchildren()[0].getchildren()[0]
    elem=list(act)
    ment=list(act)
    
    indices=[]
    datadict={}
    i=0
    
    for element in elem:
        elemnt=element.getchildren()
        for children in elemnt:
            if len(children.getchildren())>1:
                indices.append(element)
                if indices[0] in ment:
                    ment.remove(indices[0])
                else:
                    data={}
                    for elment in ment:
                        mentary=elment.getchildren()
                        for child in mentary:
                            i+=1
                            data[child.tag]=child.text
                    grandchildren=children.getchildren()
                    for gk in grandchildren:
                        data[gk.tag]=gk.text
                        datadict["row{0}".format(i)]=data
    
    data_frame=pd.DataFrame.from_dict(data=datadict, orient='index')
    return data_frame