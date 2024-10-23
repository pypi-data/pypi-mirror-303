from .utils import *
from .models import BaseDetectModel, BaseObjectDetect


class ObjectDetectModel(BaseDetectModel):
    def __init__(self, device):
        super(ObjectDetectModel, self).__init__(device)
        self.model = create(self.rules_dict.detect_mode,(self.rules_dict, device))


class ObjectDetect(BaseObjectDetect):
    def __init__(self, device):
        super(ObjectDetect, self).__init__(device)
        self.detect = ObjectDetectModel(device)