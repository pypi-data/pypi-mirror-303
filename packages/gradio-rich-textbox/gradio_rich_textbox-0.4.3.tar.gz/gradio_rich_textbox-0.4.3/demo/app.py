
import gradio as gr
from gradio_rich_textbox import RichTextbox


example = RichTextbox().example_inputs()

demo = gr.Interface(
    lambda x:x,
    RichTextbox(),  # interactive version of your component
    RichTextbox(),  # static version of your component
    examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
