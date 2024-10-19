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
