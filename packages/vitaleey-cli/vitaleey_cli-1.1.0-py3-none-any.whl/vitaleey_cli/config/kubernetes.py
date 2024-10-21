from dataclasses import dataclass

from .config import CommandConfig, Config

__all__ = ["kubernetes_config"]


@dataclass(frozen=True)
class KubernetesDataclass(CommandConfig):
    """
    Configuration for the application

    Options:
    - cluster_name: The cluster name
    """

    pindakaas: str = "pindakaas"
    cluster_name: str = ""


class KubernetesConfig(Config):
    """
    Kubernetes configuration
    """

    dataclass = KubernetesDataclass


kubernetes_config = KubernetesConfig()
