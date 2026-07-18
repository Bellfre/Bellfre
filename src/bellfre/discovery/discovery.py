class Discovery:
    def __init__(self, registry):
        self.registry = registry

    def find(self, capability_id: str):
        return self.registry.find(capability_id)