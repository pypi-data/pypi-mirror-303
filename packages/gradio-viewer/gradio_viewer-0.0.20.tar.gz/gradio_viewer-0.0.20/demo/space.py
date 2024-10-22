
import gradio as gr
from app import demo as app
import os

_docs = {'Viewer': {'description': 'A base class for defining methods that all input/output components should have.', 'members': {'__init__': {'value': {'type': 'Any', 'default': 'None', 'description': None}, 'height': {'type': 'int | None', 'default': 'None', 'description': None}, 'label': {'type': 'str | None', 'default': 'None', 'description': None}, 'info': {'type': 'str | None', 'default': 'None', 'description': None}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': None}, 'container': {'type': 'bool', 'default': 'True', 'description': None}, 'scale': {'type': 'int | None', 'default': 'None', 'description': None}, 'min_width': {'type': 'int | None', 'default': 'None', 'description': None}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': None}, 'visible': {'type': 'bool', 'default': 'True', 'description': None}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': None}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': None}, 'render': {'type': 'bool', 'default': 'True', 'description': None}, 'load_fn': {'type': 'Callable[..., Any] | None', 'default': 'None', 'description': None}, 'every': {'type': 'Timer | float | None', 'default': 'None', 'description': None}, 'n': {'type': 'int', 'default': '0', 'description': None}, 'max_size': {'type': 'int', 'default': '5000000', 'description': None}, 'max_pages': {'type': 'int', 'default': '100', 'description': None}, 'ms_files': {'type': 'bool', 'default': 'True', 'description': None}, 'libre_office': {'type': 'bool', 'default': 'True', 'description': None}, 'interface_language': {'type': 'str', 'default': '"fr"', 'description': None}}, 'postprocess': {'value': {'type': 'str | list[str] | None', 'description': 'Expects a `str` filepath or URL, or a `list[str]` of filepaths/URLs.'}}, 'preprocess': {'return': {'type': 'str', 'description': "the data after preprocessing, sent to the user's function in the backend"}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': ''}, 'upload': {'type': None, 'default': None, 'description': ''}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'Viewer': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_viewer`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_viewer/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_viewer"></a>  
</div>

Visualise any type of files
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_viewer
```

## Usage

```python
import gradio as gr
from gradio_viewer import Viewer


def set_interface():
    view_with_ms = Viewer(
        value=[
            "./demo/data/Le_Petit_Chaperon_Rouge_Modifie.docx",
            "./demo/data/mermaid_graph-2.html",
            "./demo/data/graphique_couts_annuels.png",
            "./demo/data/Le_Petit_Chaperon_Rouge.zouzou",
            "./demo/data/viewer.py",
        ],
        elem_classes=["visualisation"],
        n=0,
        height=300,
        visible=True,
        ms_files=True,
    )

    view_without_ms = Viewer(
        value=[
            "./demo/data/Le_Petit_Chaperon_Rouge_Modifie.docx",
            "./demo/data/mermaid_graph-2.html",
            "./demo/data/graphique_couts_annuels.png",
            "./demo/data/Le_Petit_Chaperon_Rouge.zouzou",
        ],
        elem_classes=["visualisation"],
        n=1,
        height=300,
        visible=True,
        ms_files=False,
    )
    empty_view1 = view_with_ms
    empty_view2 = view_without_ms
    return view_with_ms, view_without_ms, empty_view1, empty_view2


with gr.Blocks() as demo:
    with gr.Row():
        view_with_ms = Viewer(visible=False)
        view_without_ms = Viewer(visible=False)
        empty_view1 = Viewer(visible=False)
        empty_view2 = Viewer(visible=False)
    demo.load(
        set_interface, outputs=[view_with_ms, view_without_ms, empty_view1, empty_view2]
    ).then(
        fn=lambda: (
            Viewer(visible=False, value=None, elem_id="empty1"),
            Viewer(visible=False, value=[], elem_id="empty2"),
        ),
        outputs=[empty_view1, empty_view2],
    )

if __name__ == "__main__":
    demo.launch()

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `Viewer`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["Viewer"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["Viewer"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, the data after preprocessing, sent to the user's function in the backend.
- **As output:** Should return, expects a `str` filepath or URL, or a `list[str]` of filepaths/URLs.

 ```python
def predict(
    value: str
) -> str | list[str] | None:
    return value
```
""", elem_classes=["md-custom", "Viewer-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          Viewer: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
