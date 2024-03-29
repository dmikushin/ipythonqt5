import os
from PyQt5.QtWidgets import *

# Import the console machinery from ipython
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager
from IPython.lib import guisupport

class QJupyterWidget(RichJupyterWidget):
    """ Convenience class for a live IPython console widget. We can replace the standard banner using the customBanner argument"""
    def __init__(self,customBanner=None,*args,**kwargs):
        if not customBanner is None: self.banner=customBanner
        super(QJupyterWidget, self).__init__(*args,**kwargs)
        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel()
        kernel_manager.kernel.gui = 'qt4'
        self.kernel_client = kernel_client = self._kernel_manager.client()
        kernel_client.start_channels()

        def stop():
            kernel_client.stop_channels()
            kernel_manager.shutdown_kernel()
            guisupport.get_app_qt4().exit()            
        self.exit_requested.connect(stop)

    def pushVariables(self,variableDict):
        """ Given a dictionary containing name / value pairs, push those variables to the IPython console widget """
        self.kernel_manager.kernel.shell.push(variableDict)
    def clearTerminal(self):
        """ Clears the terminal """
        self._control.clear()    
    def printText(self,text):
        """ Prints some plain text to the console """
        self._append_plain_text(text)        
    def executeCommand(self,command):
        """ Execute a command in the frame of the console widget """
        self._execute(command,False)


class ExampleWidget(QWidget):
    """ Main GUI Widget including a button and IPython Console widget inside vertical layout """
    def __init__(self, parent=None):
        super(ExampleWidget, self).__init__(parent)
        layout = QVBoxLayout(self)
        self.button = QPushButton('Another widget')
        jupyterConsole = QJupyterWidget(customBanner="Welcome to the embedded Jupyter console\n")
        layout.addWidget(self.button)
        layout.addWidget(jupyterConsole)
        # This allows the variable foo and method print_process_id to be accessed from the ipython console
        jupyterConsole.pushVariables({"foo":43,"print_process_id":print_process_id})
        jupyterConsole.printText("The variable 'foo' and the method 'print_process_id()' are available. Use the 'whos' command for information.")

def print_process_id():
    print("Process ID is: %d" % os.getpid())

def main():
    app  = QApplication([])
    widget = ExampleWidget()
    widget.show()
    app.exec_()    

if __name__ == '__main__':
    main()

