from cloth_recomm import recommend_cloth
from weather_crowling import cal_weather
import telegram_module

#cal_weather 객체인 one생성
one = cal_weather([1162069500,1156060500])
#one의 load_var함수를 통해 크롤링 해서 계산한 값들을 받아옴
weather,tem, umbre, weather1, tem1, umbre1 = one.load_var()
print(one.crowling_weather())
#recommend_cloth의 객체인 ha 객체 생성 , 파일과 딕셔너리를 넣어줌
ha=recommend_cloth('./cloth.pkl',
{
    'top': [
        ['줄무늬 민소매', '빨간 민소매', '하늘색 민소매'], 
        ['단가라티', '고양이반팔티', '마하그리드 반팔티'], 
        ['하늘색 셔츠', '흰색셔츠', '베이지 셔츠'], 
        ['흰색 긴팔', '녹색 긴팔', '폴로 긴팔'], 
        ['GAP 맨투맨', '칼하트 맨투맨', 'GCP 맨투맨']], 
    'bottom': [
        ['검정 반바지', '네이비 반바지', '아이보리 반바지'], 
        ['베이지 면바지', '카키 면바지', '검정 슬랙스'], 
        ['연청바지', '진청바지', '회색 긴바지']], 
    'dress': ['검정 원피스', '아이보리 원피스', '꽃무늬 원피스'], 
    'outer': [
        ['베이지 가디건', '줄무늬 가디건', '후리스'],
        ['베이지 자켓', '검정 자켓', '크림 자켓'],
         ['갈색 코트', '회색 코트'], ['롱패딩', '숏패딩']]
})

#옷 추천 결과를 받아옴
result = ha.select_cloth(tem)

#텔레그램 모듈에서 load_telegram()함수를 통해 bot과 chat_id를 받아옴
bot, chat_id = telegram_module.load_telegram()
#텔레그램 메시지 보내는 함수에 모든 결과를 넣어줌
telegram_module.alarm_weather(bot, chat_id, weather,tem, umbre, weather1, tem1, umbre1,result)