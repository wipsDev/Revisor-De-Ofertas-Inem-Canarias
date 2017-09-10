#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from heapq import merge


#Tutoriales interesantes
#http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/









#Para extraer todos los links de la web

#for link in soup.find_all('a'):
#    print(link.get('href'))


# Extrae el numero de Ofertas totales que tiene la pagina, pero no se puede utilizar porque no muestra el numero real de ofertas (Error reportado)

#A = soup.find('div', attrs={'class': 'leftPagingContainer'}) # Busca Por id de la clase
#A = A.text.split(" ")[8]
#A = int(A.replace(".", ""))
#OfertasHoy = A
#Paginas=OfertasHoy/10
#print Paginas

#Detecta la ultima pagina de la que se pueden extraer datos






def Detectandopaginas():
	Pag=1

	while True:
		
			
		try:
			url="http://www3.gobiernodecanarias.org/empleo/portal/web/sce/servicios/ofertas?page=" + str(Pag) 
			
			#print url


			r = requests.get(url)
			r = r.content
			soup = BeautifulSoup(r, "lxml")
			soup = soup.body.div

			B = soup.find('div', attrs={'class': 'contenedorSinResultados'})
			B = B.encode("utf-8").split("\n")[1]
				
			if B == "No hay ningún registro.":
				#print url
				break

				

		except:
			A=1

		Pag=Pag+1
			
	#print "Las paginas llegan hasta " + str(Pag)
	return Pag+1
	

# Detectandopaginas()






def ExtraerPuestosPrimerNivel(url):
	
	r = requests.get(url)
	r = r.content
	soup = BeautifulSoup(r, "lxml")
	soup = soup.body.div

	
	
	soup = soup.table


	soup = soup.find_all(title=True)
	
	x=0
	while True:
		print "###############"
		soup1 = soup[x]

		EnlaceAOferta = soup1['href']
		DescripcionOferta = soup1['title'].encode('utf-8')



		soup1 = str(soup1).split('>')
		soup1 = soup1[1]
		soup1 = soup1.split('\n')
		soup1 = soup1[0]
		soup1 = soup1.split(' - ')
		NumeroOferta=soup1[0]
		Puesto=soup1[1]



		#print DescripcionOferta
		#print EnlaceAOferta
		#print NumeroOferta
		#print Puesto



		list1 = [EnlaceAOferta,EnlaceAOferta,NumeroOferta,Puesto]
		list2 = DetalleOferta(EnlaceAOferta)
		

		list1.extend(list2)
		ListaFinal = list1


		
		print ListaFinal


		


		x=x+1
		if x == 10:
			print "###############"
			print
			break



def DetalleOferta(enlace):

	#enlace = "/empleo/portal/web/sce/servicios/ofertas/ofertas_empleo/05.2017.003211"

	url = "http://www3.gobiernodecanarias.org/" + enlace




	r = requests.get(url)
	r = r.content

	soup = BeautifulSoup(r, "lxml")
	soup = soup.body.div



	#Titulo de oferta

	B = soup.find('span', attrs={'class': 'listbox_title listbox_blue'})
	B = B.encode("utf-8").split(">")[1]
	TituloOferta = B.split("<")[0]



	B = soup.table
	B = B.encode("utf-8").split("\n")


	# Primera tabla
	CodigoOferta = B [10].replace("	","")
	Localizacion = B [18].replace("	","")
	FPublicacion = B [26].replace("	","")
	Puestos = B [34].replace("	","")



	B = soup.find_all('td')


	# Segunda Tabla
	ProcedeETT = 		B [9].string.replace("\t","").replace('\r\n', '')
	soloDisca= 			B [11].string.replace("\t","").replace('\r\n', '')


	# Tercera Tabla
	NivelProfesional = 	B [13].encode("utf-8").replace("\t","").replace('\r\n', '').strip("<td>").strip("</td>")
	Experiencia = 		B [15].encode("utf-8").replace("\t","").replace('\r\n', '').strip("<td>").strip("</td>")
	NivelAcademico = 	B [17].encode("utf-8").replace("\t","").replace('\r\n', '').strip("<td>").strip("</td>")
	Titulacion = 		B [19].encode("utf-8").replace("\t","").replace('\r\n', '').strip("<td>").strip("</td>")
	Idiomas = 			B [21].encode("utf-8").replace("\t","").replace('\r\n', '').strip("<td>").strip("</td>")
	ConInformatica = 	B [24].encode("utf-8").replace("\t","").replace('\r\n', '').strip("<td>").strip("</td>")
	OtrosCon = 			B [26].encode("utf-8").replace("\t","").replace('\r\n', '').strip("<td>").strip("</td>")
	CertProfe = 		B [28].encode("utf-8").replace("\t","").replace('\r\n', '').strip("<td>").strip("</td>")
	PermisoConducir = 	B [30].encode("utf-8").replace("\t","").replace('\r\n', '').strip("<td>").strip("</td>")
	InfoAdicional = 	B [32].encode("utf-8").replace("\t","").replace('\r\n', '').strip("<td>").strip("</td>")


	DatosPuesto=[TituloOferta,CodigoOferta,Localizacion,FPublicacion,Puestos,ProcedeETT,soloDisca,NivelProfesional,Experiencia,NivelAcademico,Titulacion,Idiomas,ConInformatica,OtrosCon,CertProfe,PermisoConducir,InfoAdicional]

	return DatosPuesto




	A=0
	for x in DatosPuesto:
		DatosPuesto[A]=str(DatosPuesto[A])
		print str(A) + " " +  str(x)
		A = A+1




"""
A=0
for x in B:
	print str(A) + " " +  str(x)
	A = A+1
"""















# Inicio

NumeroDePaginas = Detectandopaginas()



for x in range(NumeroDePaginas):
	print x

	url='http://www3.gobiernodecanarias.org/empleo/portal/web/sce/servicios/ofertas?page=' + str(x)
	print url




	try:
		ExtraerPuestosPrimerNivel(url)
	except:
		pass
	

