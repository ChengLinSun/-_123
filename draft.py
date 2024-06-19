import streamlit as st
from zhipuai import ZhipuAI


st.set_page_config(page_title='代码检查器', layout='wide')
st.title("代码检查器")
api_key=st.text_input("请输入密钥")
client = ZhipuAI(api_key=api_key)
code_area = st.text_area("请输入代码", height=300)
if st.button("AI检查代码"):
    if code_area.strip() == '':
        st.warning("请输入代码后再点击检查代码。")
    else:
        response = client.chat.completions.create(
            model="glm-4",  # 选择适合的模型
            messages=[
                {"role": "user",
                 "content": f"你是一个编程专家，请检查以下代码，如果有问题，你就告诉我哪里出了问题，并且提出修改建议，如果没问题，你就夸夸我，用中文回答。代码如下：\n\n{code_area}"},
            ],
            stream=True,
        )

        st.subheader("对话结果")
        output = ""
        for chunk in response:
            delta_content = chunk.choices[0].delta.content
            output += delta_content
        st.text(output)
