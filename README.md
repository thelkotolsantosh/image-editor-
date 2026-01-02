# 📸 Image Editor - PDF Export Tool : A simple desktop image editor built with PyQt5. Edit your images and export them as professional A4 PDF documents.

 ✨ Features

- Load Images: Support for PNG, JPEG, BMP, GIF formats
- Edit Tools:
  - 🔄 Rotate (0-360°)
  - ☀️ Brightness control
  - 🎨 Contrast adjustment
  - 🌈 Saturation control
  - 🔀 Flip (Horizontal/Vertical)
- Save Options:
  - Save edited images as PNG, JPEG, or BMP
  - Export as A4 PDF with automatic scaling
- Preview: Real-time preview of all edits

 🚀 Quick Start

# Prerequisites
- Python 3.7+
- pip

# Installation

bash
# Clone the repository
git clone https://github.com/yourusername/image-editor.git
cd image-editor

# Install dependencies
pip install -r requirements.txt


# Run the Application

bash
python main.py


 📖 Usage
1. Load Image: Click "📂 Load Image" to select a JPEG or PNG file
2. Edit: Use the sliders and controls to adjust:
   - Rotate the image
   - Adjust brightness and contrast
   - Modify saturation
   - Flip horizontally or vertically
3. Save: 
   - Click "💾 Save as Image" to export as image format
   - Click "📄 Save as PDF (A4)" to export as A4 PDF
4. Reset: Click "🔄 Reset" to undo all changes

 🛠️ Technologies Used
- PyQt5 - Cross-platform GUI framework
- Pillow (PIL) - Image processing
- ReportLab - PDF generation

 📁 Project Structure
image-editor/
├── main.py              # Main application
├── requirements.txt     # Dependencies
├── README.md           # Documentation
└── .gitignore          # Git ignore file


 💡 Tips
- A4 PDF automatically scales and centers your image with proper margins
- All edits are non-destructive - use "Reset" to start over
- The editor supports both landscape and portrait images

 📝 License

This project is open source and available under the MIT License.

 🤝 Contributing

Contributions are welcome! Feel free to open issues and pull requests.

 👨‍💻 Author 
Created with ❤️ for image enthusiasts

---

Note: This is a beginner-friendly image editor. For professional image editing, consider GIMP or Photoshop.
