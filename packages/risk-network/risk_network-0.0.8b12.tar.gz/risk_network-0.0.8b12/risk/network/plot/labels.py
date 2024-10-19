"""
risk/network/plot/labels
~~~~~~~~~~~~~~~~~~~~~~~~
"""

from typing import Any, Dict, List, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from risk.log import params
from risk.network.graph import NetworkGraph
from risk.network.plot.utils import calculate_bounding_box, get_annotated_domain_colors, to_rgba

TERM_DELIMITER = "::::"  # String used to separate multiple domain terms when constructing composite domain labels


class Labels:
    """Class to handle the annotation of network graphs with labels for different domains."""

    def __init__(self, graph: NetworkGraph, ax: plt.Axes):
        """Initialize the Labeler object with a network graph and matplotlib axes.

        Args:
            graph (NetworkGraph): NetworkGraph object containing the network data.
            ax (plt.Axes): Matplotlib axes object to plot the labels on.
        """
        self.graph = graph
        self.ax = ax

    def plot_labels(
        self,
        scale: float = 1.05,
        offset: float = 0.10,
        font: str = "Arial",
        fontcase: Union[str, None] = None,
        fontsize: int = 10,
        fontcolor: Union[str, List, Tuple, np.ndarray] = "black",
        fontalpha: Union[float, None] = 1.0,
        arrow_linewidth: float = 1,
        arrow_style: str = "->",
        arrow_color: Union[str, List, Tuple, np.ndarray] = "black",
        arrow_alpha: Union[float, None] = 1.0,
        arrow_base_shrink: float = 0.0,
        arrow_tip_shrink: float = 0.0,
        max_labels: Union[int, None] = None,
        max_label_lines: Union[int, None] = None,
        min_label_lines: int = 1,
        max_chars_per_line: Union[int, None] = None,
        min_chars_per_line: int = 1,
        words_to_omit: Union[List, None] = None,
        overlay_ids: bool = False,
        ids_to_keep: Union[List, Tuple, np.ndarray, None] = None,
        ids_to_replace: Union[Dict, None] = None,
    ) -> None:
        """Annotate the network graph with labels for different domains, positioned around the network for clarity.

        Args:
            scale (float, optional): Scale factor for positioning labels around the perimeter. Defaults to 1.05.
            offset (float, optional): Offset distance for labels from the perimeter. Defaults to 0.10.
            font (str, optional): Font name for the labels. Defaults to "Arial".
            fontcase (str, None, optional): Case transformation for the labels. Can be "capitalize", "lower", "title",
                "upper", or None. Defaults to None.
            fontsize (int, optional): Font size for the labels. Defaults to 10.
            fontcolor (str, list, tuple, or np.ndarray, optional): Color of the label text. Can be a string or RGBA array.
                Defaults to "black".
            fontalpha (float, None, optional): Transparency level for the font color. If provided, it overrides any existing alpha
                values found in fontcolor. Defaults to 1.0.
            arrow_linewidth (float, optional): Line width of the arrows pointing to centroids. Defaults to 1.
            arrow_style (str, optional): Style of the arrows pointing to centroids. Defaults to "->".
            arrow_color (str, list, tuple, or np.ndarray, optional): Color of the arrows. Defaults to "black".
            arrow_alpha (float, None, optional): Transparency level for the arrow color. If provided, it overrides any existing alpha
                values found in arrow_color. Defaults to 1.0.
            arrow_base_shrink (float, optional): Distance between the text and the base of the arrow. Defaults to 0.0.
            arrow_tip_shrink (float, optional): Distance between the arrow tip and the centroid. Defaults to 0.0.
            max_labels (int, optional): Maximum number of labels to plot. Defaults to None (no limit).
            min_label_lines (int, optional): Minimum number of lines in a label. Defaults to 1.
            max_label_lines (int, optional): Maximum number of lines in a label. Defaults to None (no limit).
            min_chars_per_line (int, optional): Minimum number of characters in a line to display. Defaults to 1.
            max_chars_per_line (int, optional): Maximum number of characters in a line to display. Defaults to None (no limit).
            words_to_omit (list, optional): List of words to omit from the labels. Defaults to None.
            overlay_ids (bool, optional): Whether to overlay domain IDs in the center of the centroids. Defaults to False.
            ids_to_keep (list, tuple, np.ndarray, or None, optional): IDs of domains that must be labeled. To discover domain IDs,
                you can set `overlay_ids=True`. Defaults to None.
            ids_to_replace (dict, optional): A dictionary mapping domain IDs to custom labels (strings). The labels should be
                space-separated words. If provided, the custom labels will replace the default domain terms. To discover domain IDs, you
                can set `overlay_ids=True`. Defaults to None.

        Raises:
            ValueError: If the number of provided `ids_to_keep` exceeds `max_labels`.
        """
        # Log the plotting parameters
        params.log_plotter(
            label_perimeter_scale=scale,
            label_offset=offset,
            label_font=font,
            label_fontcase=fontcase,
            label_fontsize=fontsize,
            label_fontcolor=(
                "custom" if isinstance(fontcolor, np.ndarray) else fontcolor
            ),  # np.ndarray usually indicates custom colors
            label_fontalpha=fontalpha,
            label_arrow_linewidth=arrow_linewidth,
            label_arrow_style=arrow_style,
            label_arrow_color="custom" if isinstance(arrow_color, np.ndarray) else arrow_color,
            label_arrow_alpha=arrow_alpha,
            label_arrow_base_shrink=arrow_base_shrink,
            label_arrow_tip_shrink=arrow_tip_shrink,
            label_max_labels=max_labels,
            label_min_label_lines=min_label_lines,
            label_max_label_lines=max_label_lines,
            label_max_chars_per_line=max_chars_per_line,
            label_min_chars_per_line=min_chars_per_line,
            label_words_to_omit=words_to_omit,
            label_overlay_ids=overlay_ids,
            label_ids_to_keep=ids_to_keep,
            label_ids_to_replace=ids_to_replace,
        )

        # Convert ids_to_keep to a tuple if it is not None
        ids_to_keep = tuple(ids_to_keep) if ids_to_keep else tuple()
        # Set max_labels to the total number of domains if not provided (None)
        if max_labels is None:
            max_labels = len(self.graph.domain_id_to_node_ids_map)
        # Set max_label_lines and max_chars_per_line to large numbers if not provided (None)
        if max_label_lines is None:
            max_label_lines = int(1e6)
        if max_chars_per_line is None:
            max_chars_per_line = int(1e6)
        # Normalize words_to_omit to lowercase
        if words_to_omit:
            words_to_omit = set(word.lower() for word in words_to_omit)

        # Calculate the center and radius of domains to position labels around the network
        domain_id_to_centroid_map = {}
        for domain_id, node_ids in self.graph.domain_id_to_node_ids_map.items():
            if node_ids:  # Skip if the domain has no nodes
                domain_id_to_centroid_map[domain_id] = self._calculate_domain_centroid(node_ids)

        # Initialize dictionaries and lists for valid indices
        valid_indices = []  # List of valid indices to plot colors and arrows
        filtered_domain_centroids = {}  # Filtered domain centroids to plot
        filtered_domain_terms = {}  # Filtered domain terms to plot
        # Handle the ids_to_keep logic
        if ids_to_keep:
            # Process the ids_to_keep first INPLACE
            self._process_ids_to_keep(
                domain_id_to_centroid_map=domain_id_to_centroid_map,
                ids_to_keep=ids_to_keep,
                ids_to_replace=ids_to_replace,
                words_to_omit=words_to_omit,
                max_labels=max_labels,
                min_label_lines=min_label_lines,
                max_label_lines=max_label_lines,
                min_chars_per_line=min_chars_per_line,
                max_chars_per_line=max_chars_per_line,
                filtered_domain_centroids=filtered_domain_centroids,
                filtered_domain_terms=filtered_domain_terms,
                valid_indices=valid_indices,
            )

        # Calculate remaining labels to plot after processing ids_to_keep
        remaining_labels = (
            max_labels - len(valid_indices) if valid_indices and max_labels else max_labels
        )
        # Process remaining domains INPLACE to fill in additional labels, if there are slots left
        if remaining_labels and remaining_labels > 0:
            self._process_remaining_domains(
                domain_id_to_centroid_map=domain_id_to_centroid_map,
                ids_to_keep=ids_to_keep,
                ids_to_replace=ids_to_replace,
                words_to_omit=words_to_omit,
                remaining_labels=remaining_labels,
                min_chars_per_line=min_chars_per_line,
                max_chars_per_line=max_chars_per_line,
                max_label_lines=max_label_lines,
                min_label_lines=min_label_lines,
                filtered_domain_centroids=filtered_domain_centroids,
                filtered_domain_terms=filtered_domain_terms,
                valid_indices=valid_indices,
            )

        # Calculate the bounding box around the network
        center, radius = calculate_bounding_box(self.graph.node_coordinates, radius_margin=scale)
        # Calculate the best positions for labels
        best_label_positions = _calculate_best_label_positions(
            filtered_domain_centroids, center, radius, offset
        )
        # Convert all domain colors to RGBA using the to_rgba helper function
        fontcolor = to_rgba(
            color=fontcolor, alpha=fontalpha, num_repeats=len(self.graph.domain_id_to_node_ids_map)
        )
        arrow_color = to_rgba(
            color=arrow_color,
            alpha=arrow_alpha,
            num_repeats=len(self.graph.domain_id_to_node_ids_map),
        )

        # Annotate the network with labels
        for idx, (domain, pos) in zip(valid_indices, best_label_positions.items()):
            centroid = filtered_domain_centroids[domain]
            # Split by special key TERM_DELIMITER to split annotation into multiple lines
            annotations = filtered_domain_terms[domain].split(TERM_DELIMITER)
            if fontcase is not None:
                annotations = _apply_str_transformation(words=annotations, transformation=fontcase)
            self.ax.annotate(
                "\n".join(annotations),
                xy=centroid,
                xytext=pos,
                textcoords="data",
                ha="center",
                va="center",
                fontsize=fontsize,
                fontname=font,
                color=fontcolor[idx],
                arrowprops=dict(
                    arrowstyle=arrow_style,
                    color=arrow_color[idx],
                    linewidth=arrow_linewidth,
                    shrinkA=arrow_base_shrink,
                    shrinkB=arrow_tip_shrink,
                ),
            )

        # Overlay domain ID at the centroid regardless of max_labels if requested
        if overlay_ids:
            for idx, domain in enumerate(self.graph.domain_id_to_node_ids_map):
                centroid = domain_id_to_centroid_map[domain]
                self.ax.text(
                    centroid[0],
                    centroid[1],
                    domain,
                    ha="center",
                    va="center",
                    fontsize=fontsize,
                    fontname=font,
                    color=fontcolor[idx],
                    alpha=fontalpha,
                )

    def plot_sublabel(
        self,
        nodes: Union[List, Tuple, np.ndarray],
        label: str,
        radial_position: float = 0.0,
        scale: float = 1.05,
        offset: float = 0.10,
        font: str = "Arial",
        fontsize: int = 10,
        fontcolor: Union[str, List, Tuple, np.ndarray] = "black",
        fontalpha: Union[float, None] = 1.0,
        arrow_linewidth: float = 1,
        arrow_style: str = "->",
        arrow_color: Union[str, List, Tuple, np.ndarray] = "black",
        arrow_alpha: Union[float, None] = 1.0,
        arrow_base_shrink: float = 0.0,
        arrow_tip_shrink: float = 0.0,
    ) -> None:
        """Annotate the network graph with a label for the given nodes, with one arrow pointing to each centroid of sublists of nodes.

        Args:
            nodes (list, tuple, or np.ndarray): List of node labels or list of lists of node labels.
            label (str): The label to be annotated on the network.
            radial_position (float, optional): Radial angle for positioning the label, in degrees (0-360). Defaults to 0.0.
            scale (float, optional): Scale factor for positioning the label around the perimeter. Defaults to 1.05.
            offset (float, optional): Offset distance for the label from the perimeter. Defaults to 0.10.
            font (str, optional): Font name for the label. Defaults to "Arial".
            fontsize (int, optional): Font size for the label. Defaults to 10.
            fontcolor (str, list, tuple, or np.ndarray, optional): Color of the label text. Defaults to "black".
            fontalpha (float, None, optional): Transparency level for the font color. If provided, it overrides any existing alpha values found
                in fontalpha. Defaults to 1.0.
            arrow_linewidth (float, optional): Line width of the arrow pointing to the centroid. Defaults to 1.
            arrow_style (str, optional): Style of the arrows pointing to the centroid. Defaults to "->".
            arrow_color (str, list, tuple, or np.ndarray, optional): Color of the arrow. Defaults to "black".
            arrow_alpha (float, None, optional): Transparency level for the arrow color. If provided, it overrides any existing alpha values
                found in arrow_alpha. Defaults to 1.0.
            arrow_base_shrink (float, optional): Distance between the text and the base of the arrow. Defaults to 0.0.
            arrow_tip_shrink (float, optional): Distance between the arrow tip and the centroid. Defaults to 0.0.
        """
        # Check if nodes is a list of lists or a flat list
        if any(isinstance(item, (list, tuple, np.ndarray)) for item in nodes):
            # If it's a list of lists, iterate over sublists
            node_groups = nodes
        else:
            # If it's a flat list of nodes, treat it as a single group
            node_groups = [nodes]

        # Convert fontcolor and arrow_color to RGBA
        fontcolor_rgba = to_rgba(color=fontcolor, alpha=fontalpha)
        arrow_color_rgba = to_rgba(color=arrow_color, alpha=arrow_alpha)

        # Calculate the bounding box around the network
        center, radius = calculate_bounding_box(self.graph.node_coordinates, radius_margin=scale)
        # Convert radial position to radians, adjusting for a 90-degree rotation
        radial_radians = np.deg2rad(radial_position - 90)
        label_position = (
            center[0] + (radius + offset) * np.cos(radial_radians),
            center[1] + (radius + offset) * np.sin(radial_radians),
        )

        # Iterate over each group of nodes (either sublists or flat list)
        for sublist in node_groups:
            # Map node labels to IDs
            node_ids = [
                self.graph.node_label_to_node_id_map.get(node)
                for node in sublist
                if node in self.graph.node_label_to_node_id_map
            ]
            if not node_ids or len(node_ids) == 1:
                raise ValueError(
                    "No nodes found in the network graph or insufficient nodes to plot."
                )

            # Calculate the centroid of the provided nodes in this sublist
            centroid = self._calculate_domain_centroid(node_ids)
            # Annotate the network with the label and an arrow pointing to each centroid
            self.ax.annotate(
                label,
                xy=centroid,
                xytext=label_position,
                textcoords="data",
                ha="center",
                va="center",
                fontsize=fontsize,
                fontname=font,
                color=fontcolor_rgba,
                arrowprops=dict(
                    arrowstyle=arrow_style,
                    color=arrow_color_rgba,
                    linewidth=arrow_linewidth,
                    shrinkA=arrow_base_shrink,
                    shrinkB=arrow_tip_shrink,
                ),
            )

    def _calculate_domain_centroid(self, nodes: List) -> tuple:
        """Calculate the most centrally located node in .

        Args:
            nodes (list): List of node labels to include in the subnetwork.

        Returns:
            tuple: A tuple containing the domain's central node coordinates.
        """
        # Extract positions of all nodes in the domain
        node_positions = self.graph.node_coordinates[nodes, :]
        # Calculate the pairwise distance matrix between all nodes in the domain
        distances_matrix = np.linalg.norm(node_positions[:, np.newaxis] - node_positions, axis=2)
        # Sum the distances for each node to all other nodes in the domain
        sum_distances = np.sum(distances_matrix, axis=1)
        # Identify the node with the smallest total distance to others (the centroid)
        central_node_idx = np.argmin(sum_distances)
        # Map the domain to the coordinates of its central node
        domain_central_node = node_positions[central_node_idx]
        return domain_central_node

    def _process_ids_to_keep(
        self,
        domain_id_to_centroid_map: Dict[str, np.ndarray],
        ids_to_keep: Union[List[str], Tuple[str], np.ndarray],
        ids_to_replace: Union[Dict[str, str], None],
        words_to_omit: Union[List[str], None],
        max_labels: Union[int, None],
        min_label_lines: int,
        max_label_lines: int,
        min_chars_per_line: int,
        max_chars_per_line: int,
        filtered_domain_centroids: Dict[str, np.ndarray],
        filtered_domain_terms: Dict[str, str],
        valid_indices: List[int],
    ) -> None:
        """Process the ids_to_keep, apply filtering, and store valid domain centroids and terms.

        Args:
            domain_id_to_centroid_map (dict): Mapping of domain IDs to their centroids.
            ids_to_keep (list, tuple, or np.ndarray, optional): IDs of domains that must be labeled.
            ids_to_replace (dict, optional): A dictionary mapping domain IDs to custom labels. Defaults to None.
            words_to_omit (list, optional): List of words to omit from the labels. Defaults to None.
            max_labels (int, optional): Maximum number of labels allowed.
            min_label_lines (int): Minimum number of lines in a label.
            max_label_lines (int): Maximum number of lines in a label.
            min_chars_per_line (int): Minimum number of characters in a line to display.
            max_chars_per_line (int): Maximum number of characters in a line to display.
            filtered_domain_centroids (dict): Dictionary to store filtered domain centroids (output).
            filtered_domain_terms (dict): Dictionary to store filtered domain terms (output).
            valid_indices (list): List to store valid indices (output).

        Note:
            The `filtered_domain_centroids`, `filtered_domain_terms`, and `valid_indices` are modified in-place.

        Raises:
            ValueError: If the number of provided `ids_to_keep` exceeds `max_labels`.
        """
        # Check if the number of provided ids_to_keep exceeds max_labels
        if max_labels is not None and len(ids_to_keep) > max_labels:
            raise ValueError(
                f"Number of provided IDs ({len(ids_to_keep)}) exceeds max_labels ({max_labels})."
            )

        # Process each domain in ids_to_keep
        for domain in ids_to_keep:
            if (
                domain in self.graph.domain_id_to_domain_terms_map
                and domain in domain_id_to_centroid_map
            ):
                domain_centroid = domain_id_to_centroid_map[domain]
                # No need to filter the domain terms if it is in ids_to_keep
                _ = self._validate_and_update_domain(
                    domain=domain,
                    domain_centroid=domain_centroid,
                    domain_id_to_centroid_map=domain_id_to_centroid_map,
                    ids_to_replace=ids_to_replace,
                    words_to_omit=words_to_omit,
                    min_label_lines=min_label_lines,
                    max_label_lines=max_label_lines,
                    min_chars_per_line=min_chars_per_line,
                    max_chars_per_line=max_chars_per_line,
                    filtered_domain_centroids=filtered_domain_centroids,
                    filtered_domain_terms=filtered_domain_terms,
                    valid_indices=valid_indices,
                )

    def _process_remaining_domains(
        self,
        domain_id_to_centroid_map: Dict[str, np.ndarray],
        ids_to_keep: Union[List[str], Tuple[str], np.ndarray],
        ids_to_replace: Union[Dict[str, str], None],
        words_to_omit: Union[List[str], None],
        remaining_labels: int,
        min_label_lines: int,
        max_label_lines: int,
        min_chars_per_line: int,
        max_chars_per_line: int,
        filtered_domain_centroids: Dict[str, np.ndarray],
        filtered_domain_terms: Dict[str, str],
        valid_indices: List[int],
    ) -> None:
        """Process remaining domains to fill in additional labels, respecting the remaining_labels limit.

        Args:
            domain_id_to_centroid_map (dict): Mapping of domain IDs to their centroids.
            ids_to_keep (list, tuple, or np.ndarray, optional): IDs of domains that must be labeled.
            ids_to_replace (dict, optional): A dictionary mapping domain IDs to custom labels. Defaults to None.
            words_to_omit (list, optional): List of words to omit from the labels. Defaults to None.
            remaining_labels (int): The remaining number of labels that can be generated.
            min_label_lines (int): Minimum number of lines in a label.
            max_label_lines (int): Maximum number of lines in a label.
            min_chars_per_line (int): Minimum number of characters in a line to display.
            max_chars_per_line (int): Maximum number of characters in a line to display.
            filtered_domain_centroids (dict): Dictionary to store filtered domain centroids (output).
            filtered_domain_terms (dict): Dictionary to store filtered domain terms (output).
            valid_indices (list): List to store valid indices (output).

        Note:
            The `filtered_domain_centroids`, `filtered_domain_terms`, and `valid_indices` are modified in-place.
        """
        # Counter to track how many labels have been created
        label_count = 0
        # Collect domains not in ids_to_keep
        remaining_domains = {
            domain: centroid
            for domain, centroid in domain_id_to_centroid_map.items()
            if domain not in ids_to_keep and not pd.isna(domain)
        }

        # Function to calculate distance between two centroids
        def calculate_distance(centroid1, centroid2):
            return np.linalg.norm(centroid1 - centroid2)

        # Domains to plot on network
        selected_domains = []
        # Find the farthest apart domains using centroids
        if remaining_domains and remaining_labels:
            first_domain = next(iter(remaining_domains))  # Pick the first domain to start
            selected_domains.append(first_domain)

            while len(selected_domains) < remaining_labels:
                farthest_domain = None
                max_distance = -1
                # Find the domain farthest from any already selected domain
                for candidate_domain, candidate_centroid in remaining_domains.items():
                    if candidate_domain in selected_domains:
                        continue

                    # Calculate the minimum distance to any selected domain
                    min_distance = min(
                        calculate_distance(candidate_centroid, remaining_domains[dom])
                        for dom in selected_domains
                    )
                    # Update the farthest domain if the minimum distance is greater
                    if min_distance > max_distance:
                        max_distance = min_distance
                        farthest_domain = candidate_domain

                # Add the farthest domain to the selected domains
                if farthest_domain:
                    selected_domains.append(farthest_domain)
                else:
                    break  # No more domains to select

        # Process the selected domains and add to filtered lists
        for domain in selected_domains:
            domain_centroid = remaining_domains[domain]
            is_domain_valid = self._validate_and_update_domain(
                domain=domain,
                domain_centroid=domain_centroid,
                domain_id_to_centroid_map=domain_id_to_centroid_map,
                ids_to_replace=ids_to_replace,
                words_to_omit=words_to_omit,
                min_label_lines=min_label_lines,
                max_label_lines=max_label_lines,
                min_chars_per_line=min_chars_per_line,
                max_chars_per_line=max_chars_per_line,
                filtered_domain_centroids=filtered_domain_centroids,
                filtered_domain_terms=filtered_domain_terms,
                valid_indices=valid_indices,
            )
            # Increment the label count if the domain is valid
            if is_domain_valid:
                label_count += 1
                if label_count >= remaining_labels:
                    break

    def _validate_and_update_domain(
        self,
        domain: str,
        domain_centroid: np.ndarray,
        domain_id_to_centroid_map: Dict[str, np.ndarray],
        ids_to_replace: Union[Dict[str, str], None],
        words_to_omit: Union[List[str], None],
        min_label_lines: int,
        max_label_lines: int,
        min_chars_per_line: int,
        max_chars_per_line: int,
        filtered_domain_centroids: Dict[str, np.ndarray],
        filtered_domain_terms: Dict[str, str],
        valid_indices: List[int],
    ) -> bool:
        """Validate and process the domain terms, updating relevant dictionaries if valid.

        Args:
            domain (str): Domain ID to process.
            domain_centroid (np.ndarray): Centroid position of the domain.
            domain_id_to_centroid_map (dict): Mapping of domain IDs to their centroids.
            ids_to_replace (Union[Dict[str, str], None]): A dictionary mapping domain IDs to custom labels.
            words_to_omit (Union[List[str], None]): List of words to omit from the labels.
            min_label_lines (int): Minimum number of lines required in a label.
            max_label_lines (int): Maximum number of lines allowed in a label.
            min_chars_per_line (int): Minimum number of characters allowed per line.
            max_chars_per_line (int): Maximum number of characters allowed per line.
            filtered_domain_centroids (Dict[str, np.ndarray]): Dictionary to store valid domain centroids.
            filtered_domain_terms (Dict[str, str]): Dictionary to store valid domain terms.
            valid_indices (List[int]): List of valid domain indices.

        Returns:
            bool: True if the domain is valid and added to the filtered dictionaries, False otherwise.

        Note:
            The `filtered_domain_centroids`, `filtered_domain_terms`, and `valid_indices` are modified in-place.
        """
        # Process the domain terms
        domain_terms = self._process_terms(
            domain=domain,
            ids_to_replace=ids_to_replace,
            words_to_omit=words_to_omit,
            max_label_lines=max_label_lines,
            min_chars_per_line=min_chars_per_line,
            max_chars_per_line=max_chars_per_line,
        )
        # If domain_terms is empty, skip further processing
        if not domain_terms:
            return False

        # Split the terms by TERM_DELIMITER and count the number of lines
        num_domain_lines = len(domain_terms.split(TERM_DELIMITER))
        # Check if the number of lines is greater than or equal to the minimum
        if num_domain_lines >= min_label_lines:
            filtered_domain_centroids[domain] = domain_centroid
            filtered_domain_terms[domain] = domain_terms
            # Add the index of the domain to the valid indices list
            valid_indices.append(list(domain_id_to_centroid_map.keys()).index(domain))
            return True

        return False

    def _process_terms(
        self,
        domain: str,
        ids_to_replace: Union[Dict[str, str], None],
        words_to_omit: Union[List[str], None],
        max_label_lines: int,
        min_chars_per_line: int,
        max_chars_per_line: int,
    ) -> List[str]:
        """Process terms for a domain, applying word length constraints and combining words where appropriate.

        Args:
            domain (str): The domain being processed.
            ids_to_replace (dict, optional): Dictionary mapping domain IDs to custom labels.
            words_to_omit (list, optional): List of words to omit from the labels.
            max_label_lines (int): Maximum number of lines in a label.
            min_chars_per_line (int): Minimum number of characters in a line to display.
            max_chars_per_line (int): Maximum number of characters in a line to display.

        Returns:
            str: Processed terms separated by TERM_DELIMITER, with words combined if necessary to fit within constraints.
        """
        # Handle ids_to_replace logic
        if ids_to_replace and domain in ids_to_replace:
            terms = ids_to_replace[domain].split(" ")
        else:
            terms = self.graph.domain_id_to_domain_terms_map[domain].split(" ")

        # Apply words_to_omit and word length constraints
        if words_to_omit:
            terms = [
                term
                for term in terms
                if term.lower() not in words_to_omit and len(term) >= min_chars_per_line
            ]

        # Use the combine_words function directly to handle word combinations and length constraints
        compressed_terms = _combine_words(tuple(terms), max_chars_per_line, max_label_lines)

        return compressed_terms

    def get_annotated_label_colors(
        self,
        cmap: str = "gist_rainbow",
        color: Union[str, None] = None,
        min_scale: float = 0.8,
        max_scale: float = 1.0,
        scale_factor: float = 1.0,
        random_seed: int = 888,
    ) -> np.ndarray:
        """Get colors for the labels based on node annotations or a specified colormap.

        Args:
            cmap (str, optional): Name of the colormap to use for generating label colors. Defaults to "gist_rainbow".
            color (str or None, optional): Color to use for the labels. If None, the colormap will be used. Defaults to None.
            min_scale (float, optional): Minimum intensity scale for the colors generated by the colormap.
                Controls the dimmest colors. Defaults to 0.8.
            max_scale (float, optional): Maximum intensity scale for the colors generated by the colormap.
                Controls the brightest colors. Defaults to 1.0.
            scale_factor (float, optional): Exponent for adjusting color scaling based on enrichment scores.
                A higher value increases contrast by dimming lower scores more. Defaults to 1.0.
            random_seed (int, optional): Seed for random number generation to ensure reproducibility. Defaults to 888.

        Returns:
            np.ndarray: Array of RGBA colors for label annotations.
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


def _combine_words(words: List[str], max_chars_per_line: int, max_label_lines: int) -> str:
    """Combine words to fit within the max_chars_per_line and max_label_lines constraints,
    and separate the final output by TERM_DELIMITER for plotting.

    Args:
        words (List[str]): List of words to combine.
        max_chars_per_line (int): Maximum number of characters in a line to display.
        max_label_lines (int): Maximum number of lines in a label.

    Returns:
        str: String of combined words separated by ':' for line breaks.
    """

    def try_combinations(words_batch: List[str]) -> List[str]:
        """Try to combine words within a batch and return them with combined words separated by ':'."""
        combined_lines = []
        i = 0
        while i < len(words_batch):
            current_word = words_batch[i]
            combined_word = current_word  # Start with the current word
            # Try to combine more words if possible, and ensure the combination fits within max_length
            for j in range(i + 1, len(words_batch)):
                next_word = words_batch[j]
                # Ensure that the combined word fits within the max_chars_per_line limit
                if len(combined_word) + len(next_word) + 1 <= max_chars_per_line:  # +1 for space
                    combined_word = f"{combined_word} {next_word}"
                    i += 1  # Move past the combined word
                else:
                    break  # Stop combining if the length is exceeded

            # Add the combined word only if it fits within the max_chars_per_line limit
            if len(combined_word) <= max_chars_per_line:
                combined_lines.append(combined_word)  # Add the combined word
            # Move to the next word
            i += 1

            # Stop if we've reached the max_label_lines limit
            if len(combined_lines) >= max_label_lines:
                break

        return combined_lines

    # Main logic: start with max_label_lines number of words
    combined_lines = try_combinations(words[:max_label_lines])
    remaining_words = words[max_label_lines:]  # Remaining words after the initial batch

    # Continue pulling more words until we fill the lines
    while remaining_words and len(combined_lines) < max_label_lines:
        available_slots = max_label_lines - len(combined_lines)
        words_to_add = remaining_words[:available_slots]
        remaining_words = remaining_words[available_slots:]
        combined_lines += try_combinations(words_to_add)

    # Join the final combined lines with TERM_DELIMITER, a special separator for line breaks
    return TERM_DELIMITER.join(combined_lines[:max_label_lines])


def _calculate_best_label_positions(
    filtered_domain_centroids: Dict[str, Any], center: np.ndarray, radius: float, offset: float
) -> Dict[str, Any]:
    """Calculate and optimize label positions for clarity.

    Args:
        filtered_domain_centroids (dict): Centroids of the filtered domains.
        center (np.ndarray): The center coordinates for label positioning.
        radius (float): The radius for positioning labels around the center.
        offset (float): The offset distance from the radius for positioning labels.

    Returns:
        dict: Optimized positions for labels.
    """
    num_domains = len(filtered_domain_centroids)
    # Calculate equidistant positions around the center for initial label placement
    equidistant_positions = _calculate_equidistant_positions_around_center(
        center, radius, offset, num_domains
    )
    # Create a mapping of domains to their initial label positions
    label_positions = {
        domain: position
        for domain, position in zip(filtered_domain_centroids.keys(), equidistant_positions)
    }
    # Optimize the label positions to minimize distance to domain centroids
    return _optimize_label_positions(label_positions, filtered_domain_centroids)


def _calculate_equidistant_positions_around_center(
    center: np.ndarray, radius: float, label_offset: float, num_domains: int
) -> List[np.ndarray]:
    """Calculate positions around a center at equidistant angles.

    Args:
        center (np.ndarray): The central point around which positions are calculated.
        radius (float): The radius at which positions are calculated.
        label_offset (float): The offset added to the radius for label positioning.
        num_domains (int): The number of positions (or domains) to calculate.

    Returns:
        list[np.ndarray]: List of positions (as 2D numpy arrays) around the center.
    """
    # Calculate equidistant angles in radians around the center
    angles = np.linspace(0, 2 * np.pi, num_domains, endpoint=False)
    # Compute the positions around the center using the angles
    return [
        center + (radius + label_offset) * np.array([np.cos(angle), np.sin(angle)])
        for angle in angles
    ]


def _optimize_label_positions(
    best_label_positions: Dict[str, Any], domain_centroids: Dict[str, Any]
) -> Dict[str, Any]:
    """Optimize label positions around the perimeter to minimize total distance to centroids.

    Args:
        best_label_positions (dict): Initial positions of labels around the perimeter.
        domain_centroids (dict): Centroid positions of the domains.

    Returns:
        dict: Optimized label positions.
    """
    while True:
        improvement = False  # Start each iteration assuming no improvement
        # Iterate through each pair of labels to check for potential improvements
        for i in range(len(domain_centroids)):
            for j in range(i + 1, len(domain_centroids)):
                # Calculate the current total distance
                current_distance = _calculate_total_distance(best_label_positions, domain_centroids)
                # Evaluate the total distance after swapping two labels
                swapped_distance = _swap_and_evaluate(best_label_positions, i, j, domain_centroids)
                # If the swap improves the total distance, perform the swap
                if swapped_distance < current_distance:
                    labels = list(best_label_positions.keys())
                    best_label_positions[labels[i]], best_label_positions[labels[j]] = (
                        best_label_positions[labels[j]],
                        best_label_positions[labels[i]],
                    )
                    improvement = True  # Found an improvement, so continue optimizing

        if not improvement:
            break  # Exit the loop if no improvement was found in this iteration

    return best_label_positions


def _calculate_total_distance(
    label_positions: Dict[str, Any], domain_centroids: Dict[str, Any]
) -> float:
    """Calculate the total distance from label positions to their domain centroids.

    Args:
        label_positions (dict): Positions of labels around the perimeter.
        domain_centroids (dict): Centroid positions of the domains.

    Returns:
        float: The total distance from labels to centroids.
    """
    total_distance = 0
    # Iterate through each domain and calculate the distance to its centroid
    for domain, pos in label_positions.items():
        centroid = domain_centroids[domain]
        total_distance += np.linalg.norm(centroid - pos)

    return total_distance


def _swap_and_evaluate(
    label_positions: Dict[str, Any],
    i: int,
    j: int,
    domain_centroids: Dict[str, Any],
) -> float:
    """Swap two labels and evaluate the total distance after the swap.

    Args:
        label_positions (dict): Positions of labels around the perimeter.
        i (int): Index of the first label to swap.
        j (int): Index of the second label to swap.
        domain_centroids (dict): Centroid positions of the domains.

    Returns:
        float: The total distance after swapping the two labels.
    """
    # Get the list of labels from the dictionary keys
    labels = list(label_positions.keys())
    swapped_positions = label_positions.copy()
    # Swap the positions of the two specified labels
    swapped_positions[labels[i]], swapped_positions[labels[j]] = (
        swapped_positions[labels[j]],
        swapped_positions[labels[i]],
    )
    # Calculate and return the total distance after the swap
    return _calculate_total_distance(swapped_positions, domain_centroids)


def _apply_str_transformation(words: List[str], transformation: str) -> List[str]:
    """Apply a user-specified case transformation to each word in the list without appending duplicates.

    Args:
        words (List[str]): A list of words to transform.
        transformation (str): The case transformation to apply (e.g., 'lower', 'upper', 'title', 'capitalize').

    Returns:
        List[str]: A list of transformed words with no duplicates.
    """
    transformed_words = []
    for word in words:
        if hasattr(word, transformation):
            transformed_word = getattr(word, transformation)()  # Apply the string method

            # Only append if the transformed word is not already in the list
            if transformed_word not in transformed_words:
                transformed_words.append(transformed_word)

    return transformed_words
