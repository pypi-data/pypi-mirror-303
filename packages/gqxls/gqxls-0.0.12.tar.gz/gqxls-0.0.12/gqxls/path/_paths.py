import os
from typing import List, Union, Tuple


class paths:
    def get_document_names(self,path:str,endswith:str='',path_or_name:bool=True,get_folder:bool=False)->list:
        try:
            path = os.path.abspath(path)
            if not os.path.exists(path):
                raise FileNotFoundError(f"path:{path}不存在")
            else:
                path_names = os.listdir(path)
                if path_or_name==True:
                    for i in range(len(path_names)):
                        path_names[i] = os.path.join(path, path_names[i])
                new_path_names = list()
                dict=[".pdf",'.png','.jpg','.jpeg','.txt','.doc',
                      '.docx','.gif','.mp4','.mp3','.avi','.wav',
                      '.xls','.xlsx','.ppt','.pptx','.zip','.exe'
                      ,'.rar','.mov','.bak','.htm','.html']
                if get_folder== True and endswith=='':
                    new_path_names=path_names
                    return new_path_names
                elif get_folder==False and endswith!='' and endswith.lower() in dict:
                    for name in path_names:
                        if name.endswith(endswith):
                            new_path_names.append(name)
                    return new_path_names
                elif get_folder==False and endswith=='':
                    for name in path_names:
                        if not name.endswith(''):
                            new_path_names.append(name)
                    return new_path_names
                else:
                    raise ValueError(f"endwith:{endswith}和get_folder:{get_folder}参数错误")
        except:
            raise ValueError(f"path:{path}参数错误")

    def maker_path(self,path:str)->None:
        try:
            if not os.path.exists(path):
                os.mkdir(path)
        except:
            raise ValueError(f"path:{path}参数错误")


class FilePath:
    def __init__(self,get_folder:bool=False)->None:
        """
        Brief Introduction

        Args:
            get_folder:是否获取文件夹名称,True or False
        """
        self.get_folder=get_folder
    def get_document_names(self,path:Union[str,List[str]])->List[tuple]:
        """
        Brief Introduction

        Args:
            path:文件路径或集,str or List[str]

        Returns:
            List[tuple]:[(全名,标题,后缀)]
        """
        if path == '' or path == None or path == []:
            raise ValueError(f"path:{path}配置为空")
        else:
            if self.path_exist(path)==True:
                head,tail=os.path.splitext(os.path.abspath(path))
                if tail=='':
                    name=os.listdir(path)
                    new_name=list()
                    for i in name:
                        if self.get_folder==True:
                            name,ends=os.path.splitext(i)
                            new_name.append(tuple([i,name,ends]))
                        else:
                            if os.path.splitext(i)[1]!='':
                                name,ends=os.path.splitext(i)
                                new_name.append(tuple([i,name,ends]))
                    return new_name
                else:
                    name,ends=os.path.splitext(tail)
                    new_name=list()
                    new_name.append(tuple([path,name,ends]))
                    return new_name
            elif self.path_exist(path)==False:
                raise FileNotFoundError(f"path:{path}缺失")
    def path_exist(self,path:Union[str,List[str]])->bool:
        """
        Brief Introduction

        Args:
            path:文件路径或集,str or List[str]

        Returns:
            bool:存在->True 不存在->False
        """
        if path=='' or path==None or path==[]:
            raise ValueError(f"path:{path}配置为空")
        else:
            if isinstance(path,str) and os.path.exists(path):
                return True
            elif isinstance(path,list) and all(isinstance(i,str) for i in path) and all(os.path.exists(i) for i in path):
                return True
            else:
                return False
    def get_document_paths(self,path:Union[str,List[str]])->List[tuple]:
        """
        Brief Introduction

        Args:
            path:文件路径或集,str or List[str]

        Returns:
            List[tuple]:[(绝对路径,前置路径,标题,后缀)]
        """
        if path == '' or path == None or path == []:
            raise ValueError(f"path:{path}配置为空")
        else:
            if self.path_exist(path)==True:
                head,tail=os.path.splitext(os.path.abspath(path))
                if tail=='':
                    name=os.listdir(path)
                    new_name=list()
                    for i in name:
                        if self.get_folder==True:
                            title,ends=os.path.splitext(i)
                            new_name.append(tuple([os.path.join(head,i),head,title,ends]))
                        else:
                            if os.path.splitext(i)[1]!='':
                                title,ends=os.path.splitext(i)
                                new_name.append(tuple([os.path.join(head,i),head,title,ends]))
                    return new_name
                else:
                    title,ends=os.path.splitext(tail)
                    new_name=list()
                    new_name.append(tuple([path,head,title,ends]))
                    return new_name
            elif self.path_exist(path)==False:
                raise FileNotFoundError(f"path:{path}不存在")
    def path_no_exit(self,path:Union[str,List[str]])->list:
        """
        Brief Introduction

        Args:
            path:文件路径或集,str or List[str]

        Returns:
            list:[不存在路径]
        """
        if path == '' or path == None or path == []:
            raise ValueError(f"path:{path}配置为空")
        else:
            if self.path_exist(path)==True:
                return list()
            else:
                no_exit=list()
                if isinstance(path,str):
                    no_exit.append(os.path.abspath(path))
                else:
                    for i in path:
                        if isinstance(i,str)==True and self.path_exist(i)==False:
                            no_exit.append(os.path.abspath(i))
                        elif isinstance(i,str)==False:
                            raise TypeError(f"path:{i}类型错误")
                return no_exit
    def file_maker(self,path:Union[str,List[str]])->None:
        """
        Brief Introduction

        Args:
            path:文件路径或集,str or List[str]

        Returns:
            None:创建不存在路径
        """
        if path == '' or path == None or path == []:
            raise ValueError(f"path:{path}配置为空")
        else:
            if isinstance(path,str)==True and self.path_exist(path)==False:
                os.mkdir(path)
            elif isinstance(path,list)==True and self.path_exist(path)==False and self.path_no_exit(path)!=[]:
                for i in self.path_no_exit(path):
                    os.mkdir(i)

def is_empty(parameter: Union[str, list, tuple, dict, bool, int, float]) -> bool:
    """
    Brief introduction

    Args:
        parameter:输入参数,[str,list,tuple,dict,bool,int,float]

    Returns:
        []、{}、()、'' -->True
        int、float、other parameter no empty -->False
        True -->False
        False -->True
    """
    return False if type_same(parameter,(int,float)) else not bool(parameter)

def type_name(parameter: object) -> str:
    """
    Brief introduction

    Args:
        parameter:输入参数,object

    Returns:
        parameter -->类型名称
    """
    return type(parameter).__name__

def path_exists(path:Union[str, List[str]]) -> tuple:
    """
    Brief Introduction

    Args:
        path:路径，[str, List[str]]

    Returns:
        path -->tuple(是否全部存在，True or False|不存在路径，List)
    """
    if is_empty(path):
        raise NameError(f"name '{path}' is not defined")
    else:
        nonexistent_paths=list()
        if isinstance(path, str):
            path=[path]
        elif isinstance(path,list) and all(isinstance(i,str) for i in path):
            pass
        else:
            raise NameError(f"name '{path}' is not defined")
        for sigle_path in path:
            if os.path.exists(sigle_path ):
                pass
            else:
                nonexistent_paths.append(sigle_path )
        return tuple([True if len(nonexistent_paths)==0 else False, nonexistent_paths])

def type_same(parameter:object,parameter_type:Union[type,Tuple[type,...]]) -> bool:
    """
    Brief Introduction

    Args:
        parameter:输入参数,object
        parameter_type:输入类型,type,Tuple[type,...]

    Returns:
        parameter类型相同 -->True
        parameter类型不同 -->False
    """
    if isinstance(parameter_type,type):
        parameter_type=tuple([parameter_type])
    elif isinstance(parameter_type,tuple) and all(isinstance(i,type) for i in parameter_type)==True:
        pass
    else:
        raise NameError(f"name '{parameter_type}' is not defined")
    return True if type(parameter) in parameter_type else False
def file_maker(path:Union[str, List[str]]) -> None:
    """
    Brief Introduction

    Warning:
        不支持已存在文件创建 -->Raise

    Args:
        path:创建路径，[str, List[str]]

    Returns:
        None
    """
    if is_empty(path):
        raise NameError(f"name '{path}' is not defined")
    else:
        if type_same(path,str):
            new_path=[path]
        elif type_same(path,list) and all(type_same(i,str) for i in path):
            new_path=path
        else:
            raise NameError(f"name '{path}' is not defined")
        for sigle_path in new_path:
            os.makedirs(sigle_path)
def get_film(path:Union[str, List[str]]) -> tuple:
    """
    Brief Introduction

    Note:
        get_film效率低于detail_film

    Args:
        path:信息获取路径,[str, List[str]]

    Returns:
        path -->tuple([[(绝对路径，全名，名称，后缀),...],[(绝对路径，全名，名称，None),...]],...)
    """
    if is_empty(path):
        raise NameError(f"name '{path}' is not defined")
    else:
        if isinstance(path,str):
            new_path=[os.path.abspath(path)]
        elif isinstance(path,list) and all(isinstance(i,str) for i in path):
            new_path=[os.path.abspath(i) for i in path]
        else:
            raise NameError(f"name '{path}' is not defined")
        if path_exists(new_path):
            all_names=list()
            for single_path in new_path:
                head,tail=os.path.splitext(single_path)
                folder_name=list()
                document_name=list()
                if tail=='':
                    single_path_name=os.listdir(single_path)
                    for i in single_path_name:
                        name,ends=os.path.splitext(i)
                        if ends=='':
                            folder_name.append(tuple([os.path.join(single_path,i),i,name,None]))
                        else:
                            document_name.append(tuple([os.path.join(single_path,i),i,name,ends]))
                else:
                    i=single_path.split('\\')[-1]
                    name,ends=os.path.splitext(i)
                    document_name.append(tuple([single_path,i,name,ends]))
                all_names.append([document_name,folder_name])
            return tuple(names for names in all_names)
        else:
            raise FileNotFoundError(f"path '{new_path}' exist incompletely")

def get_detail_film(path:Union[str, List[str]]) -> tuple:
    """
    Brief Introduction

    Args:
        path:信息获取路径,[str, List[str]]

    Returns:
        path -->({绝对路径，全名，名称，后缀,...},{绝对路径，全名，名称，后缀,...},...)
    """
    if is_empty(path):
        raise NameError(f"name '{path}' is not defined")
    else:
        if type_same(path,str):
            new_path=[os.path.abspath(path)]
        elif type_same(path,list) and all(type_same(i,str) for i in path):
            new_path=[os.path.abspath(i) for i in path]
        else:
            raise NameError(f"name '{path}' is not defined")
        if path_exists(new_path):
            all_names=list()
            for single_path in new_path:
                head,tail=os.path.splitext(single_path)
                information=dict()
                all_abs_path=list()
                all_path=list()
                all_name=list()
                all_ends=list()
                folder_abs_path=list()
                folder_path=list()
                folder_name=list()
                document_abs_path=list()
                document_path=list()
                document_name=list()
                if tail=='':
                    single_path_name=os.listdir(single_path)
                    for i in single_path_name:
                        name,ends=os.path.splitext(i)
                        if ends=='':
                            all_abs_path.append(os.path.join(single_path,i))
                            all_path.append(i)
                            all_name.append(name)
                            folder_abs_path.append(os.path.join(single_path,i))
                            folder_path.append(i)
                            folder_name.append(name)
                        else:
                            all_abs_path.append(os.path.join(single_path, i))
                            all_path.append(i)
                            all_name.append(name)
                            all_ends.append(ends)
                            document_abs_path.append(os.path.join(single_path,i))
                            document_path.append(i)
                            document_name.append(name)
                else:
                    i=single_path.split('\\')[-1]
                    name,ends=os.path.splitext(i)
                    all_abs_path.append(single_path)
                    all_name.append(name)
                    all_path.append(i)
                    all_ends.append(ends)
                    document_abs_path.append(single_path)
                    document_path.append(i)
                    document_name.append(name)
                new_ends=list()
                for ends in all_ends:
                    if ends not in new_ends:
                        new_ends.append(ends)
                information['all_abs_path']=all_abs_path
                information['all_path']=all_path
                information['all_name']=all_name
                information['all_ends']=new_ends
                information['folder_abs_path']=folder_abs_path
                information['folder_path']=folder_path
                information['folder_name']=folder_name
                information['document_abs_path']=document_abs_path
                information['document_path']=document_path
                information['document_name']=document_name
                all_names.append(information)
            return tuple(all_names)
        else:
            raise FileNotFoundError(f"path '{new_path}' exist incompletely")