from pydantic import BaseModel

class TimeConvertRequest(BaseModel):
    time: str
    from_tz: str
    to_tz: str

class TimeConvertResponse(BaseModel):
    original_time: str
    original_timezone: str
    converted_time: str
    converted_timezone: str
    timezone_offset: str
