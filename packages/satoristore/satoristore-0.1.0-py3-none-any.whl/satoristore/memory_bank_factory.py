from satoristore.memory_bank import MemoryBank
from satoristore.text_memory_bank import TextMemoryBank
from satoristore.multimodal_memory_bank import MultimodalMemoryBank


class MemoryBankFactory:
    def get_memory_bank(self, multimodal: bool = False) -> MemoryBank:
        """
        Returns the appropriate MemoryBank instance based on the input data.

        Parameters:
        - multimodal: A boolean indicating whether to use the MultimodalMemoryBank. Defaults to False.

        Returns:
        - An instance of TextMemoryBank or MultimodalMemoryBank.
        """
        if multimodal:
            return MultimodalMemoryBank()
        else:
            return TextMemoryBank()
