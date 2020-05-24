#!/usr/bin/env python
from constructs import Construct
from cdk8s import App, Chart

from webservice import WebService


class MyChart(Chart):
    def __init__(self, scope: Construct, name: str):
        super().__init__(scope, name)

        WebService(self, 'app1', image='arunvel1988/c1', replicas=2)
        WebService(self, 'app2', image='nginx', container_port=80)


app = App()
MyChart(app, "demo2")

app.synth()