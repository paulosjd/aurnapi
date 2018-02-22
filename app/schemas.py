from flask_marshmallow import Marshmallow, fields, Schema
from app.models import Data
from app.data.site_info import site_names

ma = Marshmallow()

class DataSchema2(ma.ModelSchema):

# (dump_to='TheName')
    class Meta:
        model = Data
        exclude = ['id']

data_schema2 = DataSchema2(many=True)

class DataSchema(Schema):
    #By default Schemas will unmarshal an input dictionary to an output dictionary whose keys are identical to the field names.
    site_name = fields.Function(lambda obj: site_names.get(obj['site_code']))
    o3 = fields.String()
    no2 = fields.String()
    so2 = fields.String()
    pm25 = fields.String()
    pm10 = fields.String()
    time = fields.String()

data_schema = DataSchema(many=True)