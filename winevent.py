#!/usr/bin/python
base_url = 'https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID={code}'

from tinydb import TinyDB, Query
import sys, logging

class LogEvent():
	title = ''
	eid = ''
	link = ''

def get_info(wineventid):
	db = TinyDB('./winevents.json')
	qeng = Query()
	log = LogEvent()

	res = db.search(qeng.id == int(wineventid))
	if len(res) == 0:
		log.title = 'Not found'
		log.link = 'Try https://www.google.com/?q=Windows+event+id+'+wineventid
	else:
		log.title = res[0]['description']
		log.link = base_url.format(code = wineventid)
	
	log.eid = wineventid
	
	return log

## Checks
if len(sys.argv) != 2:
	logging.error("Solo se acepta 1 parametro, el ID del evento...")
	exit()
if not str(sys.argv[1]).isdigit():
	logging.error("El primer parametro debe ser un numero...")
	exit()
else:
	winevent = sys.argv[1]

eventInfo = get_info(winevent)
print "\n{0} - {1} \n\t(ref: {2})\n".format(eventInfo.eid, eventInfo.title, eventInfo.link)