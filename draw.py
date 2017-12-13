import sys
import matplotlib.pyplot as plt
import numpy as np
import re
import array
from math import log
from math import sqrt
from math import floor
import os


def main():
    if len(sys.argv) > 1:
        os.mkdir(sys.argv[1])
    listf = []

    for line in sys.stdin:
        nums = line.split()
        listf.append((int(nums[0]),int(nums[1]),nums[2]))
    lof = []
    maxydim = listf[0][0]
    for i in ydim:
        if i[0] > maxydim:
            maxydim = i[0]

    for i in xrange(maxydim+1):
       lof.append([]) 
    for i in listf:
        lof[i[0]].append((i[1],i[2]))

    for cl in xrange(len(lof)):
        if len(lof) is 0:
            continue
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
