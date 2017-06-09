#!/usr/bin/env python
"""
Graph Library:

Classes: GraphNode and Graph
"""

class GraphNode:
    """
    A graph node that has a name, two kinds of edges -
        child edges(packages that depend on it) and
        parent edges (packages that it depends on);
         and a boolean flag installed, with public APIs to add/remove these attributes.
    """
    def __init__(self, name):
        self.__component_name = name
        self.__children = set()
        self.__parents = set()
        self.__installed = False

    def __str__(self):
        parents = [p.__component_name for p in self.__parents]
        children = [c.__component_name for c in self.__children]
        node_rep = (str(self.__component_name) +
                    " Parents: " + str(parents) +
                    " Children: " + str(children) +
                    " Installed: " + str(self.__installed))
        return node_rep

    def get_name(self):
        return self.__component_name

    def get_parents(self):
        return self.__parents

    def get_children(self):
        return self.__children

    def add_parent(self, parent):
        self.__parents.add(parent)

    def add_child(self, child):
        self.__children.add(child)

    def remove_parent(self, parent):
        if parent in self.__parents:
            self.__parents.remove(parent)

    def remove_child(self, child):
        if child in self.__children:
            self.__children.remove(child)

    def is_installed(self):
        return  self.__installed

    def set_installed(self, installed):
        self.__installed = installed

class Graph:
    '''
    Graph has a dict of {node_name:GraphNode}.
        It has public APIs to get nodes, parents, children;
            add/remove parents/children by adding/removing edges
            and APIs to check if a component exists or is installed.
    '''

    def __init__(self):
        self.__nodes = {}

    def get_nodes(self):
        return self.__nodes.keys()

    def remove_parents(self, child_name):
        '''
        Private method used to remove edge from parent to child.
        '''
        child_node = self.__nodes.get(child_name)
        if child_node:
            parent_nodes = child_node.get_parents()
            for parent_node in parent_nodes:
                parent_node.remove_child(child_node)

    def remove_node(self, name):
        if name in self.__nodes:
            del self.__nodes[name]

    def has_node(self, name):
        if name in self.__nodes:
            return True
        return False

    def insert_child_from(self, parent_name, child_name):
        '''
        Creates an edge from parent to child.
        '''
        if parent_name not in self.__nodes:
            self.__nodes[parent_name] = GraphNode(parent_name)
        parent_node = self.__nodes.get(parent_name)
        if child_name not in self.__nodes:
            self.__nodes[child_name] = GraphNode(child_name)
        child_node = self.__nodes.get(child_name, GraphNode(child_name))
        parent_node.add_child(child_node)
        # print('Inserted child {} for parent {}'.format(child_name, parent_name))

    def insert_parent_for(self, parent_name, child_name):
        '''
        Creates an edge from child to parent
        '''
        if parent_name not in self.__nodes:
            self.__nodes[parent_name] = GraphNode(parent_name)
        parent_node = self.__nodes.get(parent_name)
        if child_name not in self.__nodes:
            self.__nodes[child_name] = GraphNode(child_name)
        child_node = self.__nodes.get(child_name, GraphNode(child_name))
        child_node.add_parent(parent_node)
        # print('Inserted parent {} for child {}'.format \(parent_name, child_name))

    def get_parents(self, name):
        if name in self.__nodes:
            return self.__nodes[name].get_parents()
        else:
            return []

    def get_children(self, name):
        if name in self.__nodes:
            return  self.__nodes[name].get_children()
        else:
            return []

    def set_installed(self, name, installed):
        if name not in self.__nodes:
            self.__nodes[name] = GraphNode(name)
        return self.__nodes[name].set_installed(installed)

    def is_installed(self, name):
        if name in self.__nodes:
            return self.__nodes[name].is_installed()

    def print_graph(self):
        graph_rep = ''
        print(self.__nodes.keys())
        for name, node in self.__nodes.items():
            graph_rep += str(node)
            graph_rep += '\n'
        print(graph_rep)

