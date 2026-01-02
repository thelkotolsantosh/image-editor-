**#Image Editor - Setup & Usage Guide**

 🔧 Setup Instructions
#Step 1: Install Python
Make sure you have Python 3.7+ installed. Check with:
bash
python --version


#Step 2: Clone or Download
bash
git clone https://github.com/yourusername/image-editor.git
cd image-editor


#Step 3: Create Virtual Environment (Optional but Recommended)
bash
python -m venv venv

#On Windows:
venv\Scripts\activate

#On macOS/Linux:
source venv/bin/activate


#Step 4: Install Dependencies
bash
pip install -r requirements.txt


#Step 5: Run the App
bash
python main.py


 📱 How to Use
1. #Click "Load Image"#- Select a PNG, JPEG, BMP, or GIF file
2. #Edit Your Image#:
   - Use the #Rotate#spinner to rotate (0-360°)
   - Drag #Brightness#slider to lighten/darken
   - Adjust #Contrast#for more vivid colors
   - Control #Saturation#for color intensity
   - Select flip option for mirror effects
3. #Preview#- See changes in real-time
4. #Save Options#:
   - #"💾 Save as Image"#→ Saves as PNG, JPEG, or BMP
   - #"📄 Save as PDF (A4)"#→ Exports as professional A4 PDF

 🎯 Example Workflow


1. Load image → JPEG photo
2. Rotate 15° → Straighten tilted photo
3. Increase brightness 20% → Brighten dark areas
4. Increase contrast 15% → More vivid colors
5. Save as PDF → Get A4 PDF document


 ⚙️ Requirements
- PyQt5 5.15.9 - GUI Framework
- Pillow 10.0.0 - Image Processing
- ReportLab 4.0.7 - PDF Generation

 🐛 Troubleshooting
#"ModuleNotFoundError: No module named 'PyQt5'"
bash
pip install PyQt5


#"Image not loading"
- Make sure the file format is supported (PNG, JPEG, BMP, GIF)
- Check the file path has no special characters

#"PDF export fails"
- Ensure you have write permissions in the save location
- Try a different folder if your current location is read-only


 🎨 Tips for Best Results
- For A4 PDF: Works best with landscape or square images
- High-resolution images process slower but give better quality
- Adjust contrast before saturation for best color results
- Use flip and rotate together for creative effects

 📄 A4 PDF Details
- Page size: 210 × 297 mm (standard A4)
- Margins: 0.5 inches on all sides
- Image auto-scales to fit page while maintaining aspect ratio
- Centered on page for professional appearance

 🚀 Future Enhancements
Possible features to add:
- Crop tool
- Undo/Redo functionality
- Filters (Blur, Sharpen, Sepia)
- Batch processing
- Image merging


#Happy Editing! 📸#
