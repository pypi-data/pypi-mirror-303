from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import mm
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing, String, Group
from reportlab.graphics import renderPDF
import datetime
import pandas as pd 
import asyncio
import os


"""PAGESIZE = (89*mm,28*mm)
PAGEWIDTH = PAGESIZE[1]
PAGEHEIGHT = PAGESIZE[0]
TEXT_Y = 55
NUM_LABELS_X = 1
NUM_LABELS_Y = 1
LABEL_WIDTH = PAGESIZE[0] / NUM_LABELS_X
LABEL_HEIGHT = PAGESIZE[1] / NUM_LABELS_Y
SHEET_TOP = PAGESIZE[1]
BARCODE_Y = 50"""

class PDFLabels():

    """
    Represents a collection of labels on a PDF page.

    Attributes:
        num_labels_x (int): Number of labels horizontally.
        num_labels_y (int): Number of labels vertically.
        text_y (int): Vertical position of text (in points).
        barcode_y (int): Vertical position of barcode (in points).
        pagesize (tuple): Page size (width, height) in points.
        labelwidth (float): Width of a single label (in points).
        labelheight (float): Height of a single label (in points).
        sheettop (float): Top position of the label sheet (in points).
        u (range): Range of y-axis indices.
        i (range): Range of x-axis indices.
    """


    def __init__(self, pagesize:tuple, num_labels_x:int, num_labels_y:int, text_y:int, barcode_y:int) -> None:
        
        self.pagesize = pagesize
        self.num_labels_x = num_labels_x
        self.num_labels_y = num_labels_y
        self.text_y = text_y
        self.barcode_y = barcode_y
        self.pagewidth = self.pagesize[1]
        self.pageheight = self.pagesize[0]
        self.labelwidth = self.pagesize[0]/self.num_labels_x
        self.labelheight = self.pagesize[1]/self.num_labels_y
        self.sheettop = self.pagesize[1]
        self.u = range(0,self.num_labels_y)
        self.i = range(0,self.num_labels_x)

    def draw_it(self, c: Canvas, label_drawing: Drawing):  
        """
        Draws the label layout onto the specified canvas.

        Args:
            c (Canvas): The PDF canvas.
            label_drawing (Drawing): The label drawing object.
        """
        for u in range(0, self.num_labels_y):
            for i in range(0, self.num_labels_x):
                x = i * self.labelwidth
                y = self.sheettop - self.labelheight - u * self.labelheight
                renderPDF.draw(label_drawing, c, x, y)

    def map_it(self) -> list[tuple[int, int]]:
        """
        Returns a list of (x, y) coordinates for all label positions.

        Returns:
            list[tuple[int, int]]: A list of coordinate tuples.
        """        

        return [(i * self.labelwidth, self.sheettop - self.labelheight - u * self.labelheight)
            for u in range(self.num_labels_y)
            for i in range(self.num_labels_x)]
    
    def create_label(self, model: str, model_pn: str, serial_no: str, iccid: str = None) -> Drawing:
        barcode = createBarcodeDrawing("Code128", value=serial_no, width=45 * mm, height=6 * mm)
        x0, y0, bw, bh = barcode.getBounds()  # type: ignore
        barcode_x = (self.labelwidth - bw) / 2  # center barcode
        barcode_y = self.barcode_y  # spacing from label bottom (pt)
        text = String(0, self.barcode_y - 7, f"PAX {model} {model_pn}", fontName="Helvetica-Bold", fontSize=6, textAnchor="middle")
        text.x = self.labelwidth / 2  # type: ignore
        label_drawing = Drawing(self.pagewidth, self.pageheight)  # type: ignore
        label_drawing.add(text)
        if iccid:
            barcode_2 = createBarcodeDrawing("Code128", value=iccid, width=55 * mm, height=6 * mm)
            bc2x0, bc2y0, bc2bw, bc2bh = barcode_2.getBounds()  # type: ignore
            bc_2_x = (self.labelwidth - bc2bw) / 2
            text_2 = String(0, self.barcode_y - 37, "AT&T SIM: " + iccid, fontName="Helvetica-Bold", fontSize=6, textAnchor="middle")
            text_2.x = self.labelwidth / 2  # type: ignore
            label_drawing.add(barcode_2)
            label_drawing.add(text_2)
        label_drawing.add(barcode, barcode_x, barcode_y)

    def label_w_ICCID(self,model_pn: str, serial_no: str, iccid_no: str):

        barcode = createBarcodeDrawing("Code128", value=serial_no, width=45*mm, height=6*mm)
        x0, y0, bw, bh = barcode.getBounds() # type: ignore
        print(barcode.getBounds()) # type: ignore
        barcode_x = (self.labelwidth - bw) / 2  # center barcode
        barcode_y = self.barcode_y  # spacing from label bottom (pt)
        text = String(0, self.barcode_y - 7, model_pn+" S/N: "+serial_no, fontName="Helvetica-Bold", fontSize=6, textAnchor="middle")
        text.x = self.labelwidth / 2 # type: ignore
        bc_2 = createBarcodeDrawing("Code128", value=iccid_no, width=55*mm, height=6*mm)
        bc2x0, bc2y0, bc2bw, bc2bh = bc_2.getBounds() # type: ignore
        bc_2_x = (self.labelwidth - bc2bw) / 2
        text_2 = String(0, self.barcode_y - 37, "AT&T SIM: "+iccid_no, fontName="Helvetica-Bold", fontSize=6, textAnchor="middle")
        text_2.x = self.labelwidth / 2 # type: ignore
        label_drawing = Drawing(self.pagewidth,self.pageheight)# type: ignore
        bc_g = Group()
        bc_g2 = Group(bc_2)
        bc_g.add(barcode)
        bc_g.shift(barcode_x,barcode_y)
        bc_g2.shift(bc_2_x,barcode_y-30)
        label_drawing.add(bc_g)
        label_drawing.add(bc_g2)
        label_drawing.add(text)
        label_drawing.add(text_2)
        return label_drawing

    def simple_label(self,model: str, model_pn: str, serial_no: str):
        text = String(0, self.text_y, model, fontName="Helvetica-Bold", fontSize=12,textAnchor="middle")
        text.x = self.labelwidth / 2 # type: ignore
        barcode = createBarcodeDrawing("Code128", value=serial_no, width=69*mm, height=10*mm)
        x0, y0, bw, bh = barcode.getBounds() # type: ignore

        barcode_x = (self.labelwidth - bw) / 2  # center barcode
        barcode_y = self.barcode_y  # spacing from label bottom (pt)

        text_2 = String(0, barcode_y - 10, str(model_pn)+" S/N: "+str(serial_no), fontName="Helvetica", fontSize=6, textAnchor="middle")
        text_2.x = self.labelwidth / 2 # type: ignore
        label_drawing = Drawing(self.pagewidth,self.pageheight) # type: ignore
        bc_g = Group()
        bc_g.add(barcode)
        bc_g.shift(barcode_x,barcode_y)
        label_drawing.add(text)
        label_drawing.add(bc_g)
        label_drawing.add(text_2)
        
        return label_drawing     

async def create_pdf(df:pd.DataFrame, group=None, **kwargs) ->str:
    """
    Creates a PDF document containing labels for devices in the provided DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing device information.
        group (str, optional): Group identifier to include in the filename. Defaults to None.

    Returns:
        str: Message indicating successful PDF creation and filename.
    """

    filteredDataFrame = df.drop(df[(df.modelName=="Q20L")|(df.modelName=="Q10A")].index) # Filter out specific models
    # Extract data for label generation
    serial_list = filteredDataFrame['serialNo']
    mod_list = filteredDataFrame['modelName']
    #wifi_mac_list = filteredDataFrame['macAddress']
    q_20_serial_list = filteredDataFrame['accessory']
    try: 
        iccid_list = filteredDataFrame['iccid']
    except KeyError:
        iccid_list = ["nan" for serial in serial_list]
    try:     
        mod_pn_list = filteredDataFrame['pn']
    except KeyError:
        if mod_list[0] == "SP30s": 
            mod_pn_list = ['SP30-00L-264-03E0' for mod in mod_list]
        elif mod_list[0] == "S300":
            mod_pn_list = ["S300-000-364-02NA" for mod in mod_list]


        
    print(q_20_serial_list)   
    full_serial_list = [f"{serial}-{qserial}" if str(qserial) not in {"nan", "None"} else serial for serial, qserial in zip(serial_list, q_20_serial_list)]
    print(full_serial_list)
    current_date = str(datetime.datetime.today().strftime('%m.%d.%Y.%H.%M'))
    # Generate filename
    if os.path.isdir('Labels'):
        pass
    else: os.mkdir("Labels")
    filename = (f"{mod_list[0]}Labels_{current_date}_G{group}" if group else f"{mod_list[0]}Labels_{current_date}_SN{serial_list[0]}.pdf")
    label_path = os.path.join("Labels", filename)
    c = Canvas(label_path, pagesize=(89*mm,28*mm))
    for mod,mod_pn, serial, iccid in list(zip(mod_list,mod_pn_list,full_serial_list, iccid_list)):
        if str(iccid) == 'nan':
            new_label = PDFLabels((89*mm,28*mm),1,1,60,25) # type: ignore
            sticker = new_label.simple_label(f'PAX {mod}', mod_pn,serial)
            new_label.draw_it(c,sticker)
        elif str(iccid) !='nan':
            new_label = PDFLabels((89*mm,28*mm),1,1,55,50) # type: ignore
            sticker = new_label.label_w_ICCID(mod_pn,serial, iccid)
            new_label.draw_it(c,sticker)
        c.showPage()
    print(f'There are {(len(iccid_list))} Pages in this document')
    c.save()

    return f"Labels Created \n Filename: {filename} \n Pages: {(len(full_serial_list))}"

"""df = pd.read_pickle("df.pkl")
asyncio.run(create_pdf(df,None))
"""
