from django.shortcuts import render
from django.core.mail import send_mail
from contactdetail.models import Contactform
from sliderupdation.models import SliderUpdation
from blogpanel.models import Blog
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import requests
from django.shortcuts import render
def home_page(request):
        return render(request,"index.html")
def aboutpage(request):
        return render(request,'about.html')

def contactdetail(request):
        msg=''
        if request.method == 'POST':
                username=request.POST.get('username')
                useremail=request.POST.get('useremail')
                allData=Contactform(username=username,usermail=useremail)   
                allData.save()
                msg='form submitted!'
                # Render HTML template
                html_content = render_to_string('email_template.html', {
                'username': username,
                'useremail': useremail,
                })

                send_mail(
                subject="Testing mail",
                message="Hello Sangam University",
                from_email="payalkanwar4433@gmail.com",
                # MUST be a real address (same as EMAIL_HOST_USER)
                recipient_list=["tamannaregar2@gmail.com"],
                fail_silently=False,
                )
                # Send admin notification (plain text)
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

                
                return render(request,'contact.html',{'msg': msg})
        return render(request,'contact.html',{'msg': msg})

def service(request):
        return render(request,"serves.html")


from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import openai
from aiapp.models import PromptLog
import yfinance as yf
from django.http import JsonResponse

import yfinance as yf
from django.http import JsonResponse

def stock_price(request, symbol):
    try:
        # Avoid double extension (if user passes RELIANCE.NS)
        if not symbol.endswith(".NS"):
            symbol = symbol + ".NS"

        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")

        # Check if data returned
        if data is None or data.empty:
            return JsonResponse({"error": "Invalid or unsupported stock symbol"}, status=400)

        # Get the last close safely
        price = float(data["Close"].iloc[-1])

        return JsonResponse({
            "symbol": symbol.replace(".NS", "").upper(),
            "price": price
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def api_page(req):
      return render(req,'app.html')

from django.http import HttpResponse

