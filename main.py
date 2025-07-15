from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AccidentRequest(BaseModel):
    type: str

rules = {
    "후방추돌": "상대방 100% 과실 가능성이 높습니다. 사진과 블랙박스를 확보하세요.",
    "측면충돌": "과실 비율이 상황에 따라 달라집니다. 상대 차선 변경 여부를 확인하세요."
}

@app.post("/accident")
async def process_accident(req: AccidentRequest):
    result = rules.get(req.type, "해당 사고 유형은 아직 준비 중입니다.")
    return {"response": result}
