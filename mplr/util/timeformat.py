def time_format(time):
    total_seconds = int(time)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    if minutes < 10:
        formatted_duration = f"{minutes}:{seconds:02}"
    else:
        formatted_duration = f"{minutes:02}:{seconds:02}"
    return formatted_duration
