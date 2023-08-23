from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import NutritionFacts
from django.contrib.auth.decorators import login_required

# Create your views here.
def indexfunc(request):
    return render(request, 'index.html', {})

def signupfunc(request):
    user2 = User.objects.all()
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, "", password2)
            return redirect('login')
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST["username"]
        password2 = request.POST["password"]
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('daily')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required
def logoutfunc(request):
    logout(request)
    return redirect('login')


@login_required
def displayDailyIngredientRecordFunc(request):

    print('★★★ingredientRecordUpdateFunc★★★')
    print(request.POST)
    # 成分表の全データ
    context = {'object_list':NutritionFacts.objects.all()}
    if request.session.get('recipe') is None:
        request.session['recipe'] = {'breakfast':{},'lunch':{},'dinner':{},'snack':{}}
    context.update({'recipe':request.session.get('recipe')})
    if request.method == 'POST':
        # 返却用：食材と数量のデータ作成
        recipe = request.session.get('recipe')

        # 時間
        getTime = request.POST.get('time')
        # 食材名
        getName = request.POST.get('addName')
        
        # 食材追加処理
        if request.POST.get('del_name') is None:
            # 数量
            getAmount = int(request.POST.get('amount'))
            recipe[getTime].update({getName:getAmount})
        # 食材削除処理
        else:
            getDelName = request.POST.get('del_name')
            getDelTime = request.POST.get('del_time')
            recipe[getDelTime].pop(getDelName, None)

        request.session['recipe'] = recipe
        
        # 栄養データ用変数
        energyCal       = 0.0
        protein         = 0.0
        lipid           = 0.0
        foodFiberTotal  = 0.0
        calcium         = 0.0
        iron            = 0.0
        vitaminA        = 0.0
        vitaminB1       = 0.0
        vitaminB2       = 0.0
        vitaminC        = 0.0
        salt            = 0.0

        # レシピに入れた栄養データの計算
        for time in recipe.keys():
            for name, amout in recipe[time].items():
                # 食材の栄養データ取得
                result = NutritionFacts.objects.filter(name=name)\
                    .values("energyCal","protein","lipid","foodFiberTotal","calcium","iron",
                        "vitaminA","vitaminB1","vitaminB2","vitaminC","salt",)
                energyCal       += float(result[0].get('energyCal') * float(amout / 100))
                protein         += float(result[0].get('protein') * float(amout / 100))
                lipid           += float(result[0].get('lipid') * float(amout / 100))
                foodFiberTotal  += float(result[0].get('foodFiberTotal') * float(amout / 100))
                calcium         += float(result[0].get('calcium') * float(amout / 100))
                iron            += float(result[0].get('iron') * float(amout / 100))
                vitaminA        += float(result[0].get('vitaminA') * float(amout / 100))
                vitaminB1       += float(result[0].get('vitaminB1') * float(amout / 100))
                vitaminB2       += float(result[0].get('vitaminB2') * float(amout / 100))
                vitaminC        += float(result[0].get('vitaminC') * float(amout / 100))
                salt            += float(result[0].get('salt') * float(amout / 100))

        # 返却用：栄養データ作成
        nutrition = {
            "energyCal":'{:.2f}'.format(energyCal),
            "protein":'{:.2f}'.format(protein),
            "lipid":'{:.2f}'.format(lipid),
            "foodFiberTotal":'{:.2f}'.format(foodFiberTotal),
            "calcium":'{:.2f}'.format(calcium),
            "iron":'{:.2f}'.format(iron),
            "vitaminA":'{:.2f}'.format(vitaminA),
            "vitaminB1":'{:.2f}'.format(vitaminB1),
            "vitaminB2":'{:.2f}'.format(vitaminB2),
            "vitaminC":'{:.2f}'.format(vitaminC),
            "salt":'{:.2f}'.format(salt),
        }

        request.session['nutrition'] = nutrition

        # 返却用コンテキス
        context.update({"nutrition":nutrition, "recipe":recipe})
    return render(request, 'displayDailyIngredientRecord.html', context)

@login_required
def accountfunc(request):
    return render(request, 'account.html')