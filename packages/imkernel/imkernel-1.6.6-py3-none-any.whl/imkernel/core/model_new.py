import treelib
from treelib import Tree

# data 人员特性
SUPER_MODEL_NAME = "super_model"
SYSTEM_MODEL_NAME = "system_model"
SUB_MODEL_NAME = "sub_model"
PERSON_NAME = "person"
METHOD_NAME = "method"
PROCEDURE_NAME = "procedure"

from imkernel.utils import idgen
from imkernel.utils.tree_utils import tree_to_df


def system(supname, name, subname) -> Tree:
    tree = Tree()
    sup_node = tree.create_node(supname, idgen.next_id(), None, data=SUPER_MODEL_NAME)

    if isinstance(name, str):
        if not (isinstance(subname, str) or isinstance(subname, list)):
            raise ValueError("name为字符串时，subname必须是字符串或列表.")
        sys_node = tree.create_node(name, idgen.next_id(), sup_node.identifier, data=SYSTEM_MODEL_NAME)
        if isinstance(subname, str):
            tree.create_node(subname, idgen.next_id(), sys_node.identifier, data=SUB_MODEL_NAME)
        elif isinstance(subname, list):
            for sub in subname:
                if sub is not None:
                    tree.create_node(sub, idgen.next_id(), sys_node.identifier, data=SUB_MODEL_NAME)
    elif isinstance(name, list):
        if not isinstance(subname, list):
            raise ValueError("name为列表时，subname必须是对应长度的列表.")
        if len(name) != len(subname):
            raise ValueError(f"name与subname长度不匹配: name长度：{len(name)}, subname长度：{len(subname)}.")
        for i, sys in enumerate(name):
            sys_node = tree.create_node(sys, idgen.next_id(), sup_node.identifier, data=SYSTEM_MODEL_NAME)
            sub_list = subname[i]
            if sub_list is None:
                continue
            if isinstance(sub_list, str):
                tree.create_node(sub_list, idgen.next_id(), sys_node.identifier, data=SUB_MODEL_NAME)
            elif isinstance(sub_list, list):
                for sub in sub_list:
                    tree.create_node(sub, idgen.next_id(), sys_node.identifier, data=SUB_MODEL_NAME)
            else:
                raise ValueError(f"subname的元素必须是None或列表，第{i + 1}个数组类型为{type(sub_list).__name__}")
    else:
        raise ValueError(f"name类型错误，仅允许字符串或列表，实际为{type(name).__name__}")

    print(tree)
    return tree


def element(tree: treelib.Tree, sub_nid: str, dimension_type: str, name):
    if dimension_type not in [PERSON_NAME, METHOD_NAME, PROCEDURE_NAME]:
        raise Exception(f"dimension_type仅能为{[PERSON_NAME, METHOD_NAME, PROCEDURE_NAME]}中的一个")

    sub_node_list = list(tree.filter_nodes(lambda node: node.tag == sub_nid and node.data == SUB_MODEL_NAME))
    if len(sub_node_list) == 0:
        raise Exception(f"{sub_nid}不存在，请检查")
    elif len(sub_node_list) > 1:
        raise Exception(f"找到{len(sub_node_list)}个{sub_nid}，请检查")

    sub_node = sub_node_list[0]
    # tree.create_node(sub, idgen.next_id(), sys_node.identifier, data=PERSON_NAME)
    print(sub_node)


if __name__ == '__main__':
    tree_6 = system(supname='insofsys', name=['insofaiam', 'insoftest', 'insofrobot'], subname=[None, ['DTIS_511', 'NDT_SNPTC'], ['insoftube', 'insofbend', 'insoflaser']])
    df_6 = tree_to_df(tree_6)
    element(tree_6, 'DTIS_511', 'person', '747')
