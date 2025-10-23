import os 
import shutil

def copy_over(current_path,target_path):

    for element in os.listdir(current_path):
        element_path = os.path.join(current_path,element)
        if os.path.isfile(element_path):
            print(shutil.copy(element_path,target_path))
        else:
            os.mkdir(os.path.join(target_path,element))
            return copy_over(element_path,os.path.join(target_path,element))
    return


def copy_and_override(source,target):

    target_path = os.path.abspath(target)

    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    os.mkdir(target_path)

    source_path = os.path.abspath(source)

    copy_over(source_path,target_path)
    pass

