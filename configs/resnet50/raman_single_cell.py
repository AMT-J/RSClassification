_base_ = [
    '../_base_/models/resnet50/single_cell_resnet.py', '../_base_/datasets/raman_single_cell.py',
    '../_base_/schedules/raman_bs128.py', '../_base_/default_runtime.py'
]

work_dir = '50single_cell_resnet'
