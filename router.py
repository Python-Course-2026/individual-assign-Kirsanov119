from fastapi import APIRouter, HTTPException
from schemas import TimeConvertRequest, TimeConvertResponse
from service import convert_timezone

router = APIRouter(prefix="/timezone", tags=["timezone"])


@router.post("/convert", response_model=TimeConvertResponse)
def convert_time(data: TimeConvertRequest):
    if not data.time.strip():
        raise HTTPException(status_code=400, detail="Время не может быть пустым")
    if not data.from_tz.strip():
        raise HTTPException(status_code=400, detail="Исходный часовой пояс не может быть пустым")
    if not data.to_tz.strip():
        raise HTTPException(status_code=400, detail="Целевой часовой пояс не может быть пустым")

    result = convert_timezone(data.time, data.from_tz, data.to_tz)
    return result
