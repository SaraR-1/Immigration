#!/myenv/bin/python

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import json

'''
Function that parse a json input file
- Input:
    - data: file path
    - key: whether to force the type of the key or not. True as default
- Output:
    - dictionary
'''
def upload_data(data, key = True):
    res = json.load(open(data))
    if key:
        # the key "y" (year) and the values have to be a int --> transform it
        res = {k1: dict([int(k2), float(v2)] for k2, v2 in v1.items()) for k1, v1 in res.items()}
    else:
        # just the values have to be numeric (float cause le rate is not int) --> transform it
        res = {k1: dict([k2, float(v2)] for k2, v2 in v1.items()) for k1, v1 in res.items()}
    return(res)

'''
Function that parse a json input file - 
- Input:
    - data: file path. Input with structure: {k1: listv1, k2:listv2}
- Output:
    - dictionary
'''
def upload_data_list(data):
    res = json.load(open(data))
    res = {k1: [int(i) for i in v1] for k1, v1 in res.items()}

    return(res)

'''
Function to produce a single barplot for every year
- Input: 
    - data: dictionary with multiple keys: for each attribute (region - first key), 
    store the value for every year (second key)
    - years_list: list of sorted years to plot
    - x_label: string, label of axis x
    - y_label: string, label of axis x
    - path: list of string, where to save each result plot (if save == True), without the file extension
    - save: boolean variable, specify whether to save (True, default) or show (False) each result plot 
- Ouput:
    - multiple plots, one for every year in years_list
'''
def barplot_per_year(data, years_list, x_label, y_label, title, save = True, path = []):
    # Plot it!
    path = ["" for y in years_list]
    sns.set_style("whitegrid")
    sns.set_context({"figure.figsize": (10, 8)})
    temp = pd.DataFrame.from_dict(data)
    for y, p in zip(years_list, path):
        plt.figure()
        sns.barplot(y = temp.loc[y].values, x = temp.columns)

        plt.xticks(rotation=90)
        sns.despine(left=True)
        plt.xlabel(x_label, fontsize=12)
        plt.ylabel(y_label, fontsize=12)
        plt.legend(prop={'size':16})
        plt.title(title+str(y), fontsize = 16)
        if save == True:
            plt.savefig(p+".png")
        else:
            plt.show()            

def export_legend(legend, filename, expand=[-5,-5,5,5]):
    fig  = legend.figure
    fig.canvas.draw()
    bbox  = legend.get_window_extent()
    bbox = bbox.from_extents(*(bbox.extents + np.array(expand)))
    bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(filename, dpi="figure", bbox_inches=bbox)


'''
Function to produce a single lineplot for every region - every point of the line represent a single year
- Input: 
    - data: dictionary with multiple keys: for each attribute (region or zone - first key), 
    store the value for every year (second key) 
    - years_list: list of sorted years to plot
    - x_label: string, label of axis x
    - y_label: string, label of axis x
    - path: string, where to save the result plot (if save == True), without the file extension
    - save: boolean variable, specify whether to save (True, default) or show (False) the result plot 
    - palette: palette of colors to use - dictionary with structure {data_1: color_1, .., data_n: color_n}
- Ouput:
    - single lineplot, one for every region (keys in the data dictionary)
'''

def line_per_year(data, years_list, x_label, y_label, title, palette, countries_list = None, save = True,  path = "", key = True, preprocess = False, sep_legend = False):   
    if not preprocess:
        data = upload_data(data, key)
    if countries_list:
    	countries_stream = [x for x in countries_list if x in data.keys()] 
    else:
    	countries_stream = palette

    if type(palette) == list:
    	palette = {c: col for c, col in zip(countries_stream, palette)}
    sns.set_style("whitegrid")
    sns.set_context({"figure.figsize": (10, 8)})
    legend = []
    data_stream = data.keys()
    num = len(data_stream)
    for d in countries_stream:
        c = palette[d]
        if len(data[d]) == len(years_list):
            x_year = years_list
        # if our starting data are growth, not absolute for each year
        else:
            x_year = [str(y+1)+"-"+str(y) for y in years_list[:-1]]

        try:
            temp = [data[d][y] for y in x_year]
        except:
            temp = [data[d][y] for y in list(range(len(x_year)))]
        '''if isinstance(data[r], dict):
            temp = [data[r][y] for y in years_list]
            x_year = years_list
        else:
            temp = data[r]
            x_year = [str(y+1)+"-"+str(y) for y in years[:-1]]'''
        sns.pointplot(y = temp, x = x_year,label= d, color = c)
        if countries_list:
        	countries_name = pd.read_table("Data_final/country_name_coherence.csv", sep = "\t")
        	legend.append(mlines.Line2D([], [], color=c, markersize=15, label=countries_name[countries_name["iso3"] == d]["english name"].values[0].split(",")[0]))
        else:
        	legend.append(mlines.Line2D([], [], color=c, markersize=15, label=d))

    plt.xticks(rotation=45)
    sns.despine(left=True)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.title(title, fontsize = 16)
    if save == True:
        if sep_legend:
            plt.savefig(path+".png", bbox_inches='tight')
            lgd = plt.legend(handles = legend, prop={'size':14}, loc='upper center', bbox_to_anchor=(0, -0.1), fancybox=True, shadow=True, ncol = len(data))
            continent_name = title.split()[0]
            export_legend(lgd, "Temp_plot/legend_"+continent_name+"_"+x_label+".png")
        else:
            lgd = plt.legend(handles = legend, prop={'size':14}, loc='upper right', bbox_to_anchor=(1.6, 1.05), ncol=1)
            plt.savefig(path+".png", bbox_extra_artists=(lgd,), bbox_inches='tight')
    else:
        plt.show()
    plt.close()


def multiple_line_per_year(data, years_list, y_label, title, palette, countries_list = None, save = True,  path = "", key = True):
    data = json.load(open(data))
    data = {k1: {k2:[int(i) for i in v2] for k2, v2 in v1.items()} for k1, v1 in data.items()}
    for d in data:
    	c = d.replace(" ", "")
    	line_per_year(data[d], years_list, d, y_label, title+d , palette, countries_list, save = save, path = path+c, preprocess = True)


def stacked_barplot(data, years_list, x_label, y_label, title, save = True,  path = ""):
    data = upload_data_list(data)
    data_male = data["male"]
    data_female = data["female"]

    data_tot = [i+j for i, j in zip(data_male, data_female)]

    #Set general plot properties
    sns.set_style("whitegrid")
    sns.set_context({"figure.figsize": (10, 8)})

    fig, ax = plt.subplots()
    sns.barplot(y= data_tot, x = years_list, label = "Female",  color="r", alpha = .8)
    sns.barplot(y= data_male, x = years_list, label = "Male",  color="b", alpha = .8)
    sns.despine(left=True)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    lgd = plt.legend(prop={'size':16}, loc='upper right', bbox_to_anchor=(1.25, 1.05), ncol=1)
    plt.title(title, fontsize = 16)
    #plt.xticks(rotation=45)
    if save == True:
        plt.savefig(path+".png", bbox_extra_artists=(lgd,), bbox_inches='tight')
    else:
        plt.show()
    plt.close()