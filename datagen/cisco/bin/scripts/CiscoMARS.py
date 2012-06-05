from datetime import date, timedelta
import time,sys,os,traceback,random

## Define the events per second
EPS = 2

## Get common app vars, IPS's, sigs, etc. 
libPath = os.path.join(os.environ["SPLUNK_HOME"], 'etc','apps','bd-labs')

# Initialze vars
int_ips = open(os.path.join(libPath,'data','internal')).readlines()
ext_ips = open(os.path.join(libPath,'data','external')).readlines()


## Get required log samples 
log_sample  = open(os.path.join(os.environ["SPLUNK_HOME"], 'etc','apps','cisco','bin','data','cs_mars.sample'),'r').readlines()


## Define output log
log_out = open(os.path.join(os.environ["SPLUNK_HOME"], 'etc','apps','cisco','logs','rm-6050-605-1273214234_2010-05-07-06-11-44_2010-05-07-06-40-00'),'w')

def getCurrentEvent(evt):
	dest = int_ips[random.randint(0,len(int_ips)-1)].replace("\n","")
	src = ext_ips[random.randint(0,len(ext_ips)-1)].replace("\n","")
	today = date.today()
	yest = today-timedelta(days=1)
	yest = yest.strftime('%m/%d/%Y')
	clock = time.strftime(' %X')
	ts = yest + clock
	line = "404897'" + ts + evt[26:].replace('###DESTIP###',dest).replace('###SRCIP###',src)
	return line

def run():
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

run()
