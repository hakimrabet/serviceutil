#!/usr/bin/env python

import os;
import json;
import sys;

directory="/etc/init.d";
sdata_list=[];
white_list=['mysql','apache','snmp','rsyslog','gsm-utils','cron','oracle','postgre','pg','java','catalina','tomcat','mariadb','server','agent']
if(len(sys.argv)<2):
    for serviceName in os.listdir(directory):
        stat = -1;
        stat = os.system('service '+serviceName+' status  > /dev/null 2>&1 ');
        # with open(os.devnull, 'wb') as devnull:
        #     stat=call(['service', serviceName, 'status'], stdout=devnull,stderr=devnull);
        if stat == 0:
            serviceStatus='running';
        else:
            serviceStatus='stopped';

        if bool([ele.lower() for ele in white_list if (ele in serviceName.lower())]):
            sdata_list.append({"{#SNAME}": serviceName, "{#SSTATUS}": serviceStatus});


    print(json.dumps({"data": sdata_list}, indent=4));
else:
    arg1=sys.argv[1];
    stat = os.system('service ' + arg1 + ' status  > /dev/null 2>&1 ');
    serviceStatus="";
    if stat == 0:
        serviceStatus='running';
    else:
        serviceStatus='stopped';
    print(serviceStatus);
