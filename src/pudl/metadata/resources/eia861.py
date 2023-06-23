"""Definitions of data tables primarily coming from EIA-861."""
from typing import Any

RESOURCE_METADATA: dict[str, dict[str, Any]] = {
    "advanced_metering_infrastructure_eia861": {
        "description": "The data contain number of meters from automated meter readings (AMR) and advanced metering infrastructure (AMI) by state, sector, and balancing authority. The energy served (in megawatthours) for AMI systems is provided. Form EIA-861 respondents also report the number of standard meters (non AMR/AMI) in their system. Historical Changes: We started collecting the number of standard meters in 2013. The monthly survey collected these data from January 2011 to January 2017.",
        "schema": {
            "fields": [
                "advanced_metering_infrastructure",
                "automated_meter_reading",
                "balancing_authority_code_eia",
                "customer_class",
                "daily_digital_access_customers",
                "direct_load_control_customers",
                "energy_served_ami_mwh",
                "entity_type",
                "home_area_network",
                "non_amr_ami",
                "report_date",
                "short_form",
                "state",
                "utility_id_eia",
                "utility_name_eia",
                "data_maturity",
            ],
            "primary_key": [
                "balancing_authority_code_eia",
                "customer_class",
                "report_date",
                "state",
                "utility_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "balancing_authority_assn_eia861": {
        "description": "Association table showing which combinations of state, balancing authority, and utilities were observed in the data each year.",
        "schema": {
            "fields": [
                "report_date",
                "balancing_authority_id_eia",
                "utility_id_eia",
                "state",
            ],
            "primary_key": [
                "report_date",
                "balancing_authority_id_eia",
                "utility_id_eia",
                "state",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "balancing_authority_eia861": {
        "description": "Annual entity table for balancing authorities.",
        "schema": {
            "fields": [
                "report_date",
                "balancing_authority_id_eia",
                "balancing_authority_code_eia",
                "balancing_authority_name_eia",
            ],
            "primary_key": [
                "report_date",
                "balancing_authority_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "demand_response_eia861": {
        "description": "The data contain energy demand response programs by state, sector, and balancing authority. We collect data for the number of customers enrolled, energy savings, potential and actual peak savings, and associated costs.",
        "schema": {
            "fields": [
                "actual_peak_demand_savings_mw",
                "balancing_authority_code_eia",
                "customer_class",
                "customer_incentives_cost",
                "customers",
                "energy_savings_mwh",
                "other_costs",
                "potential_peak_demand_savings_mw",
                "report_date",
                "short_form",
                "state",
                "utility_id_eia",
                "utility_name_eia",
                "data_maturity",
            ],
            "primary_key": [
                "balancing_authority_code_eia",
                "customer_class",
                "report_date",
                "state",
                "utility_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "demand_response_water_heater_eia861": {
        "description": "The number of grid connected water heaters enrolled in demand response programs.",
        "schema": {
            "fields": [
                "balancing_authority_code_eia",
                "report_date",
                "state",
                "utility_id_eia",
                "water_heater",
                "data_maturity",
            ],
            "primary_key": [
                "balancing_authority_code_eia",
                "report_date",
                "state",
                "utility_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "demand_side_management_ee_dr_eia861": {
        "description": "The data contain energy efficiency incremental data, energy efficiency annual data, load management incremental data, load management annual data, annual costs, and the customer counts of price response and time response programs by sector.",
        "schema": {
            "fields": [
                "annual_indirect_program_cost",
                "annual_total_cost",
                "customer_class",
                "energy_efficiency_annual_actual_peak_reduction_mw",
                "energy_efficiency_annual_cost",
                "energy_efficiency_annual_effects_mwh",
                "energy_efficiency_annual_incentive_payment",
                "energy_efficiency_incremental_actual_peak_reduction_mw",
                "energy_efficiency_incremental_effects_mwh",
                "load_management_annual_actual_peak_reduction_mw",
                "load_management_annual_cost",
                "load_management_annual_effects_mwh",
                "load_management_annual_incentive_payment",
                "load_management_annual_potential_peak_reduction_mw",
                "load_management_incremental_actual_peak_reduction_mw",
                "load_management_incremental_effects_mwh",
                "load_management_incremental_potential_peak_reduction_mw",
                "nerc_region",
                "price_responsiveness_customers",
                "report_date",
                "state",
                "time_responsiveness_customers",
                "utility_id_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "demand_side_management_misc_eia861": {
        "schema": {
            "fields": [
                "energy_savings_estimates_independently_verified",
                "energy_savings_independently_verified",
                "entity_type",
                "major_program_changes",
                "nerc_region",
                "price_responsive_programs",
                "report_date",
                "reported_as_another_company",
                "short_form",
                "state",
                "time_responsive_programs",
                "utility_id_eia",
                "utility_name_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "demand_side_management_sales_eia861": {
        "schema": {
            "fields": [
                "nerc_region",
                "report_date",
                "sales_for_resale_mwh",
                "sales_to_ultimate_consumers_mwh",
                "state",
                "utility_id_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "distributed_generation_fuel_eia861": {
        "schema": {
            "fields": [
                "estimated_or_actual_fuel_data",
                "fuel_class",
                "fuel_pct",
                "report_date",
                "state",
                "utility_id_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "distributed_generation_misc_eia861": {
        "schema": {
            "fields": [
                "backup_capacity_mw",
                "distributed_generation_owned_capacity_mw",
                "estimated_or_actual_capacity_data",
                "generators_num_less_1_mw",
                "generators_number",
                "report_date",
                "state",
                "total_capacity_less_1_mw",
                "utility_id_eia",
                "utility_name_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "distributed_generation_tech_eia861": {
        "schema": {
            "fields": [
                "capacity_mw",
                "estimated_or_actual_tech_data",
                "report_date",
                "state",
                "tech_class",
                "utility_id_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "distribution_systems_eia861": {
        "description": "The number of distribution circuits and circuits with voltage optimization by state.",
        "schema": {
            "fields": [
                "circuits_with_voltage_optimization",
                "distribution_circuits",
                "report_date",
                "short_form",
                "state",
                "utility_id_eia",
                "utility_name_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "dynamic_pricing_eia861": {
        "description": "The number of customers enrolled in dynamic pricing programs by state, sector, and balancing authority. Respondents check if one or more customers are enrolled in time-of-use pricing, real time pricing, variable peak pricing, critical peak pricing, and critical peak rebates.",
        "schema": {
            "fields": [
                "balancing_authority_code_eia",
                "critical_peak_pricing",
                "critical_peak_rebate",
                "customer_class",
                "customers",
                "real_time_pricing",
                "report_date",
                "short_form",
                "state",
                "time_of_use_pricing",
                "utility_id_eia",
                "utility_name_eia",
                "variable_peak_pricing",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "energy_efficiency_eia861": {
        "description": "Incremental energy savings, peak demand savings, weighted average life cycle, and associated costs for the reporting year and life cycle of energy efficiency programs.",
        "schema": {
            "fields": [
                "balancing_authority_code_eia",
                "customer_class",
                "customer_incentives_incremental_cost",
                "customer_incentives_incremental_life_cycle_cost",
                "customer_other_costs_incremental_life_cycle_cost",
                "incremental_energy_savings_mwh",
                "incremental_life_cycle_energy_savings_mwh",
                "incremental_life_cycle_peak_reduction_mwh",
                "incremental_peak_reduction_mw",
                "other_costs_incremental_cost",
                "report_date",
                "short_form",
                "state",
                "utility_id_eia",
                "utility_name_eia",
                "weighted_average_life_years",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "green_pricing_eia861": {
        "description": "Green pricing program revenue, sales, and customer count by sector and state.",
        "schema": {
            "fields": [
                "customer_class",
                "customers",
                "green_pricing_revenue",
                "rec_revenue",
                "rec_sales_mwh",
                "report_date",
                "sales_mwh",
                "state",
                "utility_id_eia",
                "utility_name_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "mergers_eia861": {
        "description": "Information about utility mergers and acquisitions.",
        "schema": {
            "fields": [
                "entity_type",
                "merge_address",
                "merge_city",
                "merge_company",
                "merge_date",
                "merge_state",
                "new_parent",
                "report_date",
                "state",
                "utility_id_eia",
                "utility_name_eia",
                "zip_code",
                "zip_code_4",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "net_metering_customer_fuel_class_eia861": {
        "schema": {
            "fields": [
                "balancing_authority_code_eia",
                "capacity_mw",
                "customer_class",
                "customers",
                "energy_displaced_mwh",
                "report_date",
                "short_form",
                "sold_to_utility_mwh",
                "state",
                "tech_class",
                "utility_id_eia",
                "utility_name_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "net_metering_misc_eia861": {
        "schema": {
            "fields": [
                "balancing_authority_code_eia",
                "pv_current_flow_type",
                "report_date",
                "state",
                "utility_id_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "non_net_metering_customer_fuel_class_eia861": {
        "schema": {
            "fields": [
                "balancing_authority_code_eia",
                "capacity_mw",
                "customer_class",
                "report_date",
                "state",
                "tech_class",
                "utility_id_eia",
                "utility_name_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "non_net_metering_misc_eia861": {
        "schema": {
            "fields": [
                "backup_capacity_mw",
                "balancing_authority_code_eia",
                "generators_number",
                "pv_current_flow_type",
                "report_date",
                "state",
                "utility_id_eia",
                "utility_owned_capacity_mw",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "operational_data_misc_eia861": {
        "schema": {
            "fields": [
                "consumed_by_facility_mwh",
                "consumed_by_respondent_without_charge_mwh",
                "data_observed",
                "entity_type",
                "exchange_energy_delivered_mwh",
                "exchange_energy_received_mwh",
                "furnished_without_charge_mwh",
                "nerc_region",
                "net_generation_mwh",
                "net_power_exchanged_mwh",
                "net_wheeled_power_mwh",
                "report_date",
                "retail_sales_mwh",
                "sales_for_resale_mwh",
                "short_form",
                "state",
                "summer_peak_demand_mw",
                "total_disposition_mwh",
                "total_energy_losses_mwh",
                "total_sources_mwh",
                "transmission_by_other_losses_mwh",
                "utility_id_eia",
                "utility_name_eia",
                "wheeled_power_delivered_mwh",
                "wheeled_power_received_mwh",
                "wholesale_power_purchases_mwh",
                "winter_peak_demand_mw",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "operational_data_revenue_eia861": {
        "schema": {
            "fields": [
                "nerc_region",
                "report_date",
                "revenue",
                "revenue_class",
                "state",
                "utility_id_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "reliability_eia861": {
        "schema": {
            "fields": [
                "caidi_w_major_event_days_minus_loss_of_service_minutes",
                "caidi_w_major_event_days_minutes",
                "caidi_wo_major_event_days_minutes",
                "customers",
                "entity_type",
                "highest_distribution_voltage_kv",
                "inactive_accounts_included",
                "momentary_interruption_definition",
                "outages_recorded_automatically",
                "report_date",
                "saidi_w_major_event_days_minus_loss_of_service_minutes",
                "saidi_w_major_event_days_minutes",
                "saidi_wo_major_event_days_minutes",
                "saifi_w_major_event_days_customers",
                "saifi_w_major_event_days_minus_loss_of_service_customers",
                "saifi_wo_major_event_days_customers",
                "short_form",
                "standard",
                "state",
                "utility_id_eia",
                "utility_name_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "sales_eia861": {
        "description": "Annual electricity sales to ultimate customers broken down by utility, balancing authority, state, and customer class.",
        "schema": {
            "fields": [
                "utility_id_eia",
                "state",
                "report_date",
                "balancing_authority_code_eia",
                "customer_class",
                "business_model",
                "data_observed",
                "entity_type",
                "service_type",
                "short_form",
                "utility_name_eia",
                "customers",
                "sales_mwh",
                "sales_revenue",
                "data_maturity",
            ],
            "primary_key": [
                "utility_id_eia",
                "state",
                "report_date",
                "balancing_authority_code_eia",
                "customer_class",
                "business_model",
                "service_type",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "service_territory_eia861": {
        "description": "County FIPS codes for counties composing utility service territories.",
        "schema": {
            "fields": [
                "county",
                "short_form",
                "state",
                "utility_id_eia",
                "utility_name_eia",
                "report_date",
                "state_id_fips",
                "county_id_fips",
                "data_maturity",
            ],
            "primary_key": [
                "report_date",
                "utility_id_eia",
                "county_id_fips",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "utility_assn_eia861": {
        "description": "Association table indicating which states each utility reported data for by year.",
        "schema": {
            "fields": [
                "report_date",
                "utility_id_eia",
                "state",
            ],
            "primary_key": [
                "report_date",
                "utility_id_eia",
                "state",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "utility_data_misc_eia861": {
        "schema": {
            "fields": [
                "alternative_fuel_vehicle_2_activity",
                "alternative_fuel_vehicle_activity",
                "bundled_activity",
                "buying_distribution_activity",
                "buying_transmission_activity",
                "distribution_activity",
                "entity_type",
                "generation_activity",
                "nerc_region",
                "operates_generating_plant",
                "report_date",
                "retail_marketing_activity",
                "short_form",
                "state",
                "transmission_activity",
                "utility_id_eia",
                "utility_name_eia",
                "wholesale_marketing_activity",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "utility_data_nerc_eia861": {
        "schema": {
            "fields": [
                "nerc_region",
                "nerc_regions_of_operation",
                "report_date",
                "state",
                "utility_id_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
    "utility_data_rto_eia861": {
        "schema": {
            "fields": [
                "nerc_region",
                "report_date",
                "rtos_of_operation",
                "state",
                "utility_id_eia",
                "data_maturity",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia861"],
        "etl_group": "eia861",
    },
}
