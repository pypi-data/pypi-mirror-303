# Copyright © 2024 Contrast Security, Inc.
# See https://www.contrastsecurity.com/enduser-terms-0317a for more details.
from functools import cached_property
from typing import List, Optional

from contrast.reporting.teamserver_responses.protect_rule import ProtectRule


class NGApplicationSettings:
    def __init__(self, settings_json=None):
        self._raw_settings = settings_json or {}

    @cached_property
    def disabled_assess_rules(self) -> List[str]:
        return (
            self._raw_settings.get("settings", {})
            .get("assessment", {})
            .get("disabledRules", [])
        )

    @cached_property
    def protection_rules(self) -> List[ProtectRule]:
        return [
            ProtectRule(r)
            for r in self._raw_settings.get("settings", {})
            .get("defend", {})
            .get("protectionRules", [])
        ]

    @cached_property
    def session_id(self) -> Optional[str]:
        return (
            self._raw_settings.get("settings", {})
            .get("assessment", {})
            .get("session_id", None)
        )

    @cached_property
    def sensitive_data_masking_policy(self) -> dict:
        return self._raw_settings.get("settings", {}).get(
            "sensitive_data_masking_policy", {}
        )

    # note: there are more fields on ApplicationSettings that we currently don't use

    def common_config(self):
        ts_exclusions = self._raw_settings.get("settings", {}).get("exceptions", {})
        return {
            "application.sensitive_data_masking_policy": self.sensitive_data_masking_policy,
            "application.url_exclusions": [
                {
                    "name": exclusion.get("name", ""),
                    "modes": exclusion.get("modes", []),
                    "urls": exclusion.get("urls", []),
                    "match_strategy": exclusion.get("matchStrategy", ""),
                    "protect_rules": exclusion.get("protectionRules", []),
                    "assess_rules": exclusion.get("assessmentRules", []),
                }
                for exclusion in ts_exclusions.get("urlExceptions", [])
            ],
            "application.input_exclusions": [
                {
                    "name": exclusion.get("name", ""),
                    "modes": exclusion.get("modes", []),
                    "urls": exclusion.get("urls", []),
                    "match_strategy": exclusion.get("matchStrategy", ""),
                    "assess_rules": exclusion.get("assessmentRules", []),
                    "protect_rules": exclusion.get("protectionRules", []),
                    "input_type": exclusion.get("inputType", ""),
                    "input_name": exclusion.get("inputName", ""),
                }
                for exclusion in ts_exclusions.get("inputExceptions", [])
            ],
        }
