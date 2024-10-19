"""
risk/network/plot/contour
~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from typing import List, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg
from scipy.ndimage import label
from scipy.stats import gaussian_kde

from risk.log import params, logger
from risk.network.graph import NetworkGraph
from risk.network.plot.utils import get_annotated_domain_colors, to_rgba


class Contour:
    """Class to generate Kernel Density Estimate (KDE) contours for nodes in a network graph."""

    def __init__(self, graph: NetworkGraph, ax: plt.Axes) -> None:
        """Initialize the Contour with a NetworkGraph and axis for plotting.

        Args:
            graph (NetworkGraph): The NetworkGraph object containing the network data.
            ax (plt.Axes): The axis to plot the contours on.
        """
        self.graph = graph
        self.ax = ax

    def plot_contours(
        self,
        levels: int = 5,
        bandwidth: float = 0.8,
        grid_size: int = 250,
        color: Union[str, List, Tuple, np.ndarray] = "white",
        linestyle: str = "solid",
        linewidth: float = 1.5,
        alpha: Union[float, None] = 1.0,
        fill_alpha: Union[float, None] = None,
    ) -> None:
        """Draw KDE contours for nodes in various domains of a network graph, highlighting areas of high density.

        Args:
            levels (int, optional): Number of contour levels to plot. Defaults to 5.
            bandwidth (float, optional): Bandwidth for KDE. Controls the smoothness of the contour. Defaults to 0.8.
            grid_size (int, optional): Resolution of the grid for KDE. Higher values create finer contours. Defaults to 250.
            color (str, list, tuple, or np.ndarray, optional): Color of the contours. Can be a single color or an array of colors.
                Defaults to "white".
            linestyle (str, optional): Line style for the contours. Defaults to "solid".
            linewidth (float, optional): Line width for the contours. Defaults to 1.5.
            alpha (float, None, optional): Transparency level of the contour lines. If provided, it overrides any existing alpha values
                found in color. Defaults to 1.0.
            fill_alpha (float, None, optional): Transparency level of the contour fill. If provided, it overrides any existing alpha
                values found in color. Defaults to None.
        """
        # Log the contour plotting parameters
        params.log_plotter(
            contour_levels=levels,
            contour_bandwidth=bandwidth,
            contour_grid_size=grid_size,
            contour_color=(
                "custom" if isinstance(color, np.ndarray) else color
            ),  # np.ndarray usually indicates custom colors
            contour_alpha=alpha,
            contour_fill_alpha=fill_alpha,
        )

        # Ensure color is converted to RGBA with repetition matching the number of domains
        color = to_rgba(
            color=color, alpha=alpha, num_repeats=len(self.graph.domain_id_to_node_ids_map)
        )
        # Extract node coordinates from the network graph
        node_coordinates = self.graph.node_coordinates
        # Draw contours for each domain in the network
        for idx, (_, node_ids) in enumerate(self.graph.domain_id_to_node_ids_map.items()):
            if len(node_ids) > 1:
                self._draw_kde_contour(
                    self.ax,
                    node_coordinates,
                    node_ids,
                    color=color[idx],
                    levels=levels,
                    bandwidth=bandwidth,
                    grid_size=grid_size,
                    linestyle=linestyle,
                    linewidth=linewidth,
                    alpha=alpha,
                    fill_alpha=fill_alpha,
                )

    def plot_subcontour(
        self,
        nodes: Union[List, Tuple, np.ndarray],
        levels: int = 5,
        bandwidth: float = 0.8,
        grid_size: int = 250,
        color: Union[str, List, Tuple, np.ndarray] = "white",
        linestyle: str = "solid",
        linewidth: float = 1.5,
        alpha: Union[float, None] = 1.0,
        fill_alpha: Union[float, None] = None,
    ) -> None:
        """Plot a subcontour for a given set of nodes or a list of node sets using Kernel Density Estimation (KDE).

        Args:
            nodes (list, tuple, or np.ndarray): List of node labels or list of lists of node labels to plot the contour for.
            levels (int, optional): Number of contour levels to plot. Defaults to 5.
            bandwidth (float, optional): Bandwidth for KDE. Controls the smoothness of the contour. Defaults to 0.8.
            grid_size (int, optional): Resolution of the grid for KDE. Higher values create finer contours. Defaults to 250.
            color (str, list, tuple, or np.ndarray, optional): Color of the contour. Can be a string (e.g., 'white') or RGBA array.
                Defaults to "white".
            linestyle (str, optional): Line style for the contour. Defaults to "solid".
            linewidth (float, optional): Line width for the contour. Defaults to 1.5.
            alpha (float, None, optional): Transparency level of the contour lines. If provided, it overrides any existing alpha values
                found in color. Defaults to 1.0.
            fill_alpha (float, None, optional): Transparency level of the contour fill. If provided, it overrides any existing alpha
            values found in color. Defaults to None.

        Raises:
            ValueError: If no valid nodes are found in the network graph.
        """
        # Check if nodes is a list of lists or a flat list
        if any(isinstance(item, (list, tuple, np.ndarray)) for item in nodes):
            # If it's a list of lists, iterate over sublists
            node_groups = nodes
        else:
            # If it's a flat list of nodes, treat it as a single group
            node_groups = [nodes]

        # Convert color to RGBA using the to_rgba helper function
        color_rgba = to_rgba(color=color, alpha=alpha)

        # Iterate over each group of nodes (either sublists or flat list)
        for sublist in node_groups:
            # Filter to get node IDs and their coordinates for each sublist
            node_ids = [
                self.graph.node_label_to_node_id_map.get(node)
                for node in sublist
                if node in self.graph.node_label_to_node_id_map
            ]
            if not node_ids or len(node_ids) == 1:
                raise ValueError(
                    "No nodes found in the network graph or insufficient nodes to plot."
                )

            # Draw the KDE contour for the specified nodes
            node_coordinates = self.graph.node_coordinates
            self._draw_kde_contour(
                self.ax,
                node_coordinates,
                node_ids,
                color=color_rgba,
                levels=levels,
                bandwidth=bandwidth,
                grid_size=grid_size,
                linestyle=linestyle,
                linewidth=linewidth,
                alpha=alpha,
                fill_alpha=fill_alpha,
            )

    def _draw_kde_contour(
        self,
        ax: plt.Axes,
        pos: np.ndarray,
        nodes: List,
        levels: int = 5,
        bandwidth: float = 0.8,
        grid_size: int = 250,
        color: Union[str, np.ndarray] = "white",
        linestyle: str = "solid",
        linewidth: float = 1.5,
        alpha: Union[float, None] = 1.0,
        fill_alpha: Union[float, None] = 0.2,
    ) -> None:
        """Draw a Kernel Density Estimate (KDE) contour plot for a set of nodes on a given axis.

        Args:
            ax (plt.Axes): The axis to draw the contour on.
            pos (np.ndarray): Array of node positions (x, y).
            nodes (list): List of node indices to include in the contour.
            levels (int, optional): Number of contour levels. Defaults to 5.
            bandwidth (float, optional): Bandwidth for the KDE. Controls smoothness. Defaults to 0.8.
            grid_size (int, optional): Grid resolution for the KDE. Higher values yield finer contours. Defaults to 250.
            color (str or np.ndarray): Color for the contour. Can be a string or RGBA array. Defaults to "white".
            linestyle (str, optional): Line style for the contour. Defaults to "solid".
            linewidth (float, optional): Line width for the contour. Defaults to 1.5.
            alpha (float, None, optional): Transparency level for the contour lines. If provided, it overrides any existing alpha
                values found in color. Defaults to 1.0.
            fill_alpha (float, None, optional): Transparency level for the contour fill. If provided, it overrides any existing
                alpha values found in color. Defaults to 0.2.
        """
        # Extract the positions of the specified nodes
        points = np.array([pos[n] for n in nodes])
        if len(points) <= 1:
            return None  # Not enough points to form a contour

        # Check if the KDE forms a single connected component
        connected = False
        z = None  # Initialize z to None to avoid UnboundLocalError
        while not connected and bandwidth <= 100.0:
            try:
                # Perform KDE on the points with the given bandwidth
                kde = gaussian_kde(points.T, bw_method=bandwidth)
                xmin, ymin = points.min(axis=0) - bandwidth
                xmax, ymax = points.max(axis=0) + bandwidth
                x, y = np.mgrid[
                    xmin : xmax : complex(0, grid_size), ymin : ymax : complex(0, grid_size)
                ]
                z = kde(np.vstack([x.ravel(), y.ravel()])).reshape(x.shape)
                # Check if the KDE forms a single connected component
                connected = _is_connected(z)
                if not connected:
                    bandwidth += 0.05  # Increase bandwidth slightly and retry
            except linalg.LinAlgError:
                bandwidth += 0.05  # Increase bandwidth and retry
            except Exception as e:
                # Catch any other exceptions and log them
                logger.error(f"Unexpected error when drawing KDE contour: {e}")
                return None

        # If z is still None, the KDE computation failed
        if z is None:
            logger.error("Failed to compute KDE. Skipping contour plot for these nodes.")
            return None

        # Define contour levels based on the density
        min_density, max_density = z.min(), z.max()
        if min_density == max_density:
            logger.warning(
                "Contour levels could not be created due to lack of variation in density."
            )
            return None

        # Create contour levels based on the density values
        contour_levels = np.linspace(min_density, max_density, levels)[1:]
        if len(contour_levels) < 2 or not np.all(np.diff(contour_levels) > 0):
            logger.error("Contour levels must be strictly increasing. Skipping contour plot.")
            return None

        # Set the contour color and linestyle
        contour_colors = [color for _ in range(levels - 1)]
        # Plot the filled contours using fill_alpha for transparency
        if fill_alpha and fill_alpha > 0:
            ax.contourf(
                x,
                y,
                z,
                levels=contour_levels,
                colors=contour_colors,
                antialiased=True,
                alpha=fill_alpha,
            )

        # Plot the contour lines with the specified alpha for transparency
        c = ax.contour(
            x,
            y,
            z,
            levels=contour_levels,
            colors=contour_colors,
            linestyles=linestyle,
            linewidths=linewidth,
            alpha=alpha,
        )

        # Set linewidth for the contour lines to 0 for levels other than the base level
        for i in range(1, len(contour_levels)):
            c.collections[i].set_linewidth(0)

    def get_annotated_contour_colors(
        self,
        cmap: str = "gist_rainbow",
        color: Union[str, None] = None,
        min_scale: float = 0.8,
        max_scale: float = 1.0,
        scale_factor: float = 1.0,
        random_seed: int = 888,
    ) -> np.ndarray:
        """Get colors for the contours based on node annotations or a specified colormap.

        Args:
            cmap (str, optional): Name of the colormap to use for generating contour colors. Defaults to "gist_rainbow".
            color (str or None, optional): Color to use for the contours. If None, the colormap will be used. Defaults to None.
            min_scale (float, optional): Minimum intensity scale for the colors generated by the colormap.
                Controls the dimmest colors. Defaults to 0.8.
            max_scale (float, optional): Maximum intensity scale for the colors generated by the colormap.
                Controls the brightest colors. Defaults to 1.0.
            scale_factor (float, optional): Exponent for adjusting color scaling based on enrichment scores.
                A higher value increases contrast by dimming lower scores more. Defaults to 1.0.
            random_seed (int, optional): Seed for random number generation to ensure reproducibility. Defaults to 888.

        Returns:
            np.ndarray: Array of RGBA colors for contour annotations.
        """
        return get_annotated_domain_colors(
            graph=self.graph,
            cmap=cmap,
            color=color,
            min_scale=min_scale,
            max_scale=max_scale,
            scale_factor=scale_factor,
            random_seed=random_seed,
        )


def _is_connected(z: np.ndarray) -> bool:
    """Determine if a thresholded grid represents a single, connected component.

    Args:
        z (np.ndarray): A binary grid where the component connectivity is evaluated.

    Returns:
        bool: True if the grid represents a single connected component, False otherwise.
    """
    _, num_features = label(z)
    return num_features == 1  # Return True if only one connected component is found
