import os
import sys
import logging
import tempfile
import networkx as nx
from typing import (
    Union,
    Dict,
    List,
    Tuple,
    Set,
    Any
)
from pathlib import Path
from modeltasks.log import logger
from textwrap import shorten, wrap
from argparse import ArgumentParser
from modeltasks.registry import TaskRegistry
from modeltasks.scheduler import AbstractScheduler, ThreadedScheduler
from modeltasks.config import load_configuration_file, convert_parameter, SETTINGS
from modeltasks.util.hash import get_hash
from modeltasks.util.task import TaskVariable
from modeltasks.handler.abstract import EventHandler
from modeltasks.util.network import (
    get_root_nodes,
    sort_topologically,
    sort_topologically_parallel,
    is_start_node,
    is_end_node
)
# Re-export modules
from modeltasks.task import ModelTask


class Model:
    """
    A model is built from an ordered sequence of model tasks, each implementing a limited domain of the model's
    problem to solve. A model can be executed at any point of its task chain which leads to invoking the
    specified task process and all its required prior tasks by resolving the formulated task dependencies
    into a directed acyclical graph and then invoking one by one in the correct order. The exact execution
    and processing handling of tasks is done by a scheduler. By default, a thread-based scheduler is used.
    """

    _registry: TaskRegistry = None
    _model_tasks: Path = None
    _model_configs: List = []
    _unresolved: List = []
    _stream_handler: logging.StreamHandler = None
    _file_handler: logging.FileHandler = None
    _event_handler: EventHandler = None
    _scheduler: AbstractScheduler = None
    _workspace: Path = None
    _cache: Path = None
    _configuration: Dict = {}
    _arguments = None

    title: str = None
    logger: logging.Logger = None

    @property
    def workspace(self):
        return self._workspace

    @workspace.setter
    def workspace(self, path: Path):
        self._workspace = path
        if self._scheduler:
            self._scheduler.workspace = self._workspace

    @property
    def cache(self):
        return self._cache

    @cache.setter
    def cache(self, path: Path):
        self._cache = path
        if self._scheduler:
            self._scheduler.cache = self._cache

    def __init__(
        self,
        title: str = 'Model',
        model_tasks: Union[str, Path] = None,
        model_config: Union[Path, Dict] = None,
        scheduler: Union[Dict, AbstractScheduler] = None,
        handler: EventHandler = None,
        log_level: int = logging.INFO,
        log_file: Path = None,
        interactive: bool = True,
        settings: Dict = None
    ):
        # Title
        self.title = title

        # Settings
        if settings:
            for k, v in settings.items():
                SETTINGS[k] = v

        # Setup logging
        self.logger = logger
        self.logger.propagate = False
        if log_level:
            self.logger.setLevel(log_level)
        if not self.__class__._stream_handler:
            self.__class__._stream_handler = logging.StreamHandler()
            self.__class__._stream_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)8s: %(message)s',
                '%Y-%m-%d %H:%M:%S'
            ))
            if self.__class__._stream_handler not in self.logger.handlers:
                self.logger.addHandler(self.__class__._stream_handler)
        if isinstance(log_file, Path):
            self.__class__._file_handler = logging.FileHandler()
            self.__class__._file_handler.setFormatter(logging.Formatter(
                '%(asctime)s - %(levelname)s: %(message)s',
                '%Y-%m-%d %H:%M:%S'
            ))
            if self.__class__._file_handler not in self.logger.handlers:
                self.logger.addHandler(self.__class__._file_handler)

        # Set handler
        self._event_handler = handler or EventHandler()

        # Create scheduler
        if isinstance(scheduler, AbstractScheduler):
            self._scheduler = scheduler
        elif isinstance(scheduler, Dict):
            scheduler.setdefault('logger', self.logger)
            self._scheduler = ThreadedScheduler(**scheduler)

        # Set path from where to load model tasks
        self._model_tasks = Path(model_tasks) if model_tasks else None

        # Set the task registry (Which loads all tasks) and call event handler
        self._registry = TaskRegistry(self._model_tasks)
        try:
            self._event_handler.on_tasks_loaded([t.instance for t in self._registry.get_tasks()])
        except Exception as e:
            self.logger.error(f'Event handler error for loading tasks ({e})')

        # Set default workspace (Will set also in scheduler)
        self.workspace = Path(tempfile.gettempdir()) / get_hash(self.title)

        # Set default cache (Will set also in scheduler)
        self.cache = (self.get_parameter('LOCALAPPDATA')[0] or Path.home()) / f'.modelcache' / get_hash(self.title)

        # Apply configuration
        if model_config:
            self.configure(model_config)

        # Provide user interaction
        if interactive:
            self.interactive()

    def _build_graph(self, task_selection: Union[List, Set] = None) -> Union[nx.DiGraph, nx.MultiDiGraph]:
        """
        Returns a directed graph from all currently registered model tasks respecting their dependencies
        """
        if task_selection:
            tasks = [(t.name, t.inputs) for t in self._registry.get_tasks() if t.name in task_selection]
        else:
            tasks = [(t.name, t.inputs) for t in self._registry.get_tasks()]

        task_ids = [t[0] for t in tasks]
        nodes = []
        edges = []
        for name, inputs in tasks:
            if inputs:
                for i in inputs.values():
                    if i.dependency not in task_ids:
                        if i.dependency not in self._unresolved:
                            self._unresolved.append(i.dependency)
                            self.logger.warning(f'Missing task dependency: Cannot find task "{i.dependency}" required by "{name}"')
                    edges.append((i.dependency, name))
            else:
                nodes.append(name)
        graph = nx.DiGraph() if task_selection else nx.MultiDiGraph()
        graph.add_edges_from(edges)
        graph.add_nodes_from(nodes)
        return graph

    def _get_path_nodes(self, nodes: Union[str, None]) -> Tuple:
        """
        Returns a tuple with "entry" task and "begin" path
        """
        tasks = nodes.split(' ') if nodes else []
        if len(tasks) > 2:
            self.logger.error('Too many tasks specified (Maximum 2 allowed)')
            sys.exit()
        return (
            tasks[-1] if tasks else None,
            tasks[0] if len(tasks) == 2 else None
        )

    def _get_verified_submodels(self, task: str = None) -> List[nx.DiGraph]:
        """
        Returns a list of model graphs that were checked for validity
        """
        # Get tasks
        entry_task, first_task = self._get_path_nodes(task)

        return [
            g for g in self.resolve(task=entry_task) if self.verify_resolved_graph(
                g,
                entry_task=entry_task,
                begin_task=first_task
            )
        ]

    def configure(self, *args: [Path, Dict]):
        """
        Configure the model with one or more configuration options.
        Each configuration will overwrite any previously applied configuration.
        Use this method for instance with a template configuration and add
        the specific configuration as second argument.
        """

        quote = '"'
        for configuration in args:
            self.logger.info(f'Applying configuration {"file " + quote + str(configuration) + quote if isinstance(configuration, Path) else "object"}')
            try:
                if isinstance(configuration, dict):
                    parameters = {k: {'value': convert_parameter(v), 'source': 'Sourcecode Configuration'} for k, v in configuration.items()}
                else:
                    parameters = load_configuration_file(configuration)
            except Exception as e:
                self.logger.error(f'Could not read model configuration "{configuration}" ({e})')
                parameters = None
            if parameters:
                for k, v in parameters.items():
                    if not v.get('value') and k in self._configuration and self._configuration.get(k, {}).get('value'):
                        continue
                    else:
                        self._configuration[k] = v

    def reset(self):
        """
        Reset the current model configuration
        """

        logger.info('Resetting model configuration')
        self._configuration = {}

    def get_parameter(self, parameter: str) -> Tuple[Any, Union[str, None]]:
        """
        Looks up and returns a parameter (including its configuration source) specified by a key value.
        If the parameter key cannot be found in the model configuration, the parameter is also looked
        up in the  environment parameters and when not found, ultimately a `None` value tuple is returned
        """
        if parameter in self._configuration:
            if self._configuration.get(parameter, {}).get('value') not in (None, ''):
                return self._configuration.get(parameter, {}).get('value'), self._configuration.get(parameter, {}).get('source')
        if os.getenv(parameter) not in (None, ''):
            return convert_parameter(os.environ.get(parameter)), 'Environment parameter'
        return None, None

    def get_model_parameters(self, task: str = None, graph: Union[nx.DiGraph, nx.MultiDiGraph] = None) -> Dict:
        """
        Returns a dictionary of all configuration parameters and tasks using them.
        used by the complete model or a submodel specified by an entry task or an existing graph.
        """

        # Get validated (sub-)models
        if graph:
            models = [graph]
        else:
            models = self._get_verified_submodels(task=task)

        # Get parameters from submodels
        parameters = {}
        for m in models:
            for t in sort_topologically(m):
                for k, p in self._registry.get_task(t).parameters.items():
                    parameters.setdefault(p.key, []).append(t)

        return parameters

    def run(
        self,
        task: str = None,
        config: List[Union[Path, Dict]] = None,
        workspace: Path = None,
        cache: Path = None,
        use_cache: bool = None,
        handler: EventHandler = None
    ):
        """
        Run the complete model or only a submodel
        """

        # Set workspace
        workspace = Path(workspace) if workspace else self.workspace
        self.workspace = workspace
        if not workspace.exists():
            workspace.mkdir(exist_ok=True, parents=True)
        self.logger.info(f'Using workspace folder "{workspace}" for model processing')

        # Set cache
        cache = Path(cache) if cache else self.cache
        self.cache = cache
        if not cache.exists():
            cache.mkdir(exist_ok=True, parents=True)
        if use_cache is False:
            self.logger.info(f'Running model without intermediate result cache')
        else:
            self.logger.info(f'Using model cache folder "{cache}" for model results')

        # Configure model (Apply a configuration provided at runtime)
        if config:
            self.configure(*config)
        if self._arguments and self._arguments.list_config:
            self.list_parameters()

        # Get validated (sub-)models
        if task:
            self.logger.info(f'Running model only for specified task "{task}"')
        submodels = self._get_verified_submodels(task=task)

        # TODO: Remove all descendant from graph before first_task!
        # if first_task:
        #     graph = [graph[0][graph[0].index(first_task):]]
        #     graph = [graph[0][graph[0].index(first_task):]]

        # Check if all submodels can be executed
        for i, s in enumerate(submodels):
            model_name = 'submodel ' + str(i + 1) if len(submodels) > 1 else 'model'
            submodel_tasks = set(s.nodes)
            registry_tasks = set([t.name for t in self._registry.get_tasks()])
            if len(missing := submodel_tasks.difference(registry_tasks)) > 0:
                for m in missing:
                    self.logger.error(f'Cannot run {model_name} because of missing task "{m}" (Correct dependencies!)')
                sys.exit()

        # Schedule the model/submodels for execution
        model_parameters = {}
        parameter_sources = {}
        for i, s in enumerate(submodels):
            model_name = f'submodel ' + str(i + 1) if len(submodels) > 1 else f'model'

            # Prepare all model parameters (and check if all required parameters can be fulfilled)
            self.logger.info(f'Preparing {model_name} parameters...')
            task_parameters = self.get_model_parameters(graph=s)
            task_parameters_missing = []
            for p_key, p_tasks in task_parameters.items():
                if p_key not in model_parameters:
                    try:
                        # Get value from configuration
                        p_value, p_source = self.get_parameter(p_key)
                        # Create parameter instance and instantiate it with a value
                        p_type, p_options = [(p.type, p.options) for n, p in self._registry.get_task(p_tasks[0]).parameters.items() if p.key == p_key][0]
                        p_instance = model_parameters.setdefault(
                            p_key,
                            p_type(p_key, options=convert_parameter(p_options), value=p_value)
                        )
                        parameter_sources[p_key] = p_source
                        # If value was empty, try to use parameter instance to get parameter value
                        if p_value is None:
                            p_instance.configure_value(p_value)
                        # If the parameter still has no value, we could not lookup any and need to stop
                        if p_instance.value is None:
                            task_parameters_missing.append(dict(tasks=p_tasks, parameter=p_key))
                            continue
                    except (IndexError, KeyError):
                        self.logger.error(f'Cannot find model parameter "{p_key}" in task dependencies')
                        sys.exit()
                instance_value = '********' if model_parameters.get(p_key).obfuscate else model_parameters.get(p_key).value
                instance_source = parameter_sources.get(p_key)
                self.logger.info(
                    f'''{model_name.capitalize()} uses parameter "{p_key} = {shorten(
                        str(instance_value),
                        width=70, placeholder="..."
                    )}" (Type: {type(instance_value).__name__}, Parameter: {p_instance.__class__.__name__}, Source: {instance_source})''')
                if p_key in model_parameters:
                    continue

            # Check if we miss some parameter configurations
            if len(task_parameters_missing) > 0:
                for missing in task_parameters_missing:
                    self.logger.error(f'{model_name.capitalize()} parameter "{missing["parameter"]}" required by task(s) "{", ".join(missing["tasks"])}" is not configured (Update configuration)')
                sys.exit()

            # Create job plans for the model
            plans = self.create_job_plans(s, parameters=model_parameters)
            for pi, plan in enumerate(plans):
                self.logger.debug(f'Created task schedule for {model_name}: {" >>> ".join([", ".join([t.get("instance").name for t in p]) for p in plan])}')
                self._scheduler.schedule(plan, pipeline=f'{i}{pi}')
                self.logger.info(f'Scheduled all tasks for {model_name}')
                try:
                    (handler or self._event_handler).on_tasks_scheduled([t.get("instance") for p in plan for t in p])
                except Exception as e:
                    self.logger.error(f'Event handler error for scheduled tasks ({e})')

        # Start the scheduler (and set a dynamic workspace if provided)
        if workspace != self._scheduler.workspace:
            self._scheduler.workspace = workspace
        self.logger.info(f'Starting task scheduler ({self._scheduler.__class__.__name__})...')
        self._scheduler.run(use_cache=use_cache, handler=handler or self._event_handler)

        # Reset the registry
        self._registry.reset_registry()

    def create_job_plans(self, graph=Union[nx.Graph, nx.MultiDiGraph], parameters: Dict = {}) -> List[List]:
        """
        Create a job plan, either being a sequential list of jobs (tasks) or a list of grouped jobs which can
        be executed sequential & simultaneously by the job scheduler
        """

        # Recursively construct jobs with task instances
        def build_jobs(graph: nx.DiGraph, node: str, parent: str = None, jobs: Dict = {}):
            # Recursively traverse to its predecessors before we can create a job for the task
            for p in graph.predecessors(node):
                build_jobs(graph, p, parent=node, jobs=jobs)
            # Add a job object with a properly instantiated task instance (Add task variables, but set value later)
            if node not in jobs:
                # Use the task instance from the registry
                task = self._registry.get_task(task=node)
                task_instance = task.instance
                # Add parameter instances to task instance (Set already value from configuration)
                for attr, parameter in task.parameters.items():
                    if not isinstance(getattr(task_instance, attr), TaskVariable):
                        setattr(task_instance, attr, parameters.get(parameter.key))
                # Add input instances to task instance (Will be updated later with a value)
                for attr, input in task.inputs.items():
                    if not isinstance(getattr(task_instance, attr), TaskVariable):
                        setattr(task_instance, attr, input.type(
                            id=attr,
                            task=task_instance,
                            dependency=(input.dependency, input.name)
                        ))
                # Add output instances to task instance (Will be updated later with a value)
                for attr, output in task.outputs.items():
                    if not hasattr(task_instance, attr):
                        setattr(task_instance, attr, output.type(
                            id=attr,
                            task=task_instance
                        ))
                job = dict(
                    instance=task_instance,
                    registry=task,
                    start=is_start_node(graph, node),
                    end=is_end_node(graph, node)
                )
                jobs.update({node: job})
            return jobs

        # Build jobs
        plans = []
        for root in get_root_nodes(graph):
            # Create a job plan for each graph
            jobs = build_jobs(graph, root)
            if self._scheduler.concurrent:
                self.logger.info(f'Creating concurrent task schedule')
                plan = [list(map(lambda t: jobs[t], g)) for g in sort_topologically_parallel(graph)]
            else:
                self.logger.info(f'Creating sequential task schedule')
                plan = [[jobs[t]] for t in sort_topologically(graph)]
            plans.append(plan)

        # Return list of execution plans
        return plans

    def list_parameters(self):
        """
        Displays a list of all configured parameters
        """

        print('Configured model parameters:\n')
        parameters = sorted(list(self._configuration.keys()), key=str.lower)
        for k, v in [(p, self._configuration[p]) for p in parameters]:
            s = v.get('source')
            v = v.get('value')
            v_display = shorten(str(v), width=65, placeholder='...')
            print(f'\t- {shorten(k, width=30, placeholder="..."):30} = {v_display:65} (Type: {type(v).__name__}, Source: {s})')

        print('\nEnvironment parameters:\n')
        parameters = sorted(list(self._configuration.keys()), key=str.lower)
        for k, v in os.environ.items():
            v = convert_parameter(v)
            v_display = shorten(str(v), width=65, placeholder='...')
            print(f'\t- {shorten(k, width=30, placeholder="..."):30} = {v_display:65} (Type: {type(v).__name__}, Source: Environment)')

    def render_graph(
        self,
        task: str = None,
        output: Path = None
    ):
        """
        Output an image or mermaid diagram of the graph (and optionally save it to a file)
        """

        # Get tasks
        entry_task, first_task = self._get_path_nodes(task)

        # Get graphs
        graphs = self.resolve(task=entry_task)

        def sanitize_description(text: str) -> str:
            return text

        # Mermaid output
        if output and output.suffix == '.md':
            self.logger.info('Creating mermaid graph')
            styles = dict(
                START='fill:#037aa8,stroke:#fff,stroke-width:2px,color:#fff',
                TASK='fill:#000,stroke:#fff,stroke-width:1px,color:#fff',
                END='fill:#008c44,stroke:#fff,stroke-width:2px,color:#fff'
            )
            mermaid = ''

            for i, g in enumerate(graphs):
                groups = {}
                relations = [(
                    self._registry.get_task(t1).instance,
                    self._registry.get_task(t2).instance
                ) for (t1, t2) in g.edges()]
                inter_group_relations = []
                start_tasks = [t for t in list(g.nodes) if is_start_node(g, t)]
                end_tasks = [t for t in list(g.nodes) if is_end_node(g, t)]

                mermaid += f'# Model{": " + end_tasks[0] if len(end_tasks) == 1 else " " + i + 1 if len(graphs) > 1 else ""}\n```mermaid\nflowchart TD\n'

                for task in [self._registry.get_task(t).instance for t in list(g.nodes)]:
                    group = task.group or 'Model'
                    groups.setdefault(group, []).append(dict(
                        name=task.name,
                        description='<font size=2>{}</font>'.format(sanitize_description(shorten(
                            "<br>".join(wrap(task.__doc__.strip().split('\n')[0], 30)),
                            width=70, placeholder="..."
                        ))) if task.__doc__ else ""
                    ))


                for group, group_tasks in groups.items():
                    if len(groups) > 1:
                        mermaid += f'  subgraph {group}[Group: {group}]\n'
                    for t in group_tasks:
                        mermaid += f'    {t["name"]}("{"<br>".join([t["name"], t["description"]])}"){":::END" if t["name"] in end_tasks else ":::START" if t["name"] in start_tasks else ":::TASK"}\n'
                    mermaid += '\n'
                    for t1, t2 in relations:
                        group1 = t1.group or 'Model'
                        group2 = t2.group or 'Model'
                        # Add relations within the same group
                        if group1 == group2 and group1 == group:
                            mermaid += f'    {t1.name} --> {t2.name}\n'
                        # Add relations to other groups
                        if group1 != group2:
                            inter_group_relations.append(f'  {t1.name} --> {t2.name}\n')
                    if len(groups) > 1:
                        mermaid += '  end\n'
                for igr in set(inter_group_relations):
                    mermaid += igr
                for style, cls in styles.items():
                    mermaid += f'  classDef {style} {cls}\n'
                mermaid += '```\n'

            with open(output, 'w') as of:
                of.write(mermaid)
                self.logger.info(f'Wrote mermaid graph to "{output}"')
        else:
            try:
                # Create graph plot
                self.logger.info('Creating graph figure plot')
                import matplotlib
                import matplotlib.pyplot as plt
                from .util.network import hierarchical_position
                figure = plt.figure(
                    figsize=(12, 8 * len(graphs)),
                    dpi=150,
                    tight_layout=True
                )
                figure.suptitle(f'{self.title.capitalize()} tasks')

                # Add sub-plots per model
                for i, g in enumerate(graphs):
                    ax = figure.add_subplot(int(f'{len(graphs)}1{i+1}'))
                    if len(graphs) > 1:
                        ax.set_title(
                            f'Submodel {i+1}',
                            loc='left'
                        )
                    position = hierarchical_position(g, sort_topologically(g)[-1])
                    nx.draw_networkx_labels(
                        g,
                        position,
                        font_size=11,
                        verticalalignment='bottom',
                        bbox={
                            'ec': 'k',
                            'fc': 'yellow',
                            'alpha': 0.8,
                            'boxstyle': 'round'
                        },
                        ax=ax
                    )
                    nx.draw_networkx_nodes(
                        g,
                        position,
                        node_size=600,
                        node_color='w',
                        alpha=0.0,
                        ax=ax
                    )
                    nx.draw_networkx_edges(
                        g,
                        position,
                        alpha=0.75,
                        width=1,
                        edge_color='b',
                        arrowsize=26,
                        arrowstyle='-|>',
                        min_target_margin=0,
                        min_source_margin=20,
                        ax=ax
                    )
                    ax.set_axis_off()

                # Render / save plot
                if output:
                    # Save to image file
                    matplotlib.use('Agg')
                    figure.savefig(output)
                    self.logger.info(f'Saved graph figure plot to file "{output}"')
                else:
                    # Show graph
                    plt.show()
            except Exception as e:
                self.logger.error(f'Failed to generate graph figure plot ({e})')

    def create_document(
        self,
        task: str = None,
        document: Path = None
    ):
        """
        Output a graph documentation (and optionally save it to a file)
        """

        # Get tasks
        entry_task, first_task = self._get_path_nodes(task)

        # Get graph
        graphs = [sort_topologically(g) for g in self.resolve(task=entry_task)]

        # Create document
        try:
            quote = '"'
            self.logger.info(f'Creating model document{" for task " + quote + entry_task + quote if entry_task else ""}')
            content = [f'# Model: {self.title}{" (" + entry_task + ")" if entry_task else ""}']
            if not document:
                content.insert(0, '=' * len(content[-1].replace('#', '')))
                content.append('=' * len(content[-1].replace('#', '')))
            if len(graphs) > 1 and document:
                for gi, g in enumerate(graphs):
                    content.append(f'- [Submodel {gi + 1}](#submodel{gi + 1})')
            for gi, g in enumerate(graphs):
                if len(graphs) > 1:
                    if not document:
                        content.append('')
                        content.append(f'Submodel {gi + 1}:')
                    else:
                        content.append(f'## Submodel {gi + 1}: <a name="submodel{gi + 1}"> </a>')
                    if not document:
                        content.append('=' * len(content[-1].replace('#', '')))
                for ti, t in enumerate(g):
                    if not document:
                        content.append('')
                    content.append(f'### Task {ti}: <a name="{t}">{t}</a>')
                    if document:
                        content.append('')
                        content.append('---')
                    else:
                        content.append('-' * len(content[-1].replace('#', '')))
                    t_object = self._registry.get_task(t)
                    if not t_object:
                        content.append(f'**Error**: Task {t} cannot be resolved and is missing')
                    else:
                        content.append(f'**Description**: {t_object.instance.__doc__.strip()}')
                        # Parameters
                        if document and len(t_object.parameters) > 0:
                            content.append('')
                            content.append('Parameter | Type | Key')
                            content.append('--- | --- | ---')
                        for p, p_object in t_object.parameters.items():
                            if document:
                                content.append(f'{p} | {p_object.type.__name__} | {p_object.key}')
                            else:
                                content.append(f'- Parameter: {p} (Type={p_object.type.__name__}, Key={p_object.key})')
                        # Inputs
                        if document and len(t_object.inputs) > 0:
                            content.append('')
                            content.append('Input | Type | Dependency')
                            content.append('--- | --- | ---')
                        for i, i_object in t_object.inputs.items():
                            if document:
                                content.append(f'{i} | {i_object.type.__name__} | [{i_object.dependency} > {i_object.name}](#{i_object.dependency})')
                            else:
                                content.append(f'- Input: {i} (Type={i_object.type.__name__}, Dependency={i_object.dependency} > {i_object.name})')
                        # Outputs
                        if document and len(t_object.outputs) > 0:
                            content.append('')
                            content.append('Output | Type')
                            content.append('--- | ---')
                        for o, o_object in t_object.outputs.items():
                            if document:
                                content.append(f'{o} | {o_object.type.__name__}')
                            else:
                                content.append(f'- Output: {o} (Type={o_object.type.__name__})')

            # Show / write document
            if not document:
                for line in content:
                    print(line.replace('#', '').replace('*', ''))
            else:
                with open(document, 'w') as of:
                    of.write('\n'.join(content))
        except Exception as e:
            self.logger.error(f'Failed to generate graph document ({e})')

    def verify_resolved_graph(
        self,
        graph: Union[nx.DiGraph, nx.MultiDiGraph],
        entry_task: str = None,
        begin_task: str = None
    ) -> bool:
        """
        Verifies that resolved path matches the provided task points
        """
        topological_graph = sort_topologically(graph)
        if len(topological_graph) == 0:
            if entry_task:
                self.logger.error(f'Specified task "{entry_task}" cannot be found (Specify correct task)')
                return False
            else:
                self.logger.error(f'The resolved graph is empty (Check task dependencies)')
                return False
        if entry_task and begin_task:
            if begin_task not in topological_graph:
                self.logger.error(f'Tasks ({begin_task} -> {entry_task}) are not in same task branch or in incorrect order (Consult model with --graph)')
                return False
        return True

    def resolve(self, task: str = None, taskgroup: str = None) -> List[nx.DiGraph]:
        """
        Returns the task sequence graph for the whole model or a part of it
        """

        # TODO: Support task groups?

        self.logger.info('Resolving model task graph...')

        # Build complete graph
        graph = self._build_graph()

        # If entry point is specified
        if task:
            try:
                predecessors = nx.descendants(graph.reverse(), task)
            except nx.exception.NetworkXError as e:
                self.logger.error(f'Could not resolve model graph for task "{task}" ({e})')
                sys.exit()
            predecessors.add(task)
            sub_graphs = [self._build_graph(task_selection=predecessors)]
        else:
            # Find all end nodes
            root_nodes = []
            for component in nx.weakly_connected_components(graph):
                sub_graph = graph.subgraph(component)
                root_nodes.extend(get_root_nodes(sub_graph))
            # Build a subgraph for each found root node
            sub_graphs = []
            for n in root_nodes:
                predecessors = nx.descendants(graph.reverse(), n)
                predecessors.add(n)
                sub_graphs.append(self._build_graph(task_selection=predecessors))

        # Check if sub-graphs are valid
        for sg in sub_graphs:
            if not sg.is_directed():
                self.logger.error(f'The process graph is not directed and therefore not supported (Correct task dependencies)')
                sys.exit()

            if not nx.is_directed_acyclic_graph(sg):
                self.logger.error(f'The process graph is acyclic and therefore not supported (Correct task dependencies)')
                sys.exit()

        # Return graphs
        return sub_graphs

    def interactive(self):
        """
        Does user interaction via command line parameters. Set the model to non-interactive if you
        want to programmatically call model methods. By default a model offers the following actions:
        """
        parser = ArgumentParser(
            prog=f'{self.__class__.__name__}',
            description=f'Model "{self.title}": Run model, show help, or print graph, etc.',
            add_help=True
        )
        parser.add_argument(
            '-t',
            '--task',
            required=False,
            help='Enter the model at the specified model task'
        )
        parser.add_argument(
            '-f',
            '--force',
            action='store_true',
            default=False,
            required=False,
            help='Force a complete re-run of all model tasks and do not use the result cache'
        )
        parser.add_argument(
            '-l',
            '--list',
            action='store_true',
            default=False,
            required=False,
            help='List all model tasks in their execution order'
        )
        parser.add_argument(
            '-lc',
            '--list_config',
            action='store_true',
            default=False,
            required=False,
            help='List all configured model parameters'
        )
        parser.add_argument(
            '-g',
            '--graph',
            default=False,
            action='store_true',
            required=False,
            help='Display a model graph visualisation (Or optionally write it to an --output file)'
        )
        parser.add_argument(
            '-d',
            '--doc',
            default=False,
            action='store_true',
            required=False,
            help='Display a document of the task graph (Or optionally write it to an --output file)'
        )
        parser.add_argument(
            '-c',
            '--config',
            nargs='*',
            default=None,
            required=False,
            help='Specify one or multiple configuration files (*.ini, *.env, *.json) which will get applied in their specified order'
        )
        parser.add_argument(
            '-o',
            '--output',
            default=None,
            required=False,
            help='Specify an output file for graph images or documents'
        )
        parser.add_argument(
            '-w',
            '--workspace',
            default=None,
            required=False,
            help='Specify a workspace location for the processing the model'
        )
        parser.add_argument(
            '-mc',
            '--cache',
            default=None,
            required=False,
            help='Specify a model cache for storing intermediate task results'
        )
        parser.add_argument(
            '-r',
            '--run',
            default=False,
            action='store_true',
            required=False,
            help='Run the model (Default action). Is required when model should be run and graph shown'
        )

        self._arguments = parser.parse_args()
        if hasattr(self._arguments, 'help'):
            parser.print_help()
        elif self._arguments.list:
            # Resolve graphs
            tasks = [sort_topologically(g) for g in self.resolve(self._arguments.task)]
            task_names = [t for g in tasks for t in g]
            task_enumeration = {ig: {it: t for it, t in enumerate(g)} for ig, g in enumerate(tasks)}

            # Print module selection list
            index = 0
            task_index = {}
            print(f'Specify model task to run (One task or start and end task):')
            for gi, graph in task_enumeration.items():
                if len(list(task_enumeration.keys())) > 1:
                    print(f'\nSubmodel {gi+1} tasks:')
                else:
                    print(f'\nModel tasks:')
                for mi, m in graph.items():
                    task_index.update({index: m})
                    print(f'\t{index:4}: {m}')
                    index += 1

            # Get user selection
            task_input = input('\nSpecify model task(s) from list (Number or name): \n')
            task_input = [t.strip() for t in task_input.split(' ') if t]

            def get_index_task(task: str):
                if task.isnumeric():
                    return task_index[int(task)]
                elif task in task_names:
                    return task
                else:
                    raise ValueError()

            try:
                task_input = list(map(get_index_task, task_input))
            except (IndexError, KeyError, ValueError) as e:
                self.logger.error(f'Entered process task "{" ".join(task_input)}" unknown (Enter correct task number(s) or task name(s))')
                sys.exit()

            self.run(
                task=' '.join(task_input),
                config=[Path(c) for c in self._arguments.config] if self._arguments.config else None,
                workspace=self._arguments.workspace,
                cache=self._arguments.cache,
                use_cache=not self._arguments.force
            )
        elif self._arguments.graph and not self._arguments.run:
            self.render_graph(
                task=self._arguments.task,
                output=Path(self._arguments.output) if self._arguments.output else None
            )
        elif self._arguments.doc and not self._arguments.run:
            self.create_document(
                task=self._arguments.task,
                document=Path(self._arguments.output) if self._arguments.output else None
            )
        elif self._arguments.list_config and not self._arguments.run:
            if self._arguments.config:
                self.configure(*[Path(c) for c in self._arguments.config])
            self.list_parameters()
        else:
            if self._arguments.graph:
                self.render_graph(
                    task=self._arguments.task,
                    output=Path(self._arguments.output) if self._arguments.output else None
                )
            if self._arguments.doc:
                self.create_document(
                    task=self._arguments.task,
                    document=Path(self._arguments.output) if self._arguments.output else None
                )
            self.run(
                task=self._arguments.task,
                config=[Path(c) for c in self._arguments.config] if self._arguments.config else None,
                workspace=self._arguments.workspace,
                cache=self._arguments.cache,
                use_cache=not self._arguments.force,
            )
