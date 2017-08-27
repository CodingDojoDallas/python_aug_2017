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
		"all_Alexander_and_Wyatt_players": Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt').order_by('first_name'),
		"Atlantic_Soccer_Conference":Team.objects.filter(league__name='Atlantic Soccer Conference'), 
		"Boston_Penguins": Player.objects.filter(curr_team__team_name='Penguins'),
		"players_in_CBC": Player.objects.filter(curr_team__league__name = 'International Collegiate Baseball Conference'),
		"Lopezs": Player.objects.filter(all_teams__league__name='American Conference of Amateur Football', last_name='Lopez'),
		"all_football_players": Player.objects.filter(all_teams__league__name__icontains = 'football'),
		"Teams_with_Sophia": Team.objects.filter(curr_players__first_name = 'Sophia'), 
		"Leagues_with_Sophia": League.objects.filter(teams__curr_players__first_name='Sophia'),
		"Flores":Player.objects.filter(last_name='Flores').exclude(all_teams__team_name = 'Roughriders'),
		"Sam_Evans_Teams": Team.objects.filter(all_players__first_name='Samuel',all_players__last_name='Evans'),
		"Tiger_Cat_Players": Player.objects.filter(all_teams__team_name='Tiger-Cats')




	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")