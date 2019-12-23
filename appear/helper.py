from typing import Any, Dict
import grequests


def helper(url: str, target: str, data: Dict[str, Any]) -> None:
    print(f"sending {data} to {target}")
    payload = data.copy()
    payload["target"] = target
    rs = (grequests.post(u, json=payload) for u in (url,))
    grequests.map(rs)
