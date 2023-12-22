import ddddocr
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
ocr = ddddocr.DdddOcr(show_ad=False, beta=True)


class Image(BaseModel):
    data: str


@app.post('/')
def main(body: Image):
    ocr_answer: str = ''
    attempts: int = 0

    while len(ocr_answer) < 4 and attempts < 100:
        ocr_answer = ocr.classification(body.data).strip()
        attempts += 1

    return {
      'msg': ocr_answer,
    }
