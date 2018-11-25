import os
import tkinter

def makeUI():

	tempimg= tkinter.PhotoImage(file=os.path.join('images', 'id.gif'))
	imgtemp = tkinter.Label(image=tempimg)

	#temp image
	tempimg=tkinter.PhotoImage(file=os.path.join('images', 'id.gif'))

	tempweat = tempimg.zoom(3, 3)    #this new image is 3x the original
	tempweat = tempimg.subsample(2,2)

	imgtemp = tkinter.Label(image=tempweat)
	imgtemp.grid(row=0, column=0)

	#temp=tkinter.Label(text='Temp      ', font=("Courier", 28, 'bold'))
	#temp.grid(row=0, column=5)

	#wind image
	windimg=tkinter.PhotoImage(file=os.path.join('images', 'id2.gif'))


	windweat = windimg.zoom(3, 3)    #this new image is 3x the original
	windweat = windimg.subsample(2,2)

	imgwind = tkinter.Label(image=windweat)
	imgwind.grid(row=1, column=0)

	#img ids
	if weatherid=='200':
		print('Rainy Thunderstorm')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id3.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='201':
		print('Rainy Thunderstorm')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id3.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='202':
		print('Rainy Thunderstorm')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id3.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='230':
		print('Rainy Thunderstorm')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id3.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='231':
		print('Rainy Thunderstorm')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id3.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='232':
		print('Rainy Thunderstorm')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id3.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
			#thunderstorm

	if weatherid=='210':
		print('Thunderstorm')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id4.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='211':
		print('Thunderstorm')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id4.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='212':
		print('Thunderstorm')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id4.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='221':
		print('Thunderstorm')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id4.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
			#light rain

	if weatherid=='300':
		print('Light Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id5.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='301':
		print('Light Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id5.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)

	if weatherid=='302':
		print('Light Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id5.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='310':
		print('Light Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id5.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='311':
		print('Light Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id5.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='312':
		print('Light Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id5.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='313':
		print('Light Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id5.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='314':
		print('Light Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id5.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='321':
		print('Light Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id5.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)

			#rain
	if weatherid=='500':
		print('Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id6.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='501':
		print('Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id6.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='502':
		print('Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id6.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='503':
		print('Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id6.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='504':
		print('Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id6.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='511':
		print('Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id6.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='520':
		print('Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id6.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='521':
		print('Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id6.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='522':
		print('Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id6.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='531':
		print('Rain')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id6.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
			#snow
	if weatherid=='600':
		print('Snow')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id7.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='601':
		print('Snow')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id7.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='602':
		print('Snow')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id7.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='620':
		print('Snow')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id7.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='621':
		print('Snow')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id7.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='622':
		print('Snow')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id7.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)

	if weatherid=='611':
		print('Sleet')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id8.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='612':
		print('Sleet')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id8.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='615':
		print('Sleet')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id8.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='616':
		print('Sleet')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id8.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
			#tornado
	if weatherid=='781':
		print('TORNADO')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id9.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='900':
		print('TORNADO')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id9.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
			#sunny
	if weatherid=='800':
		print('Sunny/Clear')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id10.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='951':
	   print('Sunny/Clear')
	   weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id10.gif'))
	   typew = tkinter.Label(image=weathertype)
	   typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		 
			#lightly cloudy
	if weatherid=='801':
		print('Sunny with some clouds')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id11.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		  
			#mid cloudy
	if weatherid=='802':
		print('Cloudy')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id12.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		  
			 #heavy cloudy
	if weatherid=='803':
	   print('Lots of clouds')
	   weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id13.gif'))
	   typew = tkinter.Label(image=weathertype)
	   typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)
		
	if weatherid=='804':
		print('Lots of clouds')
		weathertype = tkinter.PhotoImage(file=os.path.join('images', 'id13.gif'))
		typew = tkinter.Label(image=weathertype)
		typew.grid(row=0, column=6,  columnspan=3, rowspan=2, padx=5, pady=5)

	root.mainloop()
	
def displayUI(data):
    degree_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Weather today in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], degree_symbol, data['sky'])
    print('Min: {}, Max: {}'.format(data['temp_min'], data['temp_max']))
    print('')
    print('Speed of Wind: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Humidity: {}'.format(data['humidity']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('ID for Weather is : {}'.format(data['typeid']))
    print('Last update from the server was : {}'.format(data['dt']))
    print('---------------------------------------')

    global weatherid
    weatherid=('{}'.format(data['typeid']))
    weathertype=('{}'.format(data['wtype']))
    print(weatherid)
    print(weathertype)
    
    weatherdata= (data['wtype'])
    weathid= (data['typeid'])
    wtempid= (data['temp'])
    wwindid= (data['wind'])
    citid= (data['city'])
    countryid= (data['country'])

    print ("-------------------------------")
    # print (str(weathid))
    # print (str(weatherdata))
    # print (str(wtempid) + "°C")
    # print (str(wwindid) + " MPH")
    # print (str(citid) + ", " + str(countryid))

    global root
    root = tkinter.Tk()
	# Controls the size of the window.
    root.geometry('900x515')
    root.title('Weather in:'+ " "  + str(citid) + ", " + str(countryid))

    #temperature
    temp=tkinter.Label(text= str(wtempid)+ "°C    ", font=("Courier", 28, 'bold'))
    temp.grid(row=0, column=5)

    #windspeed
    win=tkinter.Label(text= str(wwindid) + " MPH    ", font=("Courier", 28, 'bold'))
    win.grid(row=1, column=5)

    #weather condition text
    wean=tkinter.Label(text=" "+str(weatherdata), font=("Courier", 28, 'bold')) # make weather update show here
    wean.grid(row=4, column=6)
    makeUI()

