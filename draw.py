import sys
import matplotlib.pyplot as plt
import numpy as np
import re
import array
from math import log
from math import sqrt
from math import floor
import os
def distance(p0, p1):
    return sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
def main():
    if len(sys.argv) > 1:
        os.mkdir(sys.argv[1])
    listf = []

    for line in sys.stdin:
        nums = line.split()
        listf.append((int(nums[0]),int(nums[1]),nums[2]))

    
    ydim =  [ x[0] for x in listf]
    xdim1 = [ x[1] for x in listf]
    xdim2 = [ x[2] for x in listf] 
    lof = []
    for i in xrange(max(ydim)+1):
       lof.append([]) 
    for i in listf:
        lof[i[0]].append((i[1],i[2]))

    for cl in xrange(len(lof)):

        plt.ylim([-1,len(lof[cl])])
        for i in xrange(len(lof[cl])):
            plt.plot([lof[cl][i][0],lof[cl][i][1]],[i,i],'k-',linewidth=4,color="b", alpha=0.8)


        plt.title('Cluster {}'.format(cl))
        plt.xlabel("Position")
        plt.ylabel("Deletions")
        if(len(sys.argv) is 1):
            plt.savefig("newclusters/cl{}.png".format(cl)) 
        else:
            plt.savefig(sys.argv[1] + "/cl{}.png".format(cl))
        plt.clf()

        
main()
