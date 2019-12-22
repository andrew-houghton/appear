from typing import Any, Dict
import grequests


def helper(target: str, data: Dict[str, Any]) -> None:
    print(f"sending {data} to {target}")
    rs = (grequests.post(u, data=data) for u in ("http://localhost:5000/broadcast",))
    grequests.map(rs)
