_base_ = ['../../CO-DETR/configs/codino/co_dino_5scale_swin_l_16xb1_16e_o365tococo.py']


# model settings
num_dec_layer = 6
loss_lambda = 2.0
num_classes = 1
model = dict(
    query_head=dict(
        num_classes=num_classes,
    ),
    roi_head=[
        dict(
            type='CoStandardRoIHead',
            bbox_roi_extractor=dict(
                type='SingleRoIExtractor',
                roi_layer=dict(
                    type='RoIAlign', output_size=7, sampling_ratio=0),
                out_channels=256,
                featmap_strides=[4, 8, 16, 32, 64],
                finest_scale=56),
            bbox_head=dict(
                type='Shared2FCBBoxHead',
                in_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=num_classes,
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    target_means=[0., 0., 0., 0.],
                    target_stds=[0.1, 0.1, 0.2, 0.2]),
                reg_class_agnostic=False,
                reg_decoded_bbox=True,
                loss_cls=dict(
                    type='CrossEntropyLoss',
                    use_sigmoid=False,
                    loss_weight=1.0 * num_dec_layer * loss_lambda),
                loss_bbox=dict(
                    type='GIoULoss',
                    loss_weight=10.0 * num_dec_layer * loss_lambda)))
    ],
    bbox_head=[
        dict(
            type='CoATSSHead',
            num_classes=num_classes,
            in_channels=256,
            stacked_convs=1,
            feat_channels=256,
            anchor_generator=dict(
                type='AnchorGenerator',
                ratios=[1.0],
                octave_base_scale=8,
                scales_per_octave=1,
                strides=[4, 8, 16, 32, 64, 128]),
            bbox_coder=dict(
                type='DeltaXYWHBBoxCoder',
                target_means=[.0, .0, .0, .0],
                target_stds=[0.1, 0.1, 0.2, 0.2]),
            loss_cls=dict(
                type='FocalLoss',
                use_sigmoid=True,
                gamma=2.0,
                alpha=0.25,
                loss_weight=1.0 * num_dec_layer * loss_lambda),
            loss_bbox=dict(
                type='GIoULoss',
                loss_weight=2.0 * num_dec_layer * loss_lambda),
            loss_centerness=dict(
                type='CrossEntropyLoss',
                use_sigmoid=True,
                loss_weight=1.0 * num_dec_layer * loss_lambda)),
    ],
)

data_root = '../data/'
metainfo = {
    'classes': ('person', ),
    'palette': [(220, 20, 60),]
}
train_dataloader = dict(
    dataset=dict(
        dataset=dict(
            metainfo=metainfo,
            data_root=data_root,
            ann_file='HumanArt/annotations/training_humanart_coco.json',
            data_prefix=dict(img='')))
)
val_dataloader = dict(
    dataset=dict(
        metainfo=metainfo,
        data_root=data_root,
        ann_file='HumanArt/annotations/validation_humanart_coco.json',
        data_prefix=dict(img=''))
)
test_dataloader = val_dataloader

val_evaluator = dict(
    ann_file=f'{data_root}HumanArt/annotations/validation_humanart_coco.json')
test_evaluator = val_evaluator
