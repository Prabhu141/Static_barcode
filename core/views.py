from barcode import Code128
from barcode.writer import ImageWriter
from django.http import HttpResponse
from fpdf import FPDF
from .models import Barcode
from .serializers import BarcodeSerializer
import os
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

def index(request):
    return HttpResponse("Hello !!!")

class Barcodeinlistview(ListCreateAPIView):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer



class Barcodedeleteview(RetrieveUpdateDestroyAPIView):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer


dot = './media/barcode/'
class BarcodeGenerateView(ListCreateAPIView):
    serializer_class = BarcodeSerializer
    queryset = Barcode.objects.all()
    def post(self, request):
        number = request.data.get('number')
        if not number:
            number = request.query_params.get('number')
        try:
            my_code = Code128(number, writer=ImageWriter())
            barcodefilename = dot + number + '.png'
            filename = dot + number 
            my_code.save(filename)

            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # Add file name before the barcode image
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, txt=number, ln=1, align="C")

            # Add the barcode image
            pdf.image(barcodefilename, x=pdf.w / 2 - 50, y=pdf.h / 2 - 50, w=100)

            # Save the PDF file
            #pdf_filename = dot + "barcodescenter-static.pdf"
            pdfformat = '.pdf'
            pdf_filename = dot + f"{number}{pdfformat}"
            # pdf_filename = f"{number}.pdf"
            pdf.output(pdf_filename)
            # for barcode_filename in barcodefilename:
            os.remove(barcodefilename)
            domain = request.get_host()
            ## not saving into database
            file_paths = '/media/barcode/'+ f"{number}{pdfformat}"
            file_url = f"http://{domain}{file_paths}"

            # Save the barcode data to the database
            chat = Barcode.objects.create(number=number, pdf=file_url)
            serializer = BarcodeSerializer(chat)
            return Response(serializer.data)
            # barcode = Barcode(number=number)
            # barcode.save()

            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



















class codeinlistview(ListCreateAPIView):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer



class codedeleteview(RetrieveUpdateDestroyAPIView):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer


dot = './media/barcode/'
class codeGenerateView(ListCreateAPIView):
    serializer_class = BarcodeSerializer
    queryset = Barcode.objects.all()
    def post(self, request):
        number = request.data.get('number')
        if not number:
            number = request.query_params.get('number')
        try:
            my_code = Code128(number, writer=ImageWriter())
            barcodefilename = dot + number + '.png'
            filename = dot + number 
            my_code.save(filename)

            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # Add file name before the barcode image
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, txt=number, ln=1, align="C")

            # Add the barcode image
            pdf.image(barcodefilename, x=pdf.w / 2 - 50, y=pdf.h / 2 - 50, w=100)

            # Save the PDF file
            #pdf_filename = dot + "barcodescenter-static.pdf"
            pdfformat = '.pdf'
            pdf_filename = dot + f"{number}{pdfformat}"
            # pdf_filename = f"{number}.pdf"
            pdf.output(pdf_filename)
            os.remove(barcodefilename)
            domain = request.get_host()
            ## not saving into database
            file_paths = '/media/barcode/'+ f"{number}{pdfformat}"
            file_url = f"http://{domain}{file_paths}"
            data = {
            "inputnumber": number,
            "outputpdf": file_url,
            }
            return Response(data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)










