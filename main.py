from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *

import webbrowser

global VERSION, PACK
PACK = 7
VERSION = 'v0.1'

# Report a bug on GitHub:
def OpenLink(url):
	webbrowser.open(url)

# Show software information:
def Information():
	showinfo('Information', f'Resource Pack converter {VERSION},\nDevelopped by the Compliance Team,\nAll rights reserved.')

# Launch Pack conversion:
def AskFileDirectory(packVersionOutput):
	if inputEntry.get() == '':
		showerror('Error', 'You need to add your pack version first')
	else:
		try:
			int(inputEntry.get())
		except ValueError:
			showerror('Error', f'Wrong Pack Version set! your: {inputEntry.get()}')
		else:
			if (int(inputEntry.get()) > 0 and int(inputEntry.get()) < PACK and int(inputEntry.get()) != PACK):
				directory = filedialog.askdirectory()

				if directory != '':
					packVersionInput = inputEntry.get()
					return Convert(packVersionInput, packVersionOutput, directory)
				else:
					return
			else:
				return showerror('Error', f'Wrong Pack Version set! your: {inputEntry.get()}')

def Convert(input, output, directory):
	print(f'{input},{output},{directory}')

# Tkinter window & stuff
main = Tk()
main.title(f'Resource Pack Converter {VERSION}')

Label(main, width=64, text='\nThis is a useful tutorial on how use this script\n Lorem ipsum doloret sitamet Lorem ipsum doloret sitamet\nLorem ipsum doloret sitamet Lorem ipsum doloret sitamet\nLorem ipsum doloret sitamet').pack()
Label(main, text='\nYour Minecraft Pack Version').pack()

inputEntry = Entry(main, width=32)
inputEntry.pack()

outputLabel = Label(main, text='\nMinecraft Version you want').pack()

Button(main, width=32, anchor='w', text='Pack: 7 Version: 1.17', 						command= lambda: AskFileDirectory(7)).pack()
Button(main, width=32, anchor='w', text='Pack: 6 Version: 1.16.2 - 1.16.4',	command= lambda: AskFileDirectory(6)).pack()
Button(main, width=32, anchor='w', text='Pack: 5 Version: 1.15 - 1.16.1',		command= lambda: AskFileDirectory(5)).pack()
Button(main, width=32, anchor='w', text='Pack: 4 Version: 1.13 - 1.14.4',		command= lambda: AskFileDirectory(4)).pack()
Button(main, width=32, anchor='w', text='Pack: 3 Version: 1.11.2 - 1.12.2', command= lambda: AskFileDirectory(3)).pack()
Button(main, width=32, anchor='w', text='Pack: 2 Version: 1.9 - 1.10.2',		command= lambda: AskFileDirectory(2)).pack()
Button(main, width=32, anchor='w', text='Pack: 1 Version: 1.6.1 - 1.8.9',		command= lambda: AskFileDirectory(1)).pack()
Label(main, text='').pack()

mainMenu = Menu(main)

helpMenu = Menu(mainMenu, tearoff=0)
helpMenu.add_command(label='Information', command= lambda: Information())
helpMenu.add_command(label='GitHub', command= lambda: OpenLink('https://github.com/Compliance-Resource-Pack/Resource-Pack-Converter'))
helpMenu.add_command(label='Report Bug',  command= lambda: OpenLink('https://github.com/Compliance-Resource-Pack/Resource-Pack-Converter/issues'))

for label, menu in [('Help', helpMenu)]:
	mainMenu.add_cascade(label=label, menu=menu)

main.config(menu=mainMenu)
main.mainloop()