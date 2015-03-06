import gtk, sys, serial

class PyApp(gtk.Window):
   
    def __init__(self):
        super(PyApp, self).__init__()

        arduino = serial.Serial('/dev/ttyACM0', 9600, timeout = 3.0)

        def b1(b):
         arduino.write('3\r\n')

        def b1(b):
         arduino.write('4\r\n')

        def base(b):
         arduino.write('2\r\n')
        
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
        btn1.connect('clicked', b1)
        btn2.connect('clicked', b2)
        btn2.connect('clicked', base)

        fixed = gtk.Fixed()

        fixed.put(btn1, 50, 93)
        fixed.put(btn2, 150, 93)
        fixed.put(btn3, 260, 93)
        
        self.connect("destroy", gtk.main_quit)
        
        self.add(fixed)
        self.show_all()


PyApp()
gtk.main()