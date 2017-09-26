#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pi-model.py
#  
#  Copyright 2016 David Kohen 
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#~ "Hardware Revision Code from cpuinfo","Model and PCB Revision","RAM", Notes
import os
import subprocess

# cat /proc/device-tree/model

models = {
#~ Revision	Release Date	Model	        PCB Revision	Memory	            Notes
"Beta":	    ["Q1 2012", "Pi B (Beta)",             "?",     "256 Mb",           "Beta Board"],
"0002":	    ["Q1 2012",	"Pi B	",                 "1.0",	"256 Mb",           ""],
"0003":	    ["Q3 2012",	"Pi B (ECN0001)",          "1.0",  	"256 Mb",   	    "Fuses mod and D14 removed"],
"0004":	    ["Q3 2012",	"Pi B",                    "2.0",	"256 Mb",   	    "Sony"],
"0005":	    ["Q4 2012",	"Pi B",                    "2.0",  	"256 Mb",	        "Qisda"],
"0006":	    ["Q4 2012",	"Pi B",                    "2.0",	"256 Mb",   	    "Egoman"],
"0007":	    ["Q1 2013",	"Pi A",                    "2.0",  	"256 Mb",   	    "Egoman"],
"0008":	    ["Q1 2013",	"Pi A",                    "2.0",	"256 Mb",       	"Sony"],
"0009":	    ["Q1 2013",	"Pi A",                    "2.0",  	"256 Mb",	        "Qisda"],
"000d":	    ["Q4 2012",	"Pi B",                    "2.0",  	"512 Mb",         	"Egoman"],
"000e":	    ["Q4 2012",	"Pi B",                    "2.0",  	"512 Mb",	        "Sony"],
"000f":	    ["Q4 2012",	"Pi B",                    "2.0",	"512 Mb",   	    "Qisda"],
"0010":	    ["Q3 2014",	"Pi B+",                   "1.0",   "512 Mb",   	    "Sony"],
"0011":	    ["Q2 2014",	"Pi Compute Module 1",     "1.0",	"512 Mb",       	"Sony"],
"0012":	    ["Q4 2014",	"Pi A+",                   "1.1",  	"256 Mb",   	    "Sony"],
"0013":	    ["Q1 2015",	"Pi B+",                   "1.2",	"512 Mb",   	     "?"],
"0014":	    ["Q2 2014",	"Pi Compute Module 1",     "1.0",  	"512 Mb",       	"EMbest"],
"0015":	    ["?",	    "Pi A+",                   "1.1",	"256 Mb / 512 Mb",	"EMbest"],
"a01040":	["Unknown",	"Pi 2 Model B",            "1.0",  	"1 GB",          	"Unknown"],
"a01041":	["Q1 2015",	"Pi 2 Model B",            "1.1",	"1 GB",	            "Sony"],
"a21041":	["Q1 2015",	"Pi 2 Model B",            "1.1",  	"1 GB",         	"EMbest"],
"a22042":	["Q3 2016",	"Pi 2 Model B (BCM2837)",  "1.2",  	"1 GB",         	"EMbest"],
"900092":	["Q4 2015",	"Pi Zero",                 "1.2",	"512 Mb",       	"Sony"],
"900093":	["Q2 2016",	"Pi Zero",                 "1.3",  	"512 Mb",       	"Sony"],
"920093":	["Q4 2016?","Pi Zero",                 "1.3",	"512 Mb",       	"EMbest"],
"9000c1":	["Q1 2017",	"Pi Zero W",               "1.1",  	"512 Mb",       	"Sony"],
"a020a0":	["Q1 2017",	"Compute Module 3 +Lite",  "1.0"	"1 GB",	            "Sony"],
"a02082":	["Q1 2016",	"Pi 3 Model B",            "1.2",  	"1 GB",         	"Sony"],
"a22082":	["Q1 2016",	"Pi 3 Model B",            "1.2",	"1 GB",         	"EMbest"],
};


def main(args):
    if (len(args) == 1):        
        try:
            revision = subprocess.check_output(["grep","Revision","/proc/cpuinfo"])
        except subprocess.CalledProcessError as grepexc:                                                                                                   
            print ("Error getting revision number (not a Pi?)")
            return 1
        revision = revision.split()[2]
    else:
        revision = args[1]
    try:
        model = models[revision]
    except:
        model = ["?","Unknown","?","?","?"]
    print(str(model[1])+" v."+str(model[2])+" "+str(model[4])+" (Revision: "+revision+")" )
    if (revision == "0015"):  # handle exception whre 0015 has two different possible memory sizes
        # get the memory size to help resolve 0015 issue
        try:
            mem = subprocess.check_output(["grep","MemTotal","/proc/meminfo"])
            mem = int(mem.split()[1])/1024 # turn it into Mb
            memStr = "Reported usable RAM is "+str(mem)+"Mb";
        except subprocess.CalledProcessError as grepexc:                                                                                                   
            print ("Can't get memory size")
        print("* Note: for this board RAM can be 256Mb or 512Mb")
        print(memStr)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))   
    
    
