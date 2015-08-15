from gi.repository import Notify
import os

Notify.init("SMS")
Hello = Notify.Notification.new("Başlık", "Mesaj", os.path.dirname(os.path.realpath(__file__))+ "/icon.png")
Hello.show()
