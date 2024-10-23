from typing import Optional

from pydantic import BaseModel


class NeutrinoTask(BaseModel):
    task_name: str
    task_id: str
    status: str
    threshold: Optional[int] = 1
    threshold_unit: Optional[str] = 'minutes'
    additional_data: Optional[dict[str, str]] = {}
    timestamp: Optional[str] = ''
    type: Optional[str] = ''
    runner: Optional[str] = '',
    application: Optional[str] = ''
    host: Optional[str] = ''
