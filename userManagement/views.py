from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import NutritionFacts

# Create your views here.
def indexfunc(request):
    return render(request, 'index.html', {})

def signupfunc(request):
    user2 = User.objects.all()
    print(user2)
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, "", password2)
    return render(request, 'login.html')

def loginfunc(request):
    if request.method == 'POST':
        print("login post now")
        username2 = request.POST["username"]
        password2 = request.POST["password"]
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("login->home")
            return render(request, 'home.html')
            # return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def homefunc(request):
    # 成分表の全データ
    print(request.session.get('object_list'))
    if request.session.get('object_list') is None:
        context = {'object_list':NutritionFacts.objects.all()}
    if request.method == 'POST':
        # 時間
        time = request.POST.get('time')
        # 食材名
        name = request.POST.get('addName')
        # 数量
        amout = int(request.POST.get('amount'))
        
        # 返却用：食材と数量のデータ作成
        print(request.session.get('recipe'))
        recipe = request.session.get('recipe')
        print(recipe)
        if recipe is None:
            recipe = ({time:{name:amout}})
        elif recipe.get(time) is None:
            recipe.update({time:{name:amout}})
        else:
            recipe[time].update({name:amout})
        request.session['recipe'] = recipe
        print(request.session.get('recipe'))
        
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
            for name in recipe[time].keys():
                # 食材の栄養データ取得
                result = NutritionFacts.objects.filter(name=name)\
                    .values("energyCal","protein","lipid","foodFiberTotal","calcium","iron",
                        "vitaminA","vitaminB1","vitaminB2","vitaminC","salt",)
                
                energyCal       =+ energyCal        + float(result[0].get('energyCal') * float(amout / 100))
                protein         =+ protein          + float(result[0].get('protein') * float(amout / 100))
                lipid           =+ lipid            + float(result[0].get('lipid') * float(amout / 100))
                foodFiberTotal  =+ foodFiberTotal   + float(result[0].get('foodFiberTotal') * float(amout / 100))
                calcium         =+ calcium          + float(result[0].get('calcium') * float(amout / 100))
                iron            =+ iron             + float(result[0].get('iron') * float(amout / 100))
                vitaminA        =+ vitaminA         + float(result[0].get('vitaminA') * float(amout / 100))
                vitaminB1       =+ vitaminB1        + float(result[0].get('vitaminB1') * float(amout / 100))
                vitaminB2       =+ vitaminB2        + float(result[0].get('vitaminB2') * float(amout / 100))
                vitaminC        =+ vitaminC         + float(result[0].get('vitaminC') * float(amout / 100))
                salt            =+ salt             + float(result[0].get('salt') * float(amout / 100))

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
        context.update({"nutrition":nutrition, "recipe":recipe})
    return render(request, 'home.html', context)