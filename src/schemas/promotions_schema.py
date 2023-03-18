from marshmallow import fields, ValidationError, validates_schema, validates
from marshmallow.validate import Range
from app import ma
from datetime import date
from models.promotions import Promotion

class PromotionSchema(ma.Schema):
    class Meta:
        ordered = True
        # define the fields to expose
        fields = ("name", "start_date", "end_date", "discount_percent")
        # foreign key fields
        load_only = ["facility_id", "id"]
    
    name = fields.String(max=100)
    discount_percent = fields.Integer(validate=Range(min=0, max=100))

    start_date = fields.DateTime(format='%d-%m-%Y', required=True)
    end_date = fields.DateTime(format='%d-%m-%Y', required=True)

    # # Validate that start_date is not in the past and is before end_date
    # @validates_schema
    # def validate_dates(self, data, **kwargs):
    #     if data["start_date"].date() < date.today():
    #         raise ValidationError("Start date cannot be in the past")
    #     if data["start_date"].date() >= data["end_date"].date():
    #         raise ValidationError("Start date must be before end date")

    @validates('start_date')
    def validate_start_date(self, value):
        if value.date() < date.today():
            raise ValidationError("Start date cannot be in the past")
        
    @validates('end_date')
    def validate_end_date(self, value):
        if value.date() < date.today():
            raise ValidationError("End date cannot be in the past")

    @validates_schema
    def validate_dates(self, data):
        if data["start_date"].date() >= data["end_date"].date():
            raise ValidationError("Start date must be before end date")
        
        
promotion_schema = PromotionSchema()
promotions_schema = PromotionSchema(many=True)

