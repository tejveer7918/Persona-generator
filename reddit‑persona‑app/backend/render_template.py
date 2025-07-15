
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def render_persona_html(persona: dict, photo_url: str = "https://via.placeholder.com/300") -> str:
    """
    Renders the persona data into the HTML template.
    """
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("persona_template.html")

    context = {
        "photo_url": photo_url,
        "quote": persona.get("quote", "This user prefers to stay quiet."),
        "name": persona.get("persona_name", "Unknown"),
        "age": persona.get("demographics", {}).get("age", "N/A"),
        "occupation": persona.get("demographics", {}).get("occupation", "N/A"),
        "status": persona.get("demographics", {}).get("status", "N/A"),
        "location": persona.get("demographics", {}).get("location", "N/A"),
        "tier": persona.get("demographics", {}).get("tier", "N/A"),
        "archetype": persona.get("demographics", {}).get("archetype", "N/A"),
        "motivations": persona.get("motivations", {}).keys(),
        "personality": persona.get("personality", {}).values(),
        "behaviour": persona.get("behaviour", []),
        "frustrations": persona.get("frustrations", []),
        "goals": persona.get("goals", []),
    }

    return template.render(**context)
