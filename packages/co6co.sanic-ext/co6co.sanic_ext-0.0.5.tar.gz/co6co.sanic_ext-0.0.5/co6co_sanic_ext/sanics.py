from sanic import Sanic,utils
from typing import Optional,Callable,Any
from pathlib import Path 
from co6co.utils import log,File

from sanic.worker.loader import AppLoader
from functools import partial

def _create_App(name:str="__mp_main__",config:str=None,apiMount: Optional[Callable[[Sanic,Any], None]] = None ):
    try:
        app = Sanic(name)  
        if config==None: raise PermissionError("config")
        if app.config!=None: 
            app.config.update({"web_setting":{ 'port':8084, 'host':'0.0.0.0', 'debug': False, 'access_log':True,  'dev':False   }}) 
            customConfig=None
            if '.json'  in config: customConfig= File.File.readJsonFile(config)
            else: customConfig=utils.load_module_from_file_location(Path(config) ).configs  
            if customConfig!=None:app.config.update(customConfig)
            #log.succ(f"app 配置信息：\n{app.config}")
            if apiMount!=None: apiMount(app,customConfig) 
        return app
    except Exception as e: 
        log.err(f"创建应用失败：\n{e}{ repr(e)}\n 配置信息：{app.config}")
        raise 

def startApp(configFile:str,apiInit:Optional[Callable[[Sanic,Any], None]] ): 
    loader = AppLoader(factory=partial(_create_App,config=configFile,apiMount=apiInit)) 
    app = loader.load() 
    if app!=None and app.config!=None: 
        setting=app.config.web_setting 
        backlog=1024
        if "backlog" in  setting:backlog=setting.get("backlog")
        app.prepare( host=setting.get("host"),backlog=backlog, port=setting.get("port"),debug=setting.get("debug"), access_log=setting.get("access_log") ,dev=setting.get("dev"))  
        Sanic.serve(primary=app, app_loader=loader)
        #app.run(host=setting.get("host"), port=setting.get("port"),debug=True, access_log=True) 
    return app
