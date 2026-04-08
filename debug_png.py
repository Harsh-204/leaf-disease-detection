import sys, os, base64
from PIL import Image
import io

sys.path.insert(0, os.path.abspath("Leaf Disease"))
from main import LeafDiseaseDetector

try:
    # Create a dummy PNG image in memory
    img = Image.new('RGB', (100, 100), color = 'green')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    png_bytes = img_byte_arr.getvalue()

    b64 = base64.b64encode(png_bytes).decode("utf-8")
    d = LeafDiseaseDetector()
    print("Testing detector with PNG image but JPEG data URL...")
    print(d.analyze_leaf_image_base64(b64))
except Exception as e:
    print("EXCEPTION:", repr(e))
