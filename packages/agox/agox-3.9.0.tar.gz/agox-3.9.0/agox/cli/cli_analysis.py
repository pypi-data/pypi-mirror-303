from collections import OrderedDict
from typing import Dict

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import rich_click as click
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from rich import print


class EventHandler:
    def __init__(self, search_analysis: "SearchAnalysis", axis_dict: Dict[str, Axes], fig: Figure) -> None:
        self.search_analysis = search_analysis
        self.axis_dict = axis_dict
        self.fig = fig

        self.total_images = search_analysis.get_number_of_best_candidates()
        self.image = 0
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
        self.search_analysis.plot_configuration(ax=self.axis_dict["configuration"], image=self.image, plane=self.plane)

        if "distribution" in self.axis_dict:
            self.search_analysis.update_hist_line(image=self.image)

        self.fig.canvas.draw()


option_groups = {"agox analysis": []}
option_groups["agox analysis"].append({"name": "File options", "options": ["--reload"]})
option_groups["agox analysis"].append(
    {
        "name": "Plot options",
        "options": [
            "--backend",
            "--success",
            "--configuration",
            "--energy",
            "--distribution",
        ],
    }
)
option_groups["agox analysis"].append(
    {
        "name": "Analysis options",
        "options": ["--delta-total", "--delta-atom", "--property_name", "--thermodynamics-file", "--criterion"],
    }
)
click.rich_click.OPTION_GROUPS.update(option_groups)


@click.command("analysis")  # fmt: skip
@click.argument("directories", nargs=-1, type=click.Path(exists=True))  # fmt: skip
@click.option("--reload", "-r", is_flag=True, help="Reload the searches", default=False, show_default=True)  # fmt: skip
@click.option("--backend", "-b", type=str, help="Matplotlib backend", default="TkAgg", show_default=True)  # fmt: skip
@click.option("--success", "-s",help="Plot CDF (success curve).", is_flag=True, default=True, show_default=True, type=bool)  # fmt: skip
@click.option("--configuration", "-c", help="Plot the structures.", is_flag=True, default=True, show_default=True, type=bool)  # fmt: skip
@click.option("--energy", "-e", help="Plot the energies.", is_flag=True, default=True, show_default=True, type=bool)  # fmt: skip
@click.option("--distribution", "-d",help="Plot the distribution.", is_flag=True, default=False, show_default=True, type=bool)  # fmt: skip
@click.option("--delta-total", "-dE", help="Threshold for success in eV. Used if criteria is 'energy'.", type=float, default=1.0, show_default=True)  # fmt: skip
@click.option("--delta-atom", "-de", help="Threshold for success in eV/atom, overwrites delta-total if given", type=float, default=np.nan, show_default=True)  # fmt: skip
@click.option("--property-name", "-p", type=click.Choice(["Energy", "FreeEnergy"], case_sensitive=False), default="Energy", show_default=True, help="Property to consider")  # fmt: skip
@click.option("--criterion", "-c", type=click.Choice(["energy", "graph"], case_sensitive=False), default="energy", show_default=True, help="Criterion used to calculate success curve.")  # fmt: skip
@click.option("--thermodynamics-file", "-t", type=click.Path(exists=True), help="The thermodynamics json file that specifies references and chemical potentials to use for free energy")  # fmt: skip
def cli_analysis(
    directories: str,
    reload: bool,
    backend: str,
    success: bool,
    configuration: bool,
    energy: bool,
    distribution: bool,
    delta_total: float,
    delta_atom: float,
    property_name: str,
    criterion: str,
    thermodynamics_file: str,
) -> None:
    """
    Perform basic analysis of searches.
    """
    from timeit import default_timer as dt

    from agox.analysis import DistanceCriterion, SearchCollection, ThresholdCriterion
    from agox.analysis.property import DescriptorProperty, EnergyProperty
    from agox.analysis.search_analysis import SearchAnalysis
    from agox.models.descriptors import SpectralGraphDescriptor

    t0 = dt()
    matplotlib.use(backend)

    # Setup the search collection
    search_collection = SearchCollection(directories, reload=reload)
    print("Time taken to load: ", dt() - t0)

    for search in search_collection:
        print(search)

    # Check if we have anything to plot:
    plot_labels = ["configuration", "success", "energy", "distribution"]
    plot_bools = [configuration, success, energy, distribution]
    plotting_dict = OrderedDict()
    for label, plot_bool in zip(plot_labels, plot_bools):
        if plot_bool:
            plotting_dict[label] = plot_bool

    if len(plotting_dict) == 0:
        print("Nothing to plot.")
        return

    # Setup the figure:
    n_plots = len(plotting_dict)
    fig, axes = plt.subplots(1, n_plots, figsize=(5 * n_plots, 5))
    axes = np.atleast_1d(axes)
    axes_dict = {}

    for ax, (label, plot_bool) in zip(axes, plotting_dict.items()):
        if plot_bool:
            axes_dict[label] = ax

    # Property:
    if property_name == "Energy":
        energy_property = EnergyProperty()
        delta = delta_total if np.isnan(delta_atom) else delta_atom * len(search_collection[0].get_candidate(0, 0))
    elif property_name == "FreeEnergy":
        raise NotImplementedError("Free energy not implemented yet.")

    search_analysis = SearchAnalysis(search_collection, energy_property)

    if configuration:
        search_analysis.plot_configuration(ax=axes_dict["configuration"], image=0)

    if energy:
        search_analysis.plot_energy(ax=axes_dict["energy"])

    if success:
        if criterion == "energy":
            _, _, min_props = search_analysis.get_flat_candidates()
            e_min = np.nanmin(min_props)
            criterion = ThresholdCriterion(e_min + delta)
            search_property = energy_property
        elif criterion == "graph":
            best_candidate = search_analysis.get_flat_candidates()[0][0]
            descriptor = SpectralGraphDescriptor.from_atoms(best_candidate)
            comparate = descriptor.get_features(best_candidate)
            search_property = DescriptorProperty(descriptor)
            criterion = DistanceCriterion(threshold=1e-7, comparate=comparate)  # Graphs should match.

        search_analysis.plot_cdf(ax=axes_dict["success"], criterion=criterion, search_property=search_property)

    if distribution:
        search_analysis.plot_histogram(ax=axes_dict["distribution"], bin_size=delta, image=0)

    # Setup the event handler:
    event_handler = EventHandler(search_analysis, axes_dict, fig)
    fig.canvas.mpl_connect("key_press_event", event_handler.on_press)

    plt.show()
