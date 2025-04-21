from decimal import Decimal
from django.forms import ValidationError
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Fund, Manager
from .serializer import FundSerializer
# Create your tests here.

class FundAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.manager = Manager.objects.create(
            manager_name="John Doe",
            manager_bio="Experienced fund manager."
        )

        self.fund1 = Fund.objects.create(
            fund_name="Global Equity Fund",
            fund_manager=self.manager,
            fund_description="A diversified equity fund.",
            nav=125.75,
            date_of_creation="2022-01-15",
            performance=8.5
        )

        self.fund2 = Fund.objects.create(
            fund_name="Technology Growth Fund",
            fund_manager=self.manager,
            fund_description="An aggressive growth fund.",
            nav=150.25,
            date_of_creation="2021-06-10",
            performance=12.3
        )
    
    def test_get_all_funds(self):

        response = self.client.get('/fundapp/funds/')
        funds = Fund.objects.all()
        serializer = FundSerializer(funds, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_fund(self):

        data = {
            "fund_name": "New Equity Fund",
            "fund_manager": self.manager.manager_id,
            "fund_description": "A new equity fund.",
            "nav": 130.50,
            "date_of_creation": "2023-09-01",
            "performance": 7.8
        }

        response = self.client.post('/fundapp/funds/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Fund.objects.count(), 3)

    def test_get_fund_by_id(self):
        """
        Test retrieving a specific fund by ID.
        """
        response = self.client.get(f'/fundapp/funds/{self.fund1.fund_id}/')
        fund = Fund.objects.get(fund_id=self.fund1.fund_id)
        serializer = FundSerializer(fund)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_fund(self):
        """
        Test updating an existing fund.
        """
        data = {
            "fund_name": "Updated Fund Name",
            "performance": 9
        }
        response = self.client.put(f'/fundapp/funds/{self.fund1.fund_id}/', data, format='json')
        # Debug validation errors if the response is 400 Bad Request
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            print("Validation Errors:", response.data)

        # Ensure the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.fund1.refresh_from_db()
        self.assertEqual(self.fund1.fund_name, "Updated Fund Name")
        self.assertEqual(self.fund1.performance, 9)

    def test_delete_fund(self):
        """
        Test deleting a fund.
        """
        response = self.client.delete(f'/fundapp/funds/{self.fund1.fund_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Fund.objects.filter(fund_id=self.fund1.fund_id).exists(), False)

    def test_invalid_fund_id(self):
        """
        Test retrieving a fund with an invalid ID.
        """
        response = self.client.get('/fundapp/funds/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn(b'Not found', response.content)  # Check the response content
    
    def test_invalid_input(self):
        """
        Test creating a fund with invalid input.
        """
        data = {
            "fund_name": "Invalid Fund",
            "fund_manager": 999,  # Non-existent manager_id
            "nav": "invalid",  # Invalid data type
        }
        response = self.client.post('/fundapp/funds/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class FundModelTestCase(TestCase):
    def setUp(self):
        self.manager = Manager.objects.create(
            manager_name = "John Doe",
            manager_bio = "Experienced manager."
        )
        self.fund = Fund.objects.create(
            fund_name="Tech Growth Fund",
            fund_manager=self.manager,
            fund_description="A fund focused on tech startups.",
            nav=Decimal('100.50'),
            performance=Decimal('5.25')
        )

    def test_fund_creation(self):
        """Test that a fund is created correctly."""
        fund = Fund.objects.get(fund_name="Tech Growth Fund")
        self.assertEqual(fund.fund_manager, self.manager)
        self.assertEqual(fund.nav, Decimal('100.50'))

    def test_manager_deletion_cascade(self):
        """Test cascading deletion of funds when a manager is deleted."""
        manager_id = self.manager.manager_id
        self.manager.delete()
        self.assertFalse(Fund.objects.filter(fund_manager_id=manager_id).exists())

    def test_unique_fund_name(self):
        """Test that fund names are unique."""
        with self.assertRaises(Exception):
            Fund.objects.create(
                fund_name="Tech Growth Fund",  # Duplicate name
                fund_manager=self.manager,
                fund_description="Another fund.",
                nav=Decimal('200.00'),
                performance=Decimal('6.00')
            )

    def test_nav_positive_constraint(self):
        """Test that NAV cannot be negative."""
        with self.assertRaises(ValidationError):
            invalid_fund = Fund(
                fund_name="Invalid Fund",
                fund_manager=self.manager,
                fund_description="Invalid fund description.",
                nav=-100.00,
                performance=Decimal('5.00')
            )
            invalid_fund.full_clean()

    def test_performance_range_constraint(self):
        """Test that performance is within a valid range (-100 to 100)."""
        with self.assertRaises(ValidationError):
            invalid_fund = Fund(
                fund_name="Invalid Fund",
                fund_manager=self.manager,
                fund_description="Invalid fund description.",
                nav=Decimal('100.00'),
                performance=Decimal('150.00')  # Out of range
            )
            invalid_fund.full_clean()

