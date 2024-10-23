import os
from collar.core.ast.Source import Source, Decla, ClassDef, MethodDef, ImportDef, AssignDef,action_keys
import ast
from collar import utils
import re

class PSource(Source):

    def unparse(self):
        str_content = ast.unparse(self.tree)
        return str_content

    def build(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        self.tree = ast.parse(file_content)
        self.src_root_path,self.module_path = find_src_path(self.file_path)
        self.module_name = self.short_file_name
        self.full_module_name = self.module_path + '.' + self.module_name
        self.model_doc = ast.get_docstring(self.tree)
        body_list = ast.walk(self.tree)
        self.body = []
        self.import_list = []
        for node in body_list:
            if type(node) == ast.Import or type(node) == ast.ImportFrom:
                self.import_list.append(PImportDef(node, self))
            elif type(node) == ast.ClassDef:
                PClassDef(node, self)
        body_list = ast.walk(self.tree)
        for node in body_list:
            if type(node) == ast.FunctionDef:
                if not self.is_in_class(node):
                    PMethodDef(node,self)
    
    def is_in_class(self, node):
        for pdecla in self.body:
            if isinstance(pdecla, PClassDef):
                for x_node in pdecla.body:
                    if x_node.decla == node:
                        return True
        return False
    
    def read_def_from_module(self):
        """DF
    根据传入的文件名，用AST解析这个文件，读取变量，方法的定义，拼接成一个字符串返回。
    字符串的第一句话是这个model的全名，doc， 然后跟上变量的定义和doc，然后是方法的签名。"""
        full_path = self.file_path
        if not os.path.exists(full_path) or not os.path.isfile(full_path):
            raise FileNotFoundError(f'File not found: {full_path}')
        with open(full_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            # 将源代码解析成AST
        tree = ast.parse(file_content)
        # 使用NodeTransformer去掉方法体，保留docstring
        transformer = RemoveFunctionBodies()
        new_tree = transformer.visit(tree)
        # 将新的AST转换回源代码
        return ast.unparse(new_tree)
    
    def get_module_def_from_imports(self):
        local_imports = set()
        for imp_obj in self.import_list:
            imp = imp_obj.decla
            if isinstance(imp, ast.Import):
                for alias in imp.names:
                    file_name = is_local_import(alias.name, self.src_root_path)
                    if file_name:
                        local_imports.add(file_name)
            elif isinstance(imp, ast.ImportFrom):
                file_name = is_local_import(imp.module,self.src_root_path)
                if not file_name:
                    for n in imp.names:
                        file_name = is_local_import(f"{imp.module}.{n.name}",self.src_root_path)
                        if file_name:
                            local_imports.add(file_name)
                else:
                    local_imports.add(file_name)
        context = ''
        for file_name in local_imports:
            if os.path.getsize(file_name) > 10000:
                source = PSource(file_name)
                context += source.read_def_from_module()
            else:
                context += utils.read_file_content(file_name)
        return context
    def get_extra_def(self):
        return ""
    
    def replace_method_code(self, method, new_function_def):
        decla = method.decla
        decla.body = [decla.body[0]]
        start_from = 0
        if type(new_function_def.body[0]) == ast.Expr:
            start_from = 1
        for body_item in new_function_def.body[start_from:]:
            decla.body.append(body_item)
        method.remove_action_key_in_design_doc()
        self.changed = True
        return 
    def replace_design_doc(self, method, new_doc):
        self.replace_doc(method, new_doc)
    def replace_doc(self, method, new_doc):
        decla = method.decla
        for ak in action_keys:
            new_doc = new_doc.replace(ak + '\n', '', 1)
            new_doc = new_doc.replace(ak, '', 1)
        indentation = " "*4
        if method.class_obj != None:
            indentation = " "*8
        new_doc = format_doc(new_doc,indentation)
        docstring_node = ast.get_docstring(decla)
        if docstring_node:
            decla.body[0].value.value = new_doc
        else:
            docstring_node = ast.Expr(value=ast.Str(s=new_doc))
            decla.body.insert(0, docstring_node)
        self.changed = True
        return

    def replace_model_code(self, new_code):
        new_tree = ast.parse(new_code)
        for node in new_tree.body:
            self.tree.body.append(node)
        self.changed=True
        return self.tree

    def replace_code(self, method, new_code):
        new_bodys = ast.parse(new_code).body
        for b in new_bodys:
            if type(b) == ast.Import or type(b) == ast.ImportFrom:
                self.insert_import( b)
            elif type(b) == ast.FunctionDef:
                self.replace_method_code( method, b)
    def insert_import(self, import_def):
        tree = self.tree
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == import_def.names[0].name:
                        return
            elif isinstance(node, ast.ImportFrom):
                if type(import_def) == ast.ImportFrom:
                    if node.module == import_def.module and node.names[0].name == import_def.names[0].name:
                        return
        tree.body.insert(0, import_def)

def find_src_path(file_path):
    """-DONE
传入的文件名是一个python源文件，
请利用__init__.py来查找这个python文件所在项目的根目录，
请注意， 包含__init__.py的目录，并不一定是根目录，
最后一个包含__init__.py的目录，才是根目录"""
    current_dir = os.path.dirname(file_path)
    model_path = ""
    last_init_dir = None
    while current_dir:
        init_file = os.path.join(current_dir, '__init__.py')
        if os.path.exists(init_file):
            last_init_dir = current_dir
            if model_path == "":
                model_path = os.path.basename(current_dir)
            else:
                model_path = os.path.basename(current_dir) + "." + model_path
        else:
            break
        current_dir = os.path.dirname(current_dir)
    return last_init_dir,model_path

class PDecla(Decla):

    def build_code(self):
        self.str_code = ast.unparse(self.decla)
    def build_name(self):
        if hasattr(self.decla, "name"):
            self.name =  self.decla.name
        elif hasattr(self.decla,"names"):
            self.name = f"{self.decla.names}"
        else:
            self.name = ""
    def build_def_string(self):
         self.def_string = f"{ast.unparse(self.decla)}"
    def build_signature(self):
        self.signature = f"{ast.unparse(self.decla)}"

    def build_design_doc_string(self):
        if isinstance(self.decla, (ast.AsyncFunctionDef, ast.FunctionDef, ast.ClassDef, ast.Module)):
            self.design_doc_string = ast.get_docstring(self.decla)
            if self.design_doc_string == None:
                self.design_doc_string = ""
        else:
            self.design_doc_string = ""
        return self.design_doc_string


class PClassDef(ClassDef, PDecla):
    def build(self):
        super().build()
        body_list = self.decla.body
        for node in body_list:
            if type(node) == ast.Import or type(node) == ast.ImportFrom:
                self.import_list.append(PImportDef(node, self.source,class_obj=self))
            elif type(node) == ast.Assign:
                PAssignDef(node,self.source,class_obj=self)
            elif type(node) == ast.ClassDef:
                PClassDef(node, self.source,class_obj=self)
            elif type(node) == ast.FunctionDef:
                PMethodDef(node, self.source,class_obj=self) 

    pass

class PImportDef(ImportDef, PDecla):
    pass

class PMethodDef(MethodDef, PDecla):

    def build_def_string(self):
        self.def_string = f"{self.build_signature()} \n {self.build_design_doc_string()}"
    def build_signature(self):
        """
        从ast.FunctionDef对象中获取方法的签名（定义部分）。
        
        :param node: ast.FunctionDef 对象
        :return: 方法签名的字符串
        """
        node = self.decla
        if not isinstance(node, ast.FunctionDef):
            raise ValueError('输入节点必须是ast.FunctionDef类型')
        method_name = node.name
        args = node.args
        arg_names = [arg.arg for arg in args.args]
        if args.vararg:
            arg_names.append(f'*{args.vararg.arg}')
        if args.kwarg:
            arg_names.append(f'**{args.kwarg.arg}')
        arg_str = ', '.join(arg_names)
        method_signature = f'def {method_name}({arg_str}):'
        self.signature = method_signature
        return method_signature
    
    def remove_action_key_in_design_doc(self):
        dcs = self.design_doc_string
        for ak in action_keys:
            dcs = dcs.replace(ak + '\n', '', 1)
            dcs = dcs.replace(ak, '', 1)
        method = self.decla
        docstring_node = ast.get_docstring(method)
        if docstring_node:
            method.body[0].value.value = dcs
        else:
            docstring_node = ast.Expr(value=ast.Str(s=dcs))
            method.body.insert(0, docstring_node)
class PAssignDef(AssignDef, PDecla):
    pass

def is_local_import(pkgs,src_dir):
    """
    参数pkgs是一个import的声明，比如utils.time.create_new_time
    PROJECT_DIR是全局变量，指示了某一个项目的跟目录。
    请用pkgs这个字符串，分解后的每个目录，来匹配项目目录下的文件夹和python文件，
    直到找到了这个pkgs对应的python文件，则返回文件名。
    如果没有能够匹配上，则返回None
    """
    parts = pkgs.split('.')
    current_path = src_dir
    for part in parts:
        current_path = os.path.join(current_path, part)
        if os.path.exists(current_path):
            if os.path.isdir(current_path):
                continue
            else:
                current_path += '.py'
                if not os.path.exists(current_path):
                    return None
                if os.path.isfile(current_path):
                    return current_path
        else:
            current_path += '.py'
            if not os.path.exists(current_path):
                return None
            if os.path.isfile(current_path):
                return current_path
            return None
    return None

def get_full_path(path):
    """
    获取完整路径，如果路径是相对路径，则使用当前执行命令的路径+相对路径
    :param path: 路径
    :return: 完整路径
    """
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    return os.path.abspath(path)

def get_method_definition_and_doc(node):
    """
    获取一个AST方法对象的定义和文档字符串，并组合成一个字符串返回。
    
    :param node: ast.FunctionDef 对象
    :return: 包含方法定义和文档字符串的字符串
    """
    if not isinstance(node, ast.FunctionDef):
        raise ValueError('输入节点必须是ast.FunctionDef类型')
    method_def = get_method_signature(node)
    docstring = ast.get_docstring(node, clean=True)
    if not docstring:
        docstring = ''
    pattern = re.compile('^D[A-Z]\\n')
    matches = pattern.findall(docstring)
    if len(matches) > 0:
        docstring = docstring[3:]
    result = f"\n{method_def}\n{(docstring if docstring else '')}"
    return result

def get_method_signature(node):
    """
    从ast.FunctionDef对象中获取方法的签名（定义部分）。
    
    :param node: ast.FunctionDef 对象
    :return: 方法签名的字符串
    """
    if not isinstance(node, ast.FunctionDef):
        raise ValueError('输入节点必须是ast.FunctionDef类型')
    method_name = node.name
    args = node.args
    arg_names = [arg.arg for arg in args.args]
    if args.vararg:
        arg_names.append(f'*{args.vararg.arg}')
    if args.kwarg:
        arg_names.append(f'**{args.kwarg.arg}')
    arg_str = ', '.join(arg_names)
    method_signature = f'def {method_name}({arg_str}):'
    return method_signature

def format_doc(doc,indentation=""):
    if not doc.startswith('\n'):
        doc = '\n' + doc
    doc = doc.replace("\n\n","\n")
    lines = doc.split('\n')
    formatted_lines = [line.lstrip() for line in lines]
    formatted_doc = '\n'.join(formatted_lines)
    formatted_doc = formatted_doc.replace("\n","\n"+indentation)
    return formatted_doc

class RemoveFunctionBodies(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        # 获取方法的docstring，如果存在则保留它
        docstring = ast.get_docstring(node)
        
        # 如果有docstring，将docstring作为函数的唯一body保留
        if docstring:
            # 将docstring转换为表达式节点，放入body中
            new_body = [ast.Expr(value=ast.Constant(value=docstring))]
        else:
            # 如果没有docstring，直接设置为空body
            new_body = []
        
        # 替换函数体
        node.body = new_body
        
        # 继续遍历函数内部的节点（如果有嵌套函数等）
        return node