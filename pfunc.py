def main(filename):
	f = open(filename, 'r')
	list1 = f.readlines()
	# len(list1)
	for i in range(0, len(list1)):
		if 'TypeDefIndex' in list1[i] and 'class' in list1[i]:
			listname = list1[i].split(" ")
			namecount=0
			lastname=''
			for iname in range(0,len(listname)):
				if listname[iname] == 'class':
					nowclass=listname[iname+1]
					break
		elif '(' in list1[i]:
			listname = list1[i].split(" ")
			for iname in range(0,len(listname)):
				if '(' in listname[iname]:
					functionname= listname[iname].split("(")[0]
					functionname=nowclass+'_'+functionname
					functionname=functionname.replace('.','0')
					functionname=functionname.replace('<','$')
					functionname=functionname.replace('>','$')
					
					if functionname in lastname:
						functionname=functionname+str(namecount)
						namecount=namecount+1
					lastname=functionname
			if '0x1' in listname[len(listname)-1]:
				functionaddr=listname[len(listname)-1]
				rev = MakeNameEx(int(functionaddr,16),functionname,SN_NOWARN)
			print functionname,functionaddr
