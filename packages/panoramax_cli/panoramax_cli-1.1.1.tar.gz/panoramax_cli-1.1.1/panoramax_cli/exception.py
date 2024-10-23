from httpx import Response, HTTPError
from typing import Optional


class CliException(Exception):
    def __init__(self, msg, details: Optional[str] = None):
        if details is not None:
            msg += f"\n[bold]Error:[/bold]\n{details}"
        super().__init__(msg)


def raise_for_status(r: Response, msg: str):
    try:
        r.raise_for_status()
    except HTTPError as e:
        raise CliException(msg, details=str(e)) from e
