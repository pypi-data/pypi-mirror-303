try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    # needed for py3+qt4
    # Ref:
    # http://pyqt.sourceforge.net/Docs/PyQt4/incompatible_apis.html
    # http://stackoverflow.com/questions/21217399/pyqt4-qtcore-qvariant-object-instead-of-a-string
    # from PyQt4.QtGui import *
    # from PyQt4.QtCore import *
    pass
from pathlib import Path
from libs.combobox import ComboBox  # noqa
from libs.resources import *  # noqa (VERY IMPORTANT LINE, IMPORTING LINE CAUSES LIBS STRING BUNDLE TO LOAD PROPERLY)
from libs.constants import *  # noqa
from libs.utils import *  # noqa
from libs.settings import Settings  # noqa
from libs.shape import Shape, DEFAULT_LINE_COLOR, DEFAULT_FILL_COLOR  # noqa
from libs.stringBundle import StringBundle  # noqa
from libs.canvas import Canvas  # noqa
from libs.zoomWidget import ZoomWidget  # noqa
from libs.labelDialog import LabelDialog  # noqa
from libs.colorDialog import ColorDialog  # noqa
from libs.labelFile import LabelFile, LabelFileError, LabelFileFormat  # noqa
from libs.toolBar import ToolBar  # noqa
from libs.pascal_voc_io import PascalVocReader  # noqa
from libs.pascal_voc_io import XML_EXT  # noqa
from libs.yolo_io import YoloReader  # noqa
from libs.yolo_io import TXT_EXT  # noqa
from libs.create_ml_io import CreateMLReader  # noqa
from libs.create_ml_io import JSON_EXT  # noqa
from libs.ustr import ustr  # noqa
from libs.hashableQListWidgetItem import HashableQListWidgetItem  # noqa
