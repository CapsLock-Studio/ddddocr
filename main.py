import ddddocr
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    data: str


@app.post('/')
def main(body: Image):
    ocr_answer: str = ''
    ocr = ddddocr.DdddOcr(show_ad=False, beta=True)

    while len(ocr_answer) < 4:
        ocr_answer = ocr.classification(body.data).strip()

    return {
      'msg': ocr_answer,
    }
