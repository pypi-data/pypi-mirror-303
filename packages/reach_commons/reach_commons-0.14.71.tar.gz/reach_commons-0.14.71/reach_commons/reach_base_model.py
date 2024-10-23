from datetime import date, datetime, time

from pydantic import BaseModel
from pydantic.v1 import validator


class ReachBaseModel(BaseModel):
    def model_dump(self, *args, **kwargs):
        original_dict = super().model_dump(*args, **kwargs)

        def convert_value(value):
            if isinstance(value, datetime):
                return value.isoformat()
            elif isinstance(value, date):
                return value.isoformat()
            elif isinstance(value, time):
                return value.strftime("%H:%M:%S")
            elif isinstance(value, dict):
                return {k: convert_value(v) for k, v in value.items()}
            elif isinstance(value, list):
                return [convert_value(item) for item in value]
            return value

        return {key: convert_value(value) for key, value in original_dict.items()}


class ReachDeserializeBaseModel(BaseModel):
    @validator("*", pre=True, always=True)
    def deserialize_values(cls, value, field):
        if isinstance(value, str):
            try:
                if field.type_ == datetime:
                    return datetime.fromisoformat(value)
                elif field.type_ == date:
                    return date.fromisoformat(value)
                elif field.type_ == time:
                    return datetime.strptime(value, "%H:%M:%S").time()
            except ValueError:
                pass  # Handle the case where the string is not in the expected format
        return value
