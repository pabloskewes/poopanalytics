from tempfile import NamedTemporaryFile
from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from load_data import load_data, process_data


POOP_EMOJI = "💩"


def process_file(file) -> pd.DataFrame:
    """Processes the given file and returns a pandas DataFrame"""

    data = load_data(file)
    data = process_data(data)
    return data


def build_figure(data: pd.DataFrame) -> go.Figure:
    user_counts = data["user"].value_counts()

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=user_counts.index,
            y=user_counts.values,
            marker_color="skyblue",  # You can customize the color as needed
        )
    )

    fig.update_layout(
        title="Poop Emoji Count by User",
        xaxis=dict(title="User"),
        yaxis=dict(title="Poop Emoji Count"),
    )

    return fig


def main():
    st.title(f"Poop Analytics {POOP_EMOJI}")
    st.write("Upload your WhatsApp chat history and get some insights!")

    # File upload
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

    # Save file to temp folder
    if uploaded_file is not None:
        with NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file.seek(0)
            uploaded_file_path = Path(tmp_file.name)
            data = process_file(uploaded_file_path)

        fig = build_figure(data)

        # Display figure
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
