#!/usr/bin/env python
# coding: utf-8

from ipywidgets import DOMWidget
from traitlets import Unicode
from ._frontend import module_name, module_version


class WebGL(DOMWidget):
    _model_name = Unicode('WebGLModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('WebGLView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    # value = Unicode('Hello World').tag(sync=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._resources = []
        self._commands = []
        self._buffers = []
    def refresh(self):
        self.send({'commands':self._commands}, buffers=self._buffers)
        self._commands = []
        self._buffers  = []
    def clear_color(self, r:float, g:float, b:float, a:float):
        """Append a clearColor command to the commands buffer.

        Args:
            r (float): red [0, 1]
            g (float): green [0, 1]
            b (float): blue [0, 1]
            a (float): alpha [0, 1]
        """
        self._commands.append({
            'cmd':'clearColor', 
            'r':float(r), 
            'g':float(g), 
            'b':float(b), 
            'a':float(a)
        })
    def clear(self, color_bit_buffer=True, depth_buffer_bit=True, stencil_buffer_bit=False):
        """Append a clear command to the commands buffer.
        
        Args:
            color_bit_buffer (bool, optional): clear the depth buffer. Defaults to True.
            depth_buffer_bit (bool, optional): clear the color buffer. Defaults to True.
            stencil_buffer_bit (bool, optional): clear the stencil buffer.  Defaults to False.
        """
        self._commands.append({
            'cmd':'clear', 
            'depth':color_bit_buffer, 
            'color':depth_buffer_bit, 
            'stencil':stencil_buffer_bit
        })
    def hello_world(self):
        self._commands.append({
            'cmd': 'helloWorld'
        })
