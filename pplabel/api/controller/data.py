import json
import os
import os.path as osp
import base64

import cv2
import flask

from pplabel.config import db
from .base import crud
from ..model import Data, Project, Task
from ..schema import DataSchema
from pplabel.api.util import abort


get_all, get, post, put, delete = crud(Data, DataSchema)


# TODO: dont use flask
def get_image(data_id):
    if data_id is None:
        abort("Have to provide data_id")
    data = Data._get(data_id=data_id)
    if data is None:
        abort(f"Data with data_id {data_id} doesn't exist")
    path = data.path
    project_id = data.task.project_id
    data_dir = Project._get(project_id=project_id).data_dir
    return flask.send_from_directory(data_dir, path)

    # data_path = osp.join(data_dir, path)
    # image = cv2.imread(data_path)
    # image_png = cv2.imencode(".png", image)
    # b64_string = base64.b64encode(image_png[1]).decode("utf-8")
    # return json.dumps({"image": b64_string}), 200


def get_by_task(task_id):
    Task._exists(task_id)
    datas = Data._get(task_id=task_id, many=True)
    return DataSchema(many=True).dump(datas), 200
