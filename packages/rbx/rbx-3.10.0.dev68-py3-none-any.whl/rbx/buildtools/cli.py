from invoke import Collection, Config, Program

from .tasks import apprunner, deploy


class BuildtoolsConfig(Config):
    prefix = "rbx"


ns = Collection()
ns.add_collection(apprunner.ns, "apprunner")
ns.add_collection(deploy.ns, "ec2")

program = Program(config_class=BuildtoolsConfig, namespace=ns, version="3.10.0.dev68")
