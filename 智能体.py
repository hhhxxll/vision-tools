import gradio as gr
from cozepy import Coze, TokenAuth, COZE_CN_BASE_URL, Message, ChatEventType

# ---------------------- 1. 配置Coze认证信息 ----------------------
# 替换为你在Coze平台的「个人访问令牌」（从“授权”页面生成）
coze_api_token = "cztei_hFLUEww72wYMvAza4AWHuXnw6wI0wWWmndgKV7fg2hW5F91uAwZ3LCQO03ttnXIC7"
# 替换为你在Coze平台创建的「智能体ID」（从智能体详情页URL中获取，如 bot-xxxxxx）
bot_id = "7573584082320621587"
# 用户ID（自定义，用于区分不同用户，可填任意字符串）
user_id = "123456789"
# 初始化Coze客户端
coze = Coze(
    auth=TokenAuth(token=coze_api_token),
    base_url=COZE_CN_BASE_URL  # 国内环境使用该地址，海外环境可省略
)
# ---------------------- 2. 定义问答函数（流式输出） ----------------------
def ask_coze(question):
    if not question:
        return "请输入问题后再尝试~"

    try:
        # 调用Coze API发起流式对话
        chat_iterator = coze.chat.stream(
            bot_id=bot_id,
            user_id=user_id,
            additional_messages=[
                Message.build_user_question_text(question)
            ]
        )
        # 逐段获取并拼接回答
        full_answer = ""
        for event in chat_iterator:
            if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
                full_answer += event.message.content
        return full_answer
    except Exception as e:
        return f"调用失败：{str(e)}"
# ---------------------- 3. Gradio网页界面 ----------------------
with gr.Blocks(title="Coze问答助手") as demo:
    gr.Markdown("# 通用问答助手")
    question = gr.Textbox(label="输入问题", placeholder="例如：什么是人工智能？")
    answer = gr.Textbox(label="AI回答", lines=5)
    submit_btn = gr.Button("获取回答")

    # 绑定函数与界面组件
    submit_btn.click(
        fn=ask_coze,
        inputs=question,
        outputs=answer
    )
# 启动服务
demo.launch()