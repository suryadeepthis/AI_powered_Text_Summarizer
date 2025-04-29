import requests
import gradio as gr 

# Deepseek AI endpoint
OLLAMA_URL= "http://localhost:11434/api/generate"

def summarize_text(text):
    payload= {
        "model": "deepseek-r1:1.5b",
        "prompt": f"Summarize the following text in 1-2 sentences without losing essence:\n\n{text}",
        "stream" : False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No summary generated.")
    else:
        return f"Error: {response.text}"

# Create Gradio Interface
with gr.Blocks(title="AI-powered Text Summarizer") as demo:
    gr.HTML("""
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', sans-serif;
        }
        
        
        .overlay {
            background-color: rgba(0, 0, 0, 0.6); /* Dark overlay */            
            color: white;
        }
        h1, h2, p, label {
            color: black !important;
        }
    </style>
    <div class="overlay">
    """)

    with gr.Column(elem_classes=["main-container"]):
        gr.Markdown("<h2 style='text-align:center;'> 🧠 AI-powered Text Summarizer")
        
        with gr.Row():
            input_text = gr.Textbox(
                lines=10,
                label="Paste the text below",             
                show_label=True
            )
        submit_btn = gr.Button("Summarize")
        
        output_text = gr.Textbox(
                lines=10,
                label="Summarized Output",
                interactive=False
            )

        submit_btn.click(fn=summarize_text, inputs=input_text, outputs=output_text)
    
    gr.HTML("</div>")  # Close overlay div

# Launch the App
if __name__ == "__main__":
    demo.launch()





