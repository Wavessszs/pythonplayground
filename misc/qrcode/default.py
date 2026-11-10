from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from plyer import filechooser
from pyzbar.pyzbar import decode
from PIL import Image as PILImage

class QRScanner(BoxLayout):
    def __init__(self, **kwargs):
        super(QRScanner, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Button to open file chooser
        self.btn_open = Button(text="Choose Photo")
        self.btn_open.bind(on_press=self.open_file_chooser)
        self.add_widget(self.btn_open)

        # Label to display QR code data
        self.label = Label(text="Select an image to scan.")
        self.add_widget(self.label)

        # Image widget to show the selected image
        self.image = Image(size_hint=(1, 0.6))
        self.add_widget(self.image)

    def open_file_chooser(self, instance):
        # Open file picker and get selected file
        filechooser.open_file(on_selection=self.load_image)

    def load_image(self, selection):
        if selection:
            image_path = selection[0]
            # Load and display the selected image
            self.image.source = image_path
            self.image.reload()

            # Scan the image for QR codes
            self.scan_qr_code(image_path)

    def scan_qr_code(self, image_path):
        # Open image using Pillow
        pil_image = PILImage.open(image_path)
        decoded_objects = decode(pil_image)
        if decoded_objects:
            # Display the QR code data
            self.label.text = f"QR Code Data: {decoded_objects[0].data.decode('utf-8')}"
        else:
            self.label.text = "No QR code detected."

class QRScannerApp(App):
    def build(self):
        return QRScanner()

if __name__ == '__main__':
    QRScannerApp().run()
