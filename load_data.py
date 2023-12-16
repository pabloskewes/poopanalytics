from pathlib import Path

import pandas as pd


POOP_EMOJI = "💩"


def load_data(path: Path) -> pd.DataFrame:
    """Loads poop data from the given path and returns a pandas DataFrame"""
    lines = path.read_text().splitlines()
    lines = pd.Series([line for line in lines if POOP_EMOJI in line])
    splitted_data = lines.str.split(" - ", expand=True)
    datetimes = splitted_data[0].str.split(",", expand=True)
    user_and_message = splitted_data[1].str.split(": ", expand=True)

    data = pd.DataFrame(
        {
            "date": datetimes[0].str.strip(),
            "time": datetimes[1].str.strip(),
            "user": user_and_message[0].str.strip(),
            "message": user_and_message[1].str.strip(),
        }
    )
    return data


def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Processes the given data and returns a pandas DataFrame"""
    
    data = data.copy()
    data = data[data["message"] == POOP_EMOJI]
    
    data['date'] = pd.to_datetime(data['date'], format='%m/%d/%y')
    data['time'] = pd.to_datetime(data['time'], format='%I:%M %p')
    data['datetime'] = data['date'] + pd.to_timedelta(data['time'].dt.hour, unit='h') + pd.to_timedelta(data['time'].dt.minute, unit='m')
    

    return data
    
    