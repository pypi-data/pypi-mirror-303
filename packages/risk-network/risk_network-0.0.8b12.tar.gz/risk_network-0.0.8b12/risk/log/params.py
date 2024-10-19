"""
risk/log/params
~~~~~~~~~~~~~~~
"""

import csv
import json
import warnings
from datetime import datetime
from functools import wraps
from typing import Any, Dict

import numpy as np

from .config import logger, log_header

# Suppress all warnings - this is to resolve warnings from multiprocessing
warnings.filterwarnings("ignore")


def _safe_param_export(func):
    """A decorator to wrap parameter export functions in a try-except block for safe execution.

    Args:
        func (function): The function to be wrapped.

    Returns:
        function: The wrapped function with error handling.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            filepath = (
                kwargs.get("filepath") or args[1]
            )  # Assuming filepath is always the second argument
            logger.info(f"Parameters successfully exported to filepath: {filepath}")
            return result
        except Exception as e:
            filepath = kwargs.get("filepath") or args[1]
            logger.error(f"An error occurred while exporting parameters to {filepath}: {e}")
            return None

    return wrapper


class Params:
    """Handles the storage and logging of various parameters for network analysis.

    The Params class provides methods to log parameters related to different components of the analysis,
    such as the network, annotations, neighborhoods, graph, and plotter settings. It also stores
    the current datetime when the parameters were initialized.
    """

    def __init__(self):
        """Initialize the Params object with default settings and current datetime."""
        self.initialize()
        self.datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def initialize(self) -> None:
        """Initialize the parameter dictionaries for different components."""
        self.network = {}
        self.annotations = {}
        self.neighborhoods = {}
        self.graph = {}
        self.plotter = {}

    def log_network(self, **kwargs) -> None:
        """Log network-related parameters.

        Args:
            **kwargs: Network parameters to log.
        """
        self.network = {**self.network, **kwargs}

    def log_annotations(self, **kwargs) -> None:
        """Log annotation-related parameters.

        Args:
            **kwargs: Annotation parameters to log.
        """
        self.annotations = {**self.annotations, **kwargs}

    def log_neighborhoods(self, **kwargs) -> None:
        """Log neighborhood-related parameters.

        Args:
            **kwargs: Neighborhood parameters to log.
        """
        self.neighborhoods = {**self.neighborhoods, **kwargs}

    def log_graph(self, **kwargs) -> None:
        """Log graph-related parameters.

        Args:
            **kwargs: Graph parameters to log.
        """
        self.graph = {**self.graph, **kwargs}

    def log_plotter(self, **kwargs) -> None:
        """Log plotter-related parameters.

        Args:
            **kwargs: Plotter parameters to log.
        """
        self.plotter = {**self.plotter, **kwargs}

    @_safe_param_export
    def to_csv(self, filepath: str) -> None:
        """Export the parameters to a CSV file.

        Args:
            filepath (str): The path where the CSV file will be saved.
        """
        # Load the parameter dictionary
        params = self.load()
        # Open the file in write mode
        with open(filepath, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            # Write the header
            writer.writerow(["parent_key", "child_key", "value"])
            # Write the rows
            for parent_key, parent_value in params.items():
                if isinstance(parent_value, dict):
                    for child_key, child_value in parent_value.items():
                        writer.writerow([parent_key, child_key, child_value])
                else:
                    writer.writerow([parent_key, "", parent_value])

    @_safe_param_export
    def to_json(self, filepath: str) -> None:
        """Export the parameters to a JSON file.

        Args:
            filepath (str): The path where the JSON file will be saved.
        """
        with open(filepath, "w") as json_file:
            json.dump(self.load(), json_file, indent=4)

    @_safe_param_export
    def to_txt(self, filepath: str) -> None:
        """Export the parameters to a text file.

        Args:
            filepath (str): The path where the text file will be saved.
        """
        # Load the parameter dictionary
        params = self.load()
        # Open the file in write mode
        with open(filepath, "w") as txt_file:
            for key, value in params.items():
                # Write the key and its corresponding value
                txt_file.write(f"{key}: {value}\n")
            # Add a blank line after each entry
            txt_file.write("\n")

    def load(self) -> Dict[str, Any]:
        """Load and process various parameters, converting any np.ndarray values to lists.

        Returns:
            dict: A dictionary containing the processed parameters.
        """
        log_header("Loading parameters")
        return _convert_ndarray_to_list(
            {
                "annotations": self.annotations,
                "datetime": self.datetime,
                "graph": self.graph,
                "neighborhoods": self.neighborhoods,
                "network": self.network,
                "plotter": self.plotter,
            }
        )


def _convert_ndarray_to_list(d: Any) -> Any:
    """Recursively convert all np.ndarray values in the dictionary to lists.

    Args:
        d (dict): The dictionary to process.

    Returns:
        dict: The processed dictionary with np.ndarray values converted to lists.
    """
    if isinstance(d, dict):
        # Recursively process each value in the dictionary
        return {k: _convert_ndarray_to_list(v) for k, v in d.items()}
    elif isinstance(d, list):
        # Recursively process each item in the list
        return [_convert_ndarray_to_list(v) for v in d]
    elif isinstance(d, np.ndarray):
        # Convert numpy arrays to lists
        return d.tolist()
    else:
        # Return the value unchanged if it's not a dict, list, or ndarray
        return d
