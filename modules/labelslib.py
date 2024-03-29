from fpdf import FPDF
import pyqrcode
from PIL import Image

def parseText(text, char_limit): #TODO: Make this less hardcoded - replace this with something more general
    """
    Moves text into two lines less than the char_limit. If text is too long,
    it will be truncated.
    """
    words = text.split(" ")
    line1 = ""
    line2 = ""

    for word in words:
        if (len(line1 + " " + word) <= char_limit) and line2 == "":
            line1 = line1 + " " + word
        elif (len(line2 + " " + word) <= char_limit):
            line2 = line2 + " " + word
        else:
            # Ignore remaining characters
            break
    return line1, line2

def createValidFilename(text):
    """ Removes specified characters from filename """

    char_list = ['.', '/']
    filename = text.translate({ord(x): '' for x in char_list})
    return filename

class LabelGenerator():
    def __init__(self, label_width=1.85, label_height=0.55): # Everything in inches
        """ Generates a PDF with cuttable labels with the specified label width
        and height. Generates a unique QR code for each label. Labels will be
        automatically tiled on an 8.5 by 11 sheet of paper for printing.
        """
        self.label_width = label_width
        self.label_height = label_height

        # Do not change these parameters:
        self.page_width = 8.5
        self.page_height = 11

        # Settable page parameters - all units are the same as self.units
        self.units = 'in'
        self.x_margin = 1
        self.y_margin = 1
        self.qr_size = 0.4
        self.qr_padding = 0.05 # adds space above and next to qr code
        self.max_chars = 27 # max charcters per line

        self.pdf = FPDF(orientation='P', unit=self.units, format='A4')
        self.pdf.add_font('DIN','','fonts/DINOT-CondMedium.ttf', uni=True)
        self.pdf.set_font("DIN", size=10) # Font size currently hardcoded

    def generateQRCode(self, text):
        """ Generates a QR code in PNG format for a given string and saves
        it to the qr folder.

        Args:
            text (str): string that should be encoded within the QR code
        """
        filename = createValidFilename(str(text))

        # Generate QR code
        qr = pyqrcode.create(text)

        # Create and png file
        qr.png("qr/" + filename + ".png", scale = 2)

        # Create a jpg copy
        im = Image.open("qr/" + filename + ".png")
        rgb_im = im.convert('RGB')
        rgb_im.save("qr/" + filename + ".jpg")

    def determineLabelPosition(self, label_num):
        """ Determines the x,y location of the center of each label in
        inches.

        Args:
            label_num (int): Number of current label

        Returns:
            label_x (int): X-coordinate of center of label in inches
            label_y (int): Y-coordinate of center of label in inches
        """
        # Compute max labels per page
        max_columns = (self.page_width - 2*self.x_margin)//self.label_width
        max_rows = (self.page_height - 2*self.y_margin)//self.label_height
        max_labels = max_columns * max_rows

        # Add page if first label is on new page
        if label_num % max_labels == 0:
            self.pdf.add_page()

        # Make label_num seem like it's on the first page in the same spot
        while label_num >= max_labels:
            label_num = label_num - max_labels

        # Compute x,y location of each label in inches
        row = 0
        column = 0

        row = label_num % max_rows
        column = label_num // max_rows

        label_x = self.x_margin + column*self.label_width
        label_y = self.y_margin + row*self.label_height

        return label_x, label_y

    def generateLabels(self, label_text_list):
        """ Generates PDF containing labels for each label in label_text_list

        Args:
            label_text_list (list): list of strings to make labels for
        """
        for idx in range(len(label_text_list)):
            label_text = label_text_list[idx]
            self.generateQRCode(label_text)
            label_x, label_y = self.determineLabelPosition(idx)
            self.addLabel(label_text, label_x, label_y)

    def addLabel(self, label_text, label_x, label_y): # x, y are label position in inches
        """ Adds a new label to the current label sheet.

        Args:
            label_text (str): Text for new label
            label_x (int): X-coordinate of center of label in inches
            label_y (int): Y-coordinate of center of label in inches
        """
        # Add QR code
        filename = createValidFilename(label_text)
        self.pdf.image("qr/" + filename + ".jpg",
                       x=label_x + self.qr_padding, y=label_y + self.qr_padding,
                       w=self.qr_size)

        # Add label text
        line1, line2 = parseText(label_text, self.max_chars)
        self.pdf.text(label_x + self.qr_padding + self.qr_size, label_y + 0.2, line1)
        self.pdf.text(label_x + self.qr_padding + self.qr_size, label_y + 0.35, line2) # Numbers hardcoded to adjust for line height

        # Add rectangle grid
        self.pdf.set_line_width(0.01)
        self.pdf.set_fill_color(0, 255, 0)
        self.pdf.rect(label_x, label_y, self.label_width, self.label_height) # (float x, float y, float w, float h)

    def save_pdf(self, filename):
        """ Save PDF of labels to specified filename

        Args:
            filename (str): File directory to save PDF to
        """
        self.pdf.output(filename)

if __name__ == "__main__":
    # For testing purposes only
    l = LabelGenerator(2, 0.5)
    l.generateLabels([1,1])
    l.save_pdf("autogenerated_labels.pdf")
