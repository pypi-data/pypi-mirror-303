from typing import Tuple
import plotly.graph_objs as go
from plotly.subplots import make_subplots


class DistributionPlot():
    PREDICTION_MARKERS = ["current", "previous"]
    MAX_MARKERS_SUPPORTED = 2

    def __init__(self, x_values: list, y_values_sorted: list,
                 output_names: list, num_rows: int, num_cols: int,
                 y_limits: dict, criterion_thresholds: dict):
        self.x_values = x_values
        self.y_values_sorted = y_values_sorted
        self.output_names = output_names
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.y_limits = y_limits
        self.criterion_thresholds = criterion_thresholds
        #
        self.prediction_marker = []
        self.figure = None
        self.initial_data = None

    def _row_col_to_idx(self, row, col) -> int:
        return row * self.num_cols + col

    def _idx_to_row_col(self, idx) -> Tuple[int, int]:
        row = int(idx / self.num_cols)
        col = int(idx % self.num_cols)
        return (row, col)

    def _add_trace(self, idx, output_name):
        row, col = self._idx_to_row_col(idx)
        self.figure.add_trace(go.Scatter(x=self.x_values,
                                        y=self.y_values_sorted[idx],
                                        name=output_name,
                                        showlegend=False),
                                        row=row + 1,
                                        col=col + 1)

    def _configure_axes(self, idx, output_name):
        # Configure y-axes
        row, col = self._idx_to_row_col(idx)
        lower, upper = self.y_limits[output_name]
        self.figure.update_yaxes(range=[lower, upper],
                                row=row + 1,
                                col=col + 1)

    def _add_annotation(self, idx, output_name):
        row, col = self._idx_to_row_col(idx)
        _, upper = self.y_limits[output_name]
        self.figure.add_annotation(text=output_name,
                                    showarrow=False,
                                    xanchor="left",
                                    yanchor="bottom",
                                    y=1.0 * upper,
                                    row=row + 1,
                                    col=col + 1
        )

    def _add_threshold_line(self, idx, output_name):
        thresh = self.criterion_thresholds[output_name]
        row, col = self._idx_to_row_col(idx)
        self.figure.add_hline(y=thresh,
                                line_dash="dash",
                                line_color="gray",
                                line_width=2,
                                annotation_text=f"{thresh:.3f}",
                                annotation_position="bottom left",
                                annotation=dict(font_size=12),
                                row=row + 1,
                                col=col + 1)

    def _create_figure(self):
        # Create subplots and add traces, axes, annotations, etc.
        config = dict(rows=self.num_rows, cols=self.num_cols,
                      shared_xaxes=True, shared_yaxes=True,
                      x_title="samples", y_title="value")
        self.figure = make_subplots(**config)
        for idx in range(len(self.output_names)):
            output_name = self.output_names[idx]
            self._add_trace(idx, output_name)
            self._configure_axes(idx, output_name)
            self._add_annotation(idx, output_name)
            if output_name in self.criterion_thresholds:
                self._add_threshold_line(idx, output_name)

        legend = dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        self.figure.update_layout(legend=legend, height=850, paper_bgcolor="rgba(0,0,0,0)")
        self.initial_data = self.figure.data

    def _reset_prediction_marker(self):
        self.prediction_marker = []

    def _pop_oldest_marker(self):
        if len(self.prediction_marker) > 0:
            self.prediction_marker.pop(0)

    def _get_x_for_y(self, all_y_sorted, y_value) -> float:
        # Helper function to get x for y
        all_y_sorted = sorted(all_y_sorted + [y_value])
        x_value = all_y_sorted.index(y_value)
        return x_value

    def _handle_marker_error(self):
        if len(self.prediction_marker) > 2:
            raise RuntimeError("Marker error: maximum 2 markers supported!")

    def _plot_marker(self, p_idx, idx, marker_x_value, marker_y_value, max_y_value):
        row, col = self._idx_to_row_col(idx)
        self.figure.add_trace(go.Scatter(
            mode="markers+text",
            x=[marker_x_value],
            y=[marker_y_value],
            text=[self.PREDICTION_MARKERS[p_idx]],
            textposition="top center"
            if marker_y_value < 0.5 * max_y_value else "bottom center",
            marker=dict(color="Green", size=6, line=dict(color="Black", width=1)),
                        showlegend=False), row=row + 1, col=col + 1)

    def create_figure(self):
        self._create_figure()

    def reset_marker(self):
        self._reset_prediction_marker()

    def pop_oldest_marker(self):
        self._pop_oldest_marker()

    def add_marker(self, prediction: list):
        prediction_markers = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                idx = row * self.num_cols + col
                marker_y_value = prediction[idx]
                marker_x_value = self._get_x_for_y(
                    all_y_sorted=self.y_values_sorted[idx].copy(),
                    y_value=marker_y_value)
                prediction_markers.append((marker_x_value, marker_y_value))
        self.prediction_marker.append(prediction_markers)

    def plot(self):
        self.figure.data = self.initial_data

        self._handle_marker_error()

        for p_idx, predictions in enumerate(reversed(self.prediction_marker)):
            for idx, (marker_x_value,
                      marker_y_value) in enumerate(predictions):
                max_y_value = max(self.y_values_sorted[idx])

                self._plot_marker(p_idx, idx, marker_x_value, marker_y_value, max_y_value)
