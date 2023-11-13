model = dict(
    type='RamanClassifier',  # Classifier type
    backbone=dict(
        type='ResNetV2',  # Backbone network type
        hidden_sizes=[100] * 10,
        num_blocks=[2] * 10,
        input_dim=1941,
        num_classes=10
    ),
    loss=dict(type='CrossEntropyLoss', loss_weight=1.0),  # Loss function configuration information
)
