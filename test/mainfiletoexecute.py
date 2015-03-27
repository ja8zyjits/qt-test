from mainwindow import Ui_MainWindow
from PySide.QtGui import *
from PySide.QtCore import *
import sys

class EventEvaluator(QObject):
	def eventFilter(self,obj,event):
		if event.type()==QEvent.Paint:
			p=QStylePainter(obj)
			tab=QStyleOptionTabV3()
			for idx in range(obj.count()):
				obj.initStyleOption(tab,idx)
				if idx==0:
					bg_color=QColor("#ADEBFF")
					fg_color=QColor('black')
				elif idx==1:
					bg_color=QColor("#6CBED2")
					fg_color=QColor('black')
				elif idx==2:
					bg_color=QColor("#0099CC")
					fg_color=QColor('black')
				tab.palette.setColor(QPalette.Window,bg_color)
				tab.palette.setColor(QPalette.WindowText,fg_color)
				p.drawControl(QStyle.CE_TabBarTab,tab)
			return True
		else:
			return QObject.eventFilter(self,obj,event)
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__(None)
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.evn=EventEvaluator()
		self.ob=self.ui.tabWidget.tabBar()
		print self.ob
		self.ob.installEventFilter(self.evn)

if __name__=='__main__':
	app=QApplication(sys.argv)
	win=MainWindow()
	win.show()
	app.exec_()
	sys.exit(0)
