import os, platform, sys
def get_hostname():
    """
    Brief Introduuction

    Returns:
        None -->System host name
        成功 -->Host name
        失败 -->""
    """
    try:
        import socket
    except ImportError:
        return ""
    try:
        return socket.gethostname()
    except OSError:
        return ""
def get_system_info():
    """
    Brief Introduce:

    Returns:
        system: 系统名称
        node: 主机名
        release: 系统版本
        version: 内核版本
        machine: 机器类型
    """
    try:
        system,node,release,version,machine=os.uname()
    except:
        try:
            system=platform.system()
            node=platform.node()
            release=platform.release()
            version=platform.version()
            machine=platform.machine()
        except:
            try:
                system=sys.platform
                node=get_hostname()
                release=''
                version=''
                machine=''
            except:
                raise Exception("can't get system info")
    return system, node, release, version, machine