from flask_marshmallow import Marshmallow
from app.models import Site

ma = Marshmallow()


class DataSchema(ma.Schema):
    # By default Schemas will unmarshal an input dict to an output dict whose keys are identical to field names.
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

