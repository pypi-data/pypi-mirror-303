from pydantic import BaseModel, Field


class Config(BaseModel):
    max_img_width: int = Field(description="maximum image with in px", default=None)
    use_custom_title: bool = Field(
        description="weather use predefined TOC in titles.txt", default=False
    )
    disable_image: bool = Field(description="disable image extraction", default=False)
    disable_color: bool = Field(
        description="prevent adding html tags with colors", default=False
    )
    disable_escaping: bool = Field(
        description="prevent escaping of characters", default=False
    )
    disable_notes: bool = Field(description="do not add presenter notes", default=False)
    enable_slides: bool = Field(description="add slide deliniation", default=True)
