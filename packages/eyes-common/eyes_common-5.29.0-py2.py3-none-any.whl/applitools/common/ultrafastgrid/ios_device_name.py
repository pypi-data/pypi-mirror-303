# GENERATED FILE #
from enum import Enum

from applitools.common.utils.general_utils import DeprecatedEnumVariant

__all__ = ("IosDeviceName",)


class IosDeviceName(Enum):
    iPad_7 = "iPad (7th generation)"
    iPad_9 = "iPad (9th generation)"
    iPad_Air_4 = "iPad Air (4th generation)"
    iPad_Pro_12_9_inch_3 = "iPad Pro (12.9-inch) (3rd generation)"
    iPad_Pro_11_inch_4 = "iPad Pro (11-inch) (4th generation)"
    iPhone_8 = "iPhone 8"
    iPhone_8_Plus = "iPhone 8 Plus"
    iPhone_X = "iPhone X"
    iPhone_XR = "iPhone XR"
    iPhone_Xs = "iPhone Xs"
    iPhone_11 = "iPhone 11"
    iPhone_11_Pro_Max = "iPhone 11 Pro Max"
    iPhone_11_Pro = "iPhone 11 Pro"
    iPhone_12 = "iPhone 12"
    iPhone_12_mini = "iPhone 12 mini"
    iPhone_12_Pro_Max = "iPhone 12 Pro Max"
    iPhone_12_Pro = "iPhone 12 Pro"
    iPhone_13 = "iPhone 13"
    iPhone_13_Pro_Max = "iPhone 13 Pro Max"
    iPhone_13_Pro = "iPhone 13 Pro"
    iPhone_14 = "iPhone 14"
    iPhone_14_Pro_Max = "iPhone 14 Pro Max"
    iPhone_15 = "iPhone 15"
    iPhone_15_Pro_Max = "iPhone 15 Pro Max"

    @DeprecatedEnumVariant
    def iPad_Pro_3(self):
        """`iPad_Pro_3` is deprecated. Use `iPad_Pro_12_9_inch_3` instead"""
        return self.iPad_Pro_12_9_inch_3

    @DeprecatedEnumVariant
    def iPad_Pro_4(self):
        """`iPad_Pro_4` is deprecated. Use `iPad_Pro_11_inch_4` instead"""
        return self.iPad_Pro_11_inch_4

    @DeprecatedEnumVariant
    def iPhone_XS(self):
        """`iPhone_XS` is deprecated. Use `iPhone_Xs` instead"""
        return self.iPhone_Xs
