from bs4 import BeautifulSoup
import requests



class cal_weather:

    def __init__(self, loc_code):
        self.loc_code = loc_code
    # 오늘의 날씨는 ~
    # 강수량 if 비 소식이 있으면 
    # 오늘의 기온 앞으로 몇시간의 기온의 평균이 
    # 28도 이상 = 민소매, 반팔, 반바지, 원피스
    # 23~27도 =  반팔, 얇은 셔츠, 반바지, 면바지
    # 20~22도 = 얇은 가디건, 긴팔, 면바지, 청바지
    # 17~19도 = 얇은 니트, 맨투맨, 가디건, 청바지
    # 12~16도 = 자켓, 가디건, 면바지, 청바지
    # 9~11도 = 자켓, 트렌치코트, 니트, 청바지
    # 5도~8도 = 코트,니트
    # ~4도 = 패디, 두꺼운 코드, 기모 
    # 옷장에 있는 옷 추천
    #시각, 날씨, 기온, 체감온도, 강수량, 강수확률, 바람
        
    def crowling_weather(self):
        '''
        기상청 날씨(집 위치-출근시간, 직장위치-퇴근시간) 크롤링 함수
        '''
        #1162069500 은천동
        #1156060500 문래동
        loc_code = self.loc_code
        temperature1 ,nalssi1 ,rain1 = [],[],[]
        temperature2 ,nalssi2 ,rain2 = [],[],[]
        
        for l in range(len(loc_code)):
            
            URL = f'https://www.weather.go.kr/w/wnuri-fct2021/main/digital-forecast.do?code={loc_code[l]}&unit=m%2Fs&hr1=Y'
            res = requests.get(URL)
            

            weather_item = []
            soup = BeautifulSoup(res.text, 'html.parser')
            weather_list = soup.select('.item-wrap ul')
            #print(weather_list)
            
            if l == 0: 
                for j in range(0,6):
                    result= weather_list[j].select('li')
                    #print(result[3].text.split()[1][:2],result[1].text.split()[1][:2],result[4].text.split()[1])
                    temperature1.append(result[3].text.split()[1][:2])
                    nalssi1.append(result[1].text.split()[1][:2])
                    rain1.append(result[4].text.split()[1])
                    
            else:
                for j in range(10,12):
                    result= weather_list[j].select('li')
                    temperature2.append(result[3].text.split()[1][:2])
                    nalssi2.append(result[1].text.split()[1][:2])
                    rain2.append(result[4].text.split()[1])

        return temperature1, nalssi1,rain1, temperature2, nalssi2, rain2


    def cal_temperature(self, tem):
        '''
        평균 기온 계산 함수
        '''
        tem = list(map(int,tem))
        tem_avg =sum(tem)//len(tem)

        return tem_avg

    def cal_rain(self,rain):
        for r in rain:
            if r == '-':
                pass
            else:
                return '우산을 챙기세요.'
        return '우산 필요 없습니다.'
            

    def cal_nalssi(self,nalssi):
        '''
        대체적인 날씨 계산 함수
        '''
        sunny, cloud, grey , rainy= 0,0,0,0 #맑음, 구름, 흐림
        cnt = []
        #날씨에 어떤 게 제일 많은지 카운트
        for nal in nalssi:
            if nal =='맑음':
                sunny += 1
            elif nal == '구름':
                cloud += 1
            elif nal =='흐림':
                grey += 1
            else:
                rainy += 1

        #리스트에 append
        cnt.append(sunny)
        cnt.append(cloud)
        cnt.append(grey)
        cnt.append(rainy)
        
        #제일 큰 값 구하기
        tmp = max(cnt)
        
        #큰값 인덱스 구하기
        max_index = cnt.index(tmp)
        
        #return 값
        if max_index == 0:
            return '기분 좋은 맑은 날씨가 예상됩니다.'
        elif max_index == 1:
            return '구름이 많을 것으로 예상됩니다.'
        elif max_index == 2:
            return '흐린날씨가 예상됩니다.'
        else:
            return '비가 올 것으로 예상됩니다.'

#발표 방향성 =  주제, 라이브러리 구조 설명, 핵심 로직과 프로세스에 대한 설명, 시현


    
    def print_nalssi(self):
        temperature1, nalssi1,rain1,temperature2, nalssi2,rain2 = self.crowling_weather()
        #print(temperature, nalssi,rain)
        weather = self.cal_nalssi(nalssi1)
        tem = self.cal_temperature(temperature1)
        umbre = self.cal_rain(rain1)
        print('출근하실 때 날씨는',weather, umbre)
        print('오늘의 평균기온은',str(tem)+'도','입니다')
        

        weather1 = self.cal_nalssi(nalssi2)
        tem1 = self.cal_temperature(temperature2)
        umbre1 = self.cal_rain(rain2)
        print('퇴근하실 때 날씨는',weather1, umbre1)
        print('퇴근하실 때 기온은', str(tem1)+'도','입니다.')

    def load_var(self):
        temperature1, nalssi1,rain1,temperature2, nalssi2,rain2 = self.crowling_weather()
        #print(temperature, nalssi,rain)
        weather = self.cal_nalssi(nalssi1)
        tem = self.cal_temperature(temperature1)
        umbre = self.cal_rain(rain1)
        weather1 = self.cal_nalssi(nalssi2)
        tem1 = self.cal_temperature(temperature2)
        umbre1 = self.cal_rain(rain2)
        return weather,tem, umbre, weather1, tem1, umbre1
