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

#~ "Hardware Revision Code from cpuinfo","Model and PCB Revision","RAM"
import os
import subprocess
models = {
"0002":    ["Model B Rev 1",                                  "256MB"],
"0003":    ["Model B Rev 1 ECN0001 (no fuses, D14 removed)",  "256MB"],
"0004":    ["Model B Rev 2",                                  "256MB"],
"0005":    ["Model B Rev 2",                                  "256MB"],
"0006":    ["Model B Rev 2",                                  "256MB"],
"0007":    ["Model A",                                        "256MB"],
"0008":    ["Model A",                                        "256MB"],
"0009":    ["Model A",                                        "256MB"],
"000d":    ["Model B Rev 2",                                  "512MB"],
"000e":    ["Model B Rev 2",                                  "512MB"],
"000f":    ["Model B Rev 2",                                  "512MB"],
"0010":    ["Model B+",                                       "512MB"],
"0013":    ["Model B+",                                       "512MB"],
"0011":    ["Compute Module",                                 "512MB"],
"0014":    ["Compute Module (Embest, China)",                 "512MB"],
"0012":    ["Model A+",                                       "256MB"],
"0015":    ["Model A+ (Embest, China)*",                      "256MB"],
"0015":    ["Model A+ (Embest, China)*",                      "512MB"],
"a01041":  ["Pi 2 Model B v1.1 (Sony, UK)",                  "1024MB"],
"a21041":  ["Pi 2 Model B v1.1 (Embest, China)",             "1024MB"],
"a22042":  ["Pi 2 Model B v1.2",                             "1024MB"],
"900092":  ["PiZero v1.2",                                    "512MB"],
"900093":  ["PiZero v1.3",                                    "512MB"],
"a02082":  ["Pi 3 Model B  (Sony, UK)"	,                    "1024MB"],
"a22082":  ["Pi 3 Model B (Embest, China)",                  "1024MB"],
};

def main(args):
    try:
        revision = subprocess.check_output(["grep","Revision","/proc/cpuinfo"])
    except subprocess.CalledProcessError as grepexc:                                                                                                   
        print "Error getting revision number (not a Pi?)" 
        return 1       
    revision = revision.split()[2]
    try:
        model = models[revision]
    except:
        model = ["Unknown model","unknown"]
    print(str(model[0])+" (Revision: "+revision+")" )
    if (revision == "0015"):  # handle exception whre 0015 has two different possible memory sizes
        # get the memory size to help resolve 0015 issue
        try:
            mem = subprocess.check_output(["grep","MemTotal","/proc/meminfo"])
            mem = int(mem.split()[1])/1024 # turn it into Mb
            print ("Reported usable RAM is "+str(mem)+"Mb")
        except subprocess.CalledProcessError as grepexc:                                                                                                   
            print "Can't get memory size"
        print("* Note: for this board RAM can be 256Mb or 512Mb")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
