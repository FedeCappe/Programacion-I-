class Motocicleta:
    state = "Nuevo"
    engine_estado = True

    def __init__(self,color,patent,fuel_liters,numbers_wheels,brand,
    model,date_manufacturing,speed_tip,weight,engine):

        self.color = color
        self.patent = patent
        self.fuel_liters = fuel_liters
        self.numers_whels = numbers_wheels
        self.brand = "  "
        self.model = "  " 
        self.date_manugacturing = date_manufacturing
        self.speed_tip = speed_tip
        self.weight = weight
        self.engine = engine
        
    @property 
    def brand(self):
        return self.__brand
    @property
    def model(self):
        return self.model 
    @brand.setter
    def brand(self,new_brand):
        self.__brand = new_brand
    @model.setter
    def model(self,new_model):
        self.model = new_model
    def encender_engine(self):
        if(self.engine_estado == True):
            print("El motor esta encendido.  ")
        else: 
            print("El motor estaba apagado, ahora esta encendido. ")
            self.engine_estado == True
    def apagar_engine(self):
        if(self.engine_estado == False):
            print("El motor esta apagado. ")
        else: 
            print("El motor estaba encendido. Ahora esta apagado. ")
            self.engine_estado == False
    def consultar_precio(self):
        return getattr(self, 'precio', None)
        

    

