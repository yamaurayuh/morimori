from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NutritionFacts(models.Model):
    number = models.IntegerField()	                    #食品番号
    classification = models.CharField(max_length=10)	#食品分類
    name = models.CharField(max_length=60)	            #食品名
    disposalRate = models.FloatField()	                #廃棄率
    energyJ = models.FloatField()	                    #エネルギー(J)
    energyCal = models.FloatField()	                    #エネルギー(kcal)
    moisture = models.FloatField()	                    #水分
    proteinByAminoAcidComposition = models.FloatField()	#アミノ酸組成によるたんぱく質
    protein = models.FloatField()	                    #たんぱく質
    fattyAcidTriAcylGlycerolEquivalent = models.FloatField()	        #脂肪酸のトリアシルグリセロール当量
    cholesterol = models.FloatField()	                #コレステロール
    lipid = models.FloatField()	                        #脂質
    availableCarbohydrateMonosaccharideEquivalent = models.FloatField()	#利用可能炭水化物単糖当量
    availableCarbohydrateMassTotal = models.FloatField()	            #利用可能炭水化物質量計
    deductionLawByAvailableCarbohydrate = models.FloatField()	        #差引き法による利用可能炭水化物
    foodFiberTotal = models.FloatField()	            #食物繊維総量
    sugarAlcohol = models.FloatField()	                #糖アルコール
    carbohydrate = models.FloatField()	                #炭水化物
    organicAcid = models.FloatField()	                #有機酸
    ash = models.FloatField()	                        #灰分
    natrium = models.FloatField()	                    #ナトリウム
    potassium = models.FloatField()	                    #カリウム
    calcium = models.FloatField()	                    #カルシウム
    magnesium = models.FloatField()	                    #マグネシウム
    phosphorus = models.FloatField()	                #リン
    iron = models.FloatField()	#鉄
    zinc = models.FloatField()	#亜鉛
    copper = models.FloatField()	#銅
    manganese = models.FloatField()	#マンガン
    iodine = models.FloatField()	#ヨウ素
    selenium = models.FloatField()	#セレン
    chrome = models.FloatField()	#クロム
    molybdenum = models.FloatField()	#モリブデン
    retinol = models.FloatField()	#レチノール
    alphaCarotene = models.FloatField()	#α0カロテン
    betaCarotene = models.FloatField()	#β0カロテン
    betaCryptoxanthin = models.FloatField()	#β0クリプトキサンチン
    betaCaroteneEquivalent = models.FloatField()	#β0カロテン当量
    vitaminA = models.FloatField()	#ビタミンA
    vitaminD = models.FloatField()	#ビタミンD
    vitaminE = models.FloatField()	#ビタミンE
    betaTocopherol = models.FloatField()	#β0トコフェロール
    gammaTocopherol = models.FloatField()	#γ0トコフェロール
    deltaTocopherol = models.FloatField()	#δ0トコフェロール
    vitaminK = models.FloatField()	#ビタミンK
    vitaminB1 = models.FloatField()	#ビタミンB1
    vitaminB2 = models.FloatField()	#ビタミンB2
    niacin = models.FloatField()	#ナイアシン
    niacinEquivalent = models.FloatField()	#ナイアシン当量
    vitaminB6 = models.FloatField()	#ビタミンB6
    vitaminB12 = models.FloatField()	#ビタミンB12
    folicAcid = models.FloatField()	#葉酸
    pantothenicAcid = models.FloatField()	#パントテン酸
    biotin = models.FloatField()	#ビオチン
    vitaminC = models.FloatField()	#ビタミンC
    alcohol = models.FloatField()	#アルコール
    salt = models.FloatField()	#食塩相当量
    note = models.CharField(max_length=200, blank=True, null=True)	#備考

class mealRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1,)  # ユーザ
    day = models.DateField()                # 日付
    breakfast = models.TextField(null=False, blank=True,)      # 朝食
    lunch = models.TextField(null=False, blank=True,)          # 昼食
    dinner = models.TextField(null=False, blank=True,)         # 夕食
    snack = models.TextField(null=False, blank=True,)          # 間食
