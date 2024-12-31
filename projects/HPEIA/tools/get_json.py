import os
import json
import pickle

force_reload = True
category_mapping = {
    0: 1
}


def join_path(path, *args):
    return os.path.abspath(os.path.join(path, *args))


project_dir = join_path(os.path.dirname(os.path.abspath(__file__)), '..')
results_dir = join_path(project_dir, './results')
if os.path.exists(results_dir):
    files = os.listdir(results_dir)
else:
    files = []
pkls = set(pkl for pkl in files if pkl.endswith('.pkl'))
if force_reload:
    jsons = set()
else:
    jsons = set(json for json in files if json.endswith('.json'))

for pkl in pkls:
    if f'{pkl[:-4]}.json' not in jsons:
        pkl = join_path(results_dir, pkl)
        detections = []
        with open(pkl, 'rb') as f:
            imgs = pickle.load(f)
        for img in imgs:
            img_id, instances = img['img_id'], img['pred_instances']
            bboxes, labels, scores = \
                instances['bboxes'].tolist(), \
                instances['labels'].tolist(), \
                instances['scores'].tolist()
            for bbox, label, score in zip(bboxes, labels, scores):
                detections.append({
                    'bbox': bbox,
                    'category_id': category_mapping[label],
                    'image_id': img_id,
                    'score': score
                })
        with open(f'{pkl[:-4]}.json', "w") as f:
            json.dump(detections, f)
        pass
