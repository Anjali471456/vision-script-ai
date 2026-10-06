from huggingface_hub import InferenceClient
import os

print("Starting video generation...")

client = InferenceClient(
    provider="fal-ai"
)

prompt = """
A young Indian woman wearing a beautiful red saree
walks slowly through a lush flower garden.
She approaches a flowering tree, reaches out with her hand,
gently plucks a red hibiscus flower, and places it into
a woven basket she is carrying.

Her body moves naturally while walking.
Her arm and hand move naturally while plucking the flower.
Her saree moves gently as she walks.
Realistic human movement, natural body motion,
cinematic camera movement, photorealistic.
"""

print("Generating video... Please wait.")

video = client.text_to_video(
    prompt,
    model="Wan-AI/Wan2.2-TI2V-5B"
)

os.makedirs("output", exist_ok=True)

output_path = "output/test_video.mp4"

with open(output_path, "wb") as f:
    f.write(video)

print()
print("Video generated successfully!")
print(f"Saved at: {output_path}")