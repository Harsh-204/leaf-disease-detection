import sys
import os
import base64
sys.path.insert(0, os.path.abspath("Leaf Disease"))
from main import LeafDiseaseDetector

try:
    with open("Media/brown-spot-4 (1).jpg", "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    d = LeafDiseaseDetector()
    print("Testing detector...")
    print(d.analyze_leaf_image_base64(b64))
except Exception as e:
    print("EXCEPTION:", repr(e))
