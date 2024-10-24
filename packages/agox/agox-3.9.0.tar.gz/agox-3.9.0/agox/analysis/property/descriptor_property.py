import numpy as np

from agox.analysis import SearchData
from agox.models.descriptors import DescriptorBaseClass

from .property import ListPropertyData, Property


class DescriptorProperty(Property):
    def __init__(self, descriptor: DescriptorBaseClass) -> None:
        """
        Parameters
        ----------
        descriptor : DescriptorBaseClass
            The descriptor to compute.
        """
        self.descriptor = descriptor

    def compute(self, search_data: SearchData) -> ListPropertyData:
        """ """
        restarts = search_data.get_restarts()
        descriptor_list = []

        for restart in restarts:
            features = self.descriptor.get_features(restart.candidates)
            descriptor_list.append(features)

        indices = search_data.get_all("indices", fill=np.nan)
        identifiers = search_data.get_all_identifiers()

        return ListPropertyData(
            name=f"Descriptor-{self.descriptor.name}",
            data=descriptor_list,
            shape=("Restarts", "Indices"),
            list_axis=(identifiers, indices),
        )
