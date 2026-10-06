from ollama import chat

prompt = """
You are a professional AI video script planner.

Convert the user's story into short video scenes.

For every scene provide:
1. Scene number
2. Visual description
3. Main action or movement
4. Camera movement

The actions must describe real movement such as walking,
running, picking, opening, holding, turning, sitting, etc.

Keep the response simple and suitable for an AI video generator.

User story:
A young woman walks through a beautiful flower garden,
plucks a red flower from a tree, and places the flower
inside a basket.
"""

response = chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])