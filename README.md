# rpipywei

The simple script which checks the internet connection requesting the list of urls.
If the connection is lost, the script reboots HUAWEI router.
You can install it to Raspberry Pi computer.


## Clone the repository

```
git clone git@github.com:AleksandrIvin/rpipywei.git
cd rpipywei
```

## Create the virtual environment

```
python -m venv .venv
```

## Instal the python packages

```
python -m pip install -r requirements.txt
```

## Create .env file with congiguration variables:

```
HW_LOGIN=admin
HW_PASSWORD=admin

REQUEST_URLS=https://worldtimeapi.org/api/timezone/Europe/Warsaw.txt,https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41
REQUEST_LIMIT=3
REQUEST_TIMEOUT=30
REQUEST_SLEEP=60
```

## Setup your cron job

`crontab -e`

```
5 * * * * cd /home/path_to_folder && /home/path_to_folder/.venv/bin/python main.py > /dev/null 2>&
```
