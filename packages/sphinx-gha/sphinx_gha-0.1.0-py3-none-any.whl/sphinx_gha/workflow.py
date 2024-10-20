from __future__ import annotations

import os
from functools import cached_property
from pathlib import Path

import yaml
from sphinx import addnodes
from yaml import SafeDumper

from sphinx_gha.common import ActionsItemDirective, ActionsFileDirective, format_uses


class WorkflowInputDirective(ActionsItemDirective):
    parent_role = 'gh-actions:workflow'
    fields = ['required', 'default', 'type']
    prefix = 'input'


class WorkflowSecretDirective(WorkflowInputDirective):
    prefix = 'secret'


class WorkflowOutputDirective(ActionsItemDirective):
    parent_role = 'gh-actions:workflow'
    prefix = 'output'


class WorkflowDirective(ActionsFileDirective):
    role = 'gh-actions:workflow'
    file_type = 'workflow'

    @cached_property
    def call_node(self):
        if (on_node := self.yaml.get('on') or self.yaml.get(True)) is None:
            # fucking yaml parses `on` as a boolean even in keys what the fuck
            return self.error(f'Workflow {self.path} has no `on` node')
        if 'workflow_call' not in on_node:
            return self.error(f'Workflow {self.path} is not callable')
        else:
            return on_node.get('workflow_call') or {}

    @cached_property
    def example(self):
        if example_yaml := self.yaml.get('x-example'):
            return example_yaml

        slug = format_uses(self.path, self.env)
        name = self.yaml.get('x-example-name')
        inputs = self.yaml.get('x_example_inputs') or {}
        secrets = self.yaml.get('x_example_secrets') or {}

        for (k, d, e) in [
            ('secrets', secrets, 'x-example'),
            ('inputs', inputs, 'x-example')
        ]:
            if action_inputs := self.call_node.get(k):
                for input_name, input_meta in action_inputs.items():
                    input_meta = input_meta or {}
                    if input_example := input_meta.get(e):
                        d[input_name] = input_example

        example_yaml = {}

        if name:
            example_yaml['name'] = name
        example_yaml['uses'] = slug
        if inputs:
            example_yaml['with'] = inputs
        if secrets:
            example_yaml['secrets'] = secrets

        example_yaml = [example_yaml]
        return yaml.dump(example_yaml, Dumper=SafeDumper, sort_keys=False)

    def transform_content(self, content_node: addnodes.desc_content) -> None:
        super().transform_content(content_node)
        # Items

        item_lists = [
            ('inputs', 'Inputs', 'workflow-input'),
            ('secrets', 'Secrets', 'workflow-secret'),
            ('outputs', 'Outputs', 'workflow-output'),
        ]

        for (key, title, directive) in item_lists:
            if item_list := self.call_node.get(key):
                content_node.append(self.format_item_list(title, directive, item_list))
