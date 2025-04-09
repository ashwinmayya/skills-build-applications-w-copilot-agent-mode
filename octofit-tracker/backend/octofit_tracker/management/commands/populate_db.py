from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=30),
            User(id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(id=ObjectId(), email='zerocool@mhigh.edu', name='Elliot', age=25),
            User(id=ObjectId(), email='crashoverride@mhigh.edu', name='Dade', age=28),
            User(id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token', age=22),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(id=ObjectId(), name='Blue Team', members=[])
        team2 = Team(id=ObjectId(), name='Gold Team', members=[])
        team1.save()
        team2.save()
        for user in users:
            team1.members.append(user.id)
        team1.save()

        # Create activities
        activities = [
            Activity(id=ObjectId(), user=users[0], type='Cycling', duration=3600),
            Activity(id=ObjectId(), user=users[1], type='Crossfit', duration=7200),
            Activity(id=ObjectId(), user=users[2], type='Running', duration=5400),
            Activity(id=ObjectId(), user=users[3], type='Strength', duration=1800),
            Activity(id=ObjectId(), user=users[4], type='Swimming', duration=4500),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), user=users[0], score=100),
            Leaderboard(id=ObjectId(), user=users[1], score=90),
            Leaderboard(id=ObjectId(), user=users[2], score=95),
            Leaderboard(id=ObjectId(), user=users[3], score=85),
            Leaderboard(id=ObjectId(), user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(id=ObjectId(), user=users[0], description='Training for a road cycling event', date='2025-04-01'),
            Workout(id=ObjectId(), user=users[1], description='Training for a crossfit competition', date='2025-04-02'),
            Workout(id=ObjectId(), user=users[2], description='Training for a marathon', date='2025-04-03'),
            Workout(id=ObjectId(), user=users[3], description='Training for strength', date='2025-04-04'),
            Workout(id=ObjectId(), user=users[4], description='Training for a swimming competition', date='2025-04-05'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
