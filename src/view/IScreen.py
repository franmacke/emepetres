from abc import abstractmethod


class IScreen:
    @abstractmethod
    def render(self):
        pass