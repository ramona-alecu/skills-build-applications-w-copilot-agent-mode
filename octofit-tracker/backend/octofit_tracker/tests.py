from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout, Leaderboard

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="pass", team=self.team)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.team.name, "Test Team")

class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Team A")

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 1)

class ActivityTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="activityuser", email="activity@example.com", password="pass")
        self.activity = Activity.objects.create(user=self.user, type="run", duration=30, distance=5.0)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="workoutuser", email="workout@example.com", password="pass")
        self.workout = Workout.objects.create(name="Pushups", description="Do 20 pushups", suggested_by=self.user)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)

class LeaderboardTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="leaderuser", email="leader@example.com", password="pass")
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
