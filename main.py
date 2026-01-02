import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QSlider, QFileDialog,
                             QSpinBox, QComboBox, QMessageBox, QScrollArea)
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import Qt
from PIL import Image, ImageEnhance
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os

class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image = None
        self.edited_image = None
        self.image_path = None
        
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Image Editor - Save to PDF")
        self.setGeometry(100, 100, 1000, 700)
        
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout()
        
        # Image display area
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 2px solid #ccc; background-color: #f0f0f0;")
        self.image_label.setMinimumSize(500, 400)
        
        scroll = QScrollArea()
        scroll.setWidget(self.image_label)
        scroll.setWidgetResizable(True)
        
        main_layout.addWidget(scroll, 3)
        
        # Control panel
        control_layout = QVBoxLayout()
        
        # Load button
        load_btn = QPushButton("📂 Load Image")
        load_btn.clicked.connect(self.load_image)
        control_layout.addWidget(load_btn)
        
        # Rotate
        control_layout.addWidget(QLabel("Rotate (degrees):"))
        rotate_spinbox = QSpinBox()
        rotate_spinbox.setRange(0, 360)
        rotate_spinbox.setValue(0)
        rotate_spinbox.valueChanged.connect(lambda v: self.rotate_image(v))
        self.rotate_spinbox = rotate_spinbox
        control_layout.addWidget(rotate_spinbox)
        
        # Brightness
        control_layout.addWidget(QLabel("Brightness:"))
        brightness_slider = QSlider(Qt.Horizontal)
        brightness_slider.setRange(50, 150)
        brightness_slider.setValue(100)
        brightness_slider.valueChanged.connect(lambda v: self.adjust_brightness(v))
        self.brightness_slider = brightness_slider
        control_layout.addWidget(brightness_slider)
        
        # Contrast
        control_layout.addWidget(QLabel("Contrast:"))
        contrast_slider = QSlider(Qt.Horizontal)
        contrast_slider.setRange(50, 150)
        contrast_slider.setValue(100)
        contrast_slider.valueChanged.connect(lambda v: self.adjust_contrast(v))
        self.contrast_slider = contrast_slider
        control_layout.addWidget(contrast_slider)
        
        # Saturation
        control_layout.addWidget(QLabel("Saturation:"))
        saturation_slider = QSlider(Qt.Horizontal)
        saturation_slider.setRange(0, 200)
        saturation_slider.setValue(100)
        saturation_slider.valueChanged.connect(lambda v: self.adjust_saturation(v))
        self.saturation_slider = saturation_slider
        control_layout.addWidget(saturation_slider)
        
        # Flip options
        control_layout.addWidget(QLabel("Flip:"))
        flip_combo = QComboBox()
        flip_combo.addItems(["None", "Horizontal", "Vertical"])
        flip_combo.currentTextChanged.connect(self.apply_flip)
        self.flip_combo = flip_combo
        control_layout.addWidget(flip_combo)
        
        # Reset button
        reset_btn = QPushButton("🔄 Reset")
        reset_btn.clicked.connect(self.reset_image)
        control_layout.addWidget(reset_btn)
        
        # Save buttons
        save_regular_btn = QPushButton("💾 Save as Image")
        save_regular_btn.clicked.connect(self.save_image)
        control_layout.addWidget(save_regular_btn)
        
        save_pdf_btn = QPushButton("📄 Save as PDF (A4)")
        save_pdf_btn.clicked.connect(self.save_as_pdf)
        save_pdf_btn.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        control_layout.addWidget(save_pdf_btn)
        
        control_layout.addStretch()
        
        # Add control panel to main layout
        control_widget = QWidget()
        control_widget.setLayout(control_layout)
        control_widget.setMaximumWidth(250)
        main_layout.addWidget(control_widget, 1)
        
        main_widget.setLayout(main_layout)
    
    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Load Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        
        if file_path:
            self.image = Image.open(file_path)
            self.image_path = file_path
            self.edited_image = self.image.copy()
            self.rotate_spinbox.setValue(0)
            self.brightness_slider.setValue(100)
            self.contrast_slider.setValue(100)
            self.saturation_slider.setValue(100)
            self.flip_combo.setCurrentText("None")
            self.display_image()
    
    def display_image(self):
        if self.edited_image:
            # Resize for display
            display_image = self.edited_image.copy()
            display_image.thumbnail((600, 500), Image.Resampling.LANCZOS)
            
            # Convert to QPixmap
            data = display_image.tobytes('raw', 'RGB')
            qimage = QImage(data, display_image.width, display_image.height, 
                           display_image.width * 3, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
            
            self.image_label.setPixmap(pixmap)
    
    def rotate_image(self, angle):
        if self.image:
            self.edited_image = self.image.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
            self.apply_all_adjustments()
    
    def adjust_brightness(self, value):
        if self.image:
            self.apply_all_adjustments()
    
    def adjust_contrast(self, value):
        if self.image:
            self.apply_all_adjustments()
    
    def adjust_saturation(self, value):
        if self.image:
            self.apply_all_adjustments()
    
    def apply_flip(self, direction):
        if self.image:
            self.apply_all_adjustments()
    
    def apply_all_adjustments(self):
        if not self.image:
            return
        
        # Start with rotated image
        temp_image = self.image.rotate(self.rotate_spinbox.value(), expand=True, 
                                       resample=Image.Resampling.BICUBIC)
        
        # Apply flip
        flip_type = self.flip_combo.currentText()
        if flip_type == "Horizontal":
            temp_image = temp_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        elif flip_type == "Vertical":
            temp_image = temp_image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        
        # Convert to RGB if necessary
        if temp_image.mode != 'RGB':
            temp_image = temp_image.convert('RGB')
        
        # Apply brightness
        brightness_value = self.brightness_slider.value() / 100.0
        enhancer = ImageEnhance.Brightness(temp_image)
        temp_image = enhancer.enhance(brightness_value)
        
        # Apply contrast
        contrast_value = self.contrast_slider.value() / 100.0
        enhancer = ImageEnhance.Contrast(temp_image)
        temp_image = enhancer.enhance(contrast_value)
        
        # Apply saturation
        saturation_value = self.saturation_slider.value() / 100.0
        enhancer = ImageEnhance.Color(temp_image)
        temp_image = enhancer.enhance(saturation_value)
        
        self.edited_image = temp_image
        self.display_image()
    
    def reset_image(self):
        if self.image:
            self.edited_image = self.image.copy()
            self.rotate_spinbox.setValue(0)
            self.brightness_slider.setValue(100)
            self.contrast_slider.setValue(100)
            self.saturation_slider.setValue(100)
            self.flip_combo.setCurrentText("None")
            self.display_image()
    
    def save_image(self):
        if not self.edited_image:
            QMessageBox.warning(self, "Warning", "No image loaded!")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG (*.png);;JPEG (*.jpg);;BMP (*.bmp)"
        )
        
        if file_path:
            self.edited_image.save(file_path)
            QMessageBox.information(self, "Success", f"Image saved successfully!\n{file_path}")
    
    def save_as_pdf(self):
        if not self.edited_image:
            QMessageBox.warning(self, "Warning", "No image loaded!")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save as PDF", "", "PDF Files (*.pdf)"
        )
        
        if file_path:
            try:
                # A4 dimensions
                page_width, page_height = A4
                
                # Create a temporary image file
                temp_image_path = "/tmp/temp_image.png"
                self.edited_image.save(temp_image_path)
                
                # Create PDF
                c = canvas.Canvas(file_path, pagesize=A4)
                
                # Calculate image dimensions to fit A4 with margins
                margin = 0.5 * inch
                available_width = page_width - 2 * margin
                available_height = page_height - 2 * margin
                
                # Get image dimensions
                img_width, img_height = self.edited_image.size
                aspect_ratio = img_height / img_width
                
                # Fit image to page
                if (available_width * aspect_ratio) <= available_height:
                    final_width = available_width
                    final_height = available_width * aspect_ratio
                else:
                    final_height = available_height
                    final_width = available_height / aspect_ratio
                
                # Center the image
                x = (page_width - final_width) / 2
                y = (page_height - final_height) / 2
                
                # Draw image on PDF
                c.drawImage(temp_image_path, x, y, width=final_width, height=final_height)
                c.save()
                
                # Clean up
                os.remove(temp_image_path)
                
                QMessageBox.information(self, "Success", f"PDF saved successfully!\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save PDF:\n{str(e)}")


def main():
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
