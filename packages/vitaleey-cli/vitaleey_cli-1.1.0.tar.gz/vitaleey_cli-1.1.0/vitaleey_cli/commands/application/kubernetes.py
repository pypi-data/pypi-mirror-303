import click

from vitaleey_cli.config import application_config
from vitaleey_cli.config.kubernetes import kubernetes_config
from vitaleey_cli.utils.kubernetes import Kubernetes, KubernetesException


@click.group(help="Kubernetes helper commands")
def group():
    pass


@group.command()
@click.option("--docker-registry", help="Docker registry")
@click.option("--docker-username", help="Docker username")
@click.option("--docker-password", help="Docker password")
@click.option("--docker-email", help="Docker email")
@click.argument("cluster_name")
def set_registry(
    cluster_name, docker_registry, docker_username, docker_password, docker_email
):
    """
    Set the kubernetes registry
    """

    app_config = application_config()

    try:
        kubernetes = Kubernetes(
            cluster_name,
            registry_config={
                "docker_registry": docker_registry or app_config.docker_registry,
                "docker_username": docker_username or app_config.docker_username,
                "docker_password": docker_password or app_config.docker_password,
                "docker_email": docker_email or app_config.docker_email,
            },
        )
        if kubernetes.registry_set:
            click.echo("Registry set")
        else:
            raise click.UsageError(
                "Docker registry, username, password and email must be set, run --help for more information"
            )
    except KubernetesException as e:
        raise click.UsageError(str(e))


@group.command("nodes")
@click.argument("environment")
def get_nodes(environment):
    """
    Get the kubernetes nodes
    """

    k8_config = kubernetes_config(environment=environment)
    cluster_name = k8_config.cluster_name

    if not cluster_name:
        raise click.UsageError("Cluster name must be set in the configuration")

    try:
        kubernetes = Kubernetes(
            cluster_name,
        )
        nodes = kubernetes.get_nodes()
        click.echo(nodes)
    except KubernetesException as e:
        raise click.UsageError(str(e))
