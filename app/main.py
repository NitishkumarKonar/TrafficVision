from app.video.processor import process_video
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os


app = FastAPI(
    title="TrafficVision",
    description="AI-powered traffic detection and analytics system"
)


# =========================
# DIRECTORIES
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UPLOAD_DIR = os.path.join(
    BASE_DIR,
    "static",
    "uploads"
)

os.makedirs(UPLOAD_DIR, exist_ok=True)


# =========================
# STATIC FILES
# =========================

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)


# =========================
# TEMPLATES
# =========================

templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)


# =========================
# HOME PAGE
# =========================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# =========================
# VIDEO UPLOAD
# =========================

@app.post("/upload")
async def upload_video(
    file: UploadFile = File(...)
):

    # Save uploaded video
    input_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(input_path, "wb") as buffer:

        content = await file.read()

        buffer.write(content)

    # Create output filename
    output_filename = (
        "processed_" + file.filename
    )

    output_path = os.path.join(
        UPLOAD_DIR,
        output_filename
    )

    # Process video
    summary = process_video(
        input_path,
        output_path
    )

    return {
        "message": "Video processed successfully",
        "input_video": file.filename,
        "output_video": output_filename,
        "summary": summary
    }