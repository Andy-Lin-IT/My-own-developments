from kivy.app import App
from kivy.uix.button import Button


class HomeApp(App):
    nambers_count = 0
    def rick(self):
        HomeApp.nambers_count += 1
        return HomeApp.nambers_count
        

    def build(self):
        
        btn1 = Button(text = "button",
            font_size = 30,
            on_press = self.btn_press,
            background_color = [0,.1,.5,1],
            background_normal = '',
            border = (16, 16, 16, 16))
        return btn1
    def callback(self,instance):
        btn1.bind(on_press=callback)
        return btn1
       

    def btn_press(self, instance):
        if  instance.text == "button":
            instance.text = f"pressed {HomeApp().rick()} times"
        else:
            instance.text = f"pressed {HomeApp().rick()} times"
        if (HomeApp().nambers_count%10==0):
            instance.background_color = [1,0,0,1]
        else:
            instance.background_color = [.3,.1,.5,1]



if __name__ == "__main__":
    HomeApp().run()