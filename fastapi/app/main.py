from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse

app = FastAPI()
# 테스트하고 싶은 ALB 경로에 맞춰 prefix만 수정하세요. (예: "/test", "/api", "/auth")
router = APIRouter(prefix="")

@app.get("/", response_class=HTMLResponse)
async def debug_path(request: Request):
    # f-string을 사용하여 현재 접속된 실제 경로를 동적으로 출력합니다.
    current_path = request.url.path
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>ALB Routing Test</title>
            <style>
                body {{ font-family: sans-serif; text-align: center; padding: 50px; line-height: 1.6; }}
                .status-card {{ border: 2px solid #4CAF50; padding: 20px; display: inline-block; border-radius: 10px; }}
                .path-text {{ color: #e91e63; font-weight: bold; font-size: 1.5rem; }}
            </style>
        </head>
        <body>
            <div class="status-card">
                <h1>✅ ALB 라우팅 검증 성공</h1>
                <p>현재 FastAPI가 인식하고 있는 접속 경로는:</p>
                <p class="path-text">{current_path}</p>
                <hr>
                <p>이 메시지가 보인다면 <b>ALB Path Routing</b> 설정이 정상입니다.</p>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

app.include_router(router)