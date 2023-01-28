from slack import RTMClient
from chatgpt import ChatGPT

# 발급받은 슬랙 bot user token 기입
bot_token = "<your-slack-bot-token>"

# 지속적으로 슬랙 메세지 트래킹
@RTMClient.run_on(event="message")
def chatgptbot(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", "")
    subtype = data.get("subtype", "")
    origin_text = data.get("text", "")
    tag_code = origin_text.split(" ")[0]

    # 메세지 정보 파악
    print(data)
    # Bot이 입력한 채팅이 아닐 경우 ChatGPT 동작
    if bot_id == "" and subtype == "" and ">" in tag_code:
        channel_id = data["channel"]
        # Extracting message send by the user on the slack
        text = data.get("text", "")
        text = text.split(">")[-1].strip()
        # 해당 메세지 입력 시간을 파악하여 답글을 달 수 있도록 지정
        message_ts = data["ts"]

        #받아온 텍스트를 ChatGPT에 전달하고 ChatGPT의 답변 저장
        response = ChatGPT(text)
        # 슬랙에 메세지 전달
        web_client.chat_postMessage(channel=channel_id, text=response, thread_ts=message_ts)


if __name__ == "__main__":
    try:
        rtm_client = RTMClient(token=bot_token)
        print("Starter Bot connected and running!")
        rtm_client.start()
    except Exception as err:
        print(err)
