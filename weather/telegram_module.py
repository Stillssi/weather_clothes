import telegram
import time
def load_telegram():
    telegram_config = {}
    with open('C:/Users/gdevw/바탕 화면/Stillssi_package/weather/telegram_config','r') as f:
        configs=f.readlines()
        for config in configs:
            key,value = config.rstrip().split('=')
            telegram_config[key]=value
    token=telegram_config["token"]
    chat_id = telegram_config["chatid"]
    bot = telegram.Bot(token)
    return bot, chat_id


def alarm_weather(bot, chat_id, weather,tem, umbre, weather1, tem1, umbre1,result):
    updates = bot.get_updates()
    last_id = updates[-1].update_id
    while True:
        try:
            # 신규 메시지가 없을 경우 에러가 발생 
            # list index out of range
            # 따라서, try - except 문으로 묶어줌
            print(last_id)
            new_message = bot.get_updates(offset=last_id)[-1]
            print(new_message.message.text)
            # 만약 신규 메시지가 오늘날씨면,
            if new_message.message.text == '날씨':
                # 관련 메시지 발송
                bot.send_message(chat_id,
                 '출근하실 때 날씨는 {} {} 오늘의 평균기온은{}도 입니다.{}퇴근하실 때 날씨는 {} {} 퇴근하실 때 기온은 {}도 입니다.'.format(weather, umbre,tem,'\n',weather1, umbre1,tem1))
                
            # 만약 신규 메시지가 내일날씨면,
            # offset 값 최신화 (update_id) + 1 해줘서 그 다음부터 메시지부터 확인하도록
            elif new_message.message.text == '옷':
                bot.send_message(chat_id, '오늘의 옷 추천: {}'.format(result))
            last_id = new_message.update_id + 1
            print(last_id)
        except:
            pass

        # 텔레그램 서버 부하 줄이기 위해 3초마다 확인
        time.sleep(3)

