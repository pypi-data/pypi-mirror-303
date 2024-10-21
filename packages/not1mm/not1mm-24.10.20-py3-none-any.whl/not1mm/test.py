from dasbus.connection import SessionMessageBus

bus = SessionMessageBus()

proxy = bus.get_proxy("org.freedesktop.Notifications", "/org/freedesktop/Notifications")

id = proxy.Notify(
    "weenes", 0, "face-smile", "My notification", "Hello World!", [], {}, 0
)

print("The notification {} was sent.".format(id))
