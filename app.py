import hug

@hug.get(examples='name=Ariel&age=25')
def hello(name: hug.types.text, age: hug.types.number, hug_timer=3):
    return {'mensaje': 'Hello {0}! have {1} :V'.format(name, age),'timer': float(hug_timer)}

@hug.get('/')
def root():
    return {'mensaje':'Bienvenido a mi Api prruki!','posdata':'accede a hello/name=<tu_nombre>&age=<tu_edad>','remitente':'Ariel Andrade Garcia V:'}

