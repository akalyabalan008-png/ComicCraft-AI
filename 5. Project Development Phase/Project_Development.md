# Phase 5 – Project Development Phase

## Project Title
ComicCraft – AI-Powered Comic Generator

## Development Overview

The ComicCraft application was developed as a Generative AI-based web application. The system converts a user's story idea into a multi-panel comic and downloadable PDF.

## Backend Development

FastAPI was used to develop the backend of the application.

The backend handles:
- User requests
- Input processing
- Comic generation
- Image generation
- PDF export

Uvicorn was used to run the FastAPI application locally.

## Story Generation

Google Gemini API was integrated for AI-based story generation.

The system uses the user's:
- Character name
- Setting
- Tone
- Story prompt

to generate a suitable comic story containing scenes and dialogues.

## Image Generation

Stable Diffusion was integrated to generate comic panel images.

Hugging Face Diffusers and PyTorch were used to support the image generation process.

The application generates five comic panels based on the story.

## Comic Layout

The generated images are arranged into a structured comic layout.

Each panel represents a different scene from the generated story and contains suitable visual content and dialogue.

## Web Interface

HTML, CSS, and Jinja2 were used to create the web interface.

The interface provides:
- Input fields
- Generate Comic button
- Generated comic preview
- PDF download option

## PDF Generation

FPDF was used to create the final downloadable comic PDF.

The five generated comic panels are added to the PDF document.

## Project Output

The completed application can:
1. Accept a story idea from the user.
2. Generate a comic story using AI.
3. Generate five comic panels.
4. Display the generated panels.
5. Export the comic as a PDF.

## Development Result

The ComicCraft application was successfully developed and tested.

The final working application generates a five-panel AI-powered comic from user-provided story details and provides the comic as a downloadable PDF.

## Conclusion

The development phase successfully transformed the planned design into a working Generative AI web application. ComicCraft integrates story generation, image generation, comic layout, preview, and PDF export into a single application.
