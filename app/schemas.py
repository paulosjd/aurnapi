from marshmallow import post_dump
from flask_marshmallow import Marshmallow
from app.models import HourlyData, Site

ma = Marshmallow()


class HourlyDataSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    site_name = ma.Function(lambda obj: obj.owner.name)
    site_code = ma.Function(lambda obj: obj.owner.site_code)
    time = ma.Method(serialize='standardize_time')

    @staticmethod
    def standardize_time(obj):
        std_time = '{}-{}-{} {}'.format(*obj.time.split(' ')[0].split('/')[::-1], obj.time.split(' ')[1])
        return std_time

    class Meta:
        additional = ('ozone', 'no2', 'so2', 'pm25', 'pm10')

data_schema = HourlyDataSchema(exclude=['site_name', 'site_code'])
many_data_schema = HourlyDataSchema(many=True, exclude=['site_name', 'site_code'])
current_hour_schema = HourlyDataSchema(many=True, exclude=['id', 'ozone', 'so2'])


class SiteSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    data = ma.Nested(HourlyDataSchema, allow_none=True, dump_only=True)
    url = ma.URLFor('Site.site_detail', id='<id>')
    user = ma.Function(lambda obj: obj.user.name)

    class Meta:
        additional = ('name', 'site_code', 'region', 'type', 'latitude', 'longitude', 'defra_url', 'map_url')

    @post_dump
    def clean_missing(self, data):
        ret = data.copy()
        for key in filter(lambda key: data[key] is None, data):
            del ret[key]
        return ret

site_schema = SiteSchema()
sites_schema = SiteSchema(exclude=['defra_url', 'map_url'], many=True)


class SiteModelSchema(ma.ModelSchema):
    class Meta:
        model = Site

site_model_schema = SiteModelSchema()


class DataModelSchema(ma.ModelSchema):
    class Meta:
        model = HourlyData

hourlydata_schema = DataModelSchema()
