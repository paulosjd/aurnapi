from flask_marshmallow import Marshmallow

from app.models import Data
from app.data.site_info import site_names

ma = Marshmallow()

class BasicDataSchema(ma.ModelSchema):

    class Meta:
        model = Data
        exclude = ['id']

basic_data_schema = BasicDataSchema(many=True)

class SiteDataSchema(ma.Schema):
    #By default Schemas will unmarshal an input dictionary to an output dictionary whose keys are identical to the field names.
    #owner = ma.Function(lambda obj: obj.name.lower(), dump_to='site name')
    owner = ma.String(dump_to='site code')
    o3 = ma.String(dump_to='ozone')
    no2 = ma.String(dump_to='nitrogen dioxide')
    so2 = ma.String(dump_to='sulfur dioxide')
    time = ma.Method('standardize_time')

    def standardize_time(self, obj):
        std_time = '{}-{}-{} {}'.format(*obj.time.split(' ')[0].split('/')[::-1], obj.time.split(' ')[1])
        return std_time

    class Meta:
        additional = ('pm25', 'pm10')

site_data_schema = SiteDataSchema(many=True)
                                  
class SiteDataSchema(ma.Schema):
    #By default Schemas will unmarshal an input dictionary to an output dictionary whose keys are identical to the field names.
    #owner = ma.Function(lambda obj: obj.name.lower(), dump_to='site name')
    owner = ma.String(dump_to='site code')
    o3 = ma.String(dump_to='ozone')
    no2 = ma.String(dump_to='nitrogen dioxide')