# ComicCraft – AI-Powered Comic Generator

## Team Members

- Akalya B – Team Leader
- Abijith
- Siharth Ali
- Mohammed Anas P

## Team Member Contributions

### Akalya B – Team Leader

- Pre-requisites
- Set up the development environment
- Designing and developing the user interface

### Abijith

- Workflow
- Develop the core functionalities
- Creating dynamic templates with FastAPI's Jinja2

### Siharth Ali

- Research and select the appropriate Generative AI model
- Implement the FastAPI backend for routing and user input processing
- Preparing the application for local deployment

### Mohammed Anas P

- Define the architecture of the application
- Writing the main application logic in `routes.py`
- Testing and verifying local deployment

## Project Overview

ComicCraft is a Generative AI-based web application that converts a simple story idea into a multi-panel comic.

The user provides details such as character name, setting, tone, art style, and story prompt. The application uses Generative AI to create a comic story, scenes, dialogues, and AI-generated comic panels.

The generated comic can be previewed in the web application and exported as a downloadable PDF.

## Problem Statement

Creating a comic manually requires considerable time and effort.

Users need to create a story, characters, dialogues, scenes, and comic panels separately. Beginners may also find it difficult to design and arrange comic panels.

ComicCraft provides an AI-assisted solution that simplifies the comic creation process.

## Main Features

- AI-powered comic story generation
- Character and scene generation
- Dialogue generation
- Five-panel comic generation
- Multiple input options
- Comic book art style
- AI-generated images
- Comic panel preview
- Downloadable PDF
- Simple web interface
- FastAPI backend
- Google Gemini integration
- Stable Diffusion image generation
- Error handling

## Project Scenarios

### Scenario 1 – Comic Story Generation

The user enters a character name, setting, tone, art style, and story prompt.

ComicCraft processes the information and generates a creative comic story.

### Scenario 2 – AI Comic Panel Generation

The generated story is converted into scenes and five AI-generated comic panels.

Each panel represents a part of the story and contains suitable visual content and dialogue.

### Scenario 3 – Comic PDF Export

The generated comic panels are arranged into a final comic layout.

The complete comic can then be exported and downloaded as a PDF file.

## Technology Stack

- Python
- FastAPI
- Uvicorn
- HTML
- CSS
- Jinja2
- Google Gemini API
- Hugging Face Diffusers
- Stable Diffusion
- PyTorch
- Pillow
- FPDF
- Git
- GitHub

## Application Architecture

```text
                         User
                           |
                           v
                  HTML/CSS Frontend
                           |
                           v
                    FastAPI Backend
                           |
             +-------------+-------------+
             |                           |
             v                           v
      Google Gemini               Stable Diffusion
      Story Generation            Image Generation
             |                           |
             v                           v
       Story + Scenes             Comic Panel Images
             |                           |
             +-------------+-------------+
                           |
                           v
                    Comic Layout
                           |
                  +--------+--------+
                  |                 |
                  v                 v
            Comic Preview       FPDF Export
                                      |
                                      v
                              Downloadable PDF
```

## Project Folder Structure

```text
ComicCraft-AI/
│
├── app/
│   ├── ai/
│   ├── services/
│   ├── templates/
│   ├── static/
│   ├── config.py
│   ├── main.py
│   ├── routes.py
│   └── exporters.py
│
├── 1. Brainstorming & Ideation/
│   └── Brainstorming.md
│
├── 2. Requirement Analysis/
│   └── Requirement_Analysis.md
│
├── 3. Project Design Phase/
│   └── Project_Design.md
│
├── 4. Project Planning Phase/
│   └── Project_Planning.md
│
├── 5. Project Development Phase/
│   └── Project_Development.md
│
├── 6. Project Testing/
│   └── Project_Testing.md
│
├── 7. Project Documentation/
│   └── Project_Documentation.md
│
├── 8. Project Demonstration/
│   └── Project_Demonstration.md
│
├── .gitignore
├── LICENSE
└── README.md
```

## Project Workflow

1. User enters comic details.
2. FastAPI receives the user input.
3. Google Gemini processes the story prompt.
4. AI generates the comic story and scenes.
5. Stable Diffusion generates comic panel images.
6. The generated panels are arranged into a comic layout.
7. The comic is displayed for preview.
8. FPDF creates the final PDF.
9. User downloads the generated comic.

## User Input

The application accepts:

- Character Name
- Setting
- Tone
- Art Style
- Story Prompt

## Example Input

```text
Character Name: Finn
Setting: Mysterious Forest
Tone: Light-hearted
Art Style: Comic book

Story Prompt:
A brave fox named Finn explores a mysterious forest
and finds a lost bird. Finn helps the bird find its
way home. Along the way, they face a small challenge,
discover a hidden path, and finally reach the bird's
home safely. The two become good friends.
```

## Generated Output

ComicCraft generates:

- Comic story
- Scenes
- Dialogues
- Five comic panels
- Comic preview
- Downloadable PDF

## Testing

The application was tested for:

- User input validation
- Story generation
- AI image generation
- Comic panel generation
- Dialogue generation
- Comic preview
- PDF generation
- PDF content

The application successfully generated five comic panels and a final PDF during testing.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/akalyabalan008-png/ComicCraft-AI.git
cd ComicCraft-AI
```

### 2. Create Virtual Environment

```bash
python -m venv comiccraft-env
```

### 3. Activate Virtual Environment

For Windows:

```bash
comiccraft-env\Scripts\activate
```

### 4. Install Required Packages

```bash
pip install fastapi uvicorn jinja2 python-multipart google-generativeai diffusers transformers fpdf Pillow accelerate torch
```

### 5. Configure API Keys

Create a `.env` file and add the required API keys and configuration values.

Do not upload the `.env` file to GitHub.

### 6. Run the Application

```bash
python -m uvicorn app.main:app --reload
```

### 7. Open the Application

Open the following address in a web browser:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

## Project Demonstration

The project demonstration shows:

- ComicCraft home page
- User input
- Comic generation
- Five generated comic panels
- Comic preview
- PDF generation
- Final PDF output

The project demonstration video is submitted through the project submission platform.

## Project Advantages

- Reduces the effort required to create comics.
- Uses Generative AI for creative content.
- Generates story and comic panels automatically.
- Provides a simple user interface.
- Supports downloadable PDF output.
- Demonstrates practical use of Generative AI.

## Limitations

- AI image generation may take time.
- Generated images may vary depending on the prompt.
- Stable Diffusion requires significant system resources.
- Internet and API availability can affect AI features.
- Character appearance may vary between panels.

## Future Enhancements

- Character consistency across panels
- More comic panel layouts
- More art styles
- Voice-based story input
- Multilingual comic generation
- Advanced comic editing
- Cloud deployment
- User account and project history
- More export formats

## Conclusion

ComicCraft demonstrates how Generative AI can be used for creative content generation.

The application converts a simple story idea into a complete five-panel comic with scenes and dialogues and provides the final comic as a downloadable PDF.

The project combines Google Gemini, Stable Diffusion, FastAPI, and other technologies to provide an AI-powered comic creation experience.
