from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"all_baseball_leagues": League.objects.filter(sport__iexact="baseball"),
		"all_womens_leagues": League.objects.filter(name__contains = 'women'),
		"all_hockey_leagues": League.objects.filter(sport__icontains='hockey'),
		"all_non_football_leagues": League.objects.exclude(sport__contains='football'),
		"all_conference_leagues": League.objects.filter(name__icontains='conference'),
		"all_Atlantic_leagues": League.objects.filter(name__icontains='atlantic'),
		"all_Dallas_teams": Team.objects.filter(location='Dallas'),
		"all_Raptors_teams": Team.objects.filter(team_name__icontains = 'rapto'),
		"all_City_location_teams": Team.objects.filter(location__contains = 'City'),
		"all_first_letter_T_teams": Team.objects.filter(team_name__startswith='T'),
		"all_teams_alphabetically": Team.objects.order_by('team_name'),
		"all_teams_reverse_alpha": Team.objects.order_by('-team_name'),
		"all_last_name_Cooper_players": Player.objects.filter(last_name='Cooper'),
		"all_first_name_Joshua_players": Player.objects.filter(first_name='Joshua'),
		"all_Cooper_not_Joshua_players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua'),
		"all_Alexander_and_Wyatt_players": Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt').order_by('first_name')
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")