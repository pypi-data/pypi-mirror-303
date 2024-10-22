import hcs_core.ctxp.data_util as data_util
from os import path
from hcs_core.plan import PlanException
import logging

log = logging.getLogger(__name__)

_template_dir = path.abspath(path.join(path.dirname(__file__), "templates"))


def get(name: str, raise_on_not_found: bool = True):
    file_name = path.join(_template_dir, name)
    ret = data_util.load_data_file(file_name)

    if raise_on_not_found and not ret:
        log.error("Template path: " + file_name)
        raise PlanException("Template not found: " + name)
    return ret
