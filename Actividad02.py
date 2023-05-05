import tkinter as tk
class aplication:
    def __init__(Ventana):
        Ventana.box= tk.Tk()
        Ventana.box.grid()
        Ventana.box.title("Actividad 02")
        Ventana.box.resizable(width=0, height=0)
        Ventana.CalculoDD = tk.Label(Ventana.box,text="Convertir DMS a DD").grid(column=0,row=0)
        Ventana.Gralat    = tk.IntVar(Ventana.box,"Grados Latitud")
        Ventana.Gralon    = tk.IntVar(Ventana.box,"Grados Longitud")
        Ventana.Milat     = tk.IntVar(Ventana.box,"Minutos Latitud")
        Ventana.Milon     = tk.IntVar(Ventana.box,"Minutos Longitud")
        Ventana.Selat     = tk.DoubleVar(Ventana.box,"Segundos Latitud")
        Ventana.Selon     = tk.DoubleVar(Ventana.box,"Segundos Longitud")
        Ventana.GradLat   = tk.Entry(Ventana.box,textvariable=Ventana.Gralat).grid(column=0,row=1)
        Ventana.GradLog   = tk.Entry(Ventana.box,textvariable=Ventana.Gralon).grid(column=0,row=2)
        Ventana.MinLat    = tk.Entry(Ventana.box,textvariable=Ventana.Milat).grid(column=1,row=1)
        Ventana.MinLon    = tk.Entry(Ventana.box,textvariable=Ventana.Milon).grid(column=1,row=2)
        Ventana.SegLat    = tk.Entry(Ventana.box,textvariable=Ventana.Selat).grid(column=2,row=1)
        Ventana.SegLon    = tk.Entry(Ventana.box,textvariable=Ventana.Selon).grid(column=2,row=2)
        Ventana.BtonDMS   = tk.Button(Ventana.box,text="Calcular DMS",command=Ventana.DMS).grid(column=2,row=4)
        Ventana.AnsDMS    = tk.Label(Ventana.box,text="Resultado")
        Ventana.AnsDMS.grid(column=2,row=5,columnspan=3)
        Ventana.Lati      = tk.DoubleVar(Ventana.box,"Latitud")
        Ventana.Long      = tk.DoubleVar(Ventana.box,"Longitud")
        tk.Label(Ventana.box,text="Convertir DD a DMS").grid(column=0,row=6)
        Ventana.DDLat     = tk.Entry(Ventana.box,textvariable=Ventana.Lati).grid(column=0,row=7)
        Ventana.DDLon     = tk.Entry(Ventana.box,textvariable=Ventana.Long).grid(column=1,row=7)
        Ventana.BtonDD    = tk.Button(Ventana.box,text="Calcular DD",command=Ventana.DD).grid(column=1,row=8)
        Ventana.AnsDD     = tk.Label(Ventana.box,text="Resultado")
        Ventana.AnsDD.grid(column=0,row=9,columnspan=3)
        Ventana.box.mainloop()

    def DMS(Ventana): #Funcion para convertir DMS a DD
        G1 = int(Ventana.Gralat.get())
        M1 = int(Ventana.Milat.get())
        S1 = float(Ventana.Selat.get())
        G2 = int(Ventana.Gralon.get())
        M2 = int(Ventana.Milon.get())
        S2 = float(Ventana.Selon.get())
        if(G1<0):
            X="° S, "
        else:
            X="° N, "
        if(G2<0):
            Y="° W"
        else:
            Y="° E"
        DD1 = round(G1+int(M1)/60+float(S1)/3600,1)
        DD2 = round(G2+int(M2)/60+float(S2)/3600,1)
        DD = str(DD1) + X +  str(DD2) + Y 
        Ventana.AnsDMS.configure(text=DD)

    def DD (Ventana):  #Funcion para convertir DD a DMS
        Latitud  = float(Ventana.Lati.get())
        Longitud = float(Ventana.Long.get()) 
        G1 = int(Latitud)
        G2 = int(Longitud)
        M1 = int((Latitud-G1)*60)
        M2 = int((Longitud-G2)*60) 
        S1 = round(float((((Latitud-G1)*60)-M1)*60),1)
        S2 = round(float((((Longitud-G2)*60)-M2)*60),1)
        if(G1<0):
            X = "S, "
        else:
            X = "N, "
        if(G2<0):
            Y = "W"
        else:
            Y = "E"
        Ventana.AnsDD.configure(text=str(G1)+"° "+str(M1)+"\' "+str(S1)+"\'' " + X + str(G2)+"° "+str(M2)+"\' "+str(S2)+"\'' " + Y)
        
Ejecucion=aplication()