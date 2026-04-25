from datetime import datetime
from zoneinfo import ZoneInfo


def convert_timezone(time_str: str, from_tz: str, to_tz: str) -> dict:
    # Определяем формат времени
    if time_str.count(":") == 2:
        input_format = "%H:%M:%S"
        output_format = "%H:%M:%S"
    else:
        input_format = "%H:%M"
        output_format = "%H:%M"
        time_str = time_str + ":00"  # добавляем секунды для парсинга

    # Парсим время с сегодняшней датой
    today = datetime.now().date()
    dt = datetime.strptime(f"{today} {time_str}", f"%Y-%m-%d {input_format}")

    # Конвертируем
    dt_from = dt.replace(tzinfo=ZoneInfo(from_tz))
    dt_to = dt_from.astimezone(ZoneInfo(to_tz))

    # Разница часовых поясов
    offset = dt_to.utcoffset() - dt_from.utcoffset()
    hours = int(offset.total_seconds() // 3600)
    minutes = int(abs(offset.total_seconds() % 3600) // 60)
    sign = "+" if hours >= 0 else ""
    offset_str = f"{sign}{hours:02d}:{minutes:02d}"

    return {
        "original_time": time_str.split(":")[0] + ":" + time_str.split(":")[1],
        "original_timezone": from_tz,
        "converted_time": dt_to.strftime(output_format),
        "converted_timezone": to_tz,
        "timezone_offset": offset_str
    }
