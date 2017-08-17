from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "Hello, I am your index request!"
    request.session['product_id']=0
    if 'total' not in request.session:
        request.session['total'] = 0
        print "Hello, I am your index request!"
    return render(request, 'amadon/index.html')


def buy(request):
    print '*'*30
    total_session = request.session['total']
    request.session['quantity'] = request.POST['quantity']
    request.session['product_id'] = request.POST['product_id']
    total_session += int(request.POST['quantity'])
    request.session['total'] = total_session
    print '*'*30
    return redirect('/amadon/receipt')

def receipt(request):
    print '$'*30
    if request.session['product_id'] == '1915':
        price = float(19.99)
    elif request.session['product_id'] == '2915':
        price = float(29.99)
    elif request.session['product_id'] == '415':
        price = float(4.99)
    elif request.session['product_id'] == '4915':
        price = float(49.99)
    print '$'*30
    total_price = price * int(request.session['quantity'])
    context = {
        'quantity': request.session['quantity'],
        'total_price': total_price,
        'total_quantity': request.session['total']
    }
    print request.session['total']
    return render(request, 'amadon/receipt.html', context)

def reset(request):
    if request.method == 'GET':
        request.session.flush()
    return redirect('/amadon')