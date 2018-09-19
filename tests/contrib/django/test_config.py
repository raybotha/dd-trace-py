from ddtrace.contrib.django.conf import DatadogSettings
from django.test import TestCase, override_settings
from nose.tools import eq_


class DjangoSettingsTest(TestCase):

    @override_settings(DATADOG_TRACE={'TAGS': {'my_tag': 'my_value'}})
    def test_user_settings_defaults_to_global_if_not_provided(self):
        settings = DatadogSettings(None)
        eq_(settings.TAGS, {'my_tag': 'my_value'})

    @override_settings(DATADOG_TRACE={'TAGS': {'my_tag': 'from_settings'}})
    def test_user_settings_can_be_provided(self):
        settings = DatadogSettings({'TAGS': {'my_tag': 'provided'}})
        eq_(settings.TAGS, {'my_tag': 'provided'})

    @override_settings(DATADOG_TRACE={'DEFAULT_SERVICE': 'my-special-service'})
    def test_cache_service_name_defaults_to_default_service(self):
        settings = DatadogSettings(None)
        eq_(settings.cache_service_name, 'my-special-service')

    @override_settings(DATADOG_TRACE={'DEFAULT_SERVICE': 'my-special-service', 'CACHE_SERVICE_NAME': 'overridden'})
    def test_cache_service_name_can_be_overridden(self):
        settings = DatadogSettings(None)
        eq_(settings.cache_service_name, 'overridden')

    def test_cache_service_name_can_work_is_not_configured(self):
        settings = DatadogSettings(None)
        eq_(settings.cache_service_name, 'django')
