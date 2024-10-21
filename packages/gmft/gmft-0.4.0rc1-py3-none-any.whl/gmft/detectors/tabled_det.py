import io
import pandas as pd
from tabled.extract import extract_tables
from tabled.fileinput import load_pdfs_images
from tabled.inference.models import load_detection_models, load_recognition_models
from tabled.formats import formatter

det_models, rec_models = load_detection_models(), load_recognition_models()
# det models: EfficientViTForSemanticSegmentation, SegformerImageProcessor, EfficientViTForSemanticSegmentation, SegformerImageProcessor
# rec models: TableRecEncoderDecoderModel, SuryaProcessor, OCREncoderDecoderModel, SuryaProcessor
images, highres_images, names, text_lines = load_pdfs_images('support_arena/spantest.pdf') # (instant)
# images: list[PIL.Image.Image] 816x1056
# highres_images: list[PIL.Image.Image] 1632x2112
# names: list[str]
# text_lines: list[dict] one for each image (page)
# [{'blocks': [...], 'page': 0, 'rotation': 0, 'bbox': [...], 'width': 612, 'height': 792}]
# text_lines[#].blocks[#] = {'bbox': (156.4, 72.9, 438.6, 81.8), 'lines': LinesDict}
# LinesDict = [{'bbox': list[4], 'spans': [
# {'chars': [{'char': 'T', 'bbox': BBox}], 
# 'font': {'size': float, 'weight': float, 'name': str, 'flags': int},
# 'rotation': float,
# 'bbox': Bbox,
# 'text': str,
# 'char_start_idx': int,
# 'char_end_idx': int
# }
# ]}]

# note that the priority is as follows:
# 1. if the 


pnums = []
prev_name = None
for i, name in enumerate(names):
    if prev_name is None or prev_name != name:
        pnums.append(0)
    else:
        pnums.append(pnums[-1] + 1)

    prev_name = name
    
page_results = extract_tables(images, highres_images, text_lines, det_models, rec_models)

# print(page_results)

for name, pnum, result in zip(names, pnums, page_results):
    for i in range(result.total):
        page_cells = result.cells[i]
        page_rc = result.rows_cols[i]
        img = result.table_imgs[i]

        # base_path = os.path.join(out_folder, name)
        # os.makedirs(base_path, exist_ok=True)

        formatted_result, ext = formatter('csv', page_cells)
        df = pd.read_csv(io.StringIO(formatted_result))
        
        base_name = f"page{pnum}_table{i}"

# https://github.com/VikParuchuri/tabled/blob/master/extract.py