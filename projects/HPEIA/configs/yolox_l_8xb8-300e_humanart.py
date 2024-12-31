_base_ = ['mmdet::yolox/yolox_l_8xb8-300e_coco.py']


model = dict(bbox_head=dict(num_classes=1))

data_root = '../data/'
train_dataloader = dict(
    dataset=dict(
        dataset=dict(
            data_root=data_root,
            ann_file='HumanArt/annotations/training_humanart_coco.json',
            data_prefix=dict(img='')))
)
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        ann_file='HumanArt/annotations/validation_humanart_coco.json',
        data_prefix=dict(img=''))
)
test_dataloader = val_dataloader

val_evaluator = dict(
    ann_file=f'{data_root}HumanArt/annotations/validation_humanart_coco.json')
test_evaluator = val_evaluator
