import treelib
from treelib import Tree
import numpy as np
import pandas as pd


def get_paths_dict(tree: treelib.Tree):
    """
    获取从根节点到叶子节点的路径，并将ID替换为TAG，返回一个字典。

    参数:
    tree (Tree): treelib中的树结构。

    返回:
    dict: 包含从根节点到叶子节点路径的字典，路径以节点TAG表示。
    """
    # 获取所有从根节点到叶子节点的路径
    paths = tree.paths_to_leaves()
    # 将路径从ID转换为TAG，并构建字典
    paths_dict = {}
    for i, path in enumerate(paths):
        # 使用tag替代id
        tag_path = [tree.get_node(node_id).tag for node_id in path]
        paths_dict[f"path_{i + 1}"] = tag_path
    return paths_dict


def dict_to_df(paths_dict, names, columns):
    """
    根据获取的路径，返回df。

    参数：
    paths_dict：路径
    names：多级索引的列名
    columns：值的列名

    返回：
    df
    """
    # 转换为多级索引
    multi_index = pd.MultiIndex.from_tuples([tuple(path) for path in paths_dict.values()],
                                            names=names)
    # 创建DataFrame，值为NaN
    df = pd.DataFrame(np.nan, index=multi_index, columns=columns)
    return df
