import numpy as np
import os
from napari_intensity_plotter._widget import (
    IntensityPlotControlWidget,
    IntensityPlotWidget,
)
import tempfile

def test_intensity_plot_widget(make_napari_viewer):
    # Napari viewer を作成
    viewer = make_napari_viewer()
    # テスト用の画像データを追加
    layer = viewer.add_image(np.random.random((100, 100, 100)))
    # IntensityPlotWidget を作成し、viewer を渡す
    plot_widget = IntensityPlotWidget(viewer)
    assert plot_widget.viewer == viewer

    # IntensityPlotWidget のプロット機能をテスト
    plot_widget.update_plot(viewer, None)  # イベントがない場合も考慮
    assert plot_widget.intensity_data is not None
    assert len(plot_widget.intensity_data) == layer.data.shape[0]

    # 一時ディレクトリを作成して保存機能をテスト
    with tempfile.TemporaryDirectory() as temp_dir:
        plot_widget.update_save_directory(temp_dir)
        plot_widget.save_csv = True
        plot_widget.save_png = True
        plot_widget.save_to_csv()
        csv_path = os.path.join(temp_dir, f"{plot_widget.layer_name}_y{plot_widget.clicked_coords[1]}_x{plot_widget.clicked_coords[0]}.csv")
        png_path = os.path.join(temp_dir, f"{plot_widget.layer_name}_y{plot_widget.clicked_coords[1]}_x{plot_widget.clicked_coords[0]}.png")

        # ファイルの存在を確認
        assert os.path.exists(csv_path)
        assert os.path.exists(png_path)
