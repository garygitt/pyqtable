class table:
	class snort:
		def get_parameters(self,target_table):
			val =  str( target_table.item( target_table.currentRow() , target_table.currentColumn() ).text() )
			key = str( target_table.horizontalHeaderItem ( target_table.currentColumn() ).text() )
			try:
				key = int( str(key) )
			except Exception as err:
				key = str( key )
			try:
				val = int( str(val) )
			except Exception as err:
				val = str( val )
			return key,val
		def fin(self,target_table,key,val,cols,data):
			out=[]
			for line in data:
				lne = []
				if line[key] == val:
					for c in cols:
						lne.append( line[c] )
				if len(lne) > 0:
					out.append( tuple(lne) )
			return out
		def dictify_data(self,target_table):
			out=[];cols=[]
			rowz = int( target_table.rowCount() ); columnz = int( target_table.columnCount() )
			for row in range(rowz):
				data={}
				for column in range(columnz):
					cname =  target_table.horizontalHeaderItem(column).text(); 
					val = target_table.item(row,column).text()
					try:
						cname = int( str(cname) )
					except Exception as err:
						cname = str( cname )
					try:
						val = int( str(val) )
					except Exception as err:
						val=str( val )
					if row == 0: 
						cols.append( cname )
					data[cname]=val
				out.append(data)
			return cols,out
	@classmethod
	def sort(self,table_sender):
		key, val = self.snort().get_parameters(table_sender);
		cols, data = self.snort().dictify_data(table_sender)
		out = self.snort().fin(table_sender,key,val,cols,data)
		self.load(table_sender,out,cols,order=0,col=0)
	@classmethod
	def load(self,tabel,data,cols,**order_col):
		if order_col:
			if order_col['order']:
				sortorder =  order_col['order']
			else:
				sortorder = 0
			if order_col['col']:
				sortcol = order_col['col']
			else:
				sortcol = 0
		def intt(num):
			item = QTableWidgetItem(); item.setData(Qt.EditRole, num)
			return item
		tabel.clearContents(); 
		tabel.setSortingEnabled(False)
		tabel.setRowCount(len(data)); 
		if len(data) == 0: 
			return False
		tabel.setColumnCount(len(data[0]))
		for hn, h in enumerate(cols):
			tabel.setHorizontalHeaderItem(hn,QTableWidgetItem( str(h) ))
		for nr,row in enumerate(data):
			for itc, it in enumerate(row):
				if isinstance(it,int) or isinstance(it,long): 
					tabel.setItem(nr,itc, intt(it))
				else: 
					tabel.setItem(nr,itc, QTableWidgetItem( str(it) ))
		tabel.setSortingEnabled(True)
		tabel.sortItems(sortcol,sortorder)
