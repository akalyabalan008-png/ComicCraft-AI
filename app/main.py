import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from google import genai

from image_generator import generate_image


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/generate")
def generate_comic(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):

    prompt = f"""
Create a simple 5-panel comic story.

Story Prompt: {story_prompt}
Main Character: {character_name}
Setting: {setting}
Story Tone: {tone}
Art Style: {art_style}

For each panel provide:
- Panel title
- Short description
- Dialogue

Create exactly 5 panels.
Keep the story simple and suitable for a comic.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    comic_story = response.text

    # Create 5 image prompts
    image_paths = []

    for i in range(1, 6):

        image_prompt = f"""
Create a comic book illustration for panel {i}.

Main Character: {character_name}
Setting: {setting}
Tone: {tone}
Art Style: {art_style}

Story:
{comic_story}

Create only the visual scene for panel {i}.
Keep the main character appearance consistent.
Do not add text, speech bubbles, captions, or words inside the image.
"""

        image_path = generate_image(
            image_prompt,
            f"panel_{i}.png"
        )

        image_paths.append(image_path)

    return templates.TemplateResponse(
        request=request,
        name="comic_preview.html",
        context={
            "character_name": character_name,
            "setting": setting,
            "tone": tone,
            "art_style": art_style,
            "comic_story": comic_story,
            "image_paths": image_paths
        }
    )

