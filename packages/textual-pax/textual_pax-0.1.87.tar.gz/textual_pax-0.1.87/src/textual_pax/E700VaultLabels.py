from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, mm
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing, String, Group
from reportlab.graphics import renderPDF
from reportlab_qrcode import QRCodeImage
import pandas as pd
import datetime
import os

#from all_on_one import re_list, create_df, get_sheets_names

PAGESIZE = (5*inch, 3.5*inch)
PAGEWIDTH = PAGESIZE[0]
PAGEHEIGHT = PAGESIZE[1]
TEXT_Y = 60
NUM_LABELS_X = 3
NUM_LABELS_Y = 4
LABEL_WIDTH = PAGESIZE[0] / NUM_LABELS_X
LABEL_HEIGHT = PAGESIZE[1] / NUM_LABELS_Y
SHEET_TOP = PAGESIZE[1]
BARCODE_Y = 25
TEXT_2_Y = 30
U = range(0, NUM_LABELS_Y)
I = range(0, NUM_LABELS_X)

def simple_label(model_pn: str, serialNo_no: str):

    barcode = createBarcodeDrawing("Code128", value=serialNo_no, width=55*mm, height=8*mm)
    x0, y0, bw, bh = barcode.getBounds() # type: ignore
    barcode_x = (LABEL_WIDTH - bw) / 2  # center barcode
    barcode_y = BARCODE_Y  # spacing from label bottom (pt)
    text_2 = String(0, BARCODE_Y - 10, str(model_pn)+" S/N: "+str(serialNo_no), fontName="Helvetica", fontSize=5, textAnchor="middle")
    text_2.x = LABEL_WIDTH / 2 # type: ignore
    label_drawing = Drawing(LABEL_WIDTH,LABEL_HEIGHT) # type: ignore
    bc_g = Group()
    bc_g.add(barcode)
    bc_g.shift(barcode_x,barcode_y)

    label_drawing.add(bc_g)
    label_drawing.add(text_2)
    
    return label_drawing

def qr_write(df: pd.DataFrame):
    q_r = QRCodeImage(df.to_string(index=False),size=50 * mm)
    return q_r

def map_it():
    x_list = []
    y_list = []
    for u in range(0, NUM_LABELS_Y):
        for i in range(0, NUM_LABELS_X):
            x = i * LABEL_WIDTH
            y = SHEET_TOP - LABEL_HEIGHT - u * LABEL_HEIGHT
            x_list.append(x)
            y_list.append(y)
    return(list(zip(x_list,y_list)))

def interface_labels():
    pass      

def E700_to_VaultPDF(serialNoList, boxNo):
    
    name = f'HLD-E74G-{boxNo}' 

    modNameList = ['E700 4G' for serialNo in serialNoList]
    modPnList = ['E700-A8200-1431-503-EA' for serialNo in serialNoList]
    new_serialNo_list = []
    for serialNo in serialNoList:
        if serialNo[0:3] =="134":
            new_serialNo_list.append(serialNo)
        else:pass

    #tid_list = [term_id["terminal_id"] for term_id in terminal_dict]
    #serialNo_list = [serialNo["serialNo_No"] for serialNo in terminal_dict]
    drawing_list = []
    for  modPn, serialNo in list(zip(modPnList, new_serialNo_list)):
        sticker = simple_label(modPn, serialNo)
        drawing_list.append(sticker)
    coordinates = map_it()
    zip_list = list(zip(drawing_list,coordinates))

    Current_Date = str(datetime.datetime.today().strftime('%m.%d.%Y.%H.%M'))
    if os.path.isdir('Labels'):
        pass
    else: os.mkdir("Labels")
    filename = str(modNameList[0]+"_labels_"+Current_Date+"_G"+boxNo+".pdf") # type: ignore

    label_path = os.path.join("Labels", filename)
    c = Canvas(label_path, pagesize=PAGESIZE)
    place_file = os.path.join("Labels", filename)
    
    c = Canvas(place_file, pagesize=PAGESIZE)
    for drawing, coordinates in zip_list:
        renderPDF.draw(drawing, c,coordinates[0],coordinates[1])
    c.setFont('Helvetica-Bold', 20, None)
    text = str("Model: "+modNameList[0]+" 4G | QTY: "+str(len(new_serialNo_list)))
    print(text)
    c.drawString(10,20, text)

    c.setFont('Helvetica-Bold', 28, None)
    c.drawString(10,60,str(name))



    qr = QRCodeImage(str(serialNoList),size=30 * mm)
    qr.drawOn(c,269,10)
    print(PAGESIZE)
    c.save()

def input_serials_v_2() -> list[str]:
    """Prompts user to input base serial numbers (no accessories).  -> List of serial numbers formatted as string"""
    serial_list = []
    while True: 
        serial_no = input("\n--------------------------------------------\nPlease Input or Scan terminal serial number:\n>>>>")
        if serial_no =="BKSPC":
            serial_list.pop()
            pass
        elif ":" in serial_no: 
            pass
        elif serial_no == "0000":
            break
        else: serial_list.append(str(serial_no))
    print(serial_list)
    return serial_list

def prompt(): 
   boxNo = input("\n\n*******Please proivde Box Number in yyy format eg(001):\n>>>>")
   serialNoList = input_serials_v_2()
   box_label = E700_to_VaultPDF(serialNoList,boxNo) 

def ex_or_cont():
    choice = input("n\n\n\nTask completed.\n Press 1111 to Continue or 0000 to Quit\n>>>>")
    while True: 
        if choice == "1111":
            prompt()
        elif choice == "0000":
            break
        

def main():
    prompt()
    ex_or_cont()

if __name__ =='__main__':
    main()