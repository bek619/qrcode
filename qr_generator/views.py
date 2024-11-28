from django.shortcuts import render

# Create your views here.
# qr_generator/views.py
import qrcode
from django.shortcuts import render
from django.http import JsonResponse
import os

# QR kod yaratish funksiyasi
def generate_qr_code(request):
    if request.method == "POST":
        text = request.POST.get('text')
        
        # QR kodni yaratish
        qr = qrcode.QRCode(
            version=1,  # QR kodning o‘lchami (1 - eng kichik)
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        # QR kodni tasvirga aylantirish
        img = qr.make_image(fill='black', back_color='white')

        # Faylni saqlash
        filename = 'qr_code.png'
        img.save(os.path.join('static', filename))

        return JsonResponse({'qr_code_url': f'/static/{filename}'})

    return render(request, 'qr_generator/generate_qr.html')