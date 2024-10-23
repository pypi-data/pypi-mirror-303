from abc import ABC, abstractmethod
import os,re
from jpype import JClass,JString
action_keys = [
    "-DES",
    "-CODE",
    "-MOD",
    "-DOC",
    "-QA",
    "-UNT",
    "-RUN"
]

class Source(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)
        self.short_file_name = os.path.splitext(self.file_name)[0]
        self.body = []
        self.changed = False
        self.build()

    @abstractmethod
    def build(self):
        pass
    @abstractmethod
    def unparse(self):
        pass
    @abstractmethod
    def get_extra_def(self):
        pass
    

class Decla(ABC):
    def __init__(self, decla, source,class_obj=None):
        self.class_obj = class_obj
        if class_obj:
            class_obj.body.append(self)
        self.decla = decla
        self.source = source
        self.body = []
        self.build()
        source.body.append(self)

    @abstractmethod    
    def build_code(self):
        pass
    @abstractmethod
    def build_name(self):
        pass
    @abstractmethod
    def build_def_string(self):
        pass
    @abstractmethod
    def build_signature(self):
        pass
    @abstractmethod
    def build_design_doc_string():
        pass
    def build(self):
        self.build_code()
        self.build_name()
        self.build_signature()
        self.build_design_doc_string()
        self.build_def_string()
        pass


class ImportDef(Decla):
    def build_design_doc_string(self):
        self.design_doc_string = ''
        self.design_doc_obj = None
        pass
    pass
class ClassDef(Decla): 
    pass
class MethodDef(Decla):
    def build(self):
        super().build()
        self.build_action()
    def build_action(self):
        dd = self.design_doc_string
        self.action = None
        for ak in action_keys:
            if dd.startswith(ak):
                self.action = ak 
                self.design_doc = self.design_doc_string[len(ak):].strip()
class AssignDef(Decla):
    pass 


def remove_c_style_comments(comment_str):
    comment_str = re.sub('/\\*+', '', comment_str)
    comment_str = re.sub('\\*+/', '', comment_str)
    comment_str = re.sub('^\\s*\\*\\s?', '', comment_str, flags=re.MULTILINE)
    comment_str = re.sub('\\n\\s*\\n', '\n', comment_str)
    return comment_str.strip()


def startswith_action_key(str_doc):
    for ak in action_keys:
        if str_doc.startswith(ak):
            return True 
    return False


