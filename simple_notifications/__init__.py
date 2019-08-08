import objc
import Foundation
import uuid

try:
    from .injectionSupport import injectBundleIdentifier as inject_bundle_identifier
except ImportError:
    from injectionSupport import injectBundleIdentifier as inject_bundle_identifier

inject_bundle_identifier("org.python.PythonLauncher")


class Notification(object):
    
    def __init__(self):
        self._notification_center = Foundation.NSUserNotificationCenter.defaultUserNotificationCenter()
        self._notification = Foundation.NSUserNotification.alloc().init()
        self._title = None
        self._subtitle = None
        self._sound_name = None
        self._informative_text = None
        self._callback = None
        self._identifier = uuid.uuid1().urn
        
    
    def send(self):
        if self._title is None:
            raise ValueError("The notification title must be set")
        
        self._notification.setTitle_(self._title)
        self._notification.setIdentifier_(self._identifier)
        
        if self._subtitle is not None:
            self._notification.setSubtitle_(self._subtitle)
        
        if self._informative_text is not None:
            self._notification.setInformativeText_(self._informative_text)
        
        if self._sound_name is not None:
            self._notification.setSoundName_(self._sound_name)
            
        self._notification_center.deliverNotification_(self._notification)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value
    
    @property
    def subtitle(self):
        return self._subtitle
    
    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value
    
    @property
    def informative_text(self):
        return self._informative_text
    
    @informative_text.setter
    def informative_text(self, value):
        self._informative_text = value
    
    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value
    
    @property
    def sound(self):
        return self._sound_name
    
    @sound.setter
    def sound(self, value):
        if value is True:
            self._sound_name = "NSUserNotificationDefaultSoundName"
        else:
            self._sound_name = value
    
    @property
    def response(self):
        return self._notification.response()


def notify(title, subtitle=None, informative_text=None, sound=None):
    notification = Notification()
    notification.title = title
    notification.subtitle = subtitle
    notification.informative_text = informative_text
    notification.sound = sound
    notification.send()
    return notification

__all__=["notify","inject_bundle_identifier","Notification"]