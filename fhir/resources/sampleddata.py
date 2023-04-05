# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SampledData
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import datatype, fhirtypes


class SampledData(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A series of measurements taken by a device.
    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """

    resource_type = Field("SampledData", const=True)

    codeMap: fhirtypes.Canonical = Field(
        None,
        alias="codeMap",
        title="Defines the codes used in the data",
        description="Reference to ConceptMap that defines the codes used in the data.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ConceptMap"],
    )
    codeMap__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_codeMap", title="Extension field for ``codeMap``."
    )

    data: fhirtypes.String = Field(
        None,
        alias="data",
        title='Decimal values with spaces, or "E" | "U" | "L", or another code',
        description=(
            "A series of data points which are decimal values or codes separated by"
            ' a single space (character u20). The special codes "E" (error), "L" '
            '(below detection limit) and "U" (above detection limit) are also '
            "defined for used in place of decimal values."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_data", title="Extension field for ``data``."
    )

    dimensions: fhirtypes.PositiveInt = Field(
        None,
        alias="dimensions",
        title="Number of sample points at each time point",
        description=(
            "The number of sample points at each time point. If this value is "
            "greater than one, then the dimensions will be interlaced - all the "
            "sample points for a point in time will be recorded at once."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    dimensions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dimensions", title="Extension field for ``dimensions``."
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Multiply data by this before adding to origin",
        description=(
            "A correction factor that is applied to the sampled data points before "
            "they are added to the origin."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    interval: fhirtypes.Decimal = Field(
        None,
        alias="interval",
        title="Number of intervalUnits between samples",
        description=(
            "Amount of intervalUnits between samples, e.g. milliseconds for time-"
            "based sampling."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    interval__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_interval", title="Extension field for ``interval``."
    )

    intervalUnit: fhirtypes.Code = Field(
        None,
        alias="intervalUnit",
        title="The measurement unit of the interval between samples",
        description="The measurement unit in which the sample interval is expressed.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    intervalUnit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_intervalUnit", title="Extension field for ``intervalUnit``."
    )

    lowerLimit: fhirtypes.Decimal = Field(
        None,
        alias="lowerLimit",
        title="Lower limit of detection",
        description=(
            "The lower limit of detection of the measured points. This is needed if"
            ' any of the data points have the value "L" (lower than detection '
            "limit)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lowerLimit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lowerLimit", title="Extension field for ``lowerLimit``."
    )

    offsets: fhirtypes.String = Field(
        None,
        alias="offsets",
        title="Offsets, typically in time, at which data values were taken",
        description=(
            "A series of data points which are decimal values separated by a single"
            " space (character u20).  The units in which the offsets are expressed "
            "are found in intervalUnit.  The absolute point at which the "
            "measurements begin SHALL be conveyed outside the scope of this "
            "datatype, e.g. Observation.effectiveDateTime for a timing offset."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    offsets__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_offsets", title="Extension field for ``offsets``."
    )

    origin: fhirtypes.QuantityType = Field(
        ...,
        alias="origin",
        title="Zero value and units",
        description=(
            "The base quantity that a measured value of zero represents. In "
            "addition, this provides the units of the entire measurement series."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    upperLimit: fhirtypes.Decimal = Field(
        None,
        alias="upperLimit",
        title="Upper limit of detection",
        description=(
            "The upper limit of detection of the measured points. This is needed if"
            ' any of the data points have the value "U" (higher than detection '
            "limit)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    upperLimit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_upperLimit", title="Extension field for ``upperLimit``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SampledData`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "origin",
            "interval",
            "intervalUnit",
            "factor",
            "lowerLimit",
            "upperLimit",
            "dimensions",
            "codeMap",
            "offsets",
            "data",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1268(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("dimensions", "dimensions__ext"),
            ("intervalUnit", "intervalUnit__ext"),
        ]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
