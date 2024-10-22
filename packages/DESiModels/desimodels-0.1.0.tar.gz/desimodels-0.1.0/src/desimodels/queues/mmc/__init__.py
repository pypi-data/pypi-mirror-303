def mmc(
    arrival_rate: float = 1,
    service_rate: float = 10,
    servers: int = 1,
    max_time: float = 2018,
    backend="desimpy",
):
    """Simulate a M/M/c queue.

    Args:
        arrival_rate (float): Arrival rate.
        service_rate (float): Service rate.
        servers (int): Number of servers.
        backend (str): Backend implementation of the simulation.
    """
    _import_backend_package(backend)
    # TODO: Allow passing RNG seed.
    # TODO: Model constructor.
    # TODO: Model runner.
    # TODO: Return event log.


def _import_backend_package(backend: str):
    """Import backend package."""
    if backend == "desimpy":
        from .desimpy import MMc
    else:
        raise NotImplementedError(f"{backend=} not implemented.")
