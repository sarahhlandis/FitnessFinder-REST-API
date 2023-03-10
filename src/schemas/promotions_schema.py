from marshmallow import fields, validate, ValidationError
from app import ma
from datetime import date
from models.promotions import Promotion

class PromotionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Promotion
    
    # Validate that start_date is not in the past and is before end_date
    @ma.validates_schema
    def validate_dates(self, data, **kwargs):
        if data["start_date"] < date.today():
            raise ValidationError("Start date cannot be in the past")
        if data["start_date"] >= data["end_date"]:
            raise ValidationError("Start date must be before end date")
        
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, max=100)
    start_date = fields.Date(required=True, validate=validate_dates)
    end_date = fields.Date(required=True, format='%Y-%m-%d')
    discount = fields.Integer(required=True, validate=validate.Range(min=0, max=100))

    # foreign keys below
    facility_id = fields.Integer(required=True)

    