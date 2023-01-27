from slack import RTMClient
import chatgpt
import time
import re

RTM_READ_DELAY = 1  # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "ask"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

starterbot_id = None
token = "user-slack-token"

@RTMClient.run_on(event="message")
def chatgptbot(**payload):
    """
    This function triggers when someone sends
    a message on the slack
    """
    data = payload["data"]
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", "")
    subtype = data.get("subtype", "")
    origin_text = data.get("text","")

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

        response = chatgpt.main(text)
        # Sending message back to slack
        web_client.chat_postMessage(channel=channel_id, text=response, thread_ts=message_ts)


if __name__ == "__main__":
    try:
        rtm_client = RTMClient(token=token)
        print("Starter Bot connected and running!")
        rtm_client.start()
    except Exception as err:
        print(err)
