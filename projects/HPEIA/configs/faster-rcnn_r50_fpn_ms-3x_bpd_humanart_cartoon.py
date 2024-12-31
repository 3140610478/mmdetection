_base_ = ['mmdet::faster_rcnn/faster-rcnn_r50_fpn_ms-3x_coco.py']


model = dict(
    roi_head=dict(bbox_head=dict(num_classes=1)),
    init_cfg=dict(
        type='Pretrained',
        checkpoint="https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_mstrain_3x_coco/faster_rcnn_r50_fpn_mstrain_3x_coco_20210524_110822-e10bd31c.pth",
    )
)

data_root = '../data/'

train_dataloader = dict(
    dataset=dict(
        times=60,
        dataset=dict(
            data_root=data_root,
            ann_file='joint/train_bpd_humanart_cartoon.json',
            data_prefix=dict(img='')))
)
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        ann_file='joint/val_bpd_humanart_cartoon.json',
        data_prefix=dict(img=''))
)
test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        ann_file='joint/val_bpd_humanart_cartoon.json',
        data_prefix=dict(img=''))
)

val_evaluator = dict(
    ann_file=f'{data_root}joint/val_bpd_humanart_cartoon.json')
test_evaluator = val_evaluator