from PIL import Image, ExifTags, ImageOps
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession


def resize_image(filename: str, path_file: str, db: AsyncSession, user_id: UUID4):
    im = Image.open(path_file + '/' + filename)
    im = ImageOps.exif_transpose(im)
    rgb_im = im.convert('RGB')
    rgb_im.save(path_file + '/' + filename)
    size = (200, 200)
    im = Image.open(path_file + '/' + filename, mode="r")
    ImageOps.fit(im, size).save(path_file + '/' + str(size[0]) + "_" + filename)
