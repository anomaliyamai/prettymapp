import pickle
from pathlib import Path

from .context import plot, DRAW_SETTINGS


def test_plot():
    _location_ = Path(__file__).resolve().parent
    with open(_location_ / "mock_data/df_pre_adjusting.pickle", "rb") as handle:
        df = pickle.load(handle)

    fig = plot(df, DRAW_SETTINGS)
    assert fig
