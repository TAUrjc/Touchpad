import gtk, sys

class PyApp(gtk.Window):
   
    def __init__(self):
        super(PyApp, self).__init__()

        def hola(b):
         print "Hola Mundo"
        
        self.set_title("Buttons")
        self.set_size_request(400, 300)
        self.set_position(gtk.WIN_POS_CENTER)

        btn1 = gtk.Button("Sound1")
        btn1.set_sensitive(True)
        btn1.set_size_request(80, 80)
        btn2 = gtk.Button("Sound2")
        btn2.set_sensitive(True)
        btn2.set_size_request(80, 80)
        btn3 = gtk.Button("Base")
        btn3.set_sensitive(True)
        btn3.set_size_request(80, 80)
        btn1.connect('clicked', hola)

        fixed = gtk.Fixed()

        fixed.put(btn1, 50, 93)
        fixed.put(btn2, 150, 93)
        fixed.put(btn3, 260, 93)
        
        self.connect("destroy", gtk.main_quit)
        
        self.add(fixed)
        self.show_all()


PyApp()
gtk.main()