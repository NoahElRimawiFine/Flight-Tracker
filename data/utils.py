from datetime import datetime

def converter(*, sample_dt: str):
    date_time_object = datetime.strptime(sample_dt, "%Y/%m/%d, %H:%M:%S")

    unix_time = date_time_object - datetime(1970,1,1)