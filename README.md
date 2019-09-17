# serviceutil

## service utility for zabbix monitoring system to discover services and give me status of services in python  

put it the python script in directory  /usr/local/etc/externalscripts/

    chmod +x ServiceUtil.py
Add UserParameter in zabbix agent configuration ex in : cd /usr/local/etc/zabbix_agentd.conf 
or make new file in /usr/local/etc/zabbix_agentd.conf.d/ 

    UserParameter=services.discovery,python /usr/local/shbk/etc/externalscripts/services_discovery.py
    UserParameter=services[*],python /usr/local/shbk/etc/externalscripts/services_discovery.py $1
    
the first One is for discovery the services and select them with well known Ones. use for discovery
and the second line is for to give me the status of one service use for item prototype
