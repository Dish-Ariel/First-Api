import hug

@hug.get(examples='name=Ariel&age=25')
def hello(name: hug.types.text, age: hug.types.number, hug_timer=3):
    return {'mensaje': 'Hello {0}! have {1} :V'.format(name, age),'timer': float(hug_timer)}

@hug.get('/')
def root():
    return {'mensaje':'Bienvenido a mi Api!!!','posdata':'accede a hello/name=<tu_nombre>&age=<tu_edad>','remitente':'Ariel Andrade Garcia V:'}

@hug.default_input_format("application/json")
@hug.post('/')
def postRoot():
    return {'mensaje':'Bienvenido a mi Api-post prruki!','posdata':'accede a hello/name=<tu_nombre>&age=<tu_edad>','remitente':'Ariel Andrade Garcia V:'}

@hug.default_input_format("application/json")
@hug.get('/customer/')
def test(customer_id: hug.types.text):
    return {'customer_id':'{0}'.format(customer_id), 'Name':'Nombre','Info':'Datos'}

