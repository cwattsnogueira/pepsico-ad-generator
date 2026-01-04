# -*- coding: utf-8 -*-
"""
PepsiCo Ad Generator
Generates structured marketing copy for PepsiCo products using OpenAI + Gradio.
"""

import os
import gradio as gr
from langchain_openai import ChatOpenAI

print("🚀 PepsiCo Ad Generator starting...")

# ---------------------------------------------------------
# Load API Key (Cloud Run environment variable)
# ---------------------------------------------------------
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# ---------------------------------------------------------
# Lazy LLM initialization
# ---------------------------------------------------------
llm = None


def load_llm():
    """
    Lazily load the OpenAI Chat model (Cloud Run–friendly).
    Only created on first request.
    """
    global llm
    if llm is not None:
        return llm

    print("🔧 Initializing OpenAI Chat LLM (gpt-3.5-turbo)...")
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
    )
    print("✅ LLM initialized.")
    return llm


# ---------------------------------------------------------
# System prompt for PepsiCo ad generation
# ---------------------------------------------------------
SYSTEM_PROMPT = """
You are a senior creative copywriter for PepsiCo.
You create high-impact, on-brand, consumer-facing advertising copy.

Your outputs must ALWAYS be structured in the following sections, in this exact order:

[Campaign Title]
[Hook]
[Primary Copy]
[Variant A]
[Variant B]
[Hashtags]
[Notes for Designer]

Guidelines:
- Stay consistent with PepsiCo’s energetic, optimistic, and inclusive brand voice.
- Keep copy channel-appropriate (e.g., short & punchy for social, clearer CTAs for email).
- Respect any regional or cultural context.
- If multiple products are used, make sure they all feel naturally integrated.
- Avoid making any illegal, discriminatory, or misleading claims.
"""


# ---------------------------------------------------------
# PepsiCo products and options
# ---------------------------------------------------------
PEPSICO_PRODUCTS = [
    "Pepsi",
    "Pepsi Zero Sugar",
    "Diet Pepsi",
    "Mountain Dew",
    "Gatorade",
    "7UP",
    "Mirinda",
    "Aquafina",
    "Tropicana",
    "Lipton Iced Tea",
    "Lay's",
    "Doritos",
    "Cheetos",
    "Ruffles",
    "Quaker Oats",
]

CHANNEL_OPTIONS = [
    "Instagram Feed",
    "Instagram Reels",
    "TikTok",
    "YouTube Pre-roll",
    "In-store Signage",
    "Billboard / OOH",
    "Email Campaign",
    "Website Banner",
]

TONE_OPTIONS = [
    "Bold & energetic",
    "Playful & humorous",
    "Friendly & reassuring",
    "Premium & sophisticated",
    "Youthful & trendy",
]


# ---------------------------------------------------------
# Ad generation function
# ---------------------------------------------------------
def generate_pepsico_ad(
    products,
    campaign_goal,
    target_audience,
    channel,
    tone,
    promotion,
    region,
    extra_context,
    creativity,
):
    if not products or len(products) == 0:
        return "Please select at least one PepsiCo product."

    if not campaign_goal or campaign_goal.strip() == "":
        return "Please describe the campaign goal."

    llm = load_llm()

    products_str = ", ".join(products)

    prompt = f"""{SYSTEM_PROMPT}

Use the following brief to generate the ad:

- Products to feature: {products_str}
- Campaign goal: {campaign_goal}
- Target audience: {target_audience or "Not specified (infer a reasonable audience)."}
- Primary channel: {channel}
- Tone & style: {tone}
- Promotion / offer: {promotion or "No specific promotion."}
- Region / market: {region or "Global (no specific region)."}
- Extra context / constraints: {extra_context or "None provided."}

Adjust the style and length to fit the channel.
Return ONLY the structured sections, with the section labels exactly as defined.
"""

    try:
        response = llm.invoke(prompt)
        text = response.content.strip()

        header = "## PepsiCo Campaign Concept\n"
        meta = f"""**Channel:** {channel}  
**Tone:** {tone}  
**Products:** {products_str}  
**Goal:** {campaign_goal}  

---
"""

        return header + meta + "\n" + text

    except Exception as e:
        print(f"❌ Error during ad generation: {e}")
        return f"An error occurred while generating the ad: {e}"


# ---------------------------------------------------------
# PepsiCo UI Styling
# ---------------------------------------------------------
PRIMARY_BLUE = "#005CB4"
SECONDARY_RED = "#E41E2B"
LIGHT_GRAY = "#F5F5F5"


# ---------------------------------------------------------
# Gradio UI (Block Answer Mode)
# ---------------------------------------------------------
with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="red",
        neutral_hue="gray",
    ),
    css=f"""
        body {{
            background-color: {LIGHT_GRAY};
        }}
        .pepsico-header {{
            background: linear-gradient(90deg, {PRIMARY_BLUE}, {SECONDARY_RED});
            padding: 20px;
            border-radius: 8px;
            color: white;
            font-size: 26px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }}
        .gradio-container {{
            max-width: 950px !important;
            margin: auto;
        }}
    """,
) as demo:

    gr.HTML("""
        <div class="pepsico-header">
            PepsiCo Ad Generator (Use‑Case Prototype)
        </div>
    """)

    gr.Markdown(
        "Design a PepsiCo campaign by selecting products and filling in the brief. "
        "The assistant will return a structured, ready-to-use concept."
    )

    with gr.Row():
        with gr.Column(scale=1):
            products_input = gr.CheckboxGroup(
                PEPSICO_PRODUCTS,
                label="PepsiCo Products",
                info="Select one or more products to feature.",
            )

            channel_input = gr.Dropdown(
                CHANNEL_OPTIONS,
                label="Primary Channel",
                value="Instagram Reels",
            )

            tone_input = gr.Dropdown(
                TONE_OPTIONS,
                label="Tone & Style",
                value="Bold & energetic",
            )

            creativity_input = gr.Slider(
                minimum=0.2,
                maximum=1.2,
                value=0.7,
                step=0.1,
                label="Creativity (Temperature Hint – visual only)",
                info="Higher = more creative. Lower = safer and more conservative.",
            )

        with gr.Column(scale=1):
            campaign_goal_input = gr.Textbox(
                label="Campaign Goal",
                placeholder="e.g., Drive awareness for a new Pepsi Zero Sugar flavor",
            )

            target_audience_input = gr.Textbox(
                label="Target Audience",
                placeholder="e.g., Gen Z students, young professionals, families, etc.",
            )

            promotion_input = gr.Textbox(
                label="Promotion / Offer (optional)",
                placeholder="e.g., Buy 2 get 1 free, limited edition, etc.",
            )

            region_input = gr.Textbox(
                label="Region / Market (optional)",
                placeholder="e.g., US, LATAM, global, Middle East, etc.",
            )

            extra_context_input = gr.Textbox(
                label="Extra Context / Constraints (optional)",
                placeholder="e.g., Avoid mentioning sugar, focus on hydration, etc.",
            )

    generate_btn = gr.Button("Generate Campaign Concept", variant="primary")

    output_ad = gr.Markdown(label="Generated Campaign Concept")

    generate_btn.click(
        fn=lambda products, goal, audience, channel, tone, promo, region, extra, temp: generate_pepsico_ad(
            products,
            goal,
            audience,
            channel,
            tone,
            promo,
            region,
            extra,
            temp,
        ),
        inputs=[
            products_input,
            campaign_goal_input,
            target_audience_input,
            channel_input,
            tone_input,
            promotion_input,
            region_input,
            extra_context_input,
            creativity_input,
        ],
        outputs=output_ad,
    )

    gr.Markdown(
        "---\n*Internal demo – PepsiCo creative assistant powered by OpenAI & Gradio.*"
    )


# ---------------------------------------------------------
# Cloud Run Port Logic
# ---------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"🌐 Launching Gradio app on port {port}...")
    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        show_api=False,
        quiet=True,
    )
