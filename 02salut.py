import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Fereastra(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="GTK BOX")
		self.set_default_size(350, 100)

		self.grid = Gtk.Grid()
		self.add(self.grid)

		

		self.lb_cel = Gtk.Label("Celsius")
		self.grid.add(self.lb_cel)

		self.en_cel = Gtk.Entry()
		self.grid.attach_next_to(self.en_cel, self.lb_cel, 					  Gtk.PositionType.RIGHT, 1, 1)

		self.button1 = Gtk.Button(label="About")
		self.button1.connect("clicked", self.on_button1_clicked)
		self.grid.attach_next_to(self.button1, self.en_cel, Gtk.PositionType.RIGHT, 1, 1)

		self.lb_fah = Gtk.Label("Fahrenheit")
		self.grid.attach(self.lb_fah, 0, 1, 1, 1)

		self.en_fah = Gtk.Entry()
		self.grid.attach_next_to(self.en_fah, self.lb_fah, 					  Gtk.PositionType.RIGHT, 1,3)

		self.button2 = Gtk.Button(label="Calculate")
		self.button2.connect("clicked", self.on_button2_clicked)
		self.grid.attach_next_to(self.button2,self.en_fah, Gtk.PositionType.RIGHT, 2, 1)

	def on_button1_clicked(self, widget):
		print("SALUT!")
		dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
				Gtk.ButtonsType.OK, "Acesta este un mesaj informativ")
		dialog.format_secondary_text("Acest program este un convertor de temp.")
		dialog.run()
		dialog.destroy()

	def on_button2_clicked(self, widget):
		print("LA REVEDERE!")
		fahr = float(self.en_cel.get_text())*9/5 + 32
		str_fahr = str(fahr)
		self.en_fah.set_text(str_fahr)

fereastra = Fereastra()
fereastra.connect("destroy", Gtk.main_quit)
fereastra.show_all()
Gtk.main()
