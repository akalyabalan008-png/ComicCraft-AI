import google.generativeai as genai


def generate_outline(story_prompt, character_name, setting, tone):
    prompt = f"""
Create a simple comic story outline.

Story Prompt: {story_prompt}
Main Character: {character_name}
Setting: {setting}
Story Tone: {tone}

Create 5 comic panels.
For each panel, provide:
1. Panel title
2. Short description
3. Dialogue

Keep the story simple and clear.
"""

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text