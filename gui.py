import gtk, sys, serial, pygame

pygame.mixer.init()
sound1 = pygame.mixer.Sound('base.ogg')
sound2 = pygame.mixer.Sound('verse2.ogg')
sound3 = pygame.mixer.Sound('verse3.ogg')


class PyApp(gtk.Window):
    
    def sonido(self, lineaLeida):
	if (lineaLeida == '2\r\n'):
	    try:
		sound1.play(loops = -1);
		print "ESCRIBO DESPUES DE LA BASE"
	    except pygame.error, message:
		print "base" + sound1.name
		

	elif lineaLeida == '3\r\n':
	    try:
		sound2.play(loops = 0);
	    except pygame.error, message:
		print "sound2" + sound2.name
		
	elif lineaLeida == '4\r\n':
	    try:
		sound3.play(loops = 0);
	    except pygame.error, message:
		print "sound3" + sound3.name
	else:
	    print "Error de lectura (Leo cosas raras)"
   
    def __init__(self):
        super(PyApp, self).__init__()

        def b1(b):
         self.sonido('3\r\n')

        def b2(b):
         self.sonido('4\r\n')

        def base(b):
         self.sonido('2\r\n')
        
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
