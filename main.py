from slack import RTMClient
from chatgpt import ChatGPT

bot_token = "봇 OAuth Token을 입력"


@RTMClient.run_on(event="message")
def chatgptbot(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", "")
    subtype = data.get("subtype", "")
    origin_text = data.get("text", "")

    tag_code = origin_text.split(" ")[0]
    # print(payload)
    print(data)
    # If a message is not send by the bot
    if bot_id == "" and subtype == "" and ">" in tag_code:
        channel_id = data["channel"]
        # Extracting message send by the user on the slack
        text = data.get("text", "")
        text = text.split(">")[-1].strip()
        # 해당 메세지ts 파싱
        message_ts = data["ts"]

        response = ChatGPT(text)
        # Sending message back to slack
        web_client.chat_postMessage(channel=channel_id, text=response, thread_ts=message_ts)


if __name__ == "__main__":
    try:
        rtm_client = RTMClient(token=bot_token)
        print("Starter Bot connected and running!")
        rtm_client.start()
    except Exception as err:
        print(err)
