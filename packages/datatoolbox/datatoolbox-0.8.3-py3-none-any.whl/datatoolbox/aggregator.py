#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:13:34 2024

@author: andreasgeiges
"""


from treelib import Node, Tree


from copy import copy
from treelib import Node, Tree


tree = Tree()
n1 = tree.create_node("IPC0", 'IPC0') 
tree.create_node("IPC1", 'IPC1',  parent = n1)# root nod


tree2 = Tree()
tree2.create_node('IPC1', 'IPC1')
tree2.create_node('IPC1a', 'IPC1a', parent = 'IPC1')
tree2.create_node('IPC1b', 'IPC1b', parent = 'IPC1')


#tree.paste('IPC1', tree2)

print(tree)
#%%
class Aggregator():
    
    def __init__(self):
        
        self.tree = None
        
    def _dict2tree(self, relation:dict):
        
        trees = list()
        for source, target in relation.items():
            
            tree = Tree()
            root = tree.create_node(source, source)
            
            if isinstance(target, list):
                
                for target_node in target:
                    tree.create_node(target_node, target_node, parent = root)
            
            else:
                tree.create_node(target, target, parent = root)
                
            trees.append(tree)
            
        return trees
            
    def _add2tree(self, tree2add):
        
       
            
       if self.tree is None:
           
           self.tree = tree2add
           
       else:
           
           # check if root in existing tree
           
           if tree2add.root in self.tree:
               
               # new tree is child of existing tree
               
               
               for node in tree2add.children(tree2add.root):
                   
                   sub_tree = tree2add.subtree(node.tag)
                   self.tree.paste(tree2add.root, sub_tree)
                   
               
           elif self.tree.root in tree2add:
                   
               # new tree is parent of existing tree
               
               old_tree = copy(self.tree)
               
               self.tree = tree2add
               
               for node in old_tree.children(old_tree.root):
                   sub_tree = old_tree.subtree(node.tag)
                   self.tree.paste(old_tree.root, sub_tree)
                   
           else:
               raise(Exception('No connecting node found'))
        
    def add_relations(self, relations : dict):
        
        trees = self._dict2tree(relations)
        
        for tree in trees:
            self._add2tree(tree)
    
    
    def _leave_to_dict(self, nid, mappings):
        
        self.tree.subtree(nid).to_dict()
        
        subtree = self.tree.children(nid)
        if len(subtree)>0:
            
            mapping = {nid: []}
            for node in self.tree.children(nid):
                
                self._leave_to_dict(node.identifier, mappings)
                mapping[nid].append(node.identifier)
                
            mappings.append(mapping)
            return mappings
            
            
        else:
            return mappings
        
        
            
        
    def bottom_up_aggregations(self):
        
        root = self.tree.root
        
        mappings = list()
        
        self._leave_to_dict(root, mappings)
        
        return mappings

        
agg = self =  Aggregator()
agg.add_relations(relations = {'IPC1': ['IPC1a', 'IPC1b']})

agg.add_relations(relations = {'IPC0': ['IPC1', 'IPC2']})
agg.add_relations(relations = {'IPC2': ['IPC2a', 'IPC2b']})
agg.add_relations(relations = {'IPC2a': ['IPC2_transport', 'IPC2_aviation']})
agg.add_relations(relations = {'IPC2_aviation': ['IPC2_aviation_national', 'IPC2_aviation_international']})

print(agg.tree)

agg.bottom_up_aggregations()
