from weather_crowling import cal_weather
import random
import pickle
import os

class recommend_cloth() :
    
    def __init__(self,filename, objs):
        with open(filename, 'wb') as f:
            for a in objs:
                pickle.dump(a, f)
        self.cloth_dict = objs


    def load_dict(self):
        data_list = []
        with open('./cloth.pkl', 'rb+') as f:
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                data_list.append(data)

            self.cloth_dict = {}
            for i in data_list:
                for key, value in i.items():
                    self.cloth_dict[key] = value
        return self.cloth_dict

    def update_file(self):
        os.remove('./cloth.pkl')
        with open('./cloth.pkl', 'wb') as f:
            for a in self.cloth_dict:
                pickle.dump(a, f)

    def select_cloth(self, temper):
        print(temper)
        if temper >= 28:
            # 28도 이상 = 민소매, 반팔, 반바지, 원피스
            if random.choice(["setup", "dress"]) == "setup":
                list_top28 = [self.cloth_dict['top'][0], self.cloth_dict['top'][1]]
                result_top = random.choice(random.choice(list_top28))
                result_bottom = random.choice(random.choice(self.cloth_dict['bottom'][0]))
                return [result_top, result_bottom]
            else:
                dresschoice = random.choice(self.cloth_dict['dress'])
                return dresschoice
        
        elif temper>=23 and temper<=27:
            # 23~27도 =  반팔, 얇은 셔츠, 반바지, 면바지
            list_top2327 = [self.cloth_dict['top'][1], self.cloth_dict['top'][2]]
            list_bot2327 = [self.cloth_dict['bottom'][0], self.cloth_dict['bottom'][1]]
            result_top = random.choice(random.choice(list_top2327))
            result_bottom = random.choice(random.choice(list_bot2327))
            result = [result_top, result_bottom]
            return result

        elif temper>=20 and temper<=22:
            # 얇은 가디건, 긴팔, 면바지, 청바지
            list_bot2022 = [self.cloth_dict['bottom'][1], self.cloth_dict['bottom'][2]]
            result_top =random.choice(self.cloth_dict['top'][3])
            print(result_top)
            result_bottom = random.choice(random.choice(list_bot2022))
            result_outer = random.choice(self.cloth_dict['outer'][0])
            result = [result_outer, result_top, result_bottom]
            return result

        elif temper>=17 and temper<=19:
            #17~19도 = 얇은 니트, 맨투맨, 가디건, 청바지
            list_top2327 = [self.cloth_dict['top'][5], self.cloth_dict['top'][4]]
            result_bottom =random.choice(self.cloth_dict['bottom'][2])
            result_top = random.choice(random.choice(list_top2327))
            result_outer = random.choice(self.cloth_dict['outer'][0])
            result = [result_outer, result_top, result_bottom]
            return result  
        elif temper>=9 and temper<=16:
            #17~19도 = 얇은 니트, 맨투맨, 가디건, 청바지
            list_top916 = [self.cloth_dict['top'][5], self.cloth_dict['top'][4]]
            list_bot916 = [self.cloth_dict['bottom'][1], self.cloth_dict['bottom'][2]]
            list_outer916= [self.cloth_dict['outer'][0], self.cloth_dict['outer'][1]]
            result_top = random.choice(random.choice(list_top916))
            result_bottom = random.choice(random.choice(list_bot916))
            result_outer = random.choice(random.choice(list_outer916))
            result = [result_outer, result_top, result_bottom]
            return result
        else:
            #~8도
            list_top99 = [self.cloth_dict['top'][5], self.cloth_dict['top'][4]]
            list_bot99 = [self.cloth_dict['bottom'][1], self.cloth_dict['bottom'][2]]
            list_outer99= [self.cloth_dict['outer'][2], self.cloth_dict['outer'][3]]
            result_top = random.choice(random.choice(list_top99))
            result_bottom = random.choice(random.choice(list_bot99))
            result_outer = random.choice(random.choice(list_outer99))
            result = [result_outer, result_top, result_bottom]
            return result
    
        
    def add_cloth(self, cate, cloth, num):
        self.cloth_dict[cate][num].append(cloth)
        self.update_file()
        return 0
