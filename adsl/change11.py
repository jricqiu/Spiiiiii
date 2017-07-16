import commands
import re
import datetime

while Ture:
	ADSL_BASH = 'adsl-stop;adsl-start'
	start_time = datetime.datetime.now()
	# (status, output) = subprocess.getstatusoutput(ADSL_BASH)
	(status, output) = commands.getstatusoutput(ADSL_BASH)
	if status == 0:
		(status, output) = commands.getstatusoutput('ifconfig')
		pattern = re.compile('ppp0' + '.*?inet.*?(\d+\.\d+\.\d+\.\d+).*?netmask', re.S)
		result = re.search(pattern, output)
		if result:
			ip = result.group(1)
			end_time = datetime.datetime.now()
			tt = end_time-start_time
			print('ip:%s---------%s'%(ip, tt))
