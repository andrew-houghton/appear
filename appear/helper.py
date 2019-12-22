from typing import Any, Dict
import grequests


def helper(url: str, target: str, data: Dict[str, Any]) -> None:
    print(f"sending {data} to {target}")
    rs = (grequests.post(u, data=data) for u in (url,))
    grequests.map(rs)
