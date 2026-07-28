from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from contactdetail.models import Contactform
from sliderupdation.models import SliderUpdation
from blogpanel.models import Blog
from django.http import JsonResponse, HttpResponse
import yfinance as yf

def home_page(request):
    return render(request, "index.html")

def aboutpage(request):
    return render(request, "about.html")

def contactdetail(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')

        Contactform.objects.create(
            username=username,
            usermail=useremail
        )

        msg = 'form submitted!'

        html_content = render_to_string(
            'email_template.html',
            {
                'username': username,
                'useremail': useremail,
            }
        )

        send_mail(
            subject="Testing mail",
            message="Hello Sangam University",
            from_email="payalkanwar4433@gmail.com",
            recipient_list=["tamannaregar2@gmail.com"],
            fail_silently=False,
        )

        admin_subject = f"New Contact Form Submission from {username}"
        admin_message = (
            f"Name: {username}\n"
            f"Email: {useremail}\n"
        )

        admin_email = EmailMultiAlternatives(
            subject=admin_subject,
            body=admin_message,
            from_email="payalkanwar4433@gmail.com",
            to=["tamannaregar2@gmail.com"],
        )
        admin_email.send(fail_silently=False)

        return render(request, 'contact.html', {'msg': msg})

    return render(request, 'contact.html', {'msg': msg})

def service(request):
    return render(request, "serves.html")

def price(request):
    return render(request, "price.html")

def stock_price(request, symbol):
    try:
        if not symbol.endswith(".NS"):
            symbol += ".NS"

        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")

        if data.empty:
            return JsonResponse({"error": "Invalid or unsupported stock symbol"}, status=400)

        price = float(data["Close"].iloc[-1])

        return JsonResponse({
            "symbol": symbol.replace(".NS", "").upper(),
            "price": price
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def api_page(request):
    return render(request, "app.html")
