from PySide.QtGui import *
from PySide.QtCore import *
import sys


class CTab(QTabWidget):
	def __init__(self,parent=None):
		super(CTab,self).__init__(parent)
		bar=CTabBar(self)
		self.setTabBar(bar)


class CTabBar(QTabBar):
	def __init__(self,parent=None):
		super(CTabBar,self).__init__(parent)
		self.setStyle(QStyleFactory.create('Windows'))

	def paintEvent(self,event):
		"""Override paintEvent to draw the tabs like we want to."""
		print "here"
		p = QStylePainter(self)
		tab = QStyleOptionTab()
		tab.initFrom(self)
		selected = self.currentIndex()
		for idx in range(self.count()):
			self.initStyleOption(tab, idx)
			if idx == 0:
				bg_color = QColor('#ADEBFF')
				fg_color = QColor('black')
			elif idx == 1:
				bg_color = QColor('#6CBED2')
				fg_color = QColor('black')
			elif idx == 2:
				bg_color = QColor('#0099CC')
				fg_color = QColor('black')
			elif idx == 3:
				bg_color = QColor('#297ACC')
				fg_color = QColor('black')
			elif idx == 4:
				bg_color = QColor('#006BB2')
				fg_color = QColor('black')
			elif idx == 5:
				bg_color = QColor('#003D7A')
				fg_color = QColor('black')
			p.setBrush(bg_color)
			tab.palette.setColor(QPalette.Window, bg_color)
			tab.palette.setColor(QPalette.WindowText, fg_color)
			p.drawControl(QStyle.CE_TabBarTab, tab)


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__(None)
		self.resize(400,600)
		self.central=QWidget(self)
		self.layout=QHBoxLayout(self.central)
		self.tabwidget=CTab(self.central)
		self.tabwidget.setContextMenuPolicy(Qt.ActionsContextMenu)
		self.tabwidget.setLayoutDirection(Qt.LeftToRight)
		self.tab_1=QWidget()
		self.tabwidget.addTab(self.tab_1,"text")
		self.tab_2=QWidget()
		self.tabwidget.addTab(self.tab_2,"text")
		self.tab_3=QWidget()
		self.tabwidget.addTab(self.tab_3,"text")
		self.layout.addWidget(self.tabwidget)
		self.setCentralWidget(self.central)


if __name__=='__main__':
	app=QApplication(sys.argv)
	win=MainWindow()
	win.show()
	app.exec_()
	sys.exit(0)
