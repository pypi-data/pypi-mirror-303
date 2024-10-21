import importlib.resources as pkg_resources
from pyvis.network import Network
from TraceRecursio import config
import networkx as nx
import inspect
import os


class Trace:
    instances = {}
    os.makedirs("../data", exist_ok=True)

    def __init__(self, input_function):
        self.__input_function__ = input_function
        self.__last_frame__ = None
        self.__n_call__ = 1

        self.edges = {}
        self.frames_order = {}
        self.parameters = {}
        self.returns = {}
        self.G = nx.DiGraph()

        Trace.instances[input_function.__name__] = self

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            current_frame = inspect.currentframe()
            self._register_parameters(str(id(current_frame)), args, kwargs)
            self._get_f_back_from_history(self.__last_frame__, current_frame)
            self.__last_frame__ = current_frame
            result = self.__input_function__(instance, *args, **kwargs)
            self.returns[str(id(current_frame))] = result
            return result

        return wrapper

    def __call__(self, *args, **kwargs):
        current_frame = inspect.currentframe()
        self._register_parameters(str(id(current_frame)), args, kwargs)
        self._get_f_back_from_history(self.__last_frame__, current_frame)
        self.__last_frame__ = current_frame
        result = self.__input_function__(*args, **kwargs)
        self.returns[str(id(current_frame))] = result
        return result

    def _get_f_back_from_history(self, last_frame, current_frame):
        if last_frame is None:
            return True

        child = str(id(current_frame))

        if (
            last_frame is not None and current_frame.f_back == last_frame.f_back
        ):  # same (DECORATED!) caller:
            parent = str(
                id(last_frame.f_back.f_back)
            )  # true parent is one level above because input_function is decorated. that's why back.back

            if child not in self.frames_order.keys():
                self._register_node(child)
            self._register_edge(parent, child)
            return

        if self._get_f_back_from_history(last_frame.f_back, current_frame):
            parent = str(id(self.__last_frame__))

            if parent not in self.frames_order.keys():
                self._register_node(parent)

            if child not in self.frames_order.keys():
                self._register_node(child)

            self._register_edge(parent, child)

            return

    def _register_node(self, node):
        self.G.add_node(node, label=node)
        self.frames_order[node] = self.__n_call__
        self.__n_call__ += 1

    def _register_edge(self, parent_node, child_node):
        self.G.add_edge(parent_node, child_node)
        self.edges[parent_node] = [child_node]

    def _register_parameters(self, frame_id, args, kwargs):
        self.parameters[frame_id] = {"args": args, "kwargs": kwargs}

    @staticmethod
    def _rename_nodes(network_with_nodes, decorated_f):
        for j, node in enumerate(network_with_nodes.nodes):
            old_label = node["label"]
            new_label = (
                f"Call n. {str(decorated_f.frames_order[old_label])} "
                f"\nargs: {str(decorated_f.parameters[old_label]['args'])}"
                f"\nkwargs: {str(decorated_f.parameters[old_label]['kwargs'])}"
                f"\nreturn: {str(decorated_f.returns[old_label])}"
            )
            network_with_nodes.nodes[j]["label"] = new_label

    @classmethod
    def get_graph(cls, instance_name):
        decorated_f = cls.instances[instance_name]
        graph = decorated_f.G

        net = Network(notebook=False, directed=True)
        net.from_nx(graph)
        cls._rename_nodes(net, decorated_f)

        net.show_buttons(filter_=["layout", "physics"])

        html_filename = f"{instance_name}.html"
        net.write_html(html_filename)

        with open(html_filename, "r") as file:
            html_content = file.read()

        css_path = pkg_resources.files(config) / "default_graph.css"
        with css_path.open("r") as f:
            html_content = html_content.replace("</head>", f.read() + "</head>")

        with open(html_filename, "w") as file:
            file.write(html_content)
