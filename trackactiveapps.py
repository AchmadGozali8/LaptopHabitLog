import time
import Xlib
import Xlib.display

while True:
    display = Xlib.display.Display()
    root = display.screen().root
    windowID = root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
    window = display.create_resource_object('window', windowID)

    try:
        print window.get_wm_name()
    except:
        print 'something wrong buddy'
        pass
    time.sleep(10)