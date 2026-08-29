from bellfre.capability import (
    CapabilityProvider,
    CapabilityRequest,
)


class Discovery:
    """
    Resolves capability requests into
    capability providers.
    """

    def __init__(self, registry):
        self.registry = registry

    def find(
        self,
        request: CapabilityRequest,
    ):
        """
        Find providers for a capability request.
        """

        records = self.registry.find(
            request.capability_id
        )

        return [
            CapabilityProvider(
                record.identity,
                request.capability_id,
            )
            for record in records
        ]