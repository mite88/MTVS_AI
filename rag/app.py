from vectorstore import init_vectorstore, load_vector_from_local
from chains import build_rag_chain

# init_vectorstore()

vectorstore = load_vector_from_local()

chain = build_rag_chain(vectorstore)

question = "제가 제주도에 살고있는데요, 배송은 얼마나 걸리나요?"
result = chain.invoke(question)

print(result)

question = "물건이 마음에 안들어서 법적 조치를 하고자합니다. 방법이 뭔가요?"
result = chain.invoke(question)

print(result)
