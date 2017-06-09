#!/usr/bin/env python
"""

"""
import graph

class ComponentMgmt():
    def __init__(self):
        """
        Component Mgmt class maintains a dependency graph as a graph data structure.
        """
        self.__dep_graph = graph.Graph()

    def add_dependencies(self, child, parents):
        """
        Iterates through list of parents,
            adds a parent to the child node and a child to the parent node.
        Ex: DEPEND BROWSER HTML TCPIP
            HTML and TCPIP are the parents, BROWSER is the child
        :param child:
        :type str:
        :param parents:
        :type list of str:
        """
        for parent in parents:
            self.__dep_graph.insert_parent_for(parent_name=parent,
                                               child_name=child)
            self.__dep_graph.insert_child_from(parent_name=parent,
                                               child_name=child)
        # self.__dep_graph.print_graph()

    def install_component(self, component_name):
        """
        Recursively installs uninstalled parents and the given component.
        :param component_name:
        :type str:
        """
        parents_stack = list(self.__dep_graph.get_parents(component_name))
        while parents_stack:
            curr_parent = parents_stack.pop()
            if not self.__is_installed(curr_parent.get_name()):
                self.__install_comp(curr_parent.get_name())
                print("\tInstalling ", curr_parent.get_name())
            parents = self.__dep_graph.get_parents(curr_parent.get_name())
            if parents:
                parents_stack.extend(parents)
        if not self.__is_installed((component_name)):
            self.__install_comp(component_name)
            print("\tInstalling ", component_name)
        else:
            print("\t", component_name, " is already installed.")
        # self.__dep_graph.print_graph()

    def remove_component(self, component_name):
        """
        Iteratively removes given component and any parent components that are safe to remove.
        :param component_name:
        :type str:
        """
        if not self.__dep_graph.has_node(component_name):
            print("\t", component_name, " is not installed.")
            return
        children = self.__dep_graph.get_children(component_name)
        if children:
            print("\t", component_name, " is still needed.")
            return
        parents_queue = list(self.__dep_graph.get_parents(component_name))
        print("\tRemoving", component_name)
        self.__uninstall_comp(component_name)
        i = 0
        while parents_queue:
            curr_parent = parents_queue.pop(0)
            curr_parent_name = curr_parent.get_name()
            # print("curr", curr_parent_name)
            children = self.__dep_graph.get_children(curr_parent_name)
            if not children:
                print("\tRemoving", curr_parent_name)
                self.__uninstall_comp(curr_parent_name)
        # self.__dep_graph.print_graph()

    def list_components(self):
        """
        Lists the currently installed components.
        """
        components = self.__dep_graph.get_nodes()
        for component in components:
            print("\t", component)

    def __install_comp(self, component_name):
        """
        Private method to set the installed flag for a given component
        :param component_name:
        :type str:
        """
        self.__dep_graph.set_installed(component_name, True)

    def __uninstall_comp(self, component_name):
        """
        Private method used to:
            remove given component from each parent's children set
            set installed flag to False
            deletes the given component
        :param component_name:
        :type str:
        """
        self.__dep_graph.remove_parents(component_name)
        self.__dep_graph.set_installed(component_name, False)
        self.__dep_graph.remove_node(component_name)

    def __is_installed(self, component_name):
        """
        Returns True if component exists in the graph and is installed,
            False otherwise
        :param component_name:
        :type str:
        :return True, False:
        :rtype bool:
        """
        return self.__dep_graph.is_installed(component_name)
