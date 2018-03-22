import sys
import matplotlib.pyplot as plt
import numpy as np
import re
import array
from math import log
from math import sqrt
from math import floor
import os
import pathlib
class interval:
    def __init__(self,i1,i2):
        self.start = i1
        self.end = i2
    def __repr__(self):
        return "{}, {}".format(self.start,self.end)
class variation:
    def __init__(self,ch,list_of_intervals):
        self.ch = ch
        self.il =list_of_intervals
    def __repr__(self):
        return "{}".format(self.il)
    def distance(self,other):
        return abs(other.il[0].start - self.il[0].end)

def add_sv(dic,cluster,sv):
    if cluster not in dic:
        dic[cluster] = []
    dic[cluster].append(sv)

def main():
    if len(sys.argv) < 5:
        print("GB")
        return
    
    pathlib.Path(sys.argv[1]).mkdir(parents=True,exist_ok=True)
    int_count = int(sys.argv[2])
    colors = sys.argv[3].split(":")

    
    listv = {}
    for line in sys.stdin:
        nums = line.split()
        iter = 1
        il = []
        while iter < len(nums)-1:
            il.append(interval(int(nums[iter]),int(nums[iter+1])))
            iter+=2
        add_sv(listv,nums[-1],variation(nums[0],il))
    

    for ll in listv.values():
        ll.sort(key= lambda x:x.il[0].start)
    count = 0
#    plt.xlim([97959560, 97991129])
#    plt.ylim([-1,len(listv)])
    for ll in listv.values():
        first = ll[0]
        break


    cl = 1
    for ll in listv.values():

        for var in ll:
            for i in range(len(var.il)):
            #    print(var.il[i],count)
                plt.plot([var.il[i].start,var.il[i].end],[count,count],"-",linewidth=4,c=colors[i])
            count+=1
        var = ll[-1]
        
        count+=10

        if( first.distance(var) > int(sys.argv[4])):

            plt.title('Cluster {}'.format(cl))
            plt.xlabel("Position")
            plt.ylabel("Deletions")
            plt.savefig(sys.argv[1] + "/cl{}.png".format(cl))
            plt.clf()
            cl+=1
            first=var    
            count = 0
main()
