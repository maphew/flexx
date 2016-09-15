"""
Simple example:

.. UIExample:: 100
    
    with ui.GroupWidget(title='This is a panel'):
        with ui.VBox():
            ui.ProgressBar(value=0.2)
            ui.Button(text='click me')


Interactive example:

.. UIExample:: 100

    from flexx import app, ui, event
    
    class Example(ui.GroupWidget):
        def init(self):
            self.title = 'A silly panel'
            with ui.VBox():
                ui.ProgressBar(value=0.2)
                self.but = ui.Button(text='click me')
        
        class JS:
            @event.connect('but.mouse_down')
            def _change_group_title(self, *events):
                self.title = self.title + '-'

"""

from ... import event
from ...pyscript import window
from . import Widget


class GroupWidget(Widget):
    """ Widget to collect widgets in a named group. 
    
    It does not provide a layout. This is similar to a QGroupBox or an
    HTML fieldset.
    """
    
    class JS:
        
        def _init_phosphor_and_node(self):
            node = window.document.createElement('fieldset')
            self.phosphor = window.phosphor.ui.panel.Panel({'node': node})
            
            self._legend = window.document.createElement('legend')
            self.phosphor.node.appendChild(self._legend)
            
            self.node = self.phosphor.node
        
        @event.connect('children')
        def _keep_legend_up(self, *events):
            if len(self.children):
                first = self.children[0].outernode
                self.node.insertBefore(self._legend, first)
        
        @event.connect('title')
        def _title_changed(self, *events):
            self._legend.innerHTML = self.title
