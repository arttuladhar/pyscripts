#!/usr/bin/python

import os
import configread
from time import sleep
import shutil
import datetime

while True:
    config    = configread.readconfigFile('FileDropper.config')
    src_dir   = config["SRC_DIR"]
    dest_dir  = config["DEST_DIR"]
    sleeptime = config["SLEEPTIME"]

    """
    Reading Configuration
    """
    if config["BATCH"]:
        batchsize = int(config["BATCH"])

    if config["EXTENSION"]:
       extension = config["EXTENSION"]
       filelist = [ files for files in os.listdir(src_dir) if extension in files ]
       #print "FileList: "
    else:
        filelist = [ files for files in os.listdir(src_dir) ]

    #print filelist
    print str(datetime.datetime.now())
    print "Running Scheduled Task"
    print "Number of Files in SourceDirectory : " + str(len(filelist))

    for files in filelist[:batchsize]:
        srcfile  = src_dir+"/"+files
        destfile = dest_dir+"/"+files

        print "Copying File"
        print "Source      : " + srcfile
        print "Destination : " + destfile

        shutil.move(src_dir+"/"+files,dest_dir)

    if len(filelist) == 0:
        print "No File in Source Directory"

    print "Sleeping"
    sleep(int(sleeptime))

print "Done"
