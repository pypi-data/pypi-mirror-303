import datetime
import os
import hashlib
import typer
from collections import defaultdict

from typing import Callable, Any, Dict, List, Optional, Tuple, Literal, Type
from jinja2 import Environment, PackageLoader
from pydantic import BaseModel, Field as PField
from fastapi_toolkit.define import Schema, BaseUser

from .field_helper import FieldHelper, FieldType, LinkType
from .sql_mapping import mapping
from .utils import to_snake, plural

GENERATE_FUNC = Callable[[], str]


class NameInfo(BaseModel):
    origin: str
    snake: str
    snake_plural: str
    camel: str
    camel_plural: str
    table: str
    db: str
    schema: str
    base_schema: str
    fk: str


class FK(BaseModel):
    name: str
    key_type: str = "int"
    column: str


class AssociationTable(BaseModel):
    name: str
    left: 'ModelRenderData'
    right: 'ModelRenderData'


class LinkRenderData(BaseModel):
    link_name: str
    target_type: str
    back_populates: str

    schema_link_name: str
    schema_target_type: str
    default_value: str = ''


class Link(BaseModel):
    link_name: str
    alias: Optional[str] = None
    origin: "ModelRenderData"
    target: "ModelRenderData"
    fk: Optional[FK] = None
    table: Optional[AssociationTable] = None
    type: LinkType

    render_data: Optional[LinkRenderData] = None
    link_op_names: List[str] = PField(default_factory=list)
    link_op_codes: List[str] = PField(default_factory=list)

    def make_render(self, pair_link: "Link"):
        self.render_data = LinkRenderData(link_name=self.link_name, target_type=f'"{self.target.name.db}"',
                                          back_populates=pair_link.link_name,
                                          schema_link_name=self.link_name,
                                          schema_target_type=self.target.name.base_schema)
        if self.type == LinkType.many:
            self.render_data.target_type = f'List[{self.render_data.target_type}]'
            self.render_data.schema_target_type = f'List[{self.render_data.schema_target_type}]'
            self.render_data.default_value = 'Field(default_factory=list)'
        else:
            self.render_data.target_type = f'Optional[{self.render_data.target_type}]'
            self.render_data.schema_target_type = f'Optional[{self.render_data.schema_target_type}]'
            self.render_data.default_value = 'None'

    def link_prefix(self):
        if self.type == "one":
            target_name = self.target.name.snake
        else:
            target_name = self.target.name.snake_plural
        l_name = self.link_name
        if self.alias is not None:
            l_name = self.alias
        if l_name[-len(target_name):] != target_name:
            raise ValueError(f"link name {l_name} not match target {self.target.name.origin}")
        return l_name[:-len(target_name)]


class Field(BaseModel):
    name: NameInfo
    alias: Optional[NameInfo] = None
    type: FieldType
    index: bool


class ModelRenderData(BaseModel):
    name: NameInfo
    model: Type[Schema] = None
    fields: List[Field] = []
    links: List[Link] = []
    indexes: List[Field] = []


class CodeGenerator:
    def __init__(self, root_path='inner_code'):
        self.root_path = root_path
        self.models_path = os.path.join(root_path, 'models.py')
        self.schemas_path = os.path.join(root_path, 'schemas.py')
        self.dev_path = os.path.join(root_path, 'dev')
        self.crud_path = os.path.join(root_path, 'repo')
        self.routers_path = os.path.join(root_path, 'routers')
        self.auth_path = os.path.join(root_path, 'auth')
        self.stub_path = os.path.join(root_path, 'stub')

        self.force_rewrite = False
        self.async_repo = False

        if not os.path.exists(self.root_path):
            os.mkdir(self.root_path)
        if not os.path.exists(self.dev_path):
            os.mkdir(self.dev_path)
        if not os.path.exists(self.crud_path):
            os.mkdir(self.crud_path)
        if not os.path.exists(self.routers_path):
            os.mkdir(self.routers_path)
        if not os.path.exists(self.auth_path):
            os.mkdir(self.auth_path)
        if not os.path.exists(self.stub_path):
            os.mkdir(self.stub_path)
        self.env = Environment(
            loader=PackageLoader('fastapi_toolkit', 'templates'),
            trim_blocks=True, lstrip_blocks=True)

        self.define_schemas: Dict[str, Type[Schema]] = {}
        self.custom_types: List[Dict[str, Any]] = []
        self.association_tables: List[AssociationTable] = []
        self.parse()

    @staticmethod
    def _check_file_valid(path):
        with open(path, 'r') as f:
            line = f.readline()
            if not line.startswith('# generate_hash:'):
                return False
            content_hash = line.split(':')[1].strip()
            f.readline()
            f.readline()
            f.readline()
            content = f.read()
            return hashlib.md5(content.encode('utf8')).hexdigest() == content_hash

    def _generate_file(self, path, func: GENERATE_FUNC):
        content = func()
        generate_hash = hashlib.md5(content.encode('utf8')).hexdigest()
        if os.path.exists(path):
            with open(path, 'r') as f:
                line = f.readline()
                if line.startswith('# generate_hash:'):
                    head_hash = line.split(':')[1].strip()
                else:
                    head_hash = None
                if head_hash == generate_hash and CodeGenerator._check_file_valid(path):
                    print(f'file {path} is up to date, skip generate')
                    return
                elif not self.force_rewrite:
                    overwrite = typer.confirm(
                        f'file {path} has been changed or is out of date, do you want to overwrite it?')
                    if not overwrite:
                        return
        with open(path, 'w') as f:
            f.write(f'# generate_hash: {generate_hash}\n')
            f.write(f'"""\n'
                    f'This file was automatically generated in {datetime.datetime.now()}\n'
                    f'"""\n')
            f.write(content)

    def parse(self):
        self._parse_models()

    def _get_schemas(self, root=Schema):
        for model_ in root.__subclasses__():
            if model_ is not BaseUser:
                yield model_
            yield from self._get_schemas(model_)

    def _parse_models(self):
        self.define_schemas = {schema.__name__: schema for schema in self._get_schemas()}
        self.model_render_data = {
            schema_name: self._make_render_data_field(schema)
            for schema_name, schema in self.define_schemas.items()
        }
        self.build_links()

    def build_links(self):
        links: Dict[str, List[Link]] = defaultdict(list)
        for model in self.model_render_data.values():
            for field in filter(lambda x: x.type.link is not None, model.fields):
                field: Field
                link = Link(link_name=field.name.origin, origin=model,
                            target=self.model_render_data[field.type.link.model], type=field.type.link.type)
                if field.alias is not None:
                    link.alias = field.alias.origin
                links[model.name.origin].append(link)
            model.fields = list(filter(lambda x: x.type.link is None, model.fields))
            model.fields.sort(key=lambda x: x.type.nullable or x.type.default is not None)

        link_groups: List[Tuple[Link, Link]] = []
        visited_link = set()
        for ls in links.values():
            for link in ls:
                if id(link) in visited_link:
                    continue
                target_links = links[link.target.name.origin]
                for target_link in target_links:
                    if id(target_link) in visited_link:
                        continue
                    if (link.link_prefix() == target_link.link_prefix()
                            and link.target.name.origin == target_link.origin.name.origin
                            and target_link.target.name.origin == link.origin.name.origin):
                        visited_link.add(id(link))
                        visited_link.add(id(target_link))
                        link_groups.append((link, target_link))
                        break
                else:
                    raise ValueError(f"unable to pair {link.origin.name.origin}'s link "
                                     f"{link.link_name} to target {link.target.name.origin}")

        def make_one_many_link(l_one: Link, l_many: Link):
            l_one.fk = FK(name=f'_fk_{l_one.link_name}_{l_one.target.name.table}_id',
                          column=f"{l_one.target.name.table}.id")
            l_one.origin.links.append(l_one)
            l_many.origin.links.append(l_many)
            l_one.make_render(l_many)
            l_many.make_render(l_one)

        for l1, l2 in link_groups:
            t1, t2 = l1.type, l2.type
            match (t1, t2):
                case (LinkType.one, LinkType.one):
                    l1.origin.links.append(l1)
                    l2.origin.links.append(l2)
                    l1.fk = FK(name=f'_fk_{l1.link_name}_{l1.target.name.table}_id',
                               column=f'{l1.target.name.table}.id')
                    l1.make_render(l2)
                    l2.make_render(l1)
                case (LinkType.one, LinkType.many):
                    make_one_many_link(l1, l2)
                case (LinkType.many, LinkType.one):
                    make_one_many_link(l2, l1)
                case (LinkType.many, LinkType.many):
                    at_name = ['association_table']
                    if l1.link_prefix() != "":
                        at_name.append(l1.link_prefix().replace('_', ''))
                    at_name += [l1.origin.name.table, l2.origin.name.table]
                    association_table = AssociationTable(
                        name='_'.join(at_name),
                        left=l1.origin, right=l2.origin
                    )
                    l1.table = association_table
                    l2.table = association_table
                    self.association_tables.append(association_table)
                    l1.origin.links.append(l1)
                    l2.origin.links.append(l2)
                    l1.make_render(l2)
                    l2.make_render(l1)

        def build_link_op(link: Link, name: str, from_id: bool, from_batch: bool):
            arg = link.target.name.snake
            arg_type = link.target.name.base_schema
            if from_id:
                arg += '_id'
                arg_type = 'int'
            if from_batch:
                arg += 's'
                arg_type = f'List[{arg_type}]'
            filter_expr = f'__eq__({arg})'
            if from_batch:
                if from_id:
                    filter_expr = f'in_({arg})'
                else:
                    filter_expr = f'in_(map(lambda x: x.id, {arg}))'
            elif not from_id:
                filter_expr = f'__eq__({arg}.id)'
            query_code = f'query = query.join({link.target.name.db}).filter({link.target.name.db}.id.{filter_expr})'
            o = link.origin
            for l in o.links:
                op = 'selectinload' if l.type is LinkType.many else 'joinedload'
                query_code += f'\n    query = query.options({op}({o.name.db}.{l.link_name}))'
            link.link_op_codes.append(
                f"""
def {name}_query({arg}: {arg_type}, query=Depends(get_all_query)) -> Select:
    if type(query) is not Select:
        query = get_all_query(QueryParams())
    {query_code}
    return query
                """
            )
            link.link_op_codes.append(
                f"""
{'async ' if self.async_repo else ''}def {name}({arg}: {arg_type}, db=Depends(get_db), query=Depends(get_all_query)) -> List[{link.origin.name.db}]:
    if type(query) is not Select:
        query = get_all_query(QueryParams())
    {query_code}
    return {'(await db.scalars(query)).all() ' if self.async_repo else 'db.scalars(query).all()'}
                """
            )

        for link in (l for m in self.model_render_data.values() for l in m.links):
            build_link_op(link, f'get_{link.link_name}_id_is', True, False)
            build_link_op(link, f'get_{link.link_name}_is', False, False)
            build_link_op(link, f'get_{link.link_name}_id_has', True, True)
            build_link_op(link, f'get_{link.link_name}_has', False, True)

    def _make_render_data_field(self, schema: Type[Schema]):
        fh = FieldHelper()
        fields = []
        indexes = []
        for name, field in schema.model_fields.items():
            index = field.json_schema_extra is not None and 'index' in field.json_schema_extra and \
                    field.json_schema_extra['index'] is True
            f = Field(name=self._name_info(name), alias=self._name_info(field.alias), type=fh.parse(field), index=index)
            fields.append(f)
            if index:
                indexes.append(f)
        m = ModelRenderData(
            name=self._name_info(schema.__name__),
            fields=fields,
            indexes=indexes,
        )
        return m

    @staticmethod
    def _name_info(name: str) -> Optional[NameInfo]:
        if type(name) is not str:
            return None
        return NameInfo(
            origin=name,
            snake=to_snake(name),
            snake_plural=plural(to_snake(name)),
            camel=name,
            camel_plural=plural(name),
            table=to_snake(name),
            db=f'DB{name}',
            schema=f'Schema{name}',
            base_schema=f'SchemaBase{name}',
            fk=f'fk_{to_snake(name)}_id',
        )

    def _define2table(self) -> str:
        template = self.env.get_template('models/main.py.jinja2')
        return template.render(
            deps=self.custom_types,
            models=self.model_render_data.values(),
            association_tables=self.association_tables,
        )

    def _define2schema(self) -> str:
        template = self.env.get_template('schemas/main.py.jinja2')
        return template.render(
            deps=self.custom_types,
            models=self.model_render_data.values(),
        )

    def _from_template(self, template_name: str, **kwargs):
        def func():
            return self.env.get_template(template_name).render(**kwargs)

        return func

    def _generate_tables(self, auth_type):
        self._generate_file(os.path.join(self.root_path, 'db.py'), self._from_template('db.py.jinja2'))
        self._generate_file(os.path.join(self.root_path, 'setting.py'),
                            self._from_template('setting.py.jinja2', auth_type=auth_type))
        self._generate_file(self.models_path, self._define2table)
        self._generate_file(self.schemas_path, self._define2schema)
        self._generate_file(
            os.path.join(self.dev_path, 'db.py'),
            self._from_template(
                'dev.db.py.jinja2',
                root_path=str(self.root_path).replace('/', '.').replace('\\', '.')))
        self._generate_file(os.path.join(self.dev_path, '__init__.py'), lambda: '')

    def _generate_routers(self):
        template_path = 'async/' if self.async_repo else 'sync/'
        models = self.model_render_data.values()
        for model in models:
            self._generate_file(os.path.join(self.crud_path, f'{model.name.snake}_repo.py'),
                                self._from_template(f'repo/{template_path}main.py.jinja2', model=model))
            self._generate_file(os.path.join(self.routers_path, f'{model.name.snake}_router.py'),
                                self._from_template('routers/main.py.j2', model=model))
            self._generate_file(os.path.join(self.stub_path, f'{model.name.snake}_stub.py'),
                                self._from_template('stub/main.py.jinja2', model=model))
        self._generate_file(os.path.join(self.crud_path, '__init__.py'),
                            self._from_template(f'repo/{template_path}__init__.py.jinja2',
                                                models=models))
        self._generate_file(os.path.join(self.routers_path, '__init__.py'), self._from_template(
            'routers/init.py.j2',
            models=models,
        ))
        self._generate_file(os.path.join(self.stub_path, '__init__.py'), self._from_template(
            'stub/__init__.py.jinja2',
            models=models,
        ))

    def _generate_auth(self, mode: str):
        user_model = self.model_render_data['User']
        self._generate_file(os.path.join(self.auth_path, '__init__.py'),
                            self._from_template(f'auth/{mode}/__init__.py.j2'))
        if mode != 'key':
            self._generate_file(os.path.join(self.auth_path, 'models.py'),
                                self._from_template(f'auth/{mode}/models.py.j2', model=user_model))
        self._generate_file(os.path.join(self.auth_path, 'routes.py'), self._from_template(f'auth/{mode}/routes.py.j2'))

    def _generate_config(self):
        self._generate_file(os.path.join(self.root_path, 'config.py'), self._from_template(
            'config.py.j2', models=self.model_render_data.values()))

    def _generate_custom_types(self):
        self._generate_file(os.path.join(self.root_path, 'custom_types.py'), self._from_template(
            'custom_types.py.j2', custom_types=self.custom_types))

    def generate(self, table: bool = True, router: bool = True, mock: bool = True, auth: str = ""):
        self._generate_custom_types()
        if table:
            self._generate_tables(auth_type=auth)
        if router:
            self._generate_routers()
        if auth != "":
            self._generate_auth(mode=auth)
        self._generate_config()
