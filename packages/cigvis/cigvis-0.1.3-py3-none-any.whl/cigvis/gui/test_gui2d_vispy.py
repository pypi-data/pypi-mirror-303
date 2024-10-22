from PyQt5.QtWidgets import QWidget
import numpy as np

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore, QtGui

from vispy.app import use_app
from vispy import scene
import cigvis
from .custom_widgets import *


CANVAS_SIZE = (800, 600)  # (width, height)

INT_validator = QtCore.QRegExp(r"^[1-9][0-9]*$")
FLOAT_validator = QtCore.QRegExp(r"[-+]?[0-9]*\.?[0-9]+")


class MyMainWindow(qtw.QMainWindow):

    def __init__(self, nx=None, ny=None, clear_dim=True):
        super().__init__()

        self.clear_dim = clear_dim
        self.initUI(nx, ny)

    def initUI(self, nx, ny):
        central_widget = qtw.QWidget()
        self.main_layout = qtw.QHBoxLayout()

        self._controls = Controls2d(nx, ny, self.clear_dim)
        self.main_layout.addWidget(self._controls)
        self._canvas_wrapper = CanvasWrapper2d()
        self.main_layout.addWidget(self._canvas_wrapper.canvas.native)

        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        self._canvas_wrapper.canvas.native.setAcceptDrops(True)
        self._canvas_wrapper.canvas.native.dragEnterEvent = self.handleDragEnterEvent
        self._canvas_wrapper.canvas.native.dropEvent = self.handleDropEvent

        self._connect_controls()

    def handleDragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def handleDropEvent(self, event):
        if len(event.mimeData().urls()) > 1:
            qtw.QMessageBox.critical(self, "Error", "Only support 1 file")
            return
        fpath = event.mimeData().urls()[0].toLocalFile()
        self._controls.load_data(fpath)

    def _connect_controls(self):
        self._controls.data_loaded[list].connect(self._canvas_wrapper.set_data)
        self._controls.colormap_combo.changed.connect(self._set_cmap)
        self._controls.interp_combo.changed.connect(self._set_interp)
        self._controls.vmin_input.editingFinished.connect(
            lambda: self._canvas_wrapper.set_vmin(self._controls.vmin_input.
                                                  text()))
        self._controls.vmax_input.editingFinished.connect(
            lambda: self._canvas_wrapper.set_vmax(self._controls.vmax_input.
                                                  text()))
        self._controls.clear_btn.clicked.connect(self._canvas_wrapper.clear)
        self._controls.clear_btn.clicked.connect(self._controls.clear)

    def _set_cmap(self, cmap):
        try:
            self._canvas_wrapper.set_cmap(cmap)
        except Exception as e:
            qtw.QMessageBox.critical(self, "Error", f"Error colormap: {e}")

    def _set_interp(self, interp):
        try:
            self._canvas_wrapper.set_interp(interp)
        except Exception as e:
            qtw.QMessageBox.critical(self, "Error", f"Error interpolation method: {e}")


class CanvasWrapper2d(qtw.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = None
        self.nodes = None
        self.canvas = scene.SceneCanvas(keys='interactive', bgcolor='white', size=CANVAS_SIZE)
        # self.canvas.events.key_press.connect(self.on_key_press)

    def set_data(self, data):
        self.data = data[0]
        self.view = self.canvas.central_widget.add_view()
        self.view.interactive = False
        self.node = scene.visuals.Image(
            self.data.T, 
            interpolation=data[3], 
            cmap=data[2], 
            clim=data[1],
            parent=self.view.scene, 
        )
        self.view.camera = scene.PanZoomCamera(aspect=1)
        self.view.camera.viewbox.events.mouse_move.disconnect(
            self.view.camera.viewbox_mouse_event)

        # flip y-axis to have correct aligment
        self.view.camera.flip = (0, 1, 0)
        self.view.camera.set_range()
        # app.run()
        
    def set_cmap(self, cmap):
        cmap = cigvis.colormap.cmap_to_vispy(cmap)
        self.node.cmap = cmap

    def set_interp(self, interp):
        self.node.interpolation = interp

    def set_vmin(self, vmin):
        vmin = float(vmin)

        old_clim = self.node.clim
        self.node.clim = [vmin, old_clim[1]]

    def set_vmax(self, vmax):
        vmax = float(vmax)
        old_clim = self.node.clim
        self.node.clim = [old_clim[0], vmax]

    def clear(self):
        self.node.parent = None
        del self.node
        self.nodes = None
        del self.data
        self.data = None



class Controls2d(qtw.QWidget):

    data_loaded = QtCore.pyqtSignal(list)

    def __init__(self, nx=None, ny=None, clear_dim=True, parent=None):
        super().__init__(parent)

        self.clear_dim = clear_dim

        layout = qtw.QVBoxLayout()

        self.loaded = False

        # dimensions
        row1_layout = qtw.QHBoxLayout()
        nx_label = qtw.QLabel('nx:')
        self.nx_input = qtw.QLineEdit()
        self.nx_input.setValidator(QtGui.QRegExpValidator(INT_validator, self))
        if nx is not None:
            self.nx_input.setText(f'{nx}')
        ny_label = qtw.QLabel('ny:')
        self.ny_input = qtw.QLineEdit()
        self.ny_input.setValidator(QtGui.QRegExpValidator(INT_validator, self))
        if ny is not None:
            self.ny_input.setText(f'{ny}')
        self.load_btn = qtw.QPushButton('Load')
        self.addwidgets(row1_layout, [
            nx_label, self.nx_input, ny_label, self.ny_input, self.load_btn
        ])

        # clim
        row2_layout = qtw.QHBoxLayout()
        vmin_label = qtw.QLabel('vmin:')
        self.vmin_input = qtw.QLineEdit()
        self.vmin_input.setValidator(
            QtGui.QRegExpValidator(FLOAT_validator, self))
        vmax_label = qtw.QLabel('vmax:')
        self.vmax_input = qtw.QLineEdit()
        self.vmax_input.setValidator(
            QtGui.QRegExpValidator(FLOAT_validator, self))
        self.addwidgets(
            row2_layout,
            [vmin_label, self.vmin_input, vmax_label, self.vmax_input])

        # colormap
        row3_layout = qtw.QHBoxLayout()
        colormap_label = qtw.QLabel('Colormap:')
        self.colormap_combo = EditableComboBox()
        colormaps = [
            'gray', 'seismic', 'Petrel', 'stratum', 
            'od_seismic1', 'od_seismic2', 'od_seismic3'
        ]
        self.colormap_combo.addItems(colormaps)
        self.colormap_combo.setCurrentText('gray')  # 默认值为'gray'
        self.addwidgets(row3_layout, [colormap_label, self.colormap_combo])


        # interpolation
        row4_layout = qtw.QHBoxLayout()
        interp_label = qtw.QLabel('Interpolation:')
        self.interp_combo = EditableComboBox()
        interps = [
            'nearest', 'linear', 'cubic', 'quadric', 'sinc', 'gaussian',
            'hanning', 'hamming', 
            'hermite', 'kaiser', 'catrom', 'mitchell', 'spline16', 'spline36', 
            'bessel', 'lanczos', 'blackman',
        ]
        self.interp_combo.addItems(interps)
        self.interp_combo.setCurrentText('linear') 
        self.addwidgets(row4_layout, [interp_label, self.interp_combo])



        # update params
        row6_layout = qtw.QHBoxLayout()
        self.clear_btn = qtw.QPushButton('clear')

        self.addwidgets(row6_layout, [self.clear_btn])


        self.addlayout(layout, [row1_layout, row2_layout, row3_layout, 
                                row4_layout, row6_layout])

        layout.addStretch(1)
        self.setLayout(layout)
        self.setMaximumWidth(400)

        self.load_btn.clicked.connect(self.load_data)

    def addwidgets(self, layout, widgets):
        for widget in widgets:
            layout.addWidget(widget)

    def addlayout(self, layout, sublayouts):
        for sublayout in sublayouts:
            layout.addLayout(sublayout)

    def is_set_dim(self):
        if self.nx_input.text() and self.ny_input.text():
            return True
        else:
            return False

    def load_data(self, file_path=None):
        if self.loaded:
            qtw.QMessageBox.critical(self, "Warn",
                                     "Need to click clear to reset")
            return

        if not file_path:
            file_dialog = qtw.QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(self, 'Open Data File',
                                                       '', 'Binary Files (*)')

        if file_path and not self.is_set_dim():
            isnpy = file_path.endswith('npy')
            if not isnpy:
                qtw.QMessageBox.critical(
                    self, "Error", "Please enter values for nx, ny, and nz.")
                return

        if file_path:
            try:
                if file_path.endswith('.npy'):
                    data = np.load(file_path)
                    assert data.ndim ==2 # TODO:
                    self.nx_input.setText(str(data.shape[0]))
                    self.ny_input.setText(str(data.shape[1]))

                nx = int(self.nx_input.text())
                ny = int(self.ny_input.text())
                if not file_path.endswith('.npy'):
                    data = np.fromfile(file_path,
                                       dtype=np.float32).reshape(nx, ny)

                if not self.vmin_input.text():
                    self.vmin_input.setText(f'{data.min():.2f}')
                if not self.vmax_input.text():
                    self.vmax_input.setText(f'{data.max():.2f}')

                self.data_loaded.emit([
                    data,
                    [
                        float(self.vmin_input.text()),
                        float(self.vmax_input.text())
                    ],
                    self.colormap_combo.currentText(),
                    self.interp_combo.currentText(),
                ])
                self.loaded = True
            except Exception as e:
                qtw.QMessageBox.critical(self, "Error",
                                         f"Error loading data: {e}")

    def clear(self):
        if self.clear_dim:
            self.nx_input.clear()
            self.ny_input.clear()
        self.vmin_input.clear()
        self.vmax_input.clear()
        self.colormap_combo.setCurrentText('gray')
        self.interp_combo.setCurrentText('linear')
        self.loaded = False


def gui2d(nx=None, ny=None, clear_dim=True):
    app = use_app("pyqt5")
    app.create()
    win = MyMainWindow(nx, ny, clear_dim)
    win.show()
    app.run()



if __name__ == '__main__':
    app = use_app("pyqt5")
    app.create()
    win = MyMainWindow()
    win.show()
    app.run()