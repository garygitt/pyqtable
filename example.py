#TABLE LOAD
self.table_data = QtGui.QTableView()
cols=['rowid','data']
data = [(1,'data1'),(2,'data2'),]
table.load(self.table_data,data,cols,order=0,col=0)

#TABLE SORT
# must set context menu poicy in property editor
def context(self,pos):
		mainmenu = QtGui.QMenu("Menu", self)
		mainmenu.addAction("Sort")
		
		C =  self.mapFromGlobal(QCursor.pos())
		pos.setY(C.y()); pos.setX(C.x())
		action  = mainmenu.exec_(self.mapToGlobal(pos))
		
		if action.text() == 'Sort':
			table.sort(self.sender())
			

