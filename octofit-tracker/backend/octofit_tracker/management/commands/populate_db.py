from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import settings

from django.db import connection

from django.conf import settings as django_settings

from django.apps import apps

from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear all collections
        self.stdout.write('Deleting all data...')
        User.objects.all().delete()
        Team = self.get_or_create_team_model()
        Team.objects.all().delete()
        Activity = self.get_or_create_activity_model()
        Activity.objects.all().delete()
        Leaderboard = self.get_or_create_leaderboard_model()
        Leaderboard.objects.all().delete()
        Workout = self.get_or_create_workout_model()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass', first_name='Diana', last_name='Prince')
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass', first_name='Steve', last_name='Rogers')

        # Assign teams
        ironman.profile.team = marvel
        ironman.profile.save()
        captain.profile.team = marvel
        captain.profile.save()
        batman.profile.team = dc
        batman.profile.save()
        wonderwoman.profile.team = dc
        wonderwoman.profile.save()

        # Create Activities
        Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        Activity.objects.create(user=batman, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=wonderwoman, type='swim', duration=45, distance=2)
        Activity.objects.create(user=captain, type='run', duration=50, distance=10)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='A quick morning run', suggested_by=ironman)
        Workout.objects.create(name='Strength Circuit', description='Bodyweight strength exercises', suggested_by=batman)

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=90)
        Leaderboard.objects.create(user=wonderwoman, points=95)
        Leaderboard.objects.create(user=captain, points=80)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

    def get_or_create_team_model(self):
        class Team(models.Model):
            name = models.CharField(max_length=100, unique=True)
            class Meta:
                app_label = 'octofit_tracker'
        return Team

    def get_or_create_activity_model(self):
        User = get_user_model()
        class Activity(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            type = models.CharField(max_length=50)
            duration = models.IntegerField()
            distance = models.FloatField()
            class Meta:
                app_label = 'octofit_tracker'
        return Activity

    def get_or_create_leaderboard_model(self):
        User = get_user_model()
        class Leaderboard(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            points = models.IntegerField()
            class Meta:
                app_label = 'octofit_tracker'
        return Leaderboard

    def get_or_create_workout_model(self):
        User = get_user_model()
        class Workout(models.Model):
            name = models.CharField(max_length=100)
            description = models.TextField()
            suggested_by = models.ForeignKey(User, on_delete=models.CASCADE)
            class Meta:
                app_label = 'octofit_tracker'
        return Workout
