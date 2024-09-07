# rpipywei

##Create .env file with congiguration:

```
USER=admin
PASSWORD=admin

REQUEST_URLS=https://worldtimeapi.org/api/timezone/Europe/Warsaw.txt,https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41
REQUEST_LIMIT=3
REQUEST_TIMEOUT=30
REQUEST_SLEEP=60
```

##Setup your cron job

`crontab -e`

```
5 * * * * cd /home/path_to_folder && /home/path_to_folder/.venv/bin/python main.py > /dev/null 2>&
```
