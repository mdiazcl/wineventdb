# wineventdb
It's a simple python script with an Windows EventID database.
It's quite simple, but I found it effective when you need quick ref during Threat Huntings.

It uses TinyDB (a json based database) for storage and query.

#### To install
```bash
pip install -r reqs.txt
```
If you want to install it as a process of your Operating System (at your own risk) simply execute the following command:
```bash
sudo ln -s $(pwd)/winevent.py /usr/local/bin/winevent
```



#### Usage
```python
python winevent.py <event_id>
```

#### Example
```bash
python winevent.py 4720
> 4720 - A user account was created
	(ref: https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4720)
```

Enjoy!
Or not... it's up to you :)
