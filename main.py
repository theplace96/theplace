from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInfo(BaseModel):
    age: int
    income: int
    job: str
    region: str

# 예시 지원금 규칙 (실제론 더 복잡할 수 있어요)
support_rules = [
    {
        "조건": lambda u: u.age >= 65,
        "혜택": "노인 복지 지원금: 월 20만원"
    },
    {
        "조건": lambda u: u.income < 3000,
        "혜택": "저소득층 지원금: 월 30만원"
    },
    {
        "조건": lambda u: u.job == "농업",
        "혜택": "농업인 지원금: 월 25만원"
    },
    {
        "조건": lambda u: u.region == "서울",
        "혜택": "서울시 지역 지원금: 월 15만원"
    }
]

@app.post("/support")
async def get_support_info(user: UserInfo):
    benefits = [rule["혜택"] for rule in support_rules if rule["조건"](user)]
    if not benefits:
        return {"message": "해당 조건에 맞는 지원금이 없습니다."}
    return {"support_benefits": benefits}
