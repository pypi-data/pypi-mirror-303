from dataclasses import asdict

import yaml
from mm_std import Err, Ok, Result, hr, run_command

from mm_aptos.types import Proxies
from mm_aptos.utils import random_proxy


# noinspection DuplicatedCode
def address_to_primary_name(address: str, timeout: int = 5, proxies: Proxies = None, attempts: int = 3) -> Result[str]:
    result: Result[str] = Err("not_started")
    url = f"https://www.aptosnames.com/api/mainnet/v1/primary-name/{address}"
    for _ in range(attempts):
        res = hr(url, proxy=random_proxy(proxies), timeout=timeout)
        data = res.to_dict()
        try:
            if res.code == 200 and res.json == {}:
                return Ok("", data=data)
            return Ok(res.json["name"], data=data)
        except Exception as e:
            result = Err(e, data=data)
    return result


# noinspection DuplicatedCode
def address_to_name(address: str, timeout: int = 5, proxies: Proxies = None, attempts: int = 3) -> Result[str]:
    result: Result[str] = Err("not_started")
    url = f"https://www.aptosnames.com/api/mainnet/v1/name/{address}"
    for _ in range(attempts):
        res = hr(url, proxy=random_proxy(proxies), timeout=timeout)
        data = res.to_dict()
        try:
            if res.code == 200 and res.json == {}:
                return Ok("", data=data)
            return Ok(res.json["name"], data=data)
        except Exception as e:
            result = Err(e, data=data)
    return result


def address_to_names(address: str, cmd: str = "aptos-names", timeout: int = 5, attempts: int = 3) -> Result[list[str]]:
    result: Result[list[str]] = Err("not_started")
    cmd = f"{cmd} {address}"
    for _ in range(attempts):
        res = run_command(cmd, timeout=timeout)
        if res.stderr.strip() == "address is not valid":
            return Err("invalid_address", data=asdict(res))
        if res.code == 0:
            try:
                domains = [d["domain"] for d in yaml.safe_load(res.stdout)]
                return Ok(domains, data=asdict(res))
            except Exception as e:
                result = Err(e, data=asdict(res))
        else:
            result = Err(res.stderr or "error", data={"stdout": res.stdout, "stderr": res.stderr, "code": res.code})
    return result
