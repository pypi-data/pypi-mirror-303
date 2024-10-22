---
tags: [gradio-custom-component, File]
title: gradio_viewer
short_description: Visualise files
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_viewer`
<a href="https://pypi.org/project/gradio_viewer/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_viewer"></a>  

Visualise any type of files

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

## `Viewer`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
Any
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>height</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>info</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>load_fn</code></td>
<td align="left" style="width: 25%;">

```python
Callable[..., Any] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
Timer | float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>n</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>0</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>max_size</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>5000000</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>max_pages</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>100</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>ms_files</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>libre_office</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>interface_language</code></td>
<td align="left" style="width: 25%;">

```python
str
```

</td>
<td align="left"><code>"fr"</code></td>
<td align="left">None</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` |  |
| `upload` |  |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, the data after preprocessing, sent to the user's function in the backend.
- **As input:** Should return, expects a `str` filepath or URL, or a `list[str]` of filepaths/URLs.

 ```python
 def predict(
     value: str
 ) -> str | list[str] | None:
     return value
 ```
 
