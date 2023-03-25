from enum import Enum
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from utils.display_writer import DisplayWriter


class DisplayFontSize(int, Enum):
    FONT_SIZE_30 = (30,)
    FONT_SIZE_48 = (48,)
    FONT_SIZE_64 = (64,)
    FONT_SIZE_96 = 96


class TextDto(BaseModel):
    font_size: DisplayFontSize
    text: str


router = APIRouter()
display_writer = DisplayWriter()


@router.post("", summary="Create a sample", response_description="The created sample")
async def create_sample(text_dto: TextDto):
    print(text_dto.text)

    return jsonable_encoder(text_dto)
