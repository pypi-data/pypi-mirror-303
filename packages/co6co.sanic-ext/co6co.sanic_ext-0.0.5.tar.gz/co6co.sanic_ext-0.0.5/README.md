# 扩展 sanic

# (sanic Demo)[https://www.osgeo.cn/sanic/sanic/examples.html/]

(task)[https://python.hotexamples.com/zh/examples/sanic/Sanic/add_task/python-sanic-add_task-method-examples.html]

# 历史记录

```
0.0.1 初始版本
0.0.2.
0.0.3 优化 baseView 2024-07-26
0.0.4
    baseView: save_file
0.0.5
    result
```

webSocket 测试地址
http://www.blue-zero.com/WebSocket/
http://coolaf.com/tool/chattest

这两个遇到个问题，sanic 一执行 websocket 地址 python 就报异常框（需 c++调试）的框
后经过一个个模块删除后发现是：
在文件夹中有 multidict-6.0.2 模块，`pip list` 显示确是 6.0.4，直接移除 multidict 发现正常

# 类属性与对象属性

```
class A:
    def __init__(self) -> None:
       self.a="12"
       pass

class B(A):
    b:str="abc"
    @classmethod
    def geA(cls) -> str:
        print(cls.a)
        return cls.a

a=A()
print(a.a)

b=B()
b.a="456"
print(b.a,B.a,"b.geA:", b.geA(),"B.geA:",B.geA())

a=A()
print(a.a,A.a)
```
