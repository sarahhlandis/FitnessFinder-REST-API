from marshmallow import fields, ValidationError, validates_schema
from marshmallow.validate import Range
from app import ma
from datetime import date
from models.promotions import Promotion

class PromotionSchema(ma.Schema):
    class Meta:
        # define the fields to expose
        fields = ("id", "name", "start_date", "end_date", "discount_percent")
        # foreign key fields
        load_only = ["facility_id"]
    
    name = fields.String(max=100)
    discount_percent = fields.Integer(validate=Range(min=0, max=100))

    # Validate that start_date is not in the past and is before end_date
    @validates_schema
    def validate_dates(self, data, **kwargs):
        if data["start_date"].date() < date.today():
            raise ValidationError("Start date cannot be in the past")
        if data["start_date"].date() >= data["end_date"].date():
            raise ValidationError("Start date must be before end date")
        
    start_date = fields.DateTime(format='%m-%d-%Y', validate=validate_dates)
    end_date = fields.DateTime(format='%m-%d-%Y')
        
promotion_schema = PromotionSchema()
promotions_schema = PromotionSchema(many=True)

