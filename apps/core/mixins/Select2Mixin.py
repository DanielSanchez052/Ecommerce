class Select2Mixin(object):
     def __init__(self,*args, **kwargs):
        super(Select2Mixin, self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            try:
                if visible.field.widget.input_type == 'select':
                    visible.field.widget.attrs['class'] = 'select2'
            except AttributeError:
                print("No tiene el atributo")