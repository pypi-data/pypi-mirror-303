from __future__ import annotations

import os
from functools import cached_property
from pathlib import Path

import yaml
from docutils.parsers.rst import directives
from sphinx import addnodes
from sphinx.domains.std import StandardDomain
from sphinx.util.nodes import make_id
from yaml import SafeDumper

from sphinx_gha.common import ActionsItemDirective, ActionsFileDirective, format_uses


class ActionInputDirective(ActionsItemDirective):
    parent_role = 'gh-actions:action'
    fields = ['required', 'default']
    option_spec = {'deprecationMessage': directives.unchanged_required}
    prefix = 'input'

    def transform_content(self, content_node) -> None:
        super().transform_content(content_node)
        if deprecation_message := self.options.get('deprecationMessage'):
            admonition, msgs = self.format_deprecationMessage(deprecation_message)
            content_node.insert(0, admonition)


class ActionOutputDirective(ActionsItemDirective):
    parent_role = 'gh-actions:action'
    prefix = 'output'


class ActionEnvDirective(ActionsItemDirective):
    parent_role = 'gh-actions:action'
    fields = ['required']
    prefix = 'env'

    def add_target_and_index(self, name: str, sig: str, signode) -> None:
        super().add_target_and_index(name, sig, signode)
        objtype = 'envvar'
        node_id = make_id(self.env, self.state.document, objtype, name)
        signode['ids'].append(node_id)

        std: StandardDomain = self.env.domains['std']
        std.note_object(objtype, signode['fullname'], node_id, location=signode)


class ActionDirective(ActionsFileDirective):
    role = 'gh-actions:action'
    file_type = 'action'

    @cached_property
    def path(self):
        path = self.options.get('path')
        if path is None:
            return None
        repo_root = Path(self.env.config['sphinx_gha_repo_root'] or os.getcwd()).absolute()
        path = repo_root / Path(path)
        for filename in ['action.yml', 'action.yaml']:
            test_path = path / filename
            if test_path.exists():
                return test_path
        if path.is_file():
            return path

        self.error(f'Could not find an action definition at {path}')

    @classmethod
    def id_from_path(cls, path: Path):
        return path.parent.name

    @cached_property
    def example(self):
        if example_yaml := self.yaml.get('x-example'):
            return example_yaml

        if self.path is None:
            return ''

        slug = format_uses(self.path.parent, self.env)
        name = self.yaml.get('x-example-name')
        inputs = self.yaml.get('x_example_inputs') or {}
        env = self.yaml.get('x_example_env') or {}

        for (k, d, e) in [
            ('x-env', env, 'example'),
            ('inputs', inputs, 'x-example')
        ]:
            if action_inputs := self.yaml.get(k):
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
        if env:
            example_yaml['env'] = env

        example_yaml = [example_yaml]
        return yaml.dump(example_yaml, Dumper=SafeDumper, sort_keys=False)

    def transform_content(self, content_node: addnodes.desc_content) -> None:
        super().transform_content(content_node)

        # Items

        item_lists = [
            ('inputs', 'Inputs', 'action-input'),
            ('outputs', 'Outputs', 'action-output'),
            ('x-env', 'Environment Variables', 'action-envvar')
        ]

        for (key, title, directive) in item_lists:
            if item_list := self.yaml.get(key):
                content_node.append(self.format_item_list(title, directive, item_list))
