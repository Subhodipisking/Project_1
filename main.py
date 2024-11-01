from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout




Window.clearcolor=(1,1,1,1)






class Myapp(App):
	def build(self):
		
		flayout=FloatLayout(size_hint=(None,None),size=(800,400),pos_hint={'x':0.5,'y':1})
		lout=BoxLayout(orientation="vertical")
		
		
		self.input=TextInput(text="0",size_hint=(1,0.1),padding=10,background_color="pink",readonly=True,font_size=100,multiline=False)
		
		
		layout=GridLayout(cols=3,row_force_default=True,row_default_height=300,center_y=600, padding=40,spacing=10)
		
		
		def cut(dl):
			thing=self.input.text
			r=thing[:len(thing)-1]
			self.input.text=r
			
		
		def add(ad):
			thing=self.input.text
			r=thing[-1:]
			if r=="+" or r=="":
				pass
			else:
				a=(self.input.text)
				b=f'{a}+'
				self.input.text=b	
		
			
		def equal(eq):
			if "+" in self.input.text:
				numlist=self.input.text.split("+")
				answer=0
				for number in numlist:
						answer=answer+int(number)
				self.input.text=str(answer)		
						
			
			
			
		
			
		
		
		
		def clear(clr):
			self.input.text=""
		
		
		def func(hello):
			if self.input.text=="0":
				self.input.text=""
			
			else:
				button_text=hello.text
			self.input.text += hello.text
			
			
			
		
		
		
		
		
		#input=TextInput()
		b1=Button(text="1",font_size="40sp",on_press=func)
		b2=Button(text="2",font_size="40sp",on_press=func)
		b3=Button(text="3",font_size="40sp",on_press=func)
		b4=Button(text="4",font_size="40sp",on_press=func)
		b5=Button(text="5",font_size="40sp",on_press=func)
		b6=Button(text="6",font_size="40sp",on_press=func)
		b7=Button(text="7",font_size="40sp",on_press=func) 
		b8=Button(text="8",font_size="40sp",on_press=func)
		b9=Button(text="9",font_size="40sp",on_press=func)
		b0=Button(text="0",font_size="40sp",on_press=func)
		bc=Button(text="C",font_size="40sp",on_press=clear)
		ba=Button(text="+",font_size="40sp",on_press=add)
		bx=Button(text="X",font_size="40sp",on_press=cut)
		be=Button(text="=",font_size="40sp",on_press=equal)
		
		
		
		
		
		#layout.add_widget(input)
		layout.add_widget(b1)
		layout.add_widget(b2)
		layout.add_widget(b3)
		layout.add_widget(b4)
		layout.add_widget(b5)
		layout.add_widget(b6)
		layout.add_widget(b7)
		layout.add_widget(b8)
		layout.add_widget(b9)
		#layout.add_widget(b0)
		layout.add_widget(b0)
		layout.add_widget(bc)
		layout.add_widget(ba)
		layout.add_widget(bx)
		layout.add_widget(be)
		
		
		
		lout.add_widget(self.input)
		lout.add_widget(layout)
		lout.add_widget(flayout)
		
		
		return lout
		
		
		
		
Myapp().run()		