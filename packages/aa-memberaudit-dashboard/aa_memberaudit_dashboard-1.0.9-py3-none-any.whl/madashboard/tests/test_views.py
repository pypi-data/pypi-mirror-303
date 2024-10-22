from django.http import HttpResponse
from django.test import RequestFactory, TestCase

from allianceauth.eveonline.models import EveCharacter
from app_utils.testing import add_character_to_user, create_user_from_evecharacter

from madashboard.tests.testdata.load_allianceauth import load_allianceauth
from madashboard.tests.testdata.load_memberaudit import load_memberaudit
from madashboard.views import dashboard_memberaudit_check


class DashboardMemberAuditCheckTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_allianceauth()
        load_memberaudit()
        cls.factory = RequestFactory()
        cls.user_without_permission, cls.character_ownership = (
            create_user_from_evecharacter(character_id=1002)
        )
        cls.user_with_ma_permission, cls.character_ownership = (
            create_user_from_evecharacter(
                character_id=1001,
                permissions=["memberaudit.basic_access"],
            )
        )

    def test_dashboard_memberaudit_check_user_with_ma_premission(self):
        # given
        request = self.factory.get("/")
        request.user = self.user_with_ma_permission
        # when
        response = dashboard_memberaudit_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="memberaudit-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_dashboard_memberaudit_check_user_without_permission(self):
        # given
        request = self.factory.get("/")
        request.user = self.user_without_permission
        # when
        response = dashboard_memberaudit_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            '<div id="memberaudit-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_dashboard_memberaudit_check_many(self):
        # given
        add_character_to_user(
            self.user_with_ma_permission, EveCharacter.objects.get(character_id=1006)
        )
        add_character_to_user(
            self.user_with_ma_permission, EveCharacter.objects.get(character_id=1007)
        )
        request = self.factory.get("/")
        request.user = self.user_with_ma_permission
        # when
        response = dashboard_memberaudit_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="memberaudit-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )
