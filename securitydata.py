# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:24:54 2021
Updated on Tuesday March 9, 2021
@author: inter
"""

import csv
from random import randint, uniform
import uuid
#vh is vanetheaders, to simplify the generator
vh = {
    0:'UID',
    1:'baseline', #this is either 2 or 3
    2:'reputation', #2 to 3 is typical unless under attack
    3:'rank', #these are low .3 is typical unless under attack, delay lessens, volume and spoofing increase
    4:'duplicateaddress', #indicates spoofing 0 to 1
    5:'volumefactor', #factor of actual/capacity
    6:'delayfactor', #factor expected - actual/expected
    7:'injectioncontent', #give range as 0 to 1.0
    8:'knownattackpattern', #more sure give range as 0 to 1.0
    9:'anomalyattackpattern', #less sure give range as 0 to .9
    10:'lasttrafficdensity', # 1/s where s is spacing center to center, in feet 40 is probably good 20 is possible typical could be .01 to .05
    11:'timestamp'
    }
#iih is industrialiotheaders, to simplify the generator
iih = {
       0:'UID',
       1:'origintype',
       2:'eventtype',
       3:'attackvalue', #logically bound to the eventtype and other factors
       4:'repeatedsuspectopsalltimemins', #bound to the uid
       5:'repeatedsuspectopsalltimehours',
       6:'repeatedsuspectopsinalltimedays',
       7:'timestamp'
       }
#ot is origintype, which gives what caused event
ot = {
      0:'internal',
      1:'application',
      2:'system',
      3:'network',
      4:'script',
      5:'macro',
      6:'user'
      }
et = {
      0:'highcpufactor', #of capacity reduced from usage by multiplying by .75 (at threshold of .8) typical .6 to .8
      1:'highdiskwritefactor', #of write speed capability similar to 0 typical .6 to .8
      2:'highdiskreadfactor', #of read speed capability similar to 0 typical .6 to .8
      3:'highnetworkfactor', #of network throughput capacity similar to 0 typical .6 to .8
      4:'delayedtraffic', #(expected - actual)/expected values typical .8 to 1.0
      5:'lowwrite', #(expected-actual)/expected values typical unused if used multiply by .5 to get values .4 to .5
      6:'highstoragefactor', #value .5
      7:'unreadablesignalfile', #used to detect ransomware encryption attack value .75
      8:'missingfile', #many types of malware remove files value .5
      9:'missingdata', #some types of malware remove data from files value .5
      10:'missingapplication', #rare types of malware remove crucial applications value .5
      11:'unexpecteddatachange', #when protected data is altered by an application not on whitelist value .85
      12:'datamismatch', #changes in expected format may indicate breach of some kind value .5
      13:'corruption', #some malware alters physical hardware addressing, causing corrupted data, value .7
      14:'unexpectedsystemaccess', #malware and hackers may alter system settings, value .5
      15:'knownmalware', #suspect filenames, hashes, etc. could allow detection, value 1
      16:'knownsuspectaddress', # value 1
      17:'duplicateaddress', #typical of spoofing value 1
      18:'suspectaccount', #account which shouldn't have had access value 1
      19:'suspectedexploit', #takes advantage of potential vulnerability value .75
      20:'nosuspect', #normal activity polled or randomly detected value 0
      21:'suspectfile', #file flagged as suspect by cybersecurity value .75
      22:'suspectprocess', #process flagged as suspect by cybersecurity value .75
      23:'dataleak', #protected data is sent across network value .85
      24:'suspectedinjection', #web application's behavior is suspiciously altered by user input or script typical value .85
      25:'custom', #used to store data for other security programs used to extend suite typical value .5
      26:'suspiciousactivity', #flagged unwarranted access to protected data, odd setup procedures and installation, etc. value .85
      27:'newlog' #starting new log for security program value 0
      }
#system specs headers for iih
iissh = {
    'cpucapacity':0,
    'networkcapacity':0,
    'diskwritecapability':0,
    'diskreadcapability':0,
    'expectedperkbthroughput':0,
    'expectedperkbwrite':0
    }
class dataconstructor():
    def csvwrite(self,filename:str, header:list, valuetable:list):
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(valuetable)
    def constructVANETdata(self,rows:int,filename):
        global vh
        timestamp1 = 1613594662
        vvaluetable = []
        vheader = [vh[0],
                   vh[1],
                   vh[2],
                   vh[3],
                   vh[4],
                   vh[5],
                   vh[6],
                   vh[7],
                   vh[8],
                   vh[9],
                   vh[10],
                   vh[11]]
        rowcount = 0
        #DONE while loop
        #for row in range(0, rows):
        while rowcount <= rows:
            
            rn = randint(0,518400) #minute by minute in a year
            if rn in range(509756,511484): #rangestart	rangeend
                #spoof (with possible volumetric to trick rank)
                spoofrange = randint(18, 240) #18 minutes to 4 hours average attack ranges for effective attacks
                unq = uuid.uuid4()
                for s in range(0, spoofrange):
                    timestamp1 = timestamp1 + 60
                    vvaluetable.append([unq, #0
                                        randint(2,3), #1 baseline
                                        randint(2,5), #2 reputation
                                        uniform(.3,.5), #3 rank
                                        1, #4 duplicateaddress
                                        uniform(0.0,1.0), #5 volumefactor
                                        0, #6 delay factor
                                        uniform(0,.5), #7
                                        uniform(0.0,1.0), #8
                                        0, #9
                                        uniform(.1,.5), #10
                                        timestamp1 #11
                                        ])
                    rowcount = rowcount + 1
            elif rn in range(511485,513213):
                #volumetric (no spoof)
                volrange = randint(18, 240)
                unq = uuid.uuid4()
                for v in range(0,volrange):
                    timestamp1 = timestamp1 + 60
                    vvaluetable.append([unq, #0
                                        randint(2,3), #1
                                        randint(2,3), #2
                                        uniform(.3,.4), #3
                                        0, #4
                                        uniform(0.8,1.0), #5
                                        0, #6
                                        uniform(0,.5), #7
                                        uniform(0.0,1.0), #8
                                        0, #9
                                        uniform(.1,.5), #10
                                        timestamp1 #11
                                        ])
                    rowcount = rowcount + 1
            elif rn in range(513214,514942):
                #delay (no spoof)
                delrange = randint(18, 240)
                unq = uuid.uuid4()
                for d in range(0,delrange):
                    timestamp1 = timestamp1 + 60
                    vvaluetable.append([unq, #0
                                        randint(2,3), #1
                                        randint(2,3), #2
                                        uniform(.2,.3), #3
                                        0, #4
                                        0, #5
                                        uniform(.8,1.0), #6
                                        uniform(0,.5), #7
                                        uniform(0.0,1.0), #8
                                        0, #9
                                        uniform(.1,.5), #10
                                        timestamp1 #11
                                        ])
                    rowcount = rowcount + 1
            elif rn in range(514943,516671):
                #exploit
                exrange = randint(4, 300) #more variation in exploit similar to iiot data
                unq = uuid.uuid4()
                for ex in range(0,exrange):
                    timestamp1 = timestamp1 + 60
                    vvaluetable.append([unq, #0
                                        randint(2,3), #1
                                        randint(2,3), #2
                                        uniform(.2,.4), #3
                                        0, #4
                                        0, #5
                                        0, #6
                                        uniform(0,.5), #7
                                        0, #8
                                        uniform(0.6,0.9), #9
                                        uniform(.1,.5), #10
                                        timestamp1 #11
                                        ])
                    rowcount = rowcount + 1
            elif rn in range(516672,518400):
                #injection
                injrange = randint(4, 240) #allow for shorter attacks since injection may not do much on its own
                unq = uuid.uuid4()
                for n in range(0,injrange):
                    timestamp1 = timestamp1 + 60
                    vvaluetable.append([unq, #0
                                        randint(2,3), #1
                                        randint(2,3), #2
                                        uniform(.2,.4), #3
                                        0, #4
                                        0, #5
                                        0, #6
                                        uniform(.7,1.0), #7
                                        uniform(.7,1.0), #8
                                        0, #9
                                        uniform(.1,.5), #10
                                        timestamp1 #11
                                        ])
                    rowcount = rowcount + 1
            else:
                timestamp1 = timestamp1 + 60
                unq = uuid.uuid4()
                vvaluetable.append([unq, #0
                                    3, #1
                                    3, #2
                                    uniform(.3,.37), #3
                                    0, #4
                                    0, #5
                                    0, #6
                                    0, #7
                                    0, #8
                                    0, #9
                                    uniform(.1,.5), #10
                                    timestamp1 #11
                                    ])
                rowcount = rowcount + 1
        self.csvwrite(filename,vheader,vvaluetable)
    def constructIIoTdata(self,rows:int,filename):
        global iissh
        global iih
        global ot
        global et
        timestamp1 = 1613594662
        va = 0
        vh = 0
        vd = 0
        da = 0
        dh = 0
        dd = 0
        mi = 0
        mh = 0
        md = 0
        mw = 0
        mwh = 0
        mwd = 0
        ea = 0
        eh = 0
        ed = 0
        iheader = [iih[0],
                   iih[1],
                   iih[2],
                   iih[3],
                   iih[4],
                   iih[5],
                   iih[6],
                   iih[7]]
        ivaluetable = []
        rowcount =  0
        while rowcount <= rows:
            rn = randint(0,518400)
            
            '''
            iih = {
       0:'UID',
       2:'origintype',
       3:'eventtype',
       4:'attacklikelihood', #logically bound to the eventtype and other factors
       5:'repeatedsuspectopsalltimemin', #bound to the uid
       6:'repeatedsuspectopsalltimehours',
       7:'repeatedsuspectopsalltimedays',
       8:'timestamp'
       }
            '''
            if rn in range(509756,511484): #rangestart	rangeend
                #volumetric
                volrange = randint(18,240)
                unq = uuid.uuid4()
                for v in range(0, volrange):
                    timestamp1 = timestamp1 + 60
                    va = va + 1
                    vh = va/60 #error in previous data sets
                    vd = vh/24
                    ivaluetable.append([unq,ot[3],et[3],uniform(.6,.8),va,vh,vd,timestamp1])
                    rowcount = rowcount + 1
            elif rn in range(511485,513213):
                #delay
                delrange = randint(18, 240)
                unq = uuid.uuid4()
                for d in range(0,delrange):
                    timestamp1 = timestamp1 + 60
                    da = da + 1
                    dh = da/60
                    dd = dh/24
                    ivaluetable.append([unq,ot[3],et[4],uniform(.6,.8),da,dh,dd,timestamp1])
                    rowcount = rowcount + 1
            elif rn in range(513214,514942):
                #malware
                malrange = randint(18,240)
                unq = uuid.uuid4()
                for m in range(0, malrange):
                    timestamp1 = timestamp1 + 60
                    mw = mw + 1
                    mwh = mw/60
                    mwd = mwh/24
                    ivaluetable.append([unq,ot[1],et[15],1, mw, mwh, mwd, timestamp1])
                    rowcount = rowcount + 1
            elif rn in range(514943,516671):
                #malicious insider
                insrange = randint(18,240)
                unq = uuid.uuid4()
                for ins in range(0, insrange):
                    timestamp1 = timestamp1 + 60
                    mi = mi + 1
                    mh = mi/60
                    md = mh/24
                    #originuid, origintype, eventtype, attackvalue, repeat1, repeat2, repeat3, time
                    ivaluetable.append([unq,ot[6],et[26],uniform(.4,.6), mi, mh, md, timestamp1])
                    rowcount = rowcount + 1
            elif rn in range(516672,518400):
                #exploit
                unq = uuid.uuid4()
                exrange = randint(4, 480) #slight variation in order to test classifier data, exploits do vary
                for ex in range(0, exrange):
                    timestamp1 = timestamp1 + 60
                    ea = ea + 1
                    eh = ea/60
                    ed = eh/24
                    ivaluetable.append([unq,ot[randint(1,5)], et[19],uniform(.5,.8),ea,eh,ed, timestamp1])
                    rowcount = rowcount + 1
            else:
                #this is normal
                timestamp1 = timestamp1 + 60
                ivaluetable.append([uuid.uuid4(),ot[randint(0,6)],et[20],0,0,0,0,timestamp1])
                rowcount = rowcount + 1
        self.csvwrite(filename,iheader,ivaluetable)
def pause():
    input()
def main():
    dcon = dataconstructor()
    dcon.constructIIoTdata(43200, "iiot10.csv")
    dcon.constructVANETdata(57600, "vanet10.csv")
    print("done")
    pause()
if __name__=="__main__":
    main()

