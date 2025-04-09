from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Convert ObjectId fields to strings
        for key, value in representation.items():
            if isinstance(value, ObjectId):
                representation[key] = str(value)
        return representation

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Convert ObjectId fields to strings
        for key, value in representation.items():
            if isinstance(value, ObjectId):
                representation[key] = str(value)
        return representation

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Convert ObjectId fields to strings
        for key, value in representation.items():
            if isinstance(value, ObjectId):
                representation[key] = str(value)
        return representation