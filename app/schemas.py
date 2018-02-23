from flask_marshmallow import Marshmallow
from app.models import Data, Site


ma = Marshmallow()


class BasicDataSchema(ma.ModelSchema):

    class Meta:
        model = Data
        exclude = ['id', 'time', 'owner']

basic_schema = BasicDataSchema(many=True)


class NestedDataSchema(ma.Schema):
    owner = ma.String(dump_to='site name')
    data = ma.Function(lambda x: {'ozone': x.o3, 'NO2': x.no2, 'SO2': x.so2, 'PM10': x.pm10, 'PM2.5': x.pm25,
                                  'time': x.time})

nested_schema = NestedDataSchema(many=True)


class DataSchema(ma.Schema):
    #By default Schemas will unmarshal an input dictionary to an output dictionary whose keys are identical to the field names.
    owner = ma.String(dump_to='site code')
    o3 = ma.String(dump_to='ozone')
    time = ma.Method('standardize_time')

    def standardize_time(self, obj):
        std_time = '{}-{}-{} {}'.format(*obj.time.split(' ')[0].split('/')[::-1], obj.time.split(' ')[1])
        return std_time

    class Meta:
        additional = ('no2', 'so2', 'pm25', 'pm10')

data_schema = DataSchema(many=True)


class SiteSchema(ma.ModelSchema):

    data = ma.Nested(DataSchema)

    class Meta:
        model = Site
        exclude = ['id', 'url', 'map_url', 'data', 'current']

site_schema = SiteSchema()

