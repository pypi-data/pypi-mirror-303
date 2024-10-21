from __future__ import annotations

import logging
import os
import typing as ty
from typing import Iterable

from docutils.nodes import Element
from sphinx import application
from sphinx.addnodes import pending_xref
from sphinx.builders import Builder
from sphinx.domains import Domain, ObjType
from sphinx.environment import BuildEnvironment
from sphinx.roles import XRefRole
from sphinx.util.nodes import make_refnode, find_pending_xref_condition

from sphinx_gha.git_ref import get_git_ref
from sphinx_gha.action import ActionInputDirective, ActionOutputDirective, ActionEnvDirective, ActionDirective
from sphinx_gha.common import ActionsExampleDirective
from sphinx_gha.workflow import WorkflowInputDirective, WorkflowSecretDirective, WorkflowOutputDirective, WorkflowDirective

try:
    from yaml import CLoader as Loader, CDumper as Dumper, SafeDumper
except ImportError:
    from yaml import Loader, Dumper, SafeDumper

logger = logging.getLogger(__name__)


class GHActionsDomain(Domain):
    name = 'gha'
    label = 'Github Actions'
    directives = {
        'action': ActionDirective,
        'action-input': ActionInputDirective,
        'action-output': ActionOutputDirective,
        'action-envvar': ActionEnvDirective,
        'workflow': WorkflowDirective,
        'workflow-input': WorkflowInputDirective,
        'workflow-secret': WorkflowSecretDirective,
        'workflow-output': WorkflowOutputDirective,
        'example': ActionsExampleDirective
    }
    roles = {directive: XRefRole() for directive in directives}
    object_types = {role: ObjType(role) for role in roles.keys()}

    initial_data = {
        'objects': []
    }

    def get_full_qualified_name(self, node):
        parent_name = node.get('gh-actions:action') or node.get('gh-actions:workflow')
        target = node.get('reftarget')
        if target is None:
            return None
        else:
            return '.'.join(filter(None, [parent_name, target]))

    def get_objects(self) -> Iterable[tuple[str, str, str, str, str, int]]:
        yield from self.data['objects']

    def find_obj(self, env: BuildEnvironment, modname: str, classname: str,
                 name: str, ty: str | None, searchmode: int = 0, ) -> list[tuple[str,]]:
        pass

    def resolve_xref(self, env: BuildEnvironment, fromdocname: str, builder: Builder,
                     typ: str, target: str, node: pending_xref, contnode: Element,
                     ) -> Element | None:
        typ_name = typ.split(':')[-1]
        dispname = target
        if len(target.split('.')) == 1:
            # figure out the parent object from the current context
            if typ_name.startswith('action-'):
                parent_name = node.get('gh-actions:action')
            elif typ_name.startswith('workflow-'):
                parent_name = node.get('gh-actions:workflow')
            else:
                parent_name = None
            target = '.'.join(filter(None, [parent_name, target]))  # extend target full name with parent

        matches = [
            (docname, anchor) for name, dispname, objtyp, docname, anchor, prio in self.get_objects() if name == target and objtyp == typ
        ]

        if not matches:
            return None

        if len(matches) > 1:
            logger.warning('more than one target found for cross-reference %r: %s',
                           target, ', '.join(match[0] for match in matches))

        docname, anchor = matches[0]

        # determine the content of the reference by conditions
        content = find_pending_xref_condition(node, 'resolved')
        if content:
            children = content.children
        else:
            # if not found, use contnode
            children = [contnode]

        return make_refnode(builder, fromdocname, docname, anchor, children, title=dispname)

    def resolve_any_xref(self, env: BuildEnvironment, fromdocname: str, builder: Builder,
                         target: str, node: pending_xref, contnode: Element,
                         ) -> list[tuple[str, Element]]:
        matches = []
        for typ in self.object_types.keys():
            match = self.resolve_xref(env, fromdocname, builder, typ, target, node, contnode)
            if match is not None:
                matches.append((typ, match))
        return matches

    def note_object(self, name: str, dispname: str, typ: str, anchor: str) -> None:
        """Note a python object for cross-reference. """
        self.data['objects'].append((name, dispname, typ, self.env.docname, anchor, 1))


def setup(app: application.Sphinx) -> ty.Dict[str, ty.Any]:
    app.add_domain(GHActionsDomain)
    app.add_config_value('sphinx_gha_repo_root', os.getcwd(), 'env')
    app.add_config_value('sphinx_gha_repo_ref', lambda cfg: get_git_ref(cfg['sphinx_gha_repo_root']), 'env')
    app.add_config_value('sphinx_gha_repo_slug', 'UNKNOWN REPO', 'env')
    app.setup_extension('myst_parser')

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
