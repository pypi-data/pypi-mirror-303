from __future__ import annotations

import os
from functools import cached_property
from pathlib import Path
from typing import Optional, MutableSequence, Sequence, MutableMapping

import sphinx
import yaml
from docutils import nodes
from docutils.nodes import section, Element
from docutils.parsers.rst import directives, Directive
from docutils.statemachine import StringList
from myst_parser.mdit_to_docutils.base import DocutilsRenderer
from myst_parser.mdit_to_docutils.sphinx_ import SphinxRenderer
from myst_parser.parsers.mdit import create_md_parser
from sphinx import addnodes
from sphinx.addnodes import desc_name, desc_signature
from sphinx.directives import ObjectDescription, ObjDescT
from sphinx.directives.patches import Code
from sphinx.errors import ConfigError
from sphinx.util import ws_re
from sphinx.util.docutils import SphinxDirective
from yaml import SafeLoader, SafeDumper


def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')


yaml.representer.SafeRepresenter.add_representer(type(None), represent_none)


def format_uses(uses, env):
    slug = env.config['sphinx_gha_repo_slug']
    if slug is None:
        raise ConfigError("No repo slug provided. please set the sphinx_gha_repo_slug config variable")
    uses = Path(uses)
    file_path = uses.absolute()
    repo_root = Path(env.config['sphinx_gha_repo_root'] or os.getcwd()).absolute()
    relative_path = str(file_path.relative_to(repo_root))

    if relative_path != '.':
        slug = slug + '/' + relative_path

    git_ref = env.config['sphinx_gha_repo_ref']

    if git_ref:
        slug = slug + '@' + git_ref

    return slug


class MarkdownParsingMixin(Directive):
    @property
    def md_renderer(self):
        if not hasattr(self, '_md_renderer'):
            config = self.state.document.settings.env.myst_config
            self._md_parser = create_md_parser(config, SphinxRenderer)
            self._md_renderer = DocutilsRenderer(self._md_parser)
            self._md_renderer.setup_render({"myst_config": config}, {})
        return self._md_renderer

    def parse_markdown(self, markdown, inline=False, node=None):
        renderer = self.md_renderer
        renderer.current_node = node or Element('')
        renderer.nested_render_text(markdown, self.lineno, inline=inline)
        return renderer.current_node.children


class ActionsItemDirective(ObjectDescription[str], MarkdownParsingMixin):
    parent_role = ''
    index_template: str = '%s'
    fields = []
    option_spec = {'description': directives.unchanged_required}
    prefix = None

    @classmethod
    def __init_subclass__(cls, /, **kwargs):
        cls.option_spec |= {f: directives.unchanged_required for f in cls.fields}
        cls.option_spec |= ActionsItemDirective.option_spec

    @classmethod
    def generate(cls, item_name, item_meta, lineno, content_offset, state, state_machine):
        options = {k: str(v) for k, v in item_meta.items() if k in cls.option_spec}
        # noinspection PyTypeChecker
        directive = cls('', [item_name], options, '', lineno, content_offset, "", state, state_machine)
        node = directive.run()
        return node

    def handle_signature(self, sig: str, sig_node) -> str:
        parent = self.env.ref_context.get(self.parent_role)
        name = ws_re.sub(' ', sig)

        sig_node.clear()
        if self.prefix:
            sig_prefix = [nodes.Text(self.prefix), addnodes.desc_sig_space()]
            sig_node += addnodes.desc_annotation(str(sig_prefix), '', *sig_prefix)
        sig_node += desc_name(sig, sig)
        sig_node['name'] = sig
        if parent:
            sig_node['parent'] = parent
            sig_node['fullname'] = parent + '.' + sig
        else:
            sig_node['fullname'] = sig
        return name

    def _object_hierarchy_parts(self, sig_node) -> tuple[str, ...]:
        return tuple(sig_node['fullname'].split('.'))

    def _toc_entry_name(self, sig_node) -> str:
        return sig_node['name']

    def add_target_and_index(self, name: str, sig: str, sig_node) -> None:
        node_id = sphinx.util.nodes.make_id(self.env, self.state.document, self.objtype, name)
        sig_node['ids'].append(node_id)
        self.state.document.note_explicit_target(sig_node)

        domain = self.env.domains['gha']
        domain.note_object(sig_node['fullname'], sig_node['name'], self.objtype, node_id)

    def format_field(self, field_name: str, field_value):
        parsed, msgs = self.parse_inline(field_value, lineno=self.lineno)
        value = nodes.literal('', field_value, )
        field = nodes.field(
            '',
            nodes.field_name('', field_name.title()),
            nodes.field_body('', value),
        )
        return field, msgs

    def format_deprecationMessage(self, message):
        admonition = nodes.admonition()
        admonition['classes'].append('warning')
        title_text = 'Deprecated'
        textnodes, msg = self.state.inline_text(title_text, self.lineno)
        title = nodes.title(title_text, '', *textnodes)
        title.source, title.line = (
            self.state_machine.get_source_and_line(self.lineno))

        admonition += title
        admonition += msg

        admonition['type'] = 'deprecated'
        admonition.document = self.state.document
        self.parse_markdown(message, inline=True, node=admonition)
        return admonition, []

    def transform_content(self, content_node) -> None:
        """Insert fields as a field list."""
        field_list = nodes.field_list()
        for field_name in self.fields:
            if field_value := self.options.get(field_name):
                field, msgs = self.format_field(field_name, field_value)
                field_list.append(field)
                field_list += msgs
        if len(field_list.children) > 0:
            content_node.insert(0, field_list)

        if description := self.options.get('description'):
            self.parse_markdown(description, inline=False, node=content_node)


class ActionsExampleDirective(SphinxDirective):
    required_arguments = 0
    has_content = True

    @classmethod
    def generate(cls, content, lineno, content_offset, state, state_machine):
        # noinspection PyTypeChecker
        directive = cls('', [], [], content, lineno, content_offset, "", state, state_machine)
        node = directive.run()
        return node

    def _modify_uses(self, uses: str):
        if uses.startswith('./') or uses == '.':
            return format_uses(uses, self.env)
        else:
            return uses

    def _modify_tree(self, tree):
        if isinstance(tree, MutableSequence):
            return [self._modify_tree(item) for item in tree]
        if isinstance(tree, MutableMapping):
            if 'uses' in tree:
                tree['uses'] = self._modify_uses(tree['uses'])
        return tree

    def run(self):

        if isinstance(self.content, StringList):
            content = '\n'.join(self.content.data)
        elif isinstance(self.content, Sequence):
            content = '\n'.join(self.content)
        else:
            content = self.content
        example_yaml = yaml.load(content, SafeLoader)
        example_yaml = self._modify_tree(example_yaml)
        example_yaml = yaml.dump(example_yaml, Dumper=SafeDumper, sort_keys=False)
        code = Code('Code', ['yaml'], {}, content=example_yaml.splitlines(), lineno=self.lineno, content_offset=self.content_offset,
                    block_text='', state=self.state, state_machine=self.state_machine)
        return code.run()


class ActionsFileDirective(ObjectDescription, MarkdownParsingMixin):
    role = None
    file_type = None
    has_content = True
    final_argument_whitespace = True
    required_arguments = 0
    optional_arguments = 1
    option_spec = {
        'path': directives.unchanged,
        'noexample': directives.unchanged,
        'nodescription': directives.unchanged
    }

    @classmethod
    def id_from_path(cls, path: Path) -> str:
        if path is None:
            raise ValueError('path cannot be None')
        if (path_stem := path.stem) is not None:
            return path_stem
        else:
            raise ValueError('path stem cannot be None')

    @cached_property
    def id(self) -> str:
        if len(self.arguments) > 0:
            assert self.arguments[0] is not None
            return self.arguments[0]
        elif (path := self.path) is not None:
            return self.id_from_path(path)
        else:
            self.error('Neither a path nor name provided!')

    @cached_property
    def path(self) -> Optional[Path]:
        if (path := self.options.get('path')) is not None:
            repo_root = Path(self.env.config['sphinx_gha_repo_root'] or os.getcwd()).absolute()
            return repo_root / Path(path)
        else:
            return None

    @cached_property
    def yaml(self) -> dict:
        path = self.path
        if path is None:
            return {}
        with open(path, 'rt') as stream:
            return yaml.full_load(stream)

    @cached_property
    def example(self) -> str:
        return ''

    @property
    def domain_obj(self) -> "GHActionsDomain":
        domain_name = self.name.split(':')[0]
        return self.env.domains[domain_name]

    def get_signatures(self) -> list[str]:
        return [self.id]

    def handle_signature(self, sig: str, sig_node: desc_signature) -> ObjDescT:
        if sig is None:
            raise ValueError('sig cannot be None')
        self.env.ref_context[self.role] = self.id
        sig_node.clear()
        sig_prefix = [nodes.Text(self.file_type), addnodes.desc_sig_space()]
        sig_node += addnodes.desc_annotation(str(sig_prefix), '', *sig_prefix)
        sig_node += desc_name(sig, sig)
        name = ws_re.sub(' ', sig)
        sig_node['fullname'] = sig
        sig_node['name'] = sig
        return name

    def _object_hierarchy_parts(self, sig_node) -> tuple[str, ...]:
        return (self.id,)

    def _toc_entry_name(self, sig_node) -> str:
        if not sig_node.get('_toc_parts'):
            return ''
        name, = sig_node['_toc_parts']
        return name

    def add_target_and_index(self, name: str, sig: str, sig_node) -> None:
        node_id = sphinx.util.nodes.make_id(self.env, self.state.document, self.objtype, name)
        sig_node['ids'].append(node_id)
        self.state.document.note_explicit_target(sig_node)
        self.domain_obj.note_object(sig_node['fullname'], sig_node['name'], self.objtype, node_id)

    def transform_content(self, content_node: addnodes.desc_content) -> None:
        # Description
        generate_description = 'nodescription' not in self.options
        if generate_description and (description := self.yaml.get('description')):
            content_node.insert(0, self.parse_markdown(description))

        # Example code
        generate_example = 'noexample' not in self.options
        if generate_example and (example_yaml := self.example):
            code_section = nodes.section(
                '',
                nodes.rubric(text='Example'),
                ids=[nodes.make_id(self.id + '_example')],
                names=[nodes.fully_normalize_name('example')],
            )

            code = Code('Code', ['yaml'], {}, content=example_yaml.splitlines(), lineno=self.lineno, content_offset=self.content_offset, block_text='',
                        state=self.state, state_machine=self.state_machine)
            code_section.extend(code.run())
            content_node.append(code_section)

    def format_item_list(self, title, directive, items) -> section:
        item_list_section = nodes.section(
            '',
            nodes.rubric(text=title),
            ids=[nodes.make_id(self.id + '_' + title)],
            names=[nodes.fully_normalize_name(title)],
        )
        for item_name, item_meta in items.items():
            if item_meta is None:
                item_meta = {}
            directive_obj = self.domain_obj.directive(directive)
            item_nodes = directive_obj.generate(item_name, item_meta,
                                                self.lineno, self.content_offset,
                                                self.state, self.state_machine)
            item_list_section.extend(item_nodes)
        return item_list_section
