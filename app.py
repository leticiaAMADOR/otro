import web 
import csv

render = web.template.render('templates/', base = 'base')

urls = ('/', 'index' )
app = web.application(urls, globals())


datos=[]
with open('imss.csv','r') as file:
        data = csv.reader(file,delimiter=",")
        for row in data:
        
              datos.append(row)


class index:  
    def GET(self):      
        dato=datos
        return render.index(dato) 


if __name__=="__main__": 
    app.run()