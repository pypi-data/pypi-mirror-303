from pathlib import Path
from typing import Dict, List, Union

import matplotlib
import matplotlib.backend_bases
import matplotlib.pyplot as plt
import numpy as np
import rich_click as click
from ase import Atoms
from ase.io import read
from ase.visualize import view
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from rich import print


class EventHandler:
    def __init__(
        self, search_analysis: "SearchAnalysis", axis_dict: Dict[str, Axes], figure: Figure, configurations: List[Atoms]
    ) -> None:
        self.search_analysis = search_analysis
        self.axis_dict = axis_dict
        self.fig = figure

        self.image = 0
        self.total_images = len(configurations)
        self.configurations = configurations
        self.plane = "xy"

    def on_press(self, event: matplotlib.backend_bases.KeyEvent) -> None:
        if event.key == "right":
            self.image += 1
        elif event.key == "left":
            self.image -= 1
        elif event.key == "z":
            self.plane = "xy"
        elif event.key == "x":
            self.plane = "yz"
        elif event.key == "y":
            self.plane = "xz"

        self.image = np.clip(self.image, 0, self.total_images - 1)

        self.image_update()

    def image_update(self) -> None:
        self.axis_dict["configuration"].clear()
        self.search_analysis.plot_configuration(
            ax=self.axis_dict["configuration"], candidate=self.configurations[self.image], plane=self.plane
        )
        self.fig.canvas.draw()


@click.command(name="plot")
@click.argument("file", nargs=1, type=click.Path(exists=True))
@click.option("--output", "-o", type=click.Path(), help="Output file", default=None)
@click.option("--backend", "-b", type=str, help="Matplotlib backend.", default="TkAgg")
@click.option("--ase", "-a", is_flag=True, help="Use ASE to plot the structures.", default=False)
def cli_plot(file: str, output: Union[str, None], backend: str, ase: bool) -> None:
    """
    Plot structures from database or trajectory files.
    """
    from agox.analysis.search_analysis import SearchAnalysis
    from agox.databases.database_utilities import convert_database_to_traj

    matplotlib.use(backend)

    # Read the file:
    file = Path(file)
    if file.suffix == ".db":
        configurations = convert_database_to_traj(file)
    elif file.suffix == ".traj":
        configurations = read(file, ":")
    else:
        print("File type not")

    # # Create figure:
    if not ase:
        fig, ax = plt.subplots(1, 1, figsize=(6, 6))
        search_analysis = SearchAnalysis()
        search_analysis.plot_configuration(ax, candidate=configurations[0])

        # Create event handler:
        event_handler = EventHandler(search_analysis, {"configuration": ax}, fig, configurations)
        fig.canvas.mpl_connect("key_press_event", event_handler.on_press)

        if output is not None:
            plt.savefig(output)

        plt.show()
    else:
        view(configurations)
