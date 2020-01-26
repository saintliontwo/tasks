"""task 3 / time 51:11.2"""

import datetime
import json
import pytz
import requests


def retrieve_dates(json_str):
    json_str = json.loads(json_str)
    return json_str


def convert_to_utc(date: str):
    fmt_dt = "%Y-%m-%d %H:%M"
    json_dt = datetime.datetime.strptime(date, fmt_dt)  # datetime entity
    eastern_dt = pytz.timezone('US/Eastern').localize(json_dt)  # US/Eastern tz
    utc_dt = eastern_dt.astimezone(pytz.utc)  # UTC tz
    return utc_dt.strftime("%Y-%m-%d %H:%M")


if __name__ == "__main__":
    json_str = '{"dt": ["2019-03-28 13:27", "2019-05-15 23:14", "2020-01-15 12:29"]}'  # task data
    URL = 'http://some_example.com/controller/get_data'  # task data
    utc_date_list = []
    dates = retrieve_dates(json_str)['dt']
    for date in dates:
        utc_date_list.append(convert_to_utc(date))
    data = {'VALS': utc_date_list}
    requests.post(url=URL, params=data)
