from tkinter import *
from controller.controlador import Controlador
class Vistas:
    @staticmethod
    def borrarPantalla(ventana):
        for w in ventana.winfo_children(): w.destroy()
    
    @staticmethod
    def interfaz(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana ,text="Menu").pack(pady=7)
        Button(ventana,text="Coches",width=10,command=lambda:Vistas.menu_autos(ventana)).pack(pady=7)
        Button(ventana,text="Camionetas",width=10,command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=7)
        Button(ventana,text="Camiones",width=10,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=7)
        Button(ventana,text="Salir",width=10,command=ventana.quit).pack(pady=7)
    
    @staticmethod
    def menu_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Menu Coches").pack(pady=7)
        Button(ventana,text="Agregar",width=10,command=lambda:Vistas.insertar_autos(ventana)).pack(pady=7)
        Button(ventana,text="Consultar",width=10,command=lambda:Vistas.consultar_autos(ventana)).pack(pady=7)
        Button(ventana,text="Actualizar",width=10,command=lambda:Vistas.modificar_autos(ventana)).pack(pady=7)
        Button(ventana,text="Eliminar",width=10,command=lambda:Vistas.eliminar_autos(ventana)).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.interfaz(ventana)).pack(pady=7)
   
    @staticmethod
    def insertar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Agregar coche").pack(pady=7)
        lbl=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas"]; ents=[]
        for t in lbl:
            Label(ventana,text=t).pack(); e=Entry(ventana); e.pack(); ents.append(e)
        Button(ventana,text="Guardar",width=10,command=lambda:Controlador.insertar_auto(*[e.get() for e in ents])).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_autos(ventana)).pack(pady=7)
    
    @staticmethod
    def consultar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Coches ").pack(pady=7)
        datos=Controlador.consultar_auto("all")
        if not datos:
            Label(ventana,text="No hay coches ").pack(pady=7)
        else:
            for a in datos:
                Label(ventana,text=f"id {a[0]} {a[1]}  {a[2]} {a[3]} {a[4]} {a[5]} {a[6]}").pack()
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_autos(ventana)).pack(pady=7)
    
    @staticmethod
    def modificar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Actualizar coche").pack(pady=7)
        Label(ventana,text="Id").pack(); e=Entry(ventana); e.pack()
        Button(ventana,text="Buscar",width=10,command=lambda:Vistas.modificar_form(ventana,e.get())).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_autos(ventana)).pack(pady=7)
    
    @staticmethod
    def modificar_form(ventana,id):
        auto=Controlador.consultar_auto(id)
        if not auto:
            Vistas.borrarPantalla(ventana)
            Label(ventana,text="No existe el id").pack(pady=7)
            Button(ventana,text="Volver",width=10,command=lambda: Vistas.modificar_autos(ventana)).pack(pady=7)
            return
        if isinstance(auto,list) and len(auto)>0: auto=auto[0]
        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"Actualizar coche id {id}").pack(pady=5)
        lbl=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas"]; ents=[]
        for i,t in enumerate(lbl):
            Label(ventana,text=t).pack(); e=Entry(ventana); e.insert(0,str(auto[i+1])); e.pack(); ents.append(e)
        Button(ventana,text="Guardar",width=10,command=lambda: Controlador.modificar_auto(*[e.get() for e in ents],id)).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda: Vistas.menu_autos(ventana)).pack(pady=7)

    @staticmethod
    def eliminar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Eliminar coche").pack(pady=7)
        Label(ventana,text="Id").pack(); e=Entry(ventana); e.pack()
        Button(ventana,text="Buscar",width=10,command=lambda:Vistas.eliminar_confirmar(ventana,e.get())).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_autos(ventana)).pack(pady=7)

    @staticmethod
    def eliminar_confirmar(ventana,id):
        auto=Controlador.consultar_auto(id)
        if not auto:
            Vistas.borrarPantalla(ventana); Label(ventana,text="No existe el id").pack(pady=7)
            Button(ventana,text="Volver",width=10,command=lambda:Vistas.eliminar_autos(ventana)).pack(pady=7); return
        auto=auto[0]
        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"¿quieres borrar el coche, id {auto[0]} {auto[1]} {auto[2]} {auto[3]}").pack(pady=10)
        Button(ventana,text="Sí",width=10,command=lambda:Controlador.eliminar_auto(id)).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_autos(ventana)).pack(pady=7)




    @staticmethod
    def menu_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Menu Camionetas").pack(pady=7)
        Button(ventana,text="Agregar",width=10,command=lambda:Vistas.insertar_camionetas(ventana)).pack(pady=7)
        Button(ventana,text="Consultar",width=10,command=lambda:Vistas.consultar_camionetas(ventana)).pack(pady=7)
        Button(ventana,text="Actualizar",width=10,command=lambda:Vistas.modificar_camionetas(ventana)).pack(pady=7)
        Button(ventana,text="Eliminar",width=10,command=lambda:Vistas.eliminar_camionetas(ventana)).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.interfaz(ventana)).pack(pady=7)


    @staticmethod
    def insertar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Agregar Camioneta").pack(pady=5)
        lbls=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas","Tracción"]
        ents=[]
        for t in lbls:
            Label(ventana,text=t).pack()
            e=Entry(ventana)
            e.pack()
            ents.append(e)

        Button(ventana,text="Guardar",width=10,command=lambda:
               Controlador.insertar_camioneta(*[e.get() for e in ents])).pack(pady=7)

        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=7)


    @staticmethod
    def consultar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Camionetas").pack(pady=7)

        datos = Controlador.consultar_camioneta("all")

        if not datos:
            Label(ventana,text="No hay camionetas").pack(pady=7)
        else:
            for c in datos:
                Label(
                    ventana,
                    text=f"id {c[0]}  {c[1]}  {c[2]}  {c[3]}  {c[4]}  {c[5]}  {c[6]}  {c[7]}"
                ).pack()

        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=7)


    @staticmethod
    def modificar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Actualizar Camioneta").pack(pady=7)
        Label(ventana,text="Id").pack()

        e = Entry(ventana)
        e.pack()

        Button(ventana,text="Buscar",width=10,command=lambda:
               Vistas.modificar_form_camioneta(ventana, e.get())).pack(pady=7)

        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=7)


    @staticmethod
    def modificar_form_camioneta(ventana,id):
        c = Controlador.consultar_camioneta(id)

        if not c:
            Vistas.borrarPantalla(ventana)
            Label(ventana,text="No existe el id").pack(pady=7)
            Button(ventana,text="Volver",width=10,command=lambda:
                   Vistas.modificar_camionetas(ventana)).pack(pady=7)
            return

        if isinstance(c,list) and len(c)>0:
            c = c[0]

        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"Actualizar Camioneta id {id}").pack(pady=7)

        lbls=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas","Tracción"]
        ents=[]

        for i,t in enumerate(lbls):
            Label(ventana,text=t).pack()
            e = Entry(ventana)
            e.insert(0,str(c[i+1]))
            e.pack()
            ents.append(e)

        Button(
            ventana,
            text="Guardar",
            width=20,
            command=lambda: Controlador.modificar_camioneta(*[e.get() for e in ents], id)
        ).pack(pady=7)

        Button(ventana,text="Volver",width=10,command=lambda:
               Vistas.menu_camionetas(ventana)).pack(pady=7)



    @staticmethod
    def eliminar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Eliminar camioneta").pack(pady=7)
        Label(ventana,text="Id").pack(); e=Entry(ventana); e.pack()
        Button(ventana,text="Buscar",width=10,command=lambda:Vistas.eliminar_conf(ventana,e.get())).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=7)

    @staticmethod
    def eliminar_conf(ventana,id):
        auto=Controlador.consultar_camioneta(id)
        if not auto:
            Vistas.borrarPantalla(ventana); Label(ventana,text="No existe el id").pack(pady=7)
            Button(ventana,text="Volver",width=10,command=lambda:Vistas.eliminar_camionetas(ventana)).pack(pady=7); return
        auto=auto[0]
        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"¿quieres borrar la camioneta, id {auto[0]} {auto[1]} {auto[2]} {auto[3]}").pack(pady=10)
        Button(ventana,text="Sí",width=10,command=lambda:Controlador.eliminar_camion(id)).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=7)


    @staticmethod
    def menu_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Menu Camiones").pack(pady=7)
        Button(ventana,text="Agregar",width=10,command=lambda:Vistas.insertar_camiones(ventana)).pack(pady=7)
        Button(ventana,text="Consultar",width=10,command=lambda:Vistas.consultar_camiones(ventana)).pack(pady=7)
        Button(ventana,text="Actualizar",width=10,command=lambda:Vistas.modificar_camiones(ventana)).pack(pady=7)
        Button(ventana,text="Eliminar",width=10,command=lambda:Vistas.eliminar_camiones(ventana)).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.interfaz(ventana)).pack(pady=7)

    @staticmethod
    def insertar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Agregar Camion").pack(pady=7)
        lbl=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas","Eje","Capacidad Carga"]; ents=[]
        for t in lbl:
            Label(ventana,text=t).pack()
            e=Entry(ventana); e.pack(); ents.append(e)
        Button(ventana,text="Guardar",width=10,command=lambda:Controlador.insertar_camion(*[e.get() for e in ents])).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=7)

    @staticmethod
    def consultar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Camiones").pack(pady=7)
        datos=Controlador.consultar_camion("all")
        if not datos:
            Label(ventana,text="No hay camiones ").pack(pady=7)
        else:
            for c in datos:
                Label(ventana,text=f"id {c[0]} {c[1]} {c[2]} {c[3]} {c[4]} {c[5]} {c[6]} {c[7]} {c[8]}").pack()
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=7)

    @staticmethod
    def modificar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Actualizar camion").pack(pady=7)
        Label(ventana,text="Id").pack()
        e=Entry(ventana); e.pack()
        Button(ventana,text="Buscar",width=10,command=lambda:Vistas.modificar_form_camion(ventana,e.get())).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=7)

    @staticmethod
    def modificar_form_camion(ventana,id):
        c=Controlador.consultar_camion(id)
        if not c:
            Vistas.borrarPantalla(ventana)
            Label(ventana,text="No existe el id").pack(pady=7)
            Button(ventana,text="Volver",width=10,command=lambda:Vistas.modificar_camiones(ventana)).pack(pady=7)
            return
        if isinstance(c,list) and len(c)>0: c=c[0]
        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"Actualizar Camion id {id}").pack(pady=5)
        lbl=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas","Eje","Capacidad Carga"]; ents=[]
        for i,t in enumerate(lbl):
            Label(ventana,text=t).pack()
            e=Entry(ventana)
            e.insert(0,str(c[i+1]))
            e.pack(); ents.append(e)
        Button(ventana,text="Guardar ",width=10,command=lambda:Controlador.modificar_camion(*[e.get() for e in ents],id)).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=7)

    @staticmethod
    def eliminar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Eliminar camion").pack(pady=7)
        Label(ventana,text="Id").pack(); e=Entry(ventana); e.pack()
        Button(ventana,text="Buscar",width=10,command=lambda:Vistas.eliminar_confir(ventana,e.get())).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=7)

    @staticmethod
    def eliminar_confir(ventana,id):
        auto=Controlador.consultar_camion(id)
        if not auto:
            Vistas.borrarPantalla(ventana); Label(ventana,text="No existe el id").pack(pady=7)
            Button(ventana,text="Volver",width=10,command=lambda:Vistas.eliminar_camiones(ventana)).pack(pady=7); return
        auto=auto[0]
        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"¿quieres borrar la camioneta, id {auto[0]} {auto[1]} {auto[2]} {auto[3]}").pack(pady=10)
        Button(ventana,text="Sí",width=10,command=lambda:Controlador.eliminar_camion(id)).pack(pady=7)
        Button(ventana,text="Volver",width=10,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=7)
