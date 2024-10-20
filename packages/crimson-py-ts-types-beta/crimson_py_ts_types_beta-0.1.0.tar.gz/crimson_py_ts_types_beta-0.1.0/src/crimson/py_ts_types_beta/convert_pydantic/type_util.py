def annotated(cls):
    """
    Adds metadata injection capability to a class via square brackets ([]).
    Use this decorator to enable metadata annotations on classes.
    """

    def class_getitem(cls, params):
        if type(params) is tuple:
            cls.__metadata__ = params
            return params[0]
        else:
            return params

    cls.__class_getitem__ = classmethod(class_getitem)
    return cls
