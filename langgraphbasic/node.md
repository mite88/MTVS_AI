```python
from langgraph.graph import StateGraph
from typing import TypedDict, List

# State 정의
class Statement(TypedDict):
    messages : List[str]

# Graph 초기화
builder = StateGraph(Statement)
```


```python
# Node 함수 정의
def say_hello_node(state :Statement):
    print('say_hello_node called!')
    return {'messages': ["hello, "] }

def say_world(state :Statement):
    print('say_world_node called!')
    return {'messages': ["_world, "] }
```


```python
# 노드 추가 (함수 이름만 전달하며, 괄호()를 붙이지 않음)
builder.add_node('hello_node', say_hello_node)
builder.add_node('world_node', say_world)
```




    <langgraph.graph.state.StateGraph at 0x153ccc7ad50>



## Edge


```python
from langgraph.graph import START,END

# 엣지 추가 (길 연결)
builder.add_edge(START, 'hello_node')
builder.add_edge('hello_node', 'world_node')
builder.add_edge('world_node', END)

```




    <langgraph.graph.state.StateGraph at 0x153ccc7ad50>




```python
# 컴파일
agent = builder.compile()
```


```python
result = agent.invoke({
    'messages':[]
})

print(result)
```

    say_hello_node called!
    say_world_node called!
    {'messages': ['_world, ']}
    
