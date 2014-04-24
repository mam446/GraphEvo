
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("parseTree",["parseTree.pyx"]),
                   Extension("random",["random.pyx"]),
                   Extension("copy",["copy.pyx"]),
                   Extension("genNode",["genNode.pyx"]),
                   Extension("selectionNodes",["selectionNodes.pyx"]),
                   Extension("setNodes",["setNodes.pyx"]),
                   Extension("settings",["settings.pyx"]),
                   Extension("termNodes",["termNodes.pyx"]),
                   Extension("funcs", ["funcs.pyx"])]
)
