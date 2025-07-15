from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정
origins = ["https://placegroup.co.kr"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 사용자 요청 모델
class UserInfo(BaseModel):
    age: int
    income: int
    job: str
    region: str

# 지원금 데이터
support_programs = [
    {
        "title": "노인 복지 지원금",
        "amount": "월 20만원",
        "description": "65세 이상 어르신을 위한 생활안정 지원 제도입니다.",
        "category": "복지",
        "agency": "보건복지부",
        "url": "https://www.bokjiro.go.kr"
    },
    {
        "title": "저소득층 지원금",
        "amount": "월 30만원",
        "description": "연소득 3000만원 미만 가구에 지급되는 생활비 보조금입니다.",
        "category": "생활비",
        "agency": "기획재정부",
        "url": "https://www.gov.kr"
    },
    {
        "title": "농업인 지원금",
        "amount": "월 25만원",
        "description": "농업에 종사하는 국민을 위한 경영안정 지원금입니다.",
        "category": "농업",
        "agency": "농림축산식품부",
        "url": "https://www.mafra.go.kr"
    },
    {
        "title": "서울시 지역 지원금",
        "amount": "월 15만원",
        "description": "서울특별시 거주민을 위한 지역 생활지원금입니다.",
        "category": "지역",
        "agency": "서울특별시청",
        "url": "https://www.seoul.go.kr"
    }
]

# 지원 조건
def match_support(user: UserInfo):
    matched = []
    for program in support_programs:
        if program["title"] == "노인 복지 지원금" and user.age >= 65:
            matched.append(program)
        elif program["title"] == "저소득층 지원금" and user.income < 3000:
            matched.append(program)
        elif program["title"] == "농업인 지원금" and user.job == "농업":
            matched.append(program)
        elif program["title"] == "서울시 지역 지원금" and user.region == "서울":
            matched.append(program)
    return matched

@app.post("/support")
async def get_support_info(user: UserInfo):
    benefits = match_support(user)
    if not benefits:
        return {"message": "해당 조건에 맞는 지원금이 없습니다."}
    return {"support_benefits": benefits}
