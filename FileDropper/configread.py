#!/usr/bin/python

def readconfigFile(filename):
    try:
        #print "Reading Configuration File"
        config = open( filename, 'r')
        #print "FileName: " + config.name
    
        config_vars = {}
        for line in iter(config):
            if (line[0] == "#"):
                print line
            elif (line != ""):
                line = line.strip();
                key_val = line.split("=")
                config_vars.update({key_val[0]:key_val[1]});
    except IOError as e:
        print "I/O Exception : {0} : {1}".format(e.errno,e.strerror)
        
    config.close()
    if config_vars:
        return config_vars
    else: 
        return
#End_readconfigFile
