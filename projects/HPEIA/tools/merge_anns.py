import os
import json


force_reload = True


def join_path(path, *args):
    return os.path.abspath(os.path.join(path, *args))


project_dir = join_path(os.path.dirname(os.path.abspath(__file__)), '..')
data_dir = join_path(project_dir, '../../../data')
joint_dir = join_path(data_dir, "joint")

if not os.path.exists(joint_dir):
    os.makedirs(joint_dir)

if not os.path.exists(join_path(joint_dir, "train_bpd_humanart_coco.json")) or force_reload:
    with open(join_path(data_dir, "bizarre_pose/bizarre_pose_dataset/preprocessed/ann_train.json")) as f:
        bpd = json.loads(f.read())
    with open(join_path(data_dir, "HumanArt/annotations/training_humanart_coco.json")) as f:
        humanart = json.loads(f.read())
    with open(join_path(joint_dir, "train_bpd_humanart_coco.json"), "w") as f:
        f.write(json.dumps({
                "categories": humanart["categories"],
                "images": humanart["images"] + bpd["images"],
                "annotations": humanart["annotations"] + bpd["annotations"],
                }))

if not os.path.exists(join_path(joint_dir, "train_bpd_humanart_cartoon.json")) or force_reload:
    with open(join_path(data_dir, "bizarre_pose/bizarre_pose_dataset/preprocessed/ann_train.json")) as f:
        bpd = json.loads(f.read())
    with open(join_path(data_dir, "HumanArt/annotations/training_humanart_cartoon.json")) as f:
        humanart = json.loads(f.read())
    with open(join_path(joint_dir, "train_bpd_humanart_cartoon.json"), "w") as f:
        f.write(json.dumps({
                "categories": humanart["categories"],
                "images": humanart["images"] + bpd["images"],
                "annotations": humanart["annotations"] + bpd["annotations"],
                }))
if not os.path.exists(join_path(joint_dir, "val_bpd_humanart_coco.json")) or force_reload:
    with open(join_path(data_dir, "bizarre_pose/bizarre_pose_dataset/preprocessed/ann_val.json")) as f:
        bpd = json.loads(f.read())
    with open(join_path(data_dir, "HumanArt/annotations/validation_humanart_coco.json")) as f:
        humanart = json.loads(f.read())
    with open(join_path(joint_dir, "val_bpd_humanart_coco.json"), "w") as f:
        f.write(json.dumps({
                "categories": humanart["categories"],
                "images": humanart["images"] + bpd["images"],
                "annotations": humanart["annotations"] + bpd["annotations"],
                }))

if not os.path.exists(join_path(joint_dir, "val_bpd_humanart_cartoon.json")) or force_reload:
    with open(join_path(data_dir, "bizarre_pose/bizarre_pose_dataset/preprocessed/ann_val.json")) as f:
        bpd = json.loads(f.read())
    with open(join_path(data_dir, "HumanArt/annotations/validation_humanart_cartoon.json")) as f:
        humanart = json.loads(f.read())
    with open(join_path(joint_dir, "val_bpd_humanart_cartoon.json"), "w") as f:
        f.write(json.dumps({
                "categories": humanart["categories"],
                "images": humanart["images"] + bpd["images"],
                "annotations": humanart["annotations"] + bpd["annotations"],
                }))
if not os.path.exists(join_path(joint_dir, "test_bpd_humanart_coco.json")) or force_reload:
    with open(join_path(data_dir, "bizarre_pose/bizarre_pose_dataset/preprocessed/ann_test.json")) as f:
        bpd = json.loads(f.read())
    with open(join_path(data_dir, "HumanArt/annotations/validation_humanart_coco.json")) as f:
        humanart = json.loads(f.read())
    with open(join_path(joint_dir, "test_bpd_humanart_coco.json"), "w") as f:
        f.write(json.dumps({
                "categories": humanart["categories"],
                "images": humanart["images"] + bpd["images"],
                "annotations": humanart["annotations"] + bpd["annotations"],
                }))

if not os.path.exists(join_path(joint_dir, "test_bpd_humanart_cartoon.json")) or force_reload:
    with open(join_path(data_dir, "bizarre_pose/bizarre_pose_dataset/preprocessed/ann_test.json")) as f:
        bpd = json.loads(f.read())
    with open(join_path(data_dir, "HumanArt/annotations/validation_humanart_cartoon.json")) as f:
        humanart = json.loads(f.read())
    with open(join_path(joint_dir, "test_bpd_humanart_cartoon.json"), "w") as f:
        f.write(json.dumps({
                "categories": humanart["categories"],
                "images": humanart["images"] + bpd["images"],
                "annotations": humanart["annotations"] + bpd["annotations"],
                }))
