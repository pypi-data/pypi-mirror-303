from typing import Any, Callable


"""
MavroTk is still experimental and in early development.
At this moment, it is not intended to be used in production.
"""

def public__findTk(query: str):
    import tkinter
    return getattr(tkinter, query)


class App:
    def __init__(self) -> None:
        self.root: Any = public__findTk("Tk")()
    def public__print(self, value) -> None:
        public__findTk("Label")(self.root, text=str(value)).pack(pady=5)
    def button(self, value) -> Callable:
        def wrapper(fn: Callable) -> None:
            public__findTk("Button")(self.root, text=str(value), command=fn).pack(pady=5)
        return wrapper
    def __starter__(self) -> None:
        self.root.mainloop()