# from kivy.app import App
# from kivy.uix.camera import Camera
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button

# class app_selfie(App):
#     def make(self):
#         obj_layout = BoxLayout(orientation='vertical')

#         self.obj_camera = Camera()
#         self.obj_camera.resolution=(810,810)
#         obj_button = Button(text="Click !!")
#         obj_button.size_hint=(0.6,0.3)
#         obj_button.pos_hint={'x':35,'y':35}
#         obj_button.bind(on_press=self.selfie_take())
        
#         obj_layout.add_widget(self.obj_camera)
#         obj_layout.add_widget(obj_button)

#         return obj_layout


#     def selfie_take(self,*args):
#         print("selfie has been taken successfully")
#         self.obj_camera.export_to_png('demoselfie.png')
#     def build(self):
#         return self.make()


# if __name__ == '__main__':
#     app_selfie().run()


from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class SelfieApp(App):
    def make_layout(self):
        layout = BoxLayout(orientation='vertical')
        
        self.camera = Camera()
        self.camera.resolution=(810,810)
        button = Button(text="Click !!")
        button.size_hint=(0.6,0.3)
        button.pos_hint={'x':35,'y':35}
        button.bind(on_press=self.selfie_take)
        
        layout.add_widget(self.camera)
        layout.add_widget(button)

        return layout


    def selfie_take(self, instance):
        print("selfie has been taken successfully")
        self.camera.export_to_png('demoselfie.png')
    def build(self):
        return self.make_layout()


if __name__ == '__main__':
    SelfieApp().run()
