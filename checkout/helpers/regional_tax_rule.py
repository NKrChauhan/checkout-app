from checkout.constants import REGION


class RegionalTaxRuleHelper:
    """
    Mapping to keep tax percent based on region.
    """
    tax_region_mapping = {
        REGION.INDIA: 0  # 0% tax rate for india for now
    }

    @classmethod
    def get_tax_rule_percent_for_region(cls, region):
        try:
            return cls.tax_region_mapping[region]
        except KeyError:
            raise Exception("Tax Rule Not Found")

    @classmethod
    def get_all_tax_region_mapping(cls):
        return cls.tax_region_mapping
