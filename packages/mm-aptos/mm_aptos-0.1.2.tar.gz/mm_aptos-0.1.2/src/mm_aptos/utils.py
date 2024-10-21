from typing import cast

from mm_std import random_choice, random_str_choice

from mm_aptos.types import Nodes, Proxies


def random_node(nodes: Nodes, remove_slash: bool = True) -> str:
    node = cast(str, random_choice(nodes))
    if remove_slash and node.endswith("/"):
        node = node.removesuffix("/")
    return node


def random_proxy(proxies: Proxies) -> str | None:
    return random_str_choice(proxies)
