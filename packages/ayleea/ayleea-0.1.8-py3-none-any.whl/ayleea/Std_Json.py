#!python3
# coding=utf-8
"""
FilePath     : Std_Json.py
Description  : 定义Std_Json类，用于处理大模型训练使用的标准json数据
Author       : Ayleea zhengyalin@xiaomi.com
Date         : 2024-09-13 13:00:21
Version      : 0.1.0
"""
from pathlib import Path
import json
import random
from copy import deepcopy


# 不对std_json中的item进行set判断不需要进行dumps序列化操作
class Std_Json:
    """
    形如[{}....]的json数据
    """

    def __init__(self, std_json=None):
        self.std_data = []
        if std_json:
            self.load(std_json)

    def load(self, std_json: "Std_Json" or list[dict] or dict or str or Path):
        if isinstance(std_json, Std_Json):
            self.std_data = deepcopy(std_json.std_data)
        elif isinstance(std_json, list):
            self.std_data = std_json
        elif isinstance(std_json, (str, Path)):
            with open(std_json, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    self.std_data = data
                else:
                    raise TypeError("json file must contain a list of objects")
        elif isinstance(std_json, dict):
            self.std_data = [std_json.copy()]
        else:
            raise TypeError("std_json must be Std_Json, list, dict, str, or Path")

    def add(self, std_json):
        if isinstance(std_json, Std_Json):
            self.std_data.extend(std_json.std_data)
        else:
            new_std_json = Std_Json(std_json)
            self.std_data.extend(new_std_json.std_data)

    def save(self, std_json_file):
        with open(std_json_file, "w", encoding="utf-8") as f:
            json.dump(self.std_data, f, ensure_ascii=False, indent=4)

    def sort_by_key(self, key=None, reverse=False):
        try:
            # self.std_data.sort(key=lambda x: get_timestamp_lable(x[key_word])[0], reverse=reverse)
            self.std_data.sort(key=key, reverse=reverse)
        except TypeError:
            raise ValueError("Key must be a function")

    def remove(self, item):
        """移除元素，既可以基于索引，也可以基于内容移除"""
        if isinstance(item, int):
            try:
                del self.std_data[item]
            except IndexError:
                raise ValueError(f"Index {item} is out of bounds")
        else:
            self.std_data = [x for x in self.std_data if x != item]

    def copy(self):
        return Std_Json(self)

    def sample(self, n, seedNum=None, return_remaining=False):
        """
        返回随机n/比例个样本，并可选择返回剩余数据
        """
        if n <= 0:
            raise ValueError("Sample size must be greater than 0")
        if 0 < n < 1:
            n = int(len(self.std_data) * n)
        if n > len(self.std_data):
            raise ValueError(
                "Sample size cannot be greater than the number of elements."
            )
        if seedNum:
            random.seed(seedNum)
        sampled_data = random.sample(self.std_data, n)
        if return_remaining:
            remaining_data = [
                item for item in deepcopy(self.std_data) if item not in sampled_data
            ]
            return Std_Json(sampled_data), Std_Json(remaining_data)
        return Std_Json(sampled_data)

    def set(self, sort_key=False, ori=False):
        res_set = set()
        for item in self.std_data:
            res_set.add(json.dumps(item, ensure_ascii=False, sort_keys=sort_key))
        new_std_data = [json.loads(item) for item in res_set]
        if ori:
            self.std_data = deepcopy(new_std_data)
        return Std_Json(new_std_data)

    def __add__(self, other: "Std_Json"):
        if not isinstance(other, Std_Json):
            raise TypeError("Operand must be a Std_Json object")
        sum_std_json = self.copy()
        sum_std_json.std_data.extend(deepcopy(other.std_data))
        return sum_std_json

    def __sub__(self, other: "Std_Json"):
        if not isinstance(other, Std_Json):
            raise TypeError("Operand must be a Std_Json object")
        sub_std_data = [
            item for item in deepcopy(self.std_data) if item not in other.std_data
        ]
        return Std_Json(sub_std_data)

    def __and__(self, other: "Std_Json"):
        print("and")
        if not isinstance(other, Std_Json):
            raise TypeError("Operand must be a Std_Json object")
        temp_std_json = self.set()
        common_data = [item for item in temp_std_json if item in other.std_data]
        return Std_Json(common_data)

    def __or__(self, other: "Std_Json"):
        print("or")
        if not isinstance(other, Std_Json):
            raise TypeError("Operand must be a Std_Json object")
        combined_json = self.set()
        for item in deepcopy(other.std_data):
            if item not in combined_json.std_data:
                combined_json.std_data.append(item)
        return combined_json

    def __len__(self):
        return len(self.std_data)

    def __getitem__(self, index):
        try:
            return self.std_data[index]
        except IndexError:
            raise IndexError(f"Index {index} is out of bounds")

    def __repr__(self):
        return json.dumps(self.std_data, ensure_ascii=False, indent=4)

    def __iter__(self):
        return iter(self.std_data)


if __name__ == "__main__":
    std=Std_Json([{"a":1,"b":2},{"a":1,"b":2},{"a":1,"b":2}])
    print(std)