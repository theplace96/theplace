from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "🚗 안녕하세요! 교통사고 진행 도우미입니다."}

@app.get("/rule")
def rule_example(accident_type: str = "접촉사고"):
    if accident_type == "접촉사고":
        return {"result": "과실 비율 5:5 또는 6:4 가능성이 높습니다."}
    elif accident_type == "신호위반":
        return {"result": "과실 비율 8:2 이상으로 예상됩니다."}
    return {"result": "알 수 없는 사고 유형입니다."}
