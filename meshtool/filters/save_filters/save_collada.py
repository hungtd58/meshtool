from meshtool.args import *
from meshtool.filters.base_filters import *
import os

def FilterGenerator():
    class ColladaSaveFilter(SaveFilter):
        def __init__(self):
            super(ColladaSaveFilter, self).__init__('save_collada', 'Saves a collada file')
        def apply(self, mesh, filename):
            if os.path.exists(filename):
                raise FilterException("specified filename already exists")
            print "SAVING FILE"
            mesh.write(filename)
            return mesh
    return ColladaSaveFilter()
