from flask_marshmallow import Marshmallow

from app.models import Data
from app.data.site_info import site_names

ma = Marshmallow()

class DataSchema2(ma.ModelSchema):

    class Meta:
        model = Data
        exclude = ['id']

data_schema2 = DataSchema2(many=True)

class DataSchema(ma.Schema):
    #By default Schemas will unmarshal an input dictionary to an output dictionary whose keys are identical to the field names.
    owner = ma.Function(lambda obj: obj.name.lower(), dump_to='site name')
    o3 = ma.String(dump_to='ozone')
    no2 = ma.String(dump_to='nitrogen dioxide')
    so2 = ma.String(dump_to='sulfur dioxide')

    class Meta:
        additional = ('time', 'pm25', 'pm10')


data_schema = DataSchema(many=True)