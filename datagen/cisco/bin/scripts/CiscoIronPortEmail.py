import time,sys,os,traceback,random

## Define the events per second
EPS = 2

## Get common app vars, IPS's, sigs, etc. 
libPath = os.path.join(os.environ["SPLUNK_HOME"], 'etc','apps','bd-labs')

# Initialze vars

## Get required log samples 
log_sample  = open(os.path.join(os.environ["SPLUNK_HOME"], 'etc','apps','cisco','bin','data','cisco_esa.log'),'r').readlines()


## Define output log
log_out = open(os.path.join(os.environ["SPLUNK_HOME"], 'etc','apps','cisco','logs','ironport_mail.log'),'w')

def getCurrentEvent(evt):
	ts = time.strftime('%a %b %d %X %Y')
	line =  str(ts) + evt[24:]
	return line
	

while True:
	e = 0
	for line in log_sample:
		if e < EPS:
			l = getCurrentEvent(line)
			log_out.writelines(l)
			log_out.flush()	
			e = e + 1
		else:
			e = 0 
			l = getCurrentEvent(line)
			log_out.writelines(l)
			log_out.flush()	
			time.sleep(1)


