#!/usr/bin/env python
import component_mgmt

class Driver:
    """
    Driver class reads input and uses component manager to handle the input.
    """
    def __init__(self, fname):
        self.cmgr = component_mgmt.ComponentMgmt()
        cmds = []
        with open(fname) as cmd_file:
            cmds = cmd_file.readlines()
        for cmd in (cmds):
            print(cmd)
            tokens = [t.strip() for t in cmd.split(" ")]
            if tokens[0] == 'DEPEND':
                self.handle_depend(tokens[1:])
            elif tokens[0] == 'INSTALL':
                self.handle_install(tokens[1:])
            elif tokens[0] == 'REMOVE':
                self.handle_remove(tokens[1:])
            elif tokens[0] == 'LIST':
                self.handle_list()

    def handle_depend(self, tokens):
        child = tokens[0]
        parents = tokens[1:]
        self.cmgr.add_dependencies(child, parents)

    def handle_install(self, tokens):
        self.cmgr.install_component(tokens[0])

    def handle_remove(self, tokens):
        self.cmgr.remove_component(tokens[0])

    def handle_list(self):
        self.cmgr.list_components()

def main():
    Driver("input.txt")

if __name__ == "__main__":
    main()
