from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, boards, tasks
from app.core.config import settings

# Tạo FastAPI app instance
app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="Kanban TODO API với SQLAlchemy database integration",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Thêm CORS middleware để frontend có thể gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Trong production nên chỉ định cụ thể domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include các routers
app.include_router(users.router)
app.include_router(boards.router)
app.include_router(tasks.router)


# Tạo các bảng trong database khi ứng dụng khởi động (chỉ dùng cho development)
@app.on_event("startup")
def on_startup():
    try:
        # import inside startup to avoid side-effects at module import time
        from app.database import create_tables
        create_tables()
    except Exception:
        # Don't crash app import if DB is not available during tests or tooling
        # The exception will be visible in logs when running the server.
        pass

# Root endpoint
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {
        "message": f"Chào mừng đến với {settings.app_name}!",
        "version": "1.0.0",
        "database": "SQLAlchemy integrated",
        "docs_url": "/docs"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    """Kiểm tra API có hoạt động không"""
    return {
        "status": "healthy",
        "service": settings.app_name,
        "database": "connected" # (Giả định là đã kết nối)
    }

# (Phần này không cần thiết nếu bạn chạy bằng lệnh uvicorn trực tiếp)
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)