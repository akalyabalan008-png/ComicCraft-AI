# Phase 3 – Project Design

## Project Title
ComicCraft – AI-Powered Comic Generator

## System Architecture

ComicCraft follows a modular web application architecture.

The main components are:

- User Interface
- FastAPI Backend
- Story Generation Module
- Image Generation Module
- Comic Layout Module
- PDF Export Module

## User Interface

The user interface allows users to enter the required comic details such as:

- Character name
- Setting
- Tone
- Art style
- Story prompt

The interface also displays the generated comic panels and PDF download option.

## Backend Design

FastAPI is used as the backend framework.

The backend receives user input, processes the request, calls the required AI modules, generates the comic panels, creates the layout, and prepares the PDF output.

## Story Generation Module

Google Gemini API is used for generating the comic story.

The module processes the user's story prompt and creates:

- Story
- Scenes
- Characters
- Dialogues

## Image Generation Module

Stable Diffusion is used to generate comic panel images.

Hugging Face Diffusers and PyTorch are used to support the image generation process.

## Comic Layout Module

The generated images are arranged into a structured comic layout.

The layout module organizes the five generated panels so that the final comic can be viewed easily.

## PDF Export Module

FPDF is used to create the final PDF document.

The generated comic panels are added to the PDF and made available for download.

## Data Flow

The basic data flow is:

User Input  
↓  
FastAPI Backend  
↓  
Google Gemini – Story Generation  
↓  
Stable Diffusion – Image Generation  
↓  
Comic Layout  
↓  
PDF Export  
↓  
Final Comic Output

## Project Structure

The project is organized into separate modules to improve maintainability and development.

```text
ComicCraft
│
├── app
│   ├── ai
│   ├── services
│   ├── templates
│   ├── static
│   ├── config.py
│   ├── main.py
│   ├── routes.py
│   └── exporters.py
│
├── README.md
├── LICENSE
└── .gitignore
## Design Objective

The main design objective is to create a simple and modular system that can convert a user's story idea into AI-generated comic panels and a downloadable PDF.
## Conclusion

The project design defines the architecture, modules, data flow, and interaction between different components of ComicCraft. The modular design makes the application easier to develop, test, and maintain.
