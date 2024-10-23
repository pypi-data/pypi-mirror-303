"""
A list of image list loading strategies
"""
from dataclasses import dataclass
from functools import wraps, partial
from pathlib import Path

from PyQt5.QtWidgets import QWidget

ALIGNMENT_SHIFT = 1


def verify_everything_required_exists(self):
    """
    verifies that all properties, attributes and methods in a given class
    that were expected exist
    """
    if not self:
        raise ValueError("Need a MainWindow to use this function")
    if not (hasattr(self, 'file_list_widget') and self.file_list_widget):
        raise ValueError("Need a MainWindow to use this function")
    if not (hasattr(self, 'get_full_img_path') and self.get_full_img_path):
        raise ValueError("Need a MainWindow to use this function")
    if not (hasattr(self, 'cur_img_idx') and self.cur_img_idx):
        raise ValueError("Need a MainWindow to use this function")



def maintain_index(func):

    @wraps(func)
    def wrapper(self):
        # verify_everything_required_exists(self)

        current_index = self.cur_img_idx

        result = func(self)

        self.cur_img_idx = min(current_index, len(self.file_list_widget) - 1)
        file_list_widget_index = self.cur_img_idx + ALIGNMENT_SHIFT
        item = self.file_list_widget.item(file_list_widget_index)
        img_path = self.get_full_img_path(item.text())
        self.load_file(img_path)

        return result

    return wrapper


def maintain_file_position(func):
    """
    Finds the location of the file that is currently loaded in the editing window.
    This is done so that we can find the corresponding image in the new image list.
    
    How it works: 
    - get the current index
    - align the current index with the widget
    - get the item at that index
    - clean the item of emojis and superfluous text to get the relative path.
    - Join the common image directory with the relative path
    - Store the path to the current image
    
    - Run the operation
    
    - Reverse engineer your way back to whatever the original index format was
    - loop through the image list to find the corresponding text that lies at that file location
    - load that file
    
    :param func: The function/operation to be decorated
    :return: The decorated function
    """

    @wraps(func)
    def wrapper(self):
        # verify_everything_required_exists(self)

        cur_img_idx = self.cur_img_idx if self.cur_img_idx else 0
        cur_img_idx += ALIGNMENT_SHIFT

        if not self.m_img_list:
            result = func(self)
            self.load_file(self.m_img_list[self.cur_img_idx])
            return result

        item = self.file_list_widget.item(cur_img_idx)
        org_img_path: Path = self.get_full_img_path(item.text())

        result = func(self)

        for idx in range(self.file_list_widget.count()):
            some_item = self.file_list_widget.item(idx)
            some_img_path = self.get_full_img_path(some_item.text())
            if org_img_path == some_img_path:
                self.load_file(some_img_path)
                break
        else:
            logger.info("previous image was not found and could not be loaded")

        return result

    return wrapper



img_lst_pos_maintainer_factory = {
    "maintain_index": maintain_index,
    "maintain_file_position": maintain_file_position
}
