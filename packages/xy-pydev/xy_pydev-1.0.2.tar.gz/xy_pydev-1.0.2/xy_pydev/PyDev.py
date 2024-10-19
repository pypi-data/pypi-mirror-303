# -*- coding: UTF-8 -*-
__author__ = 'helios'
__doc__ = 'PyDev'
'''
  * @File    :   PyDev.py
  * @Time    :   2023/06/03 10:29:52
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
'''
from argparse import ArgumentParser
from xy_console.utils import inputt, printt, print_s, print_e, print_r
from xy_string.utils import is_empty_string, contains_zh
from .ModuleData import ModuleData
from .Resource import Resource


class PyDev:
    _module_data = ModuleData()
    _resource = Resource()

    parser = ArgumentParser(
        prog="xy_pydev",
        description="xy_pydev python模块开发工具",
    )

    def add_arguments(self):
        self.parser.add_argument(
            "-w",
            "--work",
            type=str,
            help="""
                工作方式
            """,
            required=False,
            nargs="?",
            default="create",
        )
        self.parser.add_argument(
            "-n",
            "--name",
            type=str,
            help="""
                Python模块名称 不能包含中文
            """,
            required=False,
            nargs="?",
            default="",
        )
        self.parser.add_argument(
            "-m",
            "--module_class_name",
            type=str,
            help="""
                模块入口类名称 不能包含中文
            """,
            required=False,
            nargs="?",
            default="",
        )
        self.parser.add_argument(
            "-s",
            "--scripts",
            type=bool,
            help="""
                是否开启全局命令
            """,
            required=False,
            nargs="?",
            default="",
        )

    def work(self):
        try:
            args, _ = self.parser.parse_known_args()
            return args.work
        except Exception:
            return None

    def module_class_name(self):
        try:
            args, _ = self.parser.parse_known_args()
            return args.module_class_name
        except Exception:
            return None

    def scripts(self):
        try:
            args, _ = self.parser.parse_known_args()
            return args.scripts
        except Exception:
            return None

    def module_name(self):
        try:
            args, _ = self.parser.parse_known_args()
            return args.name
        except Exception:
            return None

    def input_module_class_name(self, default: str) -> str | None:
        validate = inputt(
            f"是否需要修改模块入口类名称?\n当前为: {default}\n不能包含中文\nY=>代表[需要];\n其他=>代表[不需要]\n请输入[ Y/n ]\n",
        )
        if validate == "Y":
            module_class_name = inputt(
                f"请输入新的模块入口类名称\n当前为: {default}\n不能包含中文\n",
            )
            if is_empty_string(module_class_name) or contains_zh(module_class_name):
                return self.input_module_class_name(default)
            else:
                return module_class_name
        return default

    def run(self, module_name: str | None):
        printt(f"新模块名称为: {module_name}")
        module_class_name = self.module_class_name()
        if not is_empty_string(module_name) and is_empty_string(module_class_name):
            module_class_name = self.input_module_class_name("Runner")
        scripts = self.scripts()
        if scripts is False:
            scripts_input = inputt(
                f"是否需要添加全局命令?\nY=>代表[添加];\n其他=>代表[不添加]\n请输入[ Y/n ]\n",
            )
            if scripts_input == "Y":
                scripts = True
            else:
                scripts = False
        self._module_data.make_dirs(
            module_name=module_name,
        )
        self._resource.write(
            module_name=str(module_name),
            module_class_name=str(module_class_name),
            scripts=scripts if scripts else False,
        )
        print_s(
            f"新模块[{module_name}]创建完成!!!",
        )

    def input_module_name(self) -> str | None:
        module_name = inputt(
            f"请输入新模块名称, 不能包含中文\n",
        )
        if is_empty_string(module_name) or contains_zh(module_name):
            return self.input_module_name()

        return module_name

    def create(self):
        module_name = self.module_name()
        if is_empty_string(module_name):
            module_name = self.input_module_name()
            if is_empty_string(module_name):
                print_e(f"请输入新模块名称，不能包含中文")
            else:
                if contains_zh(module_name):
                    printt(f"新模块名称[{module_name}]不能包含中文")
                else:
                    self.run(module_name)
        else:
            if contains_zh(module_name):
                printt(f"新模块名称[{module_name}]不能包含中文")
            else:
                self.run(module_name=str(module_name))

    def main(self):
        self.add_arguments()
        work = self.work()
        if work == "clean":
            print_r(
                f"开始清理模块缓存...",
            )
            self._resource.clean()
        else:
            self.create()
